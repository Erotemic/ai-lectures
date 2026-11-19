# 027000 - Quadratic Integers, Norms, and the Failure of Element Factorization

**Track:** Number Theory from First Principles. **Background:** divisibility and prime factorization, squarefree integers, basic rings and fields, Gaussian integers, Pell equations, finite-dimensional linear algebra. **Aim:** derive the ring of integers in a quadratic field, its norm and discriminant, and an explicit failure of unique element factorization.

<!-- BEGIN SPOKEN LECTURE -->

# Quadratic Integers, Norms, and the Failure of Element Factorization

Six is the product of two and three. It is also the product of one plus the square root of negative five and one minus that square root. In ordinary integers, the second factorization is unavailable; in Gaussian integers, the comparable new factorizations fit within a unique factorization theorem. But in the number system built from the square root of negative five, both expressions live in the same ring and neither can be reduced to the other by rearranging irreducible factors. Unique factorization of elements fails.

This is not a technicality about a badly chosen notation. It reveals a genuinely different kind of arithmetic. To understand why, we will construct quadratic number fields, determine which of their elements deserve to be called integers, learn how norms and discriminants measure their arithmetic, and prove exactly where factorization breaks. The remedy, ideals, will then have a precise problem to solve.

## A new number system made from a square root

Choose a squarefree integer d different from one. The field Q of square root d consists of numbers a plus b times square root d, where a and b are rational. Squarefree means no prime square divides d, which prevents us from carrying an unnecessary rational square inside the radical. For example, the square root of twelve already lies in the field of the square root of three; they generate the same field.

There is a symmetry of this field that does not move ordinary rational numbers. It sends square root d to its negative. Applied to a plus b root d, it gives a minus b root d. This is conjugation. Multiply an element by its conjugate and the irrational-looking part disappears: the norm is a squared minus d times b squared. Add the two conjugates and we obtain the trace, two a. Both are rational.

Norm and trace are more than convenient formulas. Norm is multiplicative, because conjugation preserves products. Trace is additive. These operations reveal when an element has an inverse, how multiplication distorts a lattice, and how much arithmetic information survives when we descend from the larger field to the rational numbers.

For d equal to negative five, the norm of a plus b times square root of negative five is a squared plus five b squared. For d positive, it is instead a squared minus d b squared, and may be negative. Its absolute value, not always the signed norm itself, measures the index of a principal ideal in the integer lattice. The sign distinction becomes important once we leave imaginary quadratic fields.

## Which elements count as integers?

A rational number such as one half is in every quadratic field, but we do not want to declare it an integer merely because it belongs to the field. The correct definition is algebraic: an element is an algebraic integer if it satisfies a monic polynomial whose coefficients are ordinary integers. Monic means the coefficient of the highest power is exactly one. The ordinary integers satisfy this definition through linear equations, and every rational algebraic integer is an ordinary integer, by the rational-root theorem.

There is a practical criterion in a quadratic field. An element alpha has two conjugates. It satisfies a quadratic equation whose coefficients are negative its trace and its norm. If both trace and norm are ordinary integers, that equation shows alpha is an algebraic integer. Conversely, if alpha is an algebraic integer, its conjugate is also one; sums and products of algebraic integers remain algebraic integers. Trace and norm are then rational algebraic integers and hence ordinary integers. Thus, in a quadratic field, being an algebraic integer is exactly the condition that trace and norm are in Z.

The condition tells us what denominators are possible. Write alpha as x plus y root d with rational x and y. Its trace says two x must be an integer. Its norm says x squared minus d y squared must be an integer. Those facts force two y to be an integer as well. One clean proof is to multiply the norm equation by four. If two y had a denominator in lowest terms, its denominator squared would have to divide squarefree d, which is impossible unless the denominator is one.

Call two x by the integer A and two y by the integer B. The norm condition now says A squared minus d times B squared is divisible by four. If A and B are even, alpha has ordinary integer coefficients a and b. Could both be odd? Since odd squares leave remainder one modulo four, the condition says that d must also leave remainder one modulo four. No case with one odd and one even works for squarefree d. We have classified all possibilities.

When d does not leave remainder one modulo four, every algebraic integer is a plus b root d with a and b integers. But when d does leave remainder one modulo four, we must also allow half-integer combinations with matching parity. A compact basis is one together with omega, where omega is one plus root d divided by two. Every algebraic integer has the form a plus b omega with a and b integers.

For d equal to five, omega equals one plus root five over two. It is an algebraic integer because it satisfies omega squared minus omega minus one equal to zero. It would be a mistake to describe the full ring of integers in the field of root five as Z adjoin root five: that ring omits omega. For d equal to negative five, however, the full ring really is Z adjoin root negative five.

## The discriminant remembers the lattice

We can draw the algebraic integers as a lattice. In the imaginary quadratic case, their complex embeddings give a two-dimensional grid in the usual plane. The lattice's shape depends on d and on whether we used the half-integer basis. Its area is not just decorative geometry; it governs how small norms and ideals can be.

For any basis one and omega, form the matrix of its two embeddings, with the original basis elements in one row and their conjugates in the other. Square its determinant. This number is the discriminant of the basis. It measures how close the two embeddings are to becoming indistinguishable; for a quadratic basis it is simply the square of omega minus its conjugate.

If omega is root d, the difference between conjugates is two root d, so the discriminant is four d. If omega is one plus root d over two, the difference is root d, so the discriminant is d. These are the two cases for a squarefree quadratic field's fundamental discriminant.

For the field of root negative five, the discriminant is negative twenty. The complex lattice has fundamental area root five. In fact its area equals one half the square root of the absolute value of the discriminant. This relation will be the link between arithmetic and the geometry of numbers when we classify ideals by norm.

## Six has two irreducible factorizations

Return to the ring R equal to Z adjoin root negative five. Write w for that square root. The norm of a plus b w is a squared plus five b squared, a nonnegative integer, and it multiplies under products. A unit must have norm one, since the norms of an element and its inverse multiply to one. The only solutions of a squared plus five b squared equal one are plus one and minus one, so those are the only units.

Now calculate. The product of one plus w and one minus w is one minus w squared, which is six. So six equals two times three and also equals one plus w times one minus w.

We need to prove that the displayed factors are irreducible rather than simply call them prime. If an element of norm four, such as two, split into two nonunits, both factors would have integer norms at least two, so both norms would have to be two. But the equation a squared plus five b squared equal two has no integer solution. Hence two is irreducible. Similarly three has norm nine, and a nontrivial split would require norms three and three; that is also impossible.

Each of one plus w and one minus w has norm six. A nontrivial split would need norms two and three, in some order. Neither occurs. So both are irreducible. And they are not associates of two or three, whose norms differ. They are not associates of one another either, because the only units are plus one and minus one, and neither multiplication changes one plus w into one minus w.

We have proved that six possesses two different factorizations into irreducibles. Thus R is not a unique factorization domain. This argument does not say that irreducible factorization fails to exist. In fact, because the positive norm drops under a nontrivial factorization, every nonzero nonunit factors into irreducibles. The failure is uniqueness, not existence.

The difference between irreducible and prime is visible in a single test. The irreducible element two divides the product of one plus w and one minus w, because that product is six. Yet two divides neither factor: division by two would require a coefficient one half, which does not belong to R. Therefore two is not prime as an element of this ring.

## What went wrong, and what can be repaired?

The Gaussian integers admitted a Euclidean division algorithm: rounding both coordinates of a quotient gave a remainder of smaller norm. That argument yielded Bezout's identity, made irreducibles prime, and then established unique factorization. The root-negative-five lattice lacks an equally effective division procedure. A multiplicative norm alone never promised such a procedure.

There is an illuminating way to state the problem. The equations for six still know that two is related to both of the factors one plus w and one minus w. Ordinary element divisibility is too coarse to describe how that relationship splits. An ideal remembers all multiples and sums of a collection of elements, not just multiples of one chosen generator. We will see that six has a single, consistent factorization into prime ideals, even though it has two incompatible expressions as a product of irreducible elements.

The important bridge is now built. We know exactly what the integers of any quadratic field are, why an index and discriminant arise, and how an elementary factorization calculation can show that a pleasant property fails. Number theory did not lose factorization; it was asking the wrong objects to factor.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Classification of quadratic integers

Let \(d\ne1\) be squarefree, \(K=\mathbb Q(\sqrt d)\), and \(\alpha=x+y\sqrt d\), \(x,y\in\mathbb Q\). Define \(\bar\alpha=x-y\sqrt d\), \(\operatorname{Tr}(\alpha)=2x\), and \(N(\alpha)=x^2-dy^2\). The element \(\alpha\) is integral iff both trace and norm lie in \(\mathbb Z\): one direction follows from its monic quadratic polynomial, and the other from closure of algebraic integers under addition and multiplication and the rational algebraic integer criterion.

Trace and norm integrality imply \(A=2x\in\mathbb Z\) and \(B=2y\in\mathbb Z\), with \(A^2-dB^2\equiv0\pmod4\). To see \(B\in\mathbb Z\), note that \(d(2y)^2=A^2-4N(\alpha)\in\mathbb Z\); a denominator \(v\) for \(2y\) in lowest terms would force \(v^2\mid d\). Squarefreeness forces \(v=1\). A parity check now gives
\[
\boxed{\mathcal O_K=\begin{cases}
\mathbb Z[\sqrt d],&d\not\equiv1\pmod4,\\
\mathbb Z[(1+\sqrt d)/2],&d\equiv1\pmod4.
\end{cases}}
\]
Here congruence modulo four applies to negative integers in the usual manner; for \(d=-5\), \(d\equiv3\pmod4\).

### Discriminant and principal norm

For \(\omega=\sqrt d\) or \((1+\sqrt d)/2\) as above,
\[
\Delta_K=\det\begin{pmatrix}1&\omega\\1&\bar\omega\end{pmatrix}^{\!2}
=(\omega-\bar\omega)^2=
\begin{cases}4d,&d\not\equiv1\pmod4,\\d,&d\equiv1\pmod4.\end{cases}
\]
In the imaginary quadratic case the covolume of the standard embedded lattice \(\mathcal O_K\subset\mathbb C\) is \(\sqrt{|\Delta_K|}/2\). Multiplication by \(\alpha\) on a chosen integer basis has determinant \(N(\alpha)\); hence \([\mathcal O_K:(\alpha)]=|N(\alpha)|\) for \(\alpha\ne0\).

### Failure of unique element factorization in \(\mathbb Z[\sqrt{-5}]\)

Write \(w=\sqrt{-5}\). Then
\[
N(a+bw)=a^2+5b^2,\quad N(2)=4,\quad N(3)=9,\quad N(1\pm w)=6,
\]
\[
\boxed{6=2\cdot3=(1+w)(1-w).}
\]
The equations \(a^2+5b^2=2\) and \(a^2+5b^2=3\) have no integer solutions. Every nontrivial decomposition of 2 (norm 4), 3 (norm 9), or \(1\pm w\) (norm 6) would require a factor of norm 2 or 3. Thus all four are irreducible. Units are \(\pm1\); the two factorizations cannot be matched up by associates. Finally \(2\mid(1+w)(1-w)\) but \(2\nmid(1+w)\), \(2\nmid(1-w)\), showing irreducible \(\not\Rightarrow\) prime in this ring.

### Exercises

1. Prove that \((1+\sqrt{13})/2\) is integral and calculate its minimal polynomial, trace, and norm.
2. Compute the rings of integers and discriminants for \(\mathbb Q(\sqrt{-1})\), \(\mathbb Q(\sqrt{-3})\), \(\mathbb Q(\sqrt2)\), and \(\mathbb Q(\sqrt5)\).
3. Show that every nonzero nonunit of \(\mathbb Z[\sqrt{-5}]\) has norm at least four. Why does this make infinite descent of factor norms possible?
4. Show directly that \((1+w)/2\notin\mathcal O_K\), using either trace and norm or parity.
5. In a real quadratic field, find a nonzero integer element with negative norm and explain why index is the absolute norm.

### Reading and source notes

- Keith Conrad, [Quadratic integer rings and ideals](https://old.mccme.ru/dubna/2017/notes/kconrad-quadraticideals.pdf), especially the ring-of-integers classification and trace-norm criterion.
- J. S. Milne, [Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf), chapters on quadratic rings and the ring of integers.
- Wikipedia: [Quadratic field](https://en.wikipedia.org/wiki/Quadratic_field), [Algebraic integer](https://en.wikipedia.org/wiki/Algebraic_integer), [Discriminant of an algebraic number field](https://en.wikipedia.org/wiki/Discriminant_of_an_algebraic_number_field), [Unique factorization domain](https://en.wikipedia.org/wiki/Unique_factorization_domain).
