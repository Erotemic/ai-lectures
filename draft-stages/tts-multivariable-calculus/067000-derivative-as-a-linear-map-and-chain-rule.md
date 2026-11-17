# The Derivative Is a Linear Map: Jacobians You Can Actually Use

<!-- BEGIN SPOKEN LECTURE -->

# The Derivative Is a Linear Map: Jacobians You Can Actually Use

Suppose you have a device with two knobs and two displays. Turning the first knob changes both displays. So does turning the second. Perhaps you can calculate how each display responds when you move one knob and freeze the other. But the question you really want to answer is different: if you move both knobs at once, what happens to both displays?

That is the question a multivariable derivative answers. It is not fundamentally a list of partial derivatives. It is a single linear prediction for the response to a small displacement. A Jacobian matrix is how we write that prediction in coordinates.

## A complete two-input, two-output calculation

Let the first display report x squared plus x times y. Let the second report x times y plus y squared. We begin at the settings x equals one and y equals two. The readings are three and six.

Now change x by a small amount a and change y by a small amount b. Expand the first display at the new settings. The change in its reading has a first-order piece, four a plus b, and a remaining piece, a squared plus a times b. Expand the second display. Its first-order change is two a plus five b, with remainder a times b plus b squared.

These first-order changes are the derivative. They describe the output displacement caused by the input displacement. The first output is predicted to move by four times the x adjustment plus one times the y adjustment. The second is predicted to move by two times the x adjustment plus five times the y adjustment.

Put the two predictions together, and you have a two-by-two matrix: first row four, one; second row two, five. Multiplying that matrix by the column of knob adjustments produces the predicted column of display changes. It is one operation, not four unrelated computations.

Try actual numbers. Increase x by one hundredth and decrease y by two hundredths. The matrix predicts a first display change of two hundredths and a second change of minus eight hundredths. If we compute the displays exactly, their changes are one hundred ninety-nine ten-thousandths and minus seven hundred ninety-eight ten-thousandths. The differences from the linear prediction are minus one ten-thousandth and plus two ten-thousandths.

Those are not mysterious rounding errors. They are precisely the quadratic remainder terms from the expansion. If we halve both knob changes, the first-order prediction is halved, but those remainder terms become one quarter as large. That unequal rate of shrinkage is the defining feature of differentiability.

## What the small error condition actually says

There are two separate claims in saying that a function is differentiable. The first is that some linear map gives a plausible prediction. The second is that the error becomes negligible compared with the total size of the input displacement.

Imagine walking toward the original knob settings from any direction. The predicted change should differ from the true change by a quantity which, when divided by the distance walked, tends to zero. It is not enough for the error itself merely to approach zero. The error must approach zero faster than the displacement.

In our polynomial example, the remainder is built from products of two small adjustments. If the adjustment vector has length r, each individual adjustment is at most r. So every remainder term has magnitude at most a constant times r squared. Divide by r, and the bound is a constant times r. This tends to zero along every approach. We have verified the defining condition rather than relying only on the existence of partial derivatives.

This explains why the derivative is unique. Suppose two different linear rules both approximate the same function with an error smaller than first order. Follow any fixed direction and make your step shorter. The difference between those two linear rules, divided by the step length, cannot stay nonzero; otherwise one of them would have a first-order error. They must agree on every direction, so they are the same linear map.

## A partial-derivative trap

A partial derivative asks what happens along one coordinate axis. A total derivative asks for a prediction that works for all combinations of inputs. The distinction is not semantic.

Consider a function that is zero at the origin, and elsewhere is x cubed divided by x squared plus y squared. Along the x axis the function equals x. Along the y axis it equals zero. Its two partial derivatives at the origin are therefore one and zero.

If those partials formed a genuine derivative, the linear prediction at the origin would simply be the x adjustment. But follow the diagonal path where x and y are equal. The true function value is half the x coordinate. The proposed linear prediction is the whole x coordinate. The error is half the step's x component; it is first order, not smaller than first order.

There is an even stronger warning here. Every directional derivative along a straight line exists for this example. If the direction is the vector with components a and b, the directional derivative is a cubed divided by a squared plus b squared. Yet that rule is not linear in the direction. A collection of directional derivatives, even one for every straight line, does not automatically define a derivative matrix.

Fortunately there is a practical sufficient condition. If all first partial derivatives exist and are continuous throughout a neighborhood of the point, then the function is differentiable there. We can regard this as a guarantee that the axis-by-axis first-order information fits together consistently. It is sufficient, not necessary; differentiability does not require every partial derivative to be continuous in a neighborhood.

## Composition: pass a displacement through two machines

Now suppose our two knobs are themselves controlled by two other settings, u and v. The first knob equals u plus v. The second equals u minus v. If u is one and a half and v is minus one half, the knobs are again at one and two.

The first transformation converts a tiny change of u and v into changes of x and y. Increasing u by a little increases both x and y by that amount. Increasing v increases x but decreases y. Its derivative matrix has first row one, one and second row one, minus one.

The display machine then transforms changes of x and y into changes of the two readings. We already know its matrix: four, one in the first row and two, five in the second. To predict the combined change, first apply the knob transformation, then the display transformation. In matrix language, multiply the display Jacobian by the knob Jacobian, in that order.

The result has first row five, three and second row seven, minus three. Thus a small increase of u changes the first display by about five times that increase and the second display by seven times it. A small increase of v changes the first display by about three times that increase and the second by minus three times it.

You can verify a column without trusting matrix notation. Change u alone. Then both x and y increase. The first display's change rate is four from x plus one from y, giving five. The second's rate is two from x plus five from y, giving seven. That is the first column of the product. Changing v makes x increase and y decrease, producing three and minus three. The second column checks as well.

This is the multivariable chain rule: the derivative of a composition is the composition of derivatives. It is why the order of the matrices matters. Matrix multiplication is not commutative; swapping the matrices would describe a different sequence of transformations, and often the sizes would not even match.

## A path through a field

A useful special case is a path through a scalar field. Imagine temperature at position x, y is x squared plus three times y squared. A moving sensor follows the path with x equal to cosine of time and y equal to sine of time. The derivative of temperature along the path is the temperature gradient dotted with the path velocity.

At time zero the sensor is at one, zero. Its velocity points straight up, while the gradient of this temperature field points horizontally. Their dot product is zero. The temperature has zero instantaneous rate of change along that path at that instant, even though the gradient is not zero. Move in a direction perpendicular to a gradient, and the first-order change of a scalar field vanishes.

That is what a directional derivative means when a true derivative exists. We apply one linear rule to the chosen velocity. The gradient is simply the coordinate vector for that linear functional under the Euclidean dot product. For functions with several outputs, the Jacobian takes over the same role.

## Coordinate change versus a physical change

A final distinction prevents confusion later. Sometimes x and y are two physical controls and u and v are different physical controls attached to them. At other times, u and v describe the very same point in a different coordinate system. The chain rule still looks the same, but the interpretation changes.

A derivative matrix depends on which bases or coordinates we use to describe inputs and outputs. The underlying linear map does not. And a matrix with two rows and three columns is not defective merely because it is not square: it represents a map from three-dimensional input changes to two-dimensional output changes.

Before advancing to inverse functions, integrals, or Newton methods, practice a simple habit. Name the input space, name the output space, compute the Jacobian at a specific point, apply it to an actual displacement, and check the size of the neglected terms. If you can do all five, you know what the derivative is doing rather than merely how to calculate its entries.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Definition and quantified remainder

For an open set \(U\subset\mathbb R^n\), a map \(F:U\to\mathbb R^m\) is Fréchet differentiable at \(p\) if there is a linear map \(A:\mathbb R^n\to\mathbb R^m\) with
\[
F(p+h)=F(p)+Ah+r(h),\qquad \lim_{h\to0}\frac{\|r(h)\|}{\|h\|}=0.
\]
In standard coordinates \(A=DF(p)=(\partial F_i/\partial x_j)_{i,j}\).

For \(F(x,y)=(x^2+xy,xy+y^2)\) at \(p=(1,2)\):
\[
F(p)=(3,6),\quad DF(p)=\begin{pmatrix}4&1\\2&5\end{pmatrix},\quad
r(a,b)=\begin{pmatrix}a^2+ab\\ab+b^2\end{pmatrix}.
\]
If \(r_0=\sqrt{a^2+b^2}\), then each entry of \(r(a,b)\) has magnitude at most \(2r_0^2\), so \(\|r(a,b)\|_2\le 2\sqrt2\,r_0^2\). The linearization error is \(o(r_0)\). With \((a,b)=(0.01,-0.02)\), \(DF(p)(a,b)=(.02,-.08)\) and \(r=(-.0001,.0002)\).

### Directional derivatives are not enough

Define \(f(0,0)=0\) and \(f(x,y)=x^3/(x^2+y^2)\) otherwise. It is continuous at the origin because \(|f(x,y)|\le |x|\). Every two-sided directional derivative exists, and for \(v=(a,b)\ne0\),
\[
D_vf(0)=\lim_{t\to0}\frac{f(tv)-f(0)}{t}=\frac{a^3}{a^2+b^2}.
\]
But \(D_{(1,0)}f=1\), \(D_{(0,1)}f=0\), and \(D_{(1,1)}f=1/2\), violating additivity. Thus there is no total derivative.

### Chain rule calculation

For \(G(u,v)=(u+v,u-v)\) and \((u,v)=(3/2,-1/2)\):
\[
DG=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
D(F\circ G)=DF(1,2)DG=\begin{pmatrix}5&3\\7&-3\end{pmatrix}.
\]
In general \(D(F\circ G)(q)=DF(G(q))\circ DG(q)\) for differentiable maps with compatible domains and codomains.

### Scalar field along a path

For \(T(x,y)=x^2+3y^2\) and \(\gamma(t)=(\cos t,\sin t)\),
\[
\frac{d}{dt}T(\gamma(t))=\nabla T(\gamma(t))\cdot\gamma'(t)
= -2\cos t\sin t+6\sin t\cos t=4\sin t\cos t.
\]
The derivative is zero at \(t=0\).

### Exercises with answers

1. **Three-dimensional output.** For \(H(x,y)=(x+y,xy,x^2-y)\), compute \(DH(1,2)\) and \(DH(1,2)(a,b)\). **Answer:** the \(3\times2\) matrix has rows \((1,1),(2,1),(2,-1)\), so the change is \((a+b,2a+b,2a-b)\).
2. **Error estimate.** Explain why the polynomial example is differentiable even when \(a\) and \(b\) approach zero at unrelated speeds. **Answer:** the uniform bound \(\|r(a,b)\|\le2\sqrt2\,(a^2+b^2)\) depends only on total displacement length.
3. **A directional counterexample.** Compute the directional derivatives of \(x^3/(x^2+y^2)\) at the origin and test additivity. **Answer:** \(a^3/(a^2+b^2)\); compare directions \((1,0),(0,1),(1,1)\).
4. **Chain-rule dimensions.** If \(G:\mathbb R^4\to\mathbb R^2\) and \(F:\mathbb R^2\to\mathbb R^3\), what are the Jacobian sizes and their product? **Answer:** \(DG\) is \(2\times4\), \(DF\) is \(3\times2\), and \(D(F\circ G)\) is \(3\times4\).
5. **Directional temperature.** For \(T=x^2+3y^2\) at \((1,1)\), find the derivative along the unit direction \((3/5,4/5)\). **Answer:** \(\nabla T=(2,6)\), so \(D_vT=6/5+24/5=6\).

### Sources and further reading

- [OpenStax, *Calculus Volume 3*, §4.5, The Chain Rule](https://openstax.org/books/calculus-volume-3/pages/4-5-the-chain-rule), introductory multivariable chain-rule computations.
- [MIT OpenCourseWare 18.02SC, *Multivariable Calculus*](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), independent worked differentiation and geometry problems.
- [Wikipedia: Fréchet derivative](https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative), the coordinate-independent small-error definition.
- [Wikipedia: Jacobian matrix and determinant](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant), dimensions, derivative entries and matrix representation.
- Existing survey: `multivariable-calculus:001000` gives the introductory overview; this lecture expands the displacement calculations and remainder tests.
