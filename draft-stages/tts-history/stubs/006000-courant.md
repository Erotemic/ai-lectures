# 006000 — Richard Courant: How can an eigenvalue be characterized without finding its eigenvector?

**Track:** History · People and ideas. **Theme:** Variational approximation. **Background:** introductory linear algebra; the lecture defines its local objects.

<!-- BEGIN SPOKEN LECTURE -->

# Richard Courant: How can an eigenvalue be characterized without finding its eigenvector?

A matrix may be large enough that explicitly finding all its eigenvectors is cumbersome. But perhaps we can characterize one eigenvalue through a simpler optimization problem over directions and subspaces.

Richard Courant combined analysis, partial differential equations, and applied mathematics. His career linked research on variational principles with the teaching of mathematical methods for physics and computation. The Courant–Fischer min–max principle carries his name together with Ernst Fischer's. That joint name identifies a mathematical characterization, not necessarily a single jointly authored article.

Consider a symmetric three-by-three matrix with eigenvalues one, three, and seven. The largest eigenvalue is the largest Rayleigh quotient among all unit vectors: seven. The smallest is the smallest quotient: one. To characterize the middle eigenvalue, we can ask a more interesting question. Choose any two-dimensional subspace, then find its smallest Rayleigh quotient. Among all such planes, the largest possible answer is three.

Why? Every plane in three dimensions intersects the span of the first two eigendirections in a nonzero vector. On that intersection, the quotient cannot exceed three. On the other hand, choose the plane spanned by the eigendirections for three and seven; every unit vector in that plane has quotient at least three. The upper and lower pieces agree.

That is the shape of a min–max proof. A dimension argument says that an arbitrary trial subspace cannot avoid certain spectral directions. A carefully chosen spectral subspace attains the bound. No explicit formula for the middle eigenvector is needed in the statement.

This principle also explains why Rayleigh–Ritz approximations are useful. Restrict the Rayleigh quotient to a finite trial subspace. You obtain eigenvalues of a compressed matrix and can compare them with the full operator's variational values. The relationships depend on the ordering and assumptions; one should not treat every compressed eigenvalue as the exact target.

Courant's role is part of the passage from spectral calculation to geometric optimization. The principal-angle theory uses similar dimension reasoning when it compares subspaces, singular values, and residuals. A successful proof often starts by identifying the right extremal quantity.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

For Hermitian \(A\) on \(\mathbb C^n\) and ascending eigenvalues,
\(\lambda_k(A)=\max_{\dim S=n-k+1}\min_{x\in S,\|x\|=1}\langle Ax,x\rangle\).
For \(\operatorname{diag}(1,3,7)\), the middle value is \(3\). Its maximizing
plane is \(\operatorname{span}(e_2,e_3)\); any two-plane intersects
\(\operatorname{span}(e_1,e_2)\).

## Reading notes (non-spoken)

The linked biography or contributor record identifies the person; the mathematical source documents a related publication or mathematical construction. The accessible topic article supplies background. Publication and personal history are distinguished from later eponymous terminology.
