# 029750 - Reducing Quadratic Forms and Computing Class Numbers

**Track:** Number Theory from First Principles. **Background:** 029500 (forms and ideal lattices), Euclidean algorithm, integer matrices. **Aim:** derive an explicit terminating reduction algorithm and enumerate classes for discriminants -20 and -23, including a class of order three.

<!-- BEGIN SPOKEN LECTURE -->

# Reducing Quadratic Forms and Computing Class Numbers

An ideal class group is a finite group, but its definition does not immediately supply a list of its members. A class is represented by an ideal, and an ideal can be given in infinitely many ways. There are infinitely many integer bases for even one fixed lattice. How can we decide whether two presentations correspond to the same class, and how can we find all classes?

Quadratic forms make this problem concrete. Each ideal class of an imaginary quadratic field corresponds to a primitive positive definite form with the field's discriminant. Two forms represent the same class exactly when they are related by an integer change of coordinates with determinant plus one. That still leaves infinitely many coordinate changes. What we need is a way to select one economical representative from each orbit.

The method is called reduction. It uses only two elementary transformations of variables and an inequality controlled by the discriminant. It is much more than a way to make coefficients aesthetically small; it turns an abstract finite-group problem into a finite enumeration.

Write our form as a x squared plus b x y plus c y squared, where its discriminant D equals b squared minus four a c and is negative. We also require a positive. Such a form is positive definite. For a reduced form, we will require the absolute value of b to be no greater than a, and a to be no greater than c. On the boundaries, we choose the convention that b is nonnegative when its absolute value equals a or when a equals c. These tie rules avoid writing the same class twice.

Here is the first allowable move. Replace x by x plus k y and leave y unchanged, where k is any integer. This integer substitution has determinant one. The coefficient of x squared remains a. The middle coefficient becomes b plus two a k, and the coefficient of y squared becomes a k squared plus b k plus c. We choose k so that the new middle coefficient lies between negative a and positive a. This is exactly division with remainder, but with step size two a. At an endpoint we choose the positive sign.

The second allowable move swaps the two variables with a minus sign on one of them: replace x by negative y and y by x. Again the determinant is one. The new coefficients are c, negative b, and a. So if our current c is smaller than our current a, we can swap and make the leading coefficient smaller.

The algorithm alternates these operations. First use a shift to control b. If c is smaller than a, swap. Then shift again and test again. Every time a swap is necessary, the leading coefficient decreases by a positive integer. It can never decrease forever. Eventually we reach a situation with absolute b no greater than a no greater than c. A final tie adjustment gives our chosen convention. We have proved that the algorithm terminates.

There is a geometric interpretation. The coefficient a is the squared length of the first lattice vector, after an appropriate normalization. The coefficient c is the squared length of the second, and b measures twice their inner product. Our shifts subtract multiples of the first vector from the second to reduce its projection, and our swaps put the shorter vector first. In two dimensions this resembles the Euclidean algorithm for a lattice basis.

Why can reduced forms be enumerated with a finite search? Use the discriminant identity. The absolute value of D equals four a c minus b squared. Since c is at least a, this is at least four a squared minus b squared. And since the absolute value of b is no greater than a, the result is at least three a squared. Therefore the positive coefficient a is bounded above by the square root of the absolute discriminant divided by three.

This is a surprisingly strong bound. If D is negative twenty, a can be only one or two. If D is negative twenty-three, a can also be only one or two. We have replaced an infinite search over all positive integer coefficients with a few cases.

Let's enumerate discriminant negative twenty. If a is one, b must be an even integer with absolute value at most one. Therefore b is zero. The discriminant equation then gives c equal to five. Our first reduced form is one, zero, five: x squared plus five y squared.

If a is two, b is even and lies between negative two and two. If b is zero, the discriminant equation would give c equal to twenty divided by eight, which is not an integer. If b is plus or minus two, c is three. The boundary rule selects b equal to plus two. Our second reduced form is two, two, three: twice x squared plus twice x y plus three times y squared.

No other reduced forms exist. The reduction theorem says every proper equivalence class has exactly one reduced representative under the tie convention. Thus the class number is two. This independently recovers the result obtained earlier by geometry of numbers: the ideal class group of the integers with the square root of negative five has exactly two elements. The nontrivial class is its own inverse.

Let us try a field where the answer differs. Take discriminant negative twenty-three. Its field is obtained by adjoining the square root of negative twenty-three, and the full integer ring uses omega equal to one plus that square root over two. The bound once again allows a equal to one or two.

For a equal to one, the discriminant is odd, so b must be odd. With absolute b at most one, the boundary convention chooses b equal to one. Solving b squared minus four a c equals negative twenty-three gives c equal to six. The form is x squared plus x y plus six y squared.

For a equal to two, b must be odd and its absolute value at most two, so b is plus or minus one. In both cases c is three. Neither sign is excluded by the tie convention, because the absolute value of b is strictly smaller than a and a is strictly smaller than c. Thus there are two more reduced forms: twice x squared plus x y plus three y squared, and twice x squared minus x y plus three y squared.

The class number of this field is three. Notice the contrast with discriminant negative twenty. There the two signs of b equal to two led to the same class because of the boundary rule. Here the two signs of b equal to one represent different proper classes. They are inverses under the ideal-class group law, but not equal.

We can see the order-three group without asking you to learn a long composition algorithm. The integer two splits in the ring of discriminant negative twenty-three, because omega satisfies X squared minus X plus six, which reduces modulo two to X times X plus one. One prime ideal over two is P generated by two and omega, the other is its conjugate P prime generated by two and omega minus one.

The norm form of P is the reduced form two, one, three. There is no algebraic integer of norm two, because the norm in the basis one and omega is x squared plus x y plus six y squared. If y is zero, we obtain a square. If y is nonzero, completing the square shows the norm is at least six minus one quarter, which is greater than two. So P is not principal.

But one plus omega has field norm eight. To check that, omega has trace one and norm six, so the norm of one plus omega is one plus one plus six. The element one plus omega reduces to zero modulo P prime, because omega reduces to one there, but it is nonzero modulo P, where omega reduces to zero. Therefore the principal ideal generated by one plus omega contains only the prime P prime above two, with total norm eight. Unique factorization of ideals forces that principal ideal to equal P prime cubed.

So the class of P prime has cube equal to the identity, and it is not the identity itself. Its order is exactly three. There are only three classes, so this single class generates the class group. We have proved that the group is cyclic of order three, using only the splitting of two and an element of norm eight.

There is an important logical distinction in this computation. Listing reduced forms proves how many classes there are. Exhibiting the ideal relation proves how the group operation behaves. A list of three things could not by itself distinguish every possible group law in more complicated examples. We needed ideal multiplication to understand composition.

Why is the reduced representative unique? The central observation is that, in a reduced positive definite form, the leading coefficient a is the smallest value taken by the form on a primitive nonzero integer vector. The inequalities on a, b, c establish this by checking vectors with second coordinate zero, plus or minus one, or greater absolute value. The possible ties are precisely the cases in which c equals a or the middle coefficient reaches a boundary. Our tie rules handle those cases. Any proper change of variables sends primitive vectors to primitive vectors, so it preserves this smallest value. Once a is fixed, the allowed normalized middle coefficient and tie conventions determine b, and then the discriminant equation determines c. The mathematical companion spells out the short remaining check.

Reduction has given us a practical dictionary. A discriminant determines a finite list of reduced forms; the list has the same size as the ideal class group; and multiplication of ideals explains the form-class group operation. We can now go further than saying that some rational primes split. We can ask which of the reduced forms represents a given prime and thereby identify the ideal class of a prime lying above it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For positive definite \(Q=[a,b,c]\), \(D=b^2-4ac<0\), proper transformations are generated by
\[
T_k:(x,y)\mapsto(x+ky,y):\quad [a,b,c]\mapsto[a,b+2ak,a k^2+bk+c],
\]
\[
S:(x,y)\mapsto(-y,x):\quad[a,b,c]\mapsto[c,-b,a].
\]
Apply \(T_k\) to ensure \(-a<b\le a\). If \(c<a\), apply \(S\) and repeat; each necessary swap strictly decreases \(a\in\mathbb Z_{>0}\). When \(a=c\) or \(|b|=a\), normalize the tie by \(b\ge0\). A **reduced** form obeys \(|b|\le a\le c\), with \(b\ge0\) when \(|b|=a\) or \(a=c\). It satisfies
\[
|D|=4ac-b^2\ge3a^2,\qquad a\le\sqrt{|D|/3}.
\]
**Uniqueness note.** For \(|b|\le a\le c\), every primitive \((u,v)\) satisfies \(Q(u,v)\ge a\). If \(|v|\ge2\), completing the square gives \(Q\ge(4ac-b^2)v^2/(4a)\ge3a\). If \(|v|=1\), use \(Q(u,v)\ge a u^2-a|u|+a\ge a\) for every integer \(u\); if \(v=0\), primitivity forces \(|u|=1\). Equality outside \((\pm1,0)\) requires a boundary case \(a=c\) or \(|b|=a\). Class equivalence preserves the primitive minimum. At equality the remaining changes of basis differ by the boundary swaps/shifts, which the tie conditions identify; otherwise it preserves \(a\) and forces \(b\) into its single residue representative modulo \(2a\). Therefore each proper class has one reduced representative.

Enumerations:
\[
D=-20:\quad[1,0,5],\ [2,2,3],\quad h(-20)=2.
\]
\[
D=-23:\quad[1,1,6],\ [2,1,3],\ [2,-1,3],\quad h(-23)=3.
\]
For \(D=-23\), \(\omega=(1+\sqrt{-23})/2\) has \(\omega^2-\omega+6=0\), \(\operatorname{Tr}(\omega)=1\), \(N(\omega)=6\), \(N(1+\omega)=8\). The prime ideals \(P=(2,\omega)\), \(P'=(2,\omega-1)\) satisfy \((2)=PP'\). Modulo \(P'\), \(\omega\equiv1\), hence \(1+\omega\equiv0\); modulo \(P\), \(1+\omega\equiv1\). Therefore \((1+\omega)=(P')^3\), proving \(\operatorname{Cl}(\mathbb Q(\sqrt{-23}))\cong\mathbb Z/3\mathbb Z\).

### Exercises

1. Reduce \([3,4,3]\) of discriminant \(-20\) to one of the two canonical reduced forms, showing each coordinate change.
2. Enumerate the reduced primitive positive definite forms of discriminant \(-4\), \(-7\), and \(-8\), and determine their class numbers.
3. Verify that \([2,1,3]\) and \([2,-1,3]\) both have discriminant \(-23\), and explain why changing \(b\) to \(-b\) should invert a form class.
4. Verify \(N(1+\omega)=8\) in the field of discriminant \(-23\), and check the reductions modulo both prime ideals over 2.
5. Prove that a reduced form with \(a<c\) and \(|b|<a\) has only \((\pm1,0)\) as primitive vectors attaining the minimum \(a\), unless an explicitly checked exceptional equality occurs.

### Reading and source notes

- Steven Charlton, [*Primes of the Form x² + ny²*, Chapter 5](https://www.math.uni-hamburg.de/personen/charlton/teaching/primes_17/primes.pdf), reduction algorithm, uniqueness proof, and finite class enumeration.
- FLINT project, [Computing in the class group](https://flintlib.org/doc/qfb/class-group.html), proper reduced forms and Gauss composition (software documentation; use primary mathematical notes for proofs).
- Wikipedia: [Binary quadratic form](https://en.wikipedia.org/wiki/Binary_quadratic_form), [Gauss reduction theory](https://en.wikipedia.org/wiki/Binary_quadratic_form#Equivalence_and_reduction), [Ideal class group](https://en.wikipedia.org/wiki/Ideal_class_group), [Heegner number](https://en.wikipedia.org/wiki/Heegner_number).
