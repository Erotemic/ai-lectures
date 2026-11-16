# 024200 - Weak Derivatives and Sobolev Estimates on Manifolds

**Track:** Topology and Geometry. **Background:** multivariable calculus, integration by parts, vector bundles, compactness. **Central question:** what kind of convergence and multiplication can we expect from fields whose derivatives are controlled only on average?

<!-- BEGIN SPOKEN LECTURE -->

# Weak Derivatives and Sobolev Estimates on Manifolds

Smooth functions are convenient for doing geometry, but they do not form a complete space under most of the estimates produced by differential equations. Imagine approximating a connection on a bundle by a sequence of smooth connections. Suppose their curvature energies remain bounded. The sequence need not approach a smooth connection in any naive pointwise sense. If we want to say what a limit means, we need a language for derivatives, convergence, and products that survives taking limits.

That language begins with weak derivatives and Sobolev spaces. They are not an alternative kind of calculus, restricted to pathological functions. They are the completion of ordinary calculus in the measurements that partial differential equations naturally control.

## Learning a derivative from integration

Consider a function on a line. For a smooth function, integration by parts lets us move a derivative from the function to a compactly supported test function, at the price of a minus sign. This equation still makes sense if the original function merely has a locally integrable value. We declare that it has a weak derivative if there exists another locally integrable function that satisfies the same integration-by-parts rule for every smooth test function.

Take the absolute value function. Its ordinary derivative fails to exist at zero. Its weak first derivative is minus one to the left and plus one to the right. The single troublesome point does not prevent the weak derivative from being an ordinary bounded function. But the weak derivative of a step function is different. It involves a concentrated Dirac distribution at the jump; a step function is not in the first Sobolev space based on square-integrable derivatives.

A first Sobolev space records functions whose values and first weak derivatives are both square integrable. Higher Sobolev spaces record more derivatives. It matters which integrability exponent we use, because the same derivative estimate has very different strength in different dimensions.

## Why averaging changes convergence

On a circle, imagine a smooth sine wave making more and more oscillations. Divide its amplitude by its frequency. The resulting functions approach zero uniformly, and hence in square-integrable norm. But their first derivatives still have an oscillation of fixed size. Consequently they do not approach zero in the first Sobolev norm.

This simple example separates boundedness from compactness. A sequence can be bounded in the first Sobolev norm without possessing a subsequence converging strongly in that same norm. On a compact manifold, however, the Rellich compactness theorem supplies a smaller target: a bounded first-Sobolev sequence has a subsequence that converges strongly in square-integrable norm. There are no escape-to-infinity problems because the manifold is compact, but arbitrarily rapid oscillations still prevent strong convergence at the original derivative level.

We also distinguish weak convergence from strong convergence. Weak convergence says that every continuous linear measurement of the sequence converges; strong convergence says the norm of the difference tends to zero. A bounded sequence in a Hilbert Sobolev space has a weakly convergent subsequence. Rellich often turns that weak convergence into strong convergence in a lower-order norm. Neither statement, by itself, upgrades the limit to a smooth function.

## Dimension determines which products make sense

Here is the estimate that will matter repeatedly in four-dimensional gauge theory. On a compact four-dimensional manifold, a function or section with one square-integrable derivative belongs to the fourth-power integrable space, with a bound controlled by its first Sobolev norm. The same holds componentwise in local trivializations of a vector bundle.

This gives a way to multiply two rough fields. If each is fourth-power integrable, their product is square integrable, by the Holder inequality. So the quadratic part of curvature, a wedge product of two connection perturbations, makes sense at the integrability level supplied by first Sobolev regularity. The linear part of curvature involves one derivative and is also square integrable.

But do not infer that a first-Sobolev section in four dimensions is continuous. It need not be. Continuity requires stronger conditions, such as one derivative in an integrability power strictly larger than four, or enough additional derivative regularity. This failure of automatic continuity is one reason gauge transformations and nonlinear equations need carefully selected function spaces.

## From a coordinate chart to a manifold

The definitions begin on Euclidean space, but a compact smooth manifold can be covered by finitely many coordinate charts. Choose a partition of unity, multiply by its cutoff functions, and measure derivatives in each chart. Different smooth coordinate systems give equivalent Sobolev norms. On a vector bundle, choose local frames and use a connection to define covariant derivatives. Different smooth choices again lead to equivalent norms on a compact manifold.

These equivalences are essential. They show that the Sobolev space is geometric even though we use coordinates to estimate its elements. The metric and connection influence the norm, but on a fixed compact manifold they do not change which sections belong to the space.

On noncompact spaces the story needs additional hypotheses. Uniform geometric control, support conditions, and weights can affect embedding and compactness. We must not transport every compact-manifold theorem to an arbitrary open manifold without checking those conditions.

## Why the distinction matters in gauge theory

A connection can be written locally as a fixed smooth reference connection plus a Lie-algebra-valued one-form. In four dimensions, if that perturbation has one square-integrable derivative, its curvature is square integrable. The estimate tells us the nonlinear expression is defined. It does not say a bounded sequence of such connections is compact before allowing gauge transformations, nor does it say that a limit solves the same nonlinear equation.

That is the road ahead. First establish useful function spaces. Then obtain elliptic estimates for equations in those spaces. Finally, understand the additional symmetry and concentration phenomena that obstruct ordinary compactness.

The crucial lesson is that a bound is informative only when we know which topology it controls. Square-integrable curvature energy, weak convergence of connections, strong convergence of lower derivatives, and smooth convergence away from singularities are different statements. The advanced theorems work because they keep those statements separate and prove the steps connecting them.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an open set \(\Omega\subset\mathbb R^n\), \(u\in W^{k,p}(\Omega)\) iff all distributional derivatives \(\partial^\alpha u\) with \(|\alpha|\leq k\) belong to \(L^p\). For a weak first derivative \(v_i\),
\[\int_\Omega u\,\partial_i\varphi\,dx=-\int_\Omega v_i\varphi\,dx\qquad(\varphi\in C_c^\infty(\Omega)).\]
On \(S^1\), \(u_m(\theta)=\sin(m\theta)/m\) satisfies \(u_m\to0\) in \(L^2\), but \(\|u_m'\|_{L^2}=\sqrt{\pi}\), so it does not converge in \(H^1=W^{1,2}\).

For a closed smooth four-manifold \(X\), \(W^{1,2}(X)\hookrightarrow L^4(X)\) continuously, but not generally into \(C^0(X)\). Rellich gives \(W^{1,2}(X)\hookrightarrow L^2(X)\) compactly. For bundle-valued one-forms \(a,b\),
\[\|a\wedge b\|_{L^2}\leq C\|a\|_{L^4}\|b\|_{L^4}\leq C'\|a\|_{W^{1,2}}\|b\|_{W^{1,2}}.\]
With smooth reference connection \(A_0\), \(F_{A_0+a}=F_{A_0}+d_{A_0}a+a\wedge a\), using a consistent Lie-algebra bracket convention. This establishes \(F_{A_0+a}\in L^2\) when \(a\in W^{1,2}\), without asserting compactness of connection moduli.

### Exercises with answers

1. **Weak derivative.** What is the first weak derivative of \(|x|\) on a bounded interval containing zero? **Answer:** \(\operatorname{sgn}(x)\) almost everywhere; its value at zero does not matter.
2. **Oscillation.** Why do \(\sin(m\theta)/m\) fail to converge to zero in \(H^1(S^1)\)? **Answer:** the derivative has constant nonzero \(L^2\) norm.
3. **Four-dimensional product.** Which exponents make \(a\wedge b\in L^2\) if \(a,b\in L^4\)? **Answer:** Holder with \(1/4+1/4=1/2\).
4. **Limit.** Does boundedness in \(H^1\) guarantee strongly convergent \(H^1\) subsequences? **Answer:** no; on compact manifolds it gives weak \(H^1\), and a strong \(L^2\) subsequence.

### Sources and further reading

- Harvard Math 212b, [Elliptic Engineering: Sobolev spaces and elliptic estimates](https://people.math.harvard.edu/archive/212_spring01/lectures/ellipticity.pdf).
- Emmanuel Hebey, [Nonlinear Analysis on Manifolds: Sobolev Spaces and Inequalities](https://doi.org/10.1090/cln/005) (book; publisher access may apply).
- Overviews: [Sobolev space](https://en.wikipedia.org/wiki/Sobolev_space), [Rellich-Kondrachov theorem](https://en.wikipedia.org/wiki/Rellich%E2%80%93Kondrachov_theorem).
