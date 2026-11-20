# What Can Be Forgotten Without Breaking the Operation? Quotients and the Isomorphism Theorems

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic  
**Lecture:** 091000  
**Preparation:** Group multiplication, subgroups, and the notion of a homomorphism; orbit–stabilizer is useful but not required.  
**Companion:** Normality, quotient well-definedness, the first, second, and third isomorphism theorems, and subgroup correspondence.

<!-- BEGIN SPOKEN LECTURE -->

Suppose two integers are considered equivalent whenever their difference is a multiple of twelve. We can add equivalence classes and get an unambiguous answer. We can also subtract them, and if we multiply remainders we get a consistent product. The integers have been compressed into twelve possible states without destroying the arithmetic operations they inherit.

Now take the eight rigid symmetries of a square. We might want to remember only whether a symmetry preserves or reverses orientation. A rotation becomes one kind of outcome; a reflection becomes the other. Again, the original object has been compressed to a two-element group without losing the rule for composing transformations.

These two examples suggest a general question. What information may we forget while still preserving the operation? The answer leads to normal subgroups, quotient groups, and three closely related isomorphism theorems. They tell us how algebraic structures can be assembled, simplified, and compared.

## Why a subgroup is not always enough

Every subgroup H partitions a group G into left cosets: sets of the form g H, with g running through G. A coset collects elements differing by multiplication on the right by an element of H. Lagrange's theorem tells us that each coset has the same number of elements, namely the size of H.

But counting cosets is not the same as multiplying cosets. We would like to say that the product of g H and k H is the coset g k H. That rule works only if changing the representatives g and k does not change the answer.

Suppose g is replaced by g h-one and k by k h-two, with both h elements in H. Their product becomes g h-one k h-two. To bring the hidden h-one to the right of k, we must replace it by the conjugate k inverse h-one k. For the product to remain in g k H, that conjugate must belong to H. We need conjugation by arbitrary elements of G to preserve H.

That is the definition of a normal subgroup. A subgroup N is normal when g N g inverse equals N for every g in G. Then the cosets can be multiplied independently of representatives, and the quotient G modulo N is itself a group.

In an abelian group, conjugation changes nothing, so every subgroup is normal. That is why modular arithmetic and ordinary additive cosets are so accommodating. Noncommutative groups demand more care.

## One square, two very different subgroups

Let r be a quarter-turn of a square and s be a reflection, with the familiar relation s r s equals r inverse. The rotations form a four-element subgroup N: the identity, r, r squared, and r cubed. This subgroup is normal. Conjugating a rotation by another rotation leaves it unchanged, and conjugating by a reflection changes the direction of the turn but keeps it a rotation.

There are exactly two cosets, N itself and s N. Their multiplication reproduces the two-element group. Two reflections compose to a rotation; a reflection followed by a rotation is a reflection. The quotient has forgotten the angle of rotation and retained only orientation parity.

Compare the two-element subgroup H consisting of the identity and the chosen reflection s. This is a perfectly legitimate subgroup. But it is not normal. Conjugating s by a quarter-turn produces r squared s, a different reflection outside H. If we tried to multiply left cosets using representatives, changing a representative could change the alleged product coset. The object G modulo H still exists as a set of left cosets, and G acts on it, but it does not inherit the usual quotient-group multiplication.

So the obstruction is not to making equivalence classes. We can always make those. The obstruction is to having an operation on classes that does not depend on arbitrary choices of representatives.

## Kernels are the information a homomorphism loses

Suppose phi is a homomorphism from G to another group K. It preserves multiplication: phi of g h equals phi of g times phi of h. The kernel of phi consists of those inputs sent to the identity of K.

The kernel is normal. To see why, take an element n in the kernel and conjugate it by an arbitrary g. Its image is phi(g), followed by the identity, followed by phi(g) inverse. That product is the identity. So the conjugate remains in the kernel.

There is a deeper characterization. Two inputs g and h have the same image exactly when h inverse g lies in the kernel. In other words, a homomorphism identifies two inputs precisely when they differ by something the homomorphism cannot see.

This observation nearly proves the first isomorphism theorem by itself. Given phi from G to K, form the quotient by its kernel. Map the coset g times the kernel to phi(g). The map is well-defined because all elements of a coset have the same image. It is a homomorphism because phi preserves multiplication. Its image is all of phi of G, by construction. And it is injective because two cosets with the same image must be the same coset. Therefore G modulo the kernel is isomorphic to the image of phi.

The word isomorphic means that the two groups have the same multiplication structure under a bijective, operation-preserving map. The theorem does not claim that the original elements are literally the same. It says that the only identifications made by a homomorphism are those forced by its kernel, and no additional structure is lost after passing to the image.

## Two examples of the first theorem

Consider the map from the integers under addition to the integers modulo twelve. An integer is sent to its remainder class. The kernel is the set of multiples of twelve, written twelve Z. The image is all twelve residue classes. The first isomorphism theorem says that the quotient of the integers by twelve Z is isomorphic to the additive group of residues modulo twelve.

That statement seems familiar because it is how we usually introduce the residues. But it reveals the general mechanism. A congruence is a homomorphism's indistinguishability relation.

Now consider orientation parity for square symmetries. Map rotations to zero and reflections to one in the additive group modulo two. The identity and all rotations form the kernel. The image has two elements. The same theorem says that the square group modulo its rotations is isomorphic to the two-element group. We have not claimed that a square rotation equals the number zero. We have identified a structural feature shared by two different systems.

This construction also explains why a map from a group to a permutation group need not represent every element distinctly. The elements acting trivially form the kernel. Taking the quotient by that kernel produces the group of actually observable permutations.

## Two overlapping ways to simplify a group

The second isomorphism theorem describes how a subgroup and a normal subgroup interact. Let H be any subgroup of G, and N a normal subgroup of G. The set of products H N is a subgroup. Restrict the quotient map from G to G modulo N to H. Its image is H N modulo N. Its kernel consists of elements of H that also lie in N, namely H intersect N. By the first isomorphism theorem, H modulo that intersection is isomorphic to H N modulo N.

This is not a separate miracle. It is the first theorem applied to a carefully chosen homomorphism. Its content is that passing to H and then forgetting H intersect N gives exactly the portion of G modulo N visible from H.

For a concrete calculation, use the integers under addition. Take H to be multiples of four and N to be multiples of six. Their sum consists of all multiples of two: every combination of a multiple of four and a multiple of six is even, and Bézout's identity expresses two as four minus six plus four, or simply as a suitable integer combination of four and six. Their intersection consists of the multiples of twelve.

The theorem says that four Z modulo twelve Z is isomorphic to two Z modulo six Z. Each quotient has three elements. On the left, the representatives may be zero, four, and eight modulo twelve. On the right, they may be zero, two, and four modulo six. The correspondence comes from inclusion of multiples of four into the even integers, followed by reduction modulo six. For example, four maps to four, and eight maps to two. The groups are the same cyclic structure described with different representatives.

Notice that the intersection and sum of these subgroups have arithmetic meanings. For additive integer subgroups, the intersection is governed by the least common multiple, and the sum by the greatest common divisor. The second theorem expresses the relation between these two operations in group-theoretic language.

## Forgetting information in two stages

The third isomorphism theorem handles nested normal subgroups. Suppose N lies inside K and both are normal in G. We can first collapse N and form G modulo N. Inside that quotient, K modulo N is a normal subgroup. Collapsing again gives the same group structure as collapsing K from the start.

Symbolically, G modulo N, and then modulo K modulo N, is isomorphic to G modulo K.

Imagine recording an integer modulo twelve, then forgetting distinctions between residues that differ by a multiple of four. That is the same as recording the integer modulo four directly. Here N is twelve Z and K is four Z. The quotient of Z modulo twelve Z by the three-element subgroup four Z modulo twelve Z has four elements, just like Z modulo four Z.

The useful lesson is about composition. Information loss can be organized into layers. If the layers are compatible normal subgroups, the final quotient depends only on the overall information forgotten, not on whether the forgetting occurred in one step or two.

## The subgroup lattice survives compression

There is one more result that makes quotient groups manageable. The subgroups of G modulo N correspond exactly to the subgroups of G that contain N. To move from a subgroup downstairs to one upstairs, take its full inverse image under the quotient map. To move from a subgroup upstairs containing N to one downstairs, take its image. These operations reverse each other.

The requirement that the upstairs subgroup contain N is essential. Any distinction already erased by the quotient cannot be partially restored by choosing a smaller subgroup downstairs.

For example, the subgroups of the additive group of integers modulo twelve correspond to the subgroups d Z of the integers containing twelve Z. These are the subgroups for d dividing twelve: d equal to one, two, three, four, six, or twelve. The resulting quotient-group subgroups have orders twelve, six, four, three, two, and one respectively.

The correspondence also preserves normality in the appropriate sense. A subgroup above N is normal in G exactly when its image is normal in G modulo N. That makes it possible to study layers of a complicated group by examining a quotient and remembering which structures are still visible there.

## The common spine of the three theorems

The first theorem says that an operation-preserving map factors through the information its kernel forgets. The second compares restricting to a subgroup with collapsing a normal subgroup. The third says that compatible stages of collapsing can be combined. The subgroup correspondence says exactly which substructures remain visible after collapsing.

None of this requires the objects to be numbers. It works for groups of transformations, permutations, matrix groups, and Galois groups. Later, rings will have a parallel story, with ideals taking the role that normal subgroups play here. In each setting, the real question is the same: which distinctions can we identify while preserving the operations that define the structure?

The power of quotient thinking is not that it reduces a large object to a small one. Sometimes it does. Its greater power is that it explains the reduction completely. It tells us what was forgotten, what survived, and why the resulting structure can be used reliably.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(G\) be a group and \(N\trianglelefteq G\). The quotient is the set of cosets \(G/N\), with \((gN)(hN)=(gh)N\). Normality is equivalent to this operation being well-defined (for the usual coset product). If \(g'=gn_1\) and \(h'=hn_2\), then
\[
g'h'=gh(h^{-1}n_1h)n_2\in ghN.
\]

**First isomorphism theorem:** For a homomorphism \(\phi:G\to K\), the function
\[
\bar\phi:G/\ker\phi\longrightarrow\operatorname{im}\phi,
\qquad g\ker\phi\longmapsto\phi(g)
\]
is a well-defined isomorphism.

**Second:** If \(H\le G\), \(N\trianglelefteq G\), then \(HN\le G\), \(H\cap N\trianglelefteq H\), and
\[
H/(H\cap N)\cong HN/N.
\]
Example: \(H=4\mathbb Z\), \(N=6\mathbb Z\), \(H+N=2\mathbb Z\), \(H\cap N=12\mathbb Z\), giving \(4\mathbb Z/12\mathbb Z\cong 2\mathbb Z/6\mathbb Z\).

**Third:** If \(N\trianglelefteq G\), \(K\trianglelefteq G\), and \(N\subseteq K\), then \(K/N\trianglelefteq G/N\) and
\[
(G/N)/(K/N)\cong G/K.
\]

**Correspondence theorem:** Subgroups of \(G/N\) are in bijection with subgroups \(H\le G\) containing \(N\), via \(H\mapsto H/N\) and inverse image under the quotient map.

**Worked checks and exercises**

1. In \(D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\), the rotation subgroup \(\langle r\rangle\) is normal. The reflection subgroup \(\langle s\rangle\) is not, since \(rsr^{-1}=r^2s\notin\langle s\rangle\).
2. Define the homomorphism \(D_4\to C_2\) by \(r\mapsto 0\), \(s\mapsto 1\), and verify its kernel is \(\langle r\rangle\).
3. For \(\mathbb Z/12\mathbb Z\), explicitly identify the subgroup corresponding to \(3\mathbb Z\): it contains \(\{0,3,6,9\}\) and has order four.
4. Show a quotient by a non-normal subgroup need not inherit a group product by checking different representatives of two left cosets in \(D_4/\langle s\rangle\).
5. The ring version uses a two-sided ideal because both addition and multiplication must descend; compare the proof of well-definedness of coset multiplication in groups with the expansion \(ab-a'b'=a(b-b')+(a-a')b'\).

**Source notes:** Judson, *Abstract Algebra*, https://judsonbooks.org/abstract-algebra-theory-and-applications/ ; MIT OCW 18.701 Algebra I, https://ocw.mit.edu/courses/18-701-algebra-i-fall-2010/pages/calendar/ . Earlier lecture `abstract-algebra:001000` provides the first survey of kernels, actions, and quotients.
