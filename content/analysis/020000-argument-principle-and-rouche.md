# 020000 — Counting Invisible Roots: The Argument Principle and Rouché's Theorem

**Track:** Analysis from First Principles. **Background:** holomorphic zeros with multiplicity, poles, contour integrals, residues, continuous deformation of loops. **Theme:** logarithmic derivatives translate local zero/pole multiplicities into boundary winding, and strict boundary inequalities preserve root counts.

<!-- BEGIN SPOKEN LECTURE -->

# Counting Invisible Roots: The Argument Principle and Rouché's Theorem

Suppose someone hands you a polynomial of degree six and asks how many of its roots lie inside the unit circle. You could try to solve the equation, but a general sixth-degree equation has no elementary radical formula of the kind we use for quadratics. Even if a numerical solver returns six approximations, you still have to ask which roots truly lie inside the circle, and how much numerical error could change the answer.

Complex analysis offers a different kind of answer. It can count roots exactly without finding their locations. In a favorable case, you only need to compare the magnitudes of two expressions along the circle. The result may tell you that precisely two roots lie inside, counting multiplicity, without identifying either root.

There are two ideas behind that method. First, a holomorphic function winds its values around zero as its input travels around a contour; the total winding encodes the zeros and poles inside. Second, if one holomorphic term is strictly larger than another everywhere on the boundary, the smaller term cannot change the number of zeros inside when we add it. These ideas become the argument principle and Rouché's theorem.

Before proving them, we need to understand why a function's derivative divided by the function acts as a counter for zeros. The explanation begins with the order of a single zero.

## At a zero, a logarithmic derivative reveals multiplicity

Let f be holomorphic near a and suppose it has a zero of order m there. From the local Taylor expansion, we can write f as the m-th power of z minus a times another holomorphic function h that does not vanish at a.

Differentiate that factorization. Divide the result by f wherever f is nonzero. One term becomes m divided by z minus a. The other becomes h prime divided by h. Near a, the second term is holomorphic because h does not vanish. Thus the quotient f prime divided by f has a simple pole at a, even when f has a higher-order zero. Its residue is exactly m.

This is a wonderful compression of local information. A double zero contributes residue two. A fifth-order zero contributes residue five. If you look only at f itself, a high-order zero means increasingly flat behavior near the center. If you look instead at the logarithmic derivative, all that complexity collapses to a simple reciprocal term with an integer coefficient.

The story reverses for poles. If f has a pole of order m at a, it looks like h divided by z minus a to the m-th power, with h holomorphic and nonzero at a. Differentiate and divide by f. The reciprocal term now has a minus sign: negative m divided by z minus a. The residue is negative m.

So the logarithmic derivative assigns a positive integer to each zero and a negative integer to each pole, both counted with multiplicity. The remaining analytic pieces contribute no residue at those points.

This turns the residue theorem into a counting mechanism. Instead of integrating f, integrate its logarithmic derivative around a closed contour. The contour integral becomes two pi i times the number of enclosed zeros minus the number of enclosed poles, each counted with its order.

## What the contour measures geometrically

The same formula has a geometric interpretation. Suppose f has no zero or pole along the contour. As the input travels once around the boundary, its image under f traces a closed curve that avoids zero. The image may cross itself, retrace part of its path, or speed up and slow down. None of those details changes its net winding around zero, which is the geometric quantity counted by the argument principle.

Imagine tracking a continuously varying angle of the output vector as you travel along the boundary. The angle can increase and decrease, but after returning to the starting output its total change must be an integer number of full turns. That integer is the winding number of the output path about zero.

Locally, differentiating a complex logarithm of f gives f prime divided by f. Integrating this logarithmic derivative along the contour records the total change of logarithmic magnitude plus i times the change of angle. Because the output returns to its starting point, the net change of logarithmic magnitude is zero. Only the integer number of angular turns remains. The integral is two pi i times that integer.

We do not require a single-valued complex logarithm on the whole region inside the contour. If we did, we could be excluding the very zeros and poles we want to detect. We only need a continuous choice of angle along the parameter interval of the boundary path; its endpoint value may differ from its starting value by a whole number of turns.

The argument principle says these two integers are the same: the winding number of the image curve equals the number of zeros minus the number of poles inside, with multiplicity. The local factorization proves the residue calculation; the contour geometry explains why the answer must be an integer.

Here is a model you can visualize. Take f of z equal to z cubed and let the input run once counterclockwise around the unit circle. The output runs around the unit circle three times. There is one zero at the origin, but it has multiplicity three. The argument principle returns three, exactly matching the three rotations.

Now take one divided by z. The output moves clockwise once while the input moves counterclockwise. There is one pole at zero, and the count is negative one. The direction of rotation remembers the sign.

## Zeros minus poles is not the same as zeros

For a rational example, take f of z equal to z minus one quarter, squared, divided by z plus one half. On the unit disk the numerator has a double zero at one quarter, and the denominator has a simple pole at negative one half. Neither lies on the boundary. The argument principle says the image of the unit circle winds once counterclockwise around zero: two zeros minus one pole equals one.

It would be a mistake to report two on the basis of that winding number alone. The contour integral gives zeros minus poles. If we know separately that the function has no poles inside, the count is a count of zeros. For polynomials that simplification is automatic: they are entire, so they have no finite poles.

It is also essential that the boundary contain no zeros or poles. If f crosses zero while we trace the boundary, the output path passes through the point whose winding we want to measure. The winding number about zero is then undefined, and the logarithmic derivative is singular on the contour. A tiny perturbation can change how many roots are inside by pushing a boundary root inward or outward.

This is why checking the boundary is part of the theorem, not an optional numerical detail.

## Rouché's theorem: a boundary comparison that counts roots

Now suppose we have two functions, f and g, holomorphic on an open set containing a closed disk. Imagine that on the disk's boundary the magnitude of g is strictly smaller than the magnitude of f. The larger term f never vanishes on the boundary, because zero cannot have a magnitude greater than a nonnegative number. The sum f plus g cannot vanish on the boundary either, because the reverse triangle inequality gives its magnitude at least the magnitude of f minus the magnitude of g, which is positive.

Consider continuously turning on g. At the beginning we have f. At the end we have f plus g. At an intermediate time t between zero and one, we have f plus t times g. The same magnitude inequality shows that none of these intermediate functions vanishes at any boundary point.

Each intermediate function maps the input boundary to a closed output curve that avoids zero. Those output curves deform continuously into one another without passing through zero. Their winding numbers about zero cannot change during that deformation. A winding number is an integer, and continuous deformation that never crosses the excluded point cannot jump it from one integer to another.

By the argument principle, the winding number of each output curve equals the number of zeros inside, because all of these functions are holomorphic and have no poles. Thus f and f plus g have the same number of zeros inside, counted with multiplicity.

That is Rouché's theorem. Its practical power comes from the fact that the dominant function f is often a monomial, whose zero count is obvious. We do not have to solve the perturbed polynomial. We only prove a strict inequality on the boundary.

## A degree-six polynomial without solving for a single root

Consider the polynomial z to the sixth power plus five times z squared plus two. Ask how many roots lie inside the unit circle. On the boundary, the modulus of z is one. The magnitude of five times z squared is exactly five. The remaining part, z to the sixth plus two, has magnitude at most one plus two, which equals three.

So five times z squared strictly dominates the rest everywhere on the circle. By Rouché's theorem, the full polynomial has the same number of zeros inside as five times z squared. The latter has a zero at zero of multiplicity two, and no others. Therefore our degree-six polynomial has exactly two roots inside the unit circle, counted with multiplicity.

This is an exact statement. We did not find the roots, and we did not need to. Four of the six roots lie outside the closed unit disk, because our strict inequality also rules out any roots directly on the unit circle. The Fundamental Theorem of Algebra tells us there are six roots in total when multiplicity is counted.

Notice how the proof uses only an inequality and the geometry of the boundary. The individual roots could be awkward algebraic numbers. Their exact coordinates do not matter for this counting question.

## Changing the boundary reveals another count

Let us use a second example to see that different contours can reveal how roots are distributed by distance. Consider z to the fifth power plus three z plus one.

On the unit circle, the magnitude of three z is three. The remaining terms, z to the fifth plus one, have magnitude at most two. Therefore three z dominates and Rouché's theorem says the polynomial has exactly one root in the unit disk.

Now consider the circle of radius two. There the magnitude of z to the fifth is thirty-two. The magnitude of three z plus one is at most seven. This time the leading term dominates. The polynomial therefore has five roots inside the disk of radius two.

Both inequalities are strict, so there are no roots on either circle. Subtract the counts. Exactly four roots lie in the annulus between radii one and two, and exactly one lies inside radius one. We still have not found a single explicit root, but we have located the whole root population in two radial regions.

That is a powerful pattern. Vary the contour and compare with a simpler function. As long as the inequality remains valid, the number of zeros inside is fixed. When the inequality stops being provable, it does not mean the root count necessarily changes. It means that particular argument no longer certifies the answer.

## What strict inequality protects

Why is the strict sign important? Suppose someone says it is enough for the perturbation to have magnitude less than or equal to the dominant function. Take f of z equal to z and g of z equal to negative z. On the unit circle their magnitudes are equal. But f plus g is identically zero, so it has no isolated zero count at all. The deformation passes through zero everywhere on the boundary at its endpoint.

Or consider a perturbation that moves one root across the boundary. At the crossing, the polynomial vanishes at a boundary point, exactly the event excluded by a strict inequality. A non-strict comparison cannot guarantee that the zero count stays fixed.

Rouché's theorem also does not say that the roots themselves move only a little when the perturbation is small on the boundary. It guarantees a total count, not a one-to-one matching between individual roots, and not an error bound for their locations. To localize each root, one can apply the theorem separately on smaller contours, provided suitable inequalities can be established on each one.

Another subtlety is the difference between counting multiplicity and counting distinct roots. If a root has order three, it contributes three to the argument principle and to Rouché's theorem. These results count algebraic multiplicity. A proof yielding two zeros might describe two simple roots or one double root. Additional reasoning is needed to distinguish those cases.

## Why this matters beyond polynomial exercises

The same logic works for holomorphic functions that are not polynomials, so long as we can control their boundary values on the region of interest. Suppose a complicated analytic function is close, on a chosen circle, to a simpler function with known zeros. If the error is strictly smaller than the reference function's modulus everywhere on the circle, Rouché's theorem preserves the total number of zeros inside.

In numerical analysis, this is one source of rigorous root certification. A computed approximation to a function can be paired with a rigorous uniform error bound on a contour. If that error bound is smaller than the computed reference's boundary modulus, the true function and the reference have the same number of roots inside. The certificate concerns a whole region, not just a floating-point guess at a root.

The argument principle is also a conceptual bridge to topology. The count of zeros and poles is encoded by how a boundary image winds around a forbidden output value. A local analytic phenomenon—multiplicity at a point—has become a global topological integer. The residue theorem supplies the exact numerical connection between the two.

There are further consequences of this rigidity. A nonconstant holomorphic function maps open regions to open regions. Its modulus cannot have a genuine local maximum at an interior point unless the function is locally constant, and on a connected domain that means constant everywhere. Those results fit the same theme: holomorphicity in two real dimensions is much more constraining than ordinary smoothness.

The central achievement here is already complete. We can count complex zeros without solving for them. The logarithmic derivative turns zeros into positive residues and poles into negative ones. The residue theorem turns those residues into an integral. The integral records winding of boundary values around zero. And Rouché's theorem lets us preserve that winding when a boundary-dominant term is perturbed. All four viewpoints agree, provided we verify the domain, the boundary, and the multiplicities instead of relying on a suggestive picture.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Argument principle

Let \(\Gamma\) be a positively oriented piecewise-smooth Jordan curve, and f meromorphic on a neighborhood of its closure and interior, with no zeros or poles on \(\Gamma\). Write Z and P for the numbers of zeros and poles in the interior, **with multiplicity**. Then

\[
\frac1{2\pi i}\oint_\Gamma \frac{f'(z)}{f(z)}\,dz=Z-P
=\operatorname{wind}(f\circ\Gamma,0).
\]

If \(f(z)=(z-a)^m h(z)\) near a zero with h(a) nonzero, \(f'/f=m/(z-a)+h'/h\), hence residue m. If \(f(z)=h(z)/(z-a)^m\) near a pole, the residue is -m. Apply the residue theorem to \(f'/f\).

**Winding interpretation:** Along the parameterized boundary, choose a continuous lift of the argument of \(f\circ\Gamma\); this exists because the parameter interval is simply connected and the image avoids zero. Its endpoint change is \(2\pi\) times an integer. The real part of the complex logarithmic change cancels because the curve is closed; the integral records \(i\) times the angular change. No global logarithm on the interior is required.

### Rouché's theorem

If f,g are holomorphic on a neighborhood of the closure of a Jordan domain U, and \(|g(z)|<|f(z)|\) for every \(z\in\partial U\), then f and f+g have the same number of zeros in U, with multiplicity.

**Proof by homotopy:** \(H_t=f+t g\), \(0\le t\le1\), never vanishes on the boundary because \(|H_t|\ge |f|-t|g|>0\). Winding number of the boundary image is unchanged under this homotopy; apply the argument principle to each \(H_t\), which is holomorphic, hence has no poles.

### Certified root counts

1. On \(|z|=1\), for \(p(z)=z^6+5z^2+2\), choose \(f(z)=5z^2\) and \(g(z)=z^6+2\): \(|f|=5>|g|\le3\). Therefore exactly **two** roots lie in \(|z|<1\), counted with multiplicity.
2. For \(q(z)=z^5+3z+1\), on \(|z|=1\): \(|3z|=3>|z^5+1|\le2\), giving **one** root. On \(|z|=2\): \(|z^5|=32>|3z+1|\le7\), giving **five** roots. Thus there are exactly **four** roots in \(1<|z|<2\), and no roots on either circle.
3. For \(f(z)=(z-1/4)^2/(z+1/2)\) on the unit circle, zeros count Z=2, pole count P=1, and winding =1.

### Exercises with answers

1. Compute the contour integral \(\oint_{|z|=1}(f'/f)dz\) for \(f(z)=(z-1/4)^2/(z+1/2)\). **Answer:** \(2\pi i\).
2. Count the zeros of \(z^7+9z^3+1\) in the unit disk. **Answer:** Three, since \(|9z^3|=9>|z^7+1|\le2\) on the boundary.
3. Explain why applying Rouché with a non-strict inequality can fail. **Answer:** f=z, g=-z satisfy \(|g|=|f|\) on the unit circle, but f+g is identically zero; winding and isolated zero counts cannot be used.
4. Does Rouché guarantee that two roots counted inside a disk are distinct? **Answer:** No. Multiplicity is counted; a double root counts twice.
5. Can the argument principle be applied directly if the contour passes through a zero of f? **Answer:** No. The logarithmic derivative is singular there, and winding of the output path about zero is undefined.
6. Suppose \(f(z)=e^z\). What is \((2\pi i)^{-1}\oint f'/f\,dz\) around any closed Jordan contour? **Answer:** Zero, since e^z is entire and has no zeros or finite poles. Indeed \(f'/f=1\).

### Sources and further reading

- MIT OpenCourseWare, *18.04 Complex Variables with Applications*, Topic 11, Argument Principle: https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/lecture-notes/.
- MIT OpenCourseWare, *18.112 Functions of a Complex Variable*, Lecture 14: https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- Wikipedia, *Argument principle*: https://en.wikipedia.org/wiki/Argument_principle.
- Wikipedia, *Rouché's theorem*: https://en.wikipedia.org/wiki/Rouch%C3%A9%27s_theorem.
- [Tero Kilpeläinen and Antti Vähäkangas, Complex Analysis 2 (2024)](https://users.jyu.fi/~salomi/teaching/ca2_2024/Lecture_notes_eng.pdf) — Section 4.2: argument principle and zero counting by the logarithmic derivative.
