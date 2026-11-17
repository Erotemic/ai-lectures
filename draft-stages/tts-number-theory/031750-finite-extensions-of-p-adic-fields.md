# 031750 — Finite Extensions of p-adic Fields: Why There Is Only One Valuation

**Track:** Number Theory from First Principles. **Background:** 027625–027875 (integral closure and Dedekind ideals), 030500–030750 (completion), 031000 (Hensel's lemma), 031500 (quadratic examples). **Aim:** prove the general finite-extension theorem, including the unique valuation, completeness, finite residue field, and the degree formula.

<!-- BEGIN SPOKEN LECTURE -->

# Finite Extensions of p-adic Fields: Why There Is Only One Valuation

Consider the two quadratic extensions of the three-adic numbers that we constructed explicitly. In one extension, the residue field grew from three elements to nine. In the other, the residue field stayed the same but a square root of three acquired valuation one-half. We checked everything by hand, using the special equations satisfied by our square roots.

But an algebraic extension need not be quadratic, and its defining polynomial need not have such convenient terms. Suppose we start with the p-adic field and adjoin a root of an arbitrary irreducible polynomial of degree seventeen. Is it possible that several incompatible notions of p-adic distance appear? Could part of the degree disappear, neither enlarging the residue field nor refining the valuation? We want to answer these questions for every finite extension, not just for two carefully chosen examples.

Here is the theorem. Let K be a finite extension of the p-adic numbers, with its complete discrete valuation, and let L be a further finite extension of degree n. There is exactly one extension of the absolute value of K to L. With that distance, L is complete. Its integral elements form a complete discrete valuation ring, whose residue field is finite. If e is the ramification index, the number of finer valuation steps, and f is the degree of the residue-field extension, then n equals e times f.

This conclusion has several ingredients. The important point is that they fit together: finite algebraic extension, integral closure, completeness, and the absence of nontrivial idempotents in a field.

## First, the integral elements form a finite lattice

Write A for the ring of integers of K, with uniformizer pi, and let B consist of all elements of L integral over A. An element is integral if it satisfies a monic polynomial with coefficients in A. We already used this definition for ordinary number fields. Here A is a complete discrete valuation ring rather than the usual integers, but the trace-lattice argument still works.

Because K has characteristic zero, L over K is separable. Choose a primitive element theta, so every element of L is a K-linear combination of one, theta, up to theta to the power n minus one. Multiply theta by a sufficiently large power of pi so that the new generator alpha is integral. Then one, alpha, through alpha to the power n minus one form an A-lattice contained in B.

Why can B not be infinitely bigger than that lattice? Look at the trace pairing. The trace of x times y is the trace to K of the K-linear map given by multiplication by x times y. Separability makes this pairing nondegenerate. Relative to our chosen basis there is a dual basis. Any element x of B has the property that the trace of x times alpha to the j is in A, because the product is integral and the trace of an integral element is integral. Therefore the coordinates of x are trapped in a fixed A-lattice spanned by the dual basis.

So B lies between two finitely generated A-modules of rank n. It is a finite A-module. Since it is torsion-free and A is a discrete valuation ring, B is even a free A-module of rank n. Choose a basis, and as an additive topological space B looks like n copies of A. In particular, it is complete for the pi-adic topology.

We also know that B is an integrally closed, one-dimensional Noetherian domain. It is integrally closed by construction. It is Noetherian because it is finite over A. Any nonzero prime of B contracts to the maximal ideal of A, and because the quotient is integral over a finite field, that prime is maximal. Thus B is a Dedekind domain, using the criterion we proved during our study of ideal factorization.

At this stage, however, B might conceivably have several maximal ideals. The crucial next step is where completeness enters.

## Why a field extension has only one prime above pi

Suppose B had two distinct maximal ideals lying above pi. Since B is Dedekind, the ideal pi times B would factor as a product of powers of these maximal ideals. The Chinese remainder theorem would then break B modulo pi into a product of at least two nonzero rings. In that product there is an element that is one in the first factor and zero in the second. Squaring does not change it. Such an element is called an idempotent, and it is neither zero nor one.

Now lift that residue-class idempotent to B itself. The equation for an idempotent is T squared minus T equals zero. Its derivative is two T minus one. At an idempotent residue, that derivative is invertible: the square of two T minus one is one modulo pi. Hensel's iterative argument works for a ring complete in the pi-adic topology, provided the derivative is a unit. So the idempotent lifts to an actual element e of B with e squared equal to e.

But B is a subring of the field L. In a domain, e times e minus one equals zero only if e is zero or e is one. Neither lift could reduce to the idempotent we started with. Contradiction.

Thus B has exactly one maximal ideal, call it P. A Dedekind domain with one maximal ideal is a discrete valuation ring. Choose a generator varpi for P. The global uniformizer pi is not necessarily a generator of P; rather, pi equals a unit times varpi to a positive integer power e. That integer is the ramification index.

We can now define a valuation on L without guessing a norm. Every nonzero x in L is uniquely a unit of B times an integer power of varpi. Give varpi value one, units value zero, and call the resulting integer-valued function w. The valuation extending the one on K is w divided by e, because pi has w-value e. We have constructed the promised distance.

There cannot be a second extension. Any valuation on L that agrees with the valuation of K must give every element integral over A a nonnegative value. To see this, suppose an integral element had negative value and use its monic equation: its highest power would have strictly smaller valuation than every other term, so cancellation would be impossible. Thus all of B lies inside any proposed valuation ring. In particular, every B-unit has value zero, while pi has value one. Since pi is a unit times varpi to the e, varpi must have value one over e. Every element of L is a B-unit times an integer power of varpi, so all values are forced. That proves uniqueness.

## Count the degree twice

The quotient B modulo pi times B contains exactly q to the n elements, where q is the size of the residue field of K. The reason is simple: B is a free A-module of rank n, so reducing a basis modulo pi gives n independent coordinates, each with q choices.

But pi times B equals P to the e. Filter B modulo P to the e by the successive powers P, P squared, and so on. Each successive layer is a one-dimensional vector space over B modulo P, because P is generated by one uniformizer. If the residue field of B contains q to the f elements, each of the e layers contributes q to the f choices. Therefore B modulo pi has q to the e times f elements.

These two counts refer to the same finite ring. So n equals e times f. Nothing has gone missing from the extension degree. In the earlier unramified quadratic example, n was two, e was one, and f was two. In the ramified quadratic example, n was two, e was two, and f was one. Both were instances of this general identity.

There is also a useful formula for the norm. Multiplication by an element x of L is a K-linear transformation, and its determinant is the field norm of x. For a B-unit, multiplication preserves the lattice B, so its norm is an A-unit. Multiplication by varpi has a cokernel B modulo varpi B, with q to the f elements, so its determinant has pi-adic valuation f. Consequently the K-valuation of the norm of x is f times the integer valuation w of x. Dividing by n equals e f shows that the unique extended absolute value of x equals the absolute value of its field norm raised to the power one over n.

This is the same norm formula sometimes stated as the starting point of the extension theorem. Here we obtained it at the end, after building the valuation and proving it is unique. The order of the argument matters: it avoids simply assuming that a root of a polynomial automatically has a well-behaved absolute value.

## Completeness, and what the theorem does not say

Finally, since B is a free finite module over the complete ring A, it is complete for the pi-adic topology. The P-adic topology is the same topology, because pi is a unit times varpi to the e. Its fraction field L is therefore complete: a Cauchy sequence can be multiplied by a fixed power of varpi so that it lives eventually in B, where it converges. The quotient B modulo P is finite, so B is compact as well: it is topologically a finite product of the compact ring A.

Notice what we have *not* proved. We have not said that every finite extension is either entirely ramified or entirely unramified. An extension can have both effects. Nor have we shown yet that there is a uniquely determined unramified part sitting inside it. Those are further structural statements, and they will follow from the finite-field theory and Hensel lifting already available to us.

The answer to our original question is now rigorous. An arbitrary finite extension of a p-adic field has one valuation, not several. Its ring of integers has one maximal ideal. Its degree divides exactly into residue-field growth and ramification. The simple quadratic examples were not coincidences; they showed the two basic ways that the general theorem accounts for algebraic degree.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let K be a finite extension of Q_p, A=O_K, \(\pi\) a uniformizer, residue size q, and L/K finite separable of degree n. Let B be the integral closure of A in L.

### Finite integral closure and uniqueness of the maximal ideal

1. Choose integral alpha with L=K(alpha). The trace pairing is nondegenerate by separability. With M=A[alpha] and trace-dual lattice M*,
   \[ M\subseteq B\subseteq M^*=\{x\in L:\operatorname{Tr}_{L/K}(xM)\subseteq A\}. \]
   The middle inclusion uses integrality of traces. Thus B is finite torsion-free, hence free of rank n over A.
2. B is Noetherian, integrally closed, and of Krull dimension one; hence Dedekind. Its maximal ideals all contain \(\pi B\), and \(B/\pi B\) is finite Artinian.
3. If there are at least two primes over \(\pi\), CRT produces a nontrivial idempotent \(\bar e\in B/\pi B\). For \(F(T)=T^2-T\), \(F'(\bar e)=2\bar e-1\) is a unit since \((2\bar e-1)^2=1\). Lifting in the \(\pi\)-adically complete ring B gives a nontrivial idempotent in the domain B, impossible.
4. Thus B has a unique maximal ideal P=(\(\varpi\)); \(\pi B=P^e\). Every \(x\in L^\times\) is \(\varpi^{w(x)}u\) for \(u\in B^\times\), and \(v_L=w/e\) extends \(v_K\).
5. Any valuation on L extending \(v_K\) is nonnegative on integral elements, zero on \(B^\times\), and assigns \(\varpi\) value \(1/e\); this proves uniqueness.

### Fundamental degree identity and norm formula

\[
|B/\pi B|=q^n,\qquad |B/P|=q^f,\qquad |P^i/P^{i+1}|=q^f.
\]
Hence \(q^n=|B/P^e|=q^{ef}\) and \(n=ef\). The determinant of multiplication by \(\varpi\) has valuation \(f\), since its cokernel is \(B/\varpi B\) of cardinality \(q^f\); thus
\[
 v_K(N_{L/K}(x))=f\,w(x),\quad
 |x|_L=|N_{L/K}(x)|_K^{1/n}.
\]
The valuation topology is the \(\varpi\)-adic topology, the same as the \(\pi\)-adic one on B; completeness follows from \(B\cong A^n\).

**Proof prerequisites used, not hidden:** finite-module structure of integral closure via trace duality; the Dedekind criterion and invertibility of nonzero prime ideals from lectures 027625–027875; Hensel lifting in a complete ring with a unit derivative (the iteration is the same as in 031000). All fields here have characteristic zero; inseparable residue extensions are not at issue.

### Exercises

1. Why does a nonzero prime of B lying above a complete DVR's maximal ideal have to be maximal?
2. Check directly that \(F'(e)^2=1\) in a ring whenever \(e^2=e\), even in residue characteristic two.
3. Derive the determinant/norm formula from Smith normal form of a lattice endomorphism over A.
4. Reproduce \(n=ef\) for the quadratic examples Q_3(√2) and Q_3(√3).
5. Explain precisely why completeness, not just unique factorization of ideals, is used to rule out several primes over \(\pi\).

### Reading and source notes

- Andrew V. Sutherland, MIT 18.785, [Extensions of complete DVRs](https://math.mit.edu/classes/18.785/2021fa/LectureNotes10.pdf) and [Local fields and Hensel's lemmas](https://math.mit.edu/classes/18.785/2021fa/LectureNotes9.pdf).
- J. S. Milne, [Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf), integral closure, trace duality, and Dedekind domains.
- Wikipedia: [Local field](https://en.wikipedia.org/wiki/Local_field), [Ramification (mathematics)](https://en.wikipedia.org/wiki/Ramification_(mathematics)), [Discrete valuation ring](https://en.wikipedia.org/wiki/Discrete_valuation_ring).
