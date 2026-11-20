# Rules That Make Truthful Play Rational: Auctions and Mechanism Design

<!-- BEGIN SPOKEN LECTURE -->

In the usual game-theory problem, the rules are given and we ask which strategies rational players will adopt. An auction reverses the emphasis. Someone is choosing the rules: what bidders may report, who receives the object, and what everyone pays. The designer wants the participants to reveal private information or to choose actions that produce a desirable outcome. But the participants have their own objectives. A rule that would work beautifully if everyone answered honestly may perform badly if honesty is costly.

This is mechanism design. It studies games as objects we can construct. The central mathematical question is not whether a player will be morally persuaded to report the truth. It is whether the rules make truthful behavior a best response, perhaps even a best response regardless of what other players report. We will work through an auction where that strong property holds, then derive the larger idea behind Vickrey-Clarke-Groves mechanisms.

First we need a model of preferences. Suppose one indivisible object can be assigned to at most one bidder. Bidder i has a privately known value v for owning it. If the bidder receives the object and pays a price p, their utility is v minus p. If they do not receive it and pay nothing, their utility is zero. This is the quasi-linear, private-values model. It is mathematically convenient because transfers of money enter utility additively. It does not describe every real-world bidder: budget constraints, risk preferences, resale options, and interdependent values may matter. But with these hypotheses, incentive comparisons become transparent.

## A rule with a built-in reason to tell the truth

Consider a sealed-bid, second-price auction. Everyone submits a nonnegative bid. The highest bidder wins the object. The winner pays the **second-highest** bid; everyone else pays zero. Ties are resolved according to an announced rule. A bid is a message to the mechanism, not itself a payment. The bidder's actual value is private; the reported bid need not equal it.

Suppose Alice values the object at nine, Bob at six, and Carol at four. If they report their values, Alice wins and pays six. Her utility is three. Bob and Carol lose and receive zero utility. Alice could have offered a bid of seven or one hundred and still won at the same price, provided it remained above six. She has no reason to raise her reported bid simply to increase her chance of winning more of the object; there is only one object, and winning's price is determined by the competition, not her own bid.

A numerical story is helpful, but we want a theorem. Fix every other bidder's reports, no matter how arbitrary they are. Let m be the highest of those reports. The bidder whose incentives we study has true value v. If they submit a bid above m, they win and, ignoring tie complications for the moment, pay m. Their utility is v minus m. If they bid below m, they lose and get zero. The bidder's own bid determines which side of this threshold they land on, but not the price paid conditional on crossing it.

There are three cases. If v exceeds m, winning is better than losing because v minus m is positive. Truthful bidding, b equals v, crosses the threshold and wins. If v is below m, winning yields a negative utility, so losing is preferable. Truthful bidding falls below m and loses. If v equals m, winning at price m and losing both give zero utility. Truthful bidding is again no worse than the alternatives, with the tie rule handling the boundary.

That proves truthful bidding is a **weakly dominant strategy**. The proof holds for every vector of other bids, not merely when others are honest, and not merely under a particular belief distribution about their values. 'Weakly' is important: the bidder can often make other bids without changing the outcome or payoff. A dominant strategy does not have to be uniquely optimal. The theorem also does not say someone cannot benefit from coordinated misreports, because coalitional deviations are a different question.

Compare this with the first-price auction. There, the winner pays their own bid. Increasing a bid can improve the probability of winning but reduces the surplus conditional on winning. In the two-bidder uniform-value example, bidding half one's value is a symmetric Bayesian Nash equilibrium of the first-price auction, not a dominant strategy. That result depends on the distribution of opponents' types and their equilibrium behavior. The second-price truthfulness theorem is stronger and simpler: after fixing the other bids, the player's optimization problem divides at one threshold.

It is tempting to conclude that second-price auctions always earn the seller less money. That is false as a general claim. Under the two-bidder independent uniform-value, risk-neutral, symmetric benchmark, the first-price equilibrium gives the highest-value bidder's bid equal to half the winning value. The expected winning value is two thirds, so expected revenue is one third. In the second-price truthful equilibrium, revenue is the lower of the two independent uniform values, whose expectation is also one third. Equal expected revenue here is a special case of a broader revenue-equivalence phenomenon with substantial assumptions. Change reserves, risk attitudes, information structure, or bidder asymmetries, and the comparison can change.

A mechanism can simplify incentives without guaranteeing any particular revenue ranking across every possible environment. It can make the game strategically transparent yet still require careful modeling of valuations, participation, and how ties or defaults are handled.

## From auctions to choosing a common project

The second-price auction assigns one object. A community might instead have to choose a public project or allocate a collection of resources. We would like to select the outcome that maximizes the sum of participants' values. Private information makes this difficult: someone can exaggerate the value of their preferred outcome to influence the choice. Could a payment rule neutralize that incentive?

Start with two possible projects, A and B. Alice values A at eight and B at zero. Bob values A at zero and B at five. Under truthful reports, maximizing reported total value selects A, since eight exceeds five. But the allocation rule alone is manipulable. Bob might report an enormous value for B to make the mechanism choose B. A payment can make this sort of manipulation expensive in exactly the right cases.

The Vickrey-Clarke-Groves family of mechanisms begins with a declared value for each outcome from each participant. It selects an outcome maximizing the **sum of declared values**. To compute player i's payment, one may use a Clarke pivot rule: compare the maximum total value the other players could receive if i did not participate with the total value those same other players receive under the outcome selected when i does participate. Charge player i the difference. The payer is being charged for the value their presence displaces among the others.

Compute the payments in our project example, allowing either project regardless of whether someone participates. Without Alice, Bob can obtain value five by choosing B. With Alice present, the mechanism chooses A, which gives Bob zero. So Alice's payment is five minus zero, or five. Her net utility from project A is eight minus five, or three. Without Bob, Alice can obtain value eight by choosing A. With Bob present, the mechanism still chooses A, giving Alice eight. Bob's payment is eight minus eight, or zero. This result resembles a second-price auction even though the alternatives are public projects rather than private ownership of an object.

Now see the proof idea. Fix everyone else's reports. For player i, the mechanism chooses an outcome x that maximizes the sum of i's **reported** value and the other players' fixed reports. Under a VCG payment, the utility player i actually receives is their **true** value for x plus the sum of the others' reported values for x, minus a constant that depends only on the others' reports. Crucially, that constant does not depend on i's message. If i reports their true values, the mechanism chooses an outcome maximizing exactly the expression that determines i's true utility, apart from the constant. Lying may select a different outcome, but it cannot select one with a larger value of that expression.

This argument establishes dominant-strategy incentive compatibility for truthful reporting under the quasi-linear model and an allocation rule that genuinely maximizes the reported total over the feasible outcomes. The result is not about participants all sharing the same social objective. They optimize their individual utilities, while the payment rule aligns their private optimization with truthful selection. The trick is algebraic: arrange payments so each participant internalizes the effect of their reported preferences on the others.

The formal statement contains a detail worth retaining. General Groves payments need only have the form of an arbitrary function of the others' reports minus the sum of the others' reported values at the chosen outcome. The Clarke pivot choice is one particular arbitrary function, the best total the others can obtain without i. Different choices can preserve truthfulness while changing transfers and participation incentives. The budget outcome is not predetermined by incentive compatibility alone.

## Direct reports and the revelation principle

Mechanisms need not ask everyone to write down their value. They might request a bid, choose a bargaining protocol, or conduct a sequence of messages. In a complex mechanism, players could have equilibrium strategies that translate their private types into messages. The **revelation principle** says, roughly, that if a social choice rule can be implemented through an equilibrium of an indirect mechanism under a specified information model and equilibrium concept, then it can also be implemented by a corresponding direct mechanism in which truth-telling is an equilibrium.

Here is the construction. Imagine the original mechanism with its equilibrium strategies. In a new direct mechanism, each player reports their private type. The mechanism then simulates the action that type would have taken under the original equilibrium and implements the original allocation and payment. If a player could gain from a false type report in the direct mechanism, they could have made the corresponding deviation in the original equilibrium by sending the message assigned to that false report. That would contradict the assumed equilibrium condition. So truthful reports implement the same outcome rule under the corresponding solution concept.

This does **not** mean every social goal is implementable or that the direct mechanism is practically convenient. It is a reduction of the search space: when investigating what is possible under given incentive constraints, we may often study truthful direct mechanisms without losing implementable outcomes. The conditions are part of the theorem. Bayesian implementation generally yields truthful reporting in Bayesian equilibrium; dominant-strategy implementation yields a stronger direct truthfulness property when the original assumptions support it.

Mechanism design is full of impossibility boundaries. For instance, with unrestricted ordinal preferences over at least three alternatives, deterministic social-choice rules that can select any of at least three alternatives and satisfy strategy-proofness are severely constrained: the Gibbard-Satterthwaite theorem implies dictatorship under the unrestricted-preferences model with at least two voters. That is not a contradiction of VCG. VCG relies on cardinal, quasi-linear values and monetary transfers, while the classic voting theorem treats a different model. The most useful habit is to keep track of which preferences, payments, and information are allowed before transporting an impossibility or existence result between settings.

Even within quasi-linear environments, desirable properties may conflict. An efficient, truthful rule may not balance its budget. It may require positive transfers or impose charges that deter participants. A mechanism that is truthful for individuals may be vulnerable to coalitions, identities controlled by one participant, or strategic manipulation of the feasible alternatives. If private values are correlated or participants value the same hidden quality, an argument that assumes independent private values cannot simply be reused unchanged.

## The mechanism as a program with a specification

This makes mechanism design a natural subject for formal methods. We can define an environment with types, outcomes, feasible allocations, utilities, and transfers. A mechanism is a function from reports to an allocation and a payment vector. Truthfulness becomes a quantified property: for every player, every true type, every set of other reports, and every alternative report, truthful utility is at least the utility obtained by deviating. Efficiency becomes a different property: the chosen allocation maximizes the sum of true valuations when reports are truthful. Individual rationality and budget balance are yet more predicates.

The second-price proof is a small verified-program pattern. Fix an arbitrary opponent-report vector. Compute the highest competing bid m. Split on whether the player's true value is greater than, equal to, or less than m. Show the truthful choice is optimal in every case. The VCG proof is a more general algebraic refinement: rewrite the player's true utility as total reported welfare with the player's true value substituted, minus a report-independent term, and use the maximizing property of the allocation rule.

This style of reasoning connects back to every previous part of the course. A game is a function of choices and payoffs. A Nash equilibrium is a certificate of mutual best responses. A Bayesian equilibrium checks type-conditioned expected payoffs. Subgame perfection checks continuation behavior after every relevant history. A mechanism designer chooses a new game and proves that the desired strategies satisfy the right incentive constraints. The mathematical structures differ, but all rely on carefully stating which deviations are allowed and which information is fixed when comparing them.

The central result is not that one auction format wins every contest or that incentives can solve every social problem. It is that rules can sometimes make a complicated strategic question easier by changing what it is profitable to report. Truthful behavior then follows from a theorem about individual payoffs, rather than a hope about personal virtue. And where the theorem fails, its hypotheses tell us exactly which part of the institution needs a different model.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For quasi-linear utilities \(u_i(x,p_i;v_i)=v_i(x)-p_i\), a direct mechanism \((x(\hat v),p(\hat v))\) is dominant-strategy incentive compatible (DSIC) iff
\[
\forall i,v_i,\hat v_i,\hat v_{-i}:\quad
v_i(x(v_i,\hat v_{-i}))-p_i(v_i,\hat v_{-i})\ge
v_i(x(\hat v_i,\hat v_{-i}))-p_i(\hat v_i,\hat v_{-i}).
\]
In a second-price single-object auction, fixing the maximum other bid \(m\) makes winning utility \(v_i-m\) and losing utility zero. Truthful bidding selects the preferable side of this threshold for any \(m\) and tie rule that does not depend manipulably on the bidder's report.

For a feasible outcome set \(X\), Groves mechanisms select
\[
x^*(\hat v)\in\arg\max_{x\in X}\sum_j\hat v_j(x),\qquad
p_i(\hat v)=h_i(\hat v_{-i})-\sum_{j\ne i}\hat v_j(x^*(\hat v)),
\]
where \(h_i\) does not depend on \(\hat v_i\). The Clarke pivot choice is \(h_i(\hat v_{-i})=\max_{x\in X_{-i}}\sum_{j\ne i}\hat v_j(x)\), with \(X_{-i}\) the feasible outcomes without player i, when this counterfactual is defined. After fixing other reports, the player's utility when reporting truthfully equals
\[
v_i(x^*)+\sum_{j\ne i}\hat v_j(x^*)-h_i(\hat v_{-i}),
\]
which is maximized by the allocation rule if \(\hat v_i=v_i\). This proves DSIC under the model's feasibility, maximization, and quasi-linearity assumptions.

**Project example.** Two feasible projects A and B. Alice values \((8,0)\), Bob values \((0,5)\). Choose A for total welfare 8. Alice's pivot payment is 5 and net utility 3; Bob's pivot payment is 0 and net utility 0. The externality payment and welfare result are exact for the specified project model.

**Revenue benchmark.** For independent uniform \([0,1]\) values \(V_1,V_2\), \(\mathbb E[\max(V_1,V_2)]=2/3\) and \(\mathbb E[\min(V_1,V_2)]=1/3\). The first-price symmetric equilibrium bid \(v/2\) generates expected winning bid \(1/3\). A truthful second-price auction generates expected payment \(\mathbb E[\min(V_1,V_2)]=1/3\). This equality is not universal across auction environments.

**Exercises and solutions.** (1) In a second-price auction, value 7 and highest competing bid 9: should a truthful bidder win? *Solution:* no; winning would pay 9 and yield utility negative 2. (2) With value 7 and competing bid 4? *Solution:* truthful bidding wins and gives utility 3. (3) Why can a Groves payment include any \(h_i\) independent of the player's own report? *Solution:* it contributes the same constant to all outcomes considered in the player's optimization and cannot change which report maximizes true utility. (4) Does DSIC imply budget balance? *Solution:* no; truthfulness and budget balance are separate properties. (5) Does the revelation principle imply every desired allocation rule is implementable? *Solution:* no; it reduces the representation of mechanisms that are already implementable under the stated equilibrium concept.

### Sources and reading

- MIT OpenCourseWare, *Economic Applications of Game Theory*, Lectures 18-20 on auctions, revenue equivalence, and allocation rules: https://ocw.mit.edu/courses/14-12-economic-applications-of-game-theory-fall-2025/pages/calendar/
- MIT OpenCourseWare, *Game Theory with Engineering Applications*, course treatment of VCG mechanisms and incentive compatibility: https://ocw.mit.edu/courses/6-254-game-theory-with-engineering-applications-spring-2010/pages/syllabus/
- Open Yale Courses, Ben Polak, *Game Theory*, Lecture 24, auctions: https://oyc.yale.edu/economics/econ-159

The project allocation example is an independent exercise of the Clarke pivot formula. The theorem qualifications reflect the mathematical mechanism models, not claims about all real auctions.
