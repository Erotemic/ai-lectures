# 002000 — And, Or, Not, and If: Reading Mathematical Logic

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Statements and counterexamples. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# And, Or, Not, and If: Reading Mathematical Logic

Suppose I tell you: if a number is divisible by four, it is even. You understand the claim without a truth table. Yet translating it into precise logic reveals why some very familiar errors are errors. The statement is a conditional: when the premise holds, the conclusion must hold. It does not say that every even integer is divisible by four. It does not say that a number not divisible by four must be odd. Those would be different statements.

We will use letters P and Q for propositions. 'P and Q' requires both. 'P or Q' in ordinary mathematical logic means at least one of the two; it permits both. 'Not P' says P fails. 'If P, then Q' rules out exactly the situation in which P is true but Q is false. If we work in classical logic, these meanings can be displayed completely in a short table of truth values.

## What the conditional actually promises

Why do mathematicians accept a conditional with a false premise as true? Imagine a guarantee: for every integer that enters a certain machine, if the integer is a multiple of four, its output is even. The machine encounters the number six, which is not a multiple of four. The guarantee places no constraint on this case. Whatever happens to six cannot violate the conditional promise. This is the mathematical meaning of an implication, not a claim that the premise somehow caused the conclusion.

An implication is different from its converse. 'Multiple of four implies even' is true. 'Even implies multiple of four' fails at six. The inverse, 'not a multiple of four implies not even,' fails at six as well. The contrapositive, 'not even implies not a multiple of four,' is equivalent to the original implication in ordinary classical mathematics. The contrapositive changes both the direction and the truth status of the two conditions, and it is a valid route for proving the original.

A mathematician may write 'P if Q' to mean that Q implies P. 'P only if Q' reverses the role: it means P implies Q. 'P if and only if Q' asks for both directions. These short phrases are responsible for many errors when readers skim a proof. Try translating each into a plain conditional before doing any algebra.

## Combining information

Suppose a number is divisible by both two and three. We can say that it satisfies two properties joined by 'and.' If we learn a statement of the form 'it is divisible by two or by three,' we know at least one property holds but cannot assume which one. A valid argument from such an 'or' statement may need two cases. In the first, the number is divisible by two; in the second, by three. If both cases lead to the desired conclusion, then we may conclude it without deciding which alternative actually held.

Negation is also structural. The negation of 'P and Q' is 'not P or not Q.' The negation of 'P or Q' is 'not P and not Q.' These are De Morgan's laws. One way to remember them is to imagine what would have to go wrong for a two-part requirement to fail: at least one part is missing. For an either-or promise to fail, neither option is available.

Consider 'the integer is positive and even.' Its negation is 'the integer is not positive, or it is not even.' It would be wrong to demand both failures. Three is not even, so it already defeats the original conjunction even though it is positive.

## Sound inference versus convincing language

There are standard patterns of correct inference. From P and 'if P then Q,' conclude Q. This is sometimes called modus ponens. From 'if P then Q' and 'not Q,' conclude 'not P.' This is modus tollens. In contrast, from 'if P then Q' and Q, we cannot conclude P. The fact that a number is even does not tell us it is divisible by four. This error is called affirming the consequent. Likewise, knowing that P is false does not make Q false; denying the antecedent is not a valid inference.

These patterns matter inside longer arguments. A proof may contain correct computations while making an incorrect logical transition between them. When a step feels dubious, replace the mathematical nouns with the neutral names P and Q. The bare pattern often makes the missing information obvious.

## Meaning before notation

Truth tables are helpful for finite combinations of propositions, but mathematics quickly goes beyond any fixed list of statements. We ask what happens for every integer, every function, or some particular witness. That requires quantifiers. For now, keep one discipline: every time you use an implication, state what you are assuming and what you intend to obtain. Every time you use an 'or,' make sure the argument handles all alternatives. And every time you use an 'if and only if,' check that neither direction has been left unproved. The symbols are shorthand for obligations, not substitutes for reasoning.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Propositional truth conditions

| \(P\) | \(Q\) | \(P\land Q\) | \(P\lor Q\) | \(P\Rightarrow Q\) |
|---|---|---|---|---|
| T | T | T | T | T |
| T | F | F | T | F |
| F | T | F | T | T |
| F | F | F | F | T |

The converse is \(Q\Rightarrow P\). The inverse is \(\neg P\Rightarrow\neg Q\). The contrapositive is \(\neg Q\Rightarrow\neg P\), classically equivalent to the original. In fact \(P\Rightarrow Q\) is equivalent to \(\neg P\lor Q\) in classical propositional logic.

### Exercises with answers

1. Translate 'A only if B.' **Answer:** \(A\Rightarrow B\).
2. Translate 'A if B.' **Answer:** \(B\Rightarrow A\).
3. Is \((P\lor Q)\land\neg P\Rightarrow Q\) valid? **Answer:** yes; the \(P\) branch is excluded.
4. Find a counterexample to 'divisible by three implies divisible by six.' **Answer:** \(n=3\).

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [forall x: Calgary, A Free and Open Introduction to Formal Logic (Open Logic Project)](https://forallx.openlogicproject.org/).
- [Wikipedia: Logical connective](https://en.wikipedia.org/wiki/Logical_connective).
