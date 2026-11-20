# Strategies When Information Is Private: Bayesian Games and Bidding

<!-- BEGIN SPOKEN LECTURE -->

Suppose Alice is willing to pay up to eighty dollars for an object, and Bob would pay up to fifty. They are asked to submit bids without seeing each other's valuations. Alice can reason about Bob's incentives, but she cannot calculate his best response by inserting a known number into a payoff table. Bob's valuation is part of the strategic problem and part of his private information.

An ordinary simultaneous game can describe hidden actions. It cannot, without extra structure, describe the fact that different players know different payoff-relevant facts. For that we introduce **types**. A type is information privately observed by a player: a valuation, a cost, a signal, or some other variable affecting payoffs and beliefs. A Bayesian game specifies a set of possible types, a probability distribution over them, the actions available, and the payoffs for each type and action profile. A strategy is no longer a single action. It is a rule assigning an action, or a probability distribution over actions, to every type the player might have.

This is a consequential shift in perspective. Alice does not first choose her action and then learn how much she cares about the result. The mathematical model asks her to choose a **contingent plan**: what would she do if her valuation were twenty, if it were fifty, or if it were eighty? The plan as a whole must be optimal conditional on each type's information and beliefs.

## Nature moves before the players

A convenient way to model incomplete information is to imagine a first move made by Nature. Nature draws a profile of types from a specified prior distribution. Each player sees their own type, perhaps receives a signal about others, and then chooses an action. The players understand the probabilistic structure but not necessarily the realized types of their opponents. This is the Harsanyi type-space construction. It turns uncertainty about payoffs into a game with incomplete observations.

Let us distinguish two uses of probability. A mixed strategy randomizes a player's own action, possibly after observing their type. A prior or posterior belief represents uncertainty about which state or other-player type has occurred. They are not interchangeable. A pure Bayesian strategy can be completely deterministic as a function of type even though its observed actions are random to an outside observer who does not know the type.

A Bayesian Nash equilibrium requires that every player's type-contingent strategy be optimal against the other players' strategies, given that type's beliefs. Under a common prior, the type observes its private information and updates the distribution of other types accordingly. The incentive constraint is therefore a conditional expectation. It is not enough to show that a strategy performs well on average across a player's types if one particular type could gain by choosing differently.

This matters because a rare type may have very different incentives. Imagine a contractor who knows its own repair cost but a customer who knows only a distribution of costs. A high-cost contractor and a low-cost contractor may both be rational, while following different bidding policies. Testing only the contractor's average payoff could disguise an incentive for one type to misrepresent the work.

## Bayesian updating is not yet strategic signaling

Before tackling bidding, consider an information problem with no strategic sender. A device has a hidden condition, Healthy or Faulty. The prior probability of Healthy is two fifths. A test reports Good with probability three quarters when the device is healthy and one fifth when it is faulty. What does a Good result mean?

The probability of Healthy and Good together is two fifths times three quarters, or three tenths. The probability of Faulty and Good is three fifths times one fifth, or twelve hundredths. The overall probability of Good is forty-two hundredths. Bayes' rule therefore gives a posterior probability of Healthy conditional on Good equal to thirty over forty-two, or five sevenths.

Suppose a technician can undertake a repair investment that pays four units if the device is healthy and loses three if faulty. Given a probability p of health, the expected payoff from investing is four p minus three times one minus p, or seven p minus three. It is worthwhile when p exceeds three sevenths. The prior probability, two fifths, is slightly below that threshold, so the technician would not invest without information. After a Good report, five sevenths is above the threshold, so investment becomes worthwhile.

This calculation is decision theory with information, not yet a strategic signaling game. Nature generates the test result according to a fixed statistical rule. If a seller could choose whether to display the result, conceal it, or pay to manipulate it, the seller's action would depend on their type and incentives. The buyer would have to infer information from an action selected by another strategic player, not simply update from a known laboratory process. That distinction is at the center of signaling and adverse-selection models.

A Bayesian game can include either situation. What makes it a game is that more than one decision maker selects actions that affect one another's payoffs. Beliefs govern the expectations entering best responses. Equilibrium connects those beliefs to the strategies that other types actually follow.

## A first-price sealed-bid auction

Consider the simplest nontrivial auction model. Two bidders have private values for one object. Each value is drawn independently and uniformly from zero to one, and each bidder learns only their own value. Both submit nonnegative bids simultaneously. The highest bidder wins and pays their own bid; the other pays nothing. If a bidder with value v wins at price b, their payoff is v minus b. If they lose, the payoff is zero. Assume risk-neutral utility, independent private values, and no cost to submitting a bid.

We seek a symmetric Bayesian Nash equilibrium: a bidding function beta so that every type v finds beta of v optimal when the opponent uses the same function. Guess that bidders shade their valuations by bidding half of them. That is, a bidder with value v bids v divided by two. The guess is not an arbitrary slogan about bidding low. We can derive it from a conditional optimization problem.

Suppose Bob follows the rule beta of w equals w divided by two. Alice has private value v and considers bidding b, where b lies between zero and one half. She wins if Bob's value w is less than two b. Since w is uniform on zero to one, the probability of winning is two b. Her profit conditional on winning is v minus b. Therefore her expected payoff is two b times v minus b. Multiply it out: two v b minus two b squared.

Differentiate this expression with respect to the bid. The derivative is two v minus four b. It vanishes at b equal to v divided by two. The second derivative is negative four, so this is the unique maximizer within the interior range. Since v is between zero and one, v divided by two lies between zero and one half, exactly the admissible interval we used for the formula. At the endpoints the same formula remains optimal, with harmless indifference at the zero type.

We should still check deviations above one half. If Alice bids more than one half while Bob follows the proposed policy, she wins almost surely. Her payoff then is v minus b, which decreases as b increases. Among such bids, the best limiting value occurs at one half. The value from the proposed bid is v squared divided by two. The value from bidding one half and winning is v minus one half. Their difference is one half times the square of v minus one, which cannot be negative. Thus no bid above one half does better. Negative bids were excluded by the auction rules. We have checked the complete strategy space.

This proves that bidding half one's value is a best response to an opponent who also bids half their value. By symmetry, the two type-contingent bidding functions are a Bayesian Nash equilibrium. The interesting word is **type-contingent**. All players follow the same functional rule, yet an observer sees different bids because different players know different values. One cannot reduce this to a single mixed-strategy probability over two bid amounts.

At value eight tenths, Alice bids four tenths. Her probability of winning against the proposed opponent policy is eight tenths. Her profit if she wins is four tenths. Expected payoff is thirty-two hundredths. Bidding her whole valuation would win for sure but earn zero if she won. Bidding zero would almost never win and also earn essentially zero. The equilibrium bid balances a higher chance of winning against the cost of paying more when winning.

## Where the result depends on assumptions

The half-value formula is not a universal first-price auction rule. With more bidders, the winning probability for a given bid changes. Under the symmetric independent uniform model with n bidders, the equilibrium bid is the fraction n minus one over n of the private value. As competition increases, equilibrium shading becomes smaller. With correlated values, asymmetric distributions, risk aversion, reserve prices, or other auction formats, the bidding function must be rederived. There are also strategic questions when participation or information acquisition is a choice.

The calculation does, however, give a precise comparison for a later lecture. Under our symmetric equilibrium the object is awarded to the bidder with the higher value, because the bidding function is strictly increasing. The high-value bidder pays **their own shaded bid**. In a different auction format, the winner might pay the other bidder's bid. That rule will change the incentives so sharply that reporting one's actual private value becomes a dominant strategy rather than merely a Bayesian best response to a particular opponent policy.

Let us also connect Bayesian Nash equilibrium to the ordinary version. In a complete-information game with fixed payoffs, players choose best responses to known strategies. In an incomplete-information game, players choose best responses **given their types**, integrating over the opponents' possible types and their strategies. If there is only one possible type for every player, the Bayesian definition collapses to the ordinary Nash definition. It is a generalization, not an unrelated theory.

For formalization, the definitions suggest a clean hierarchy. Begin with a measurable type space and a distribution of type profiles. Define the actions and utility function. Define a strategy as a function from local observations to actions, or to probability distributions over actions. Define an interim payoff by conditional expectation. Then assert that for every player and almost every observed type, no alternative local action yields a higher interim payoff. In a finite type space, we can avoid measure-theoretic complications and work with finite sums. For continuous uniform types, the proof needs an integration framework and care at measure-zero boundaries such as tied bids.

Our auction derivation was a verification argument: assume a candidate bidding strategy and prove that no type can gain by deviating. It did not establish uniqueness among all imaginable equilibria, and it did not prove the existence theorem for arbitrary Bayesian games. Those are separate questions. This distinction is good mathematical hygiene. A correct candidate solution is not automatically a complete classification of all solutions.

The practical lesson is that private information changes the object being optimized. A player's strategy is a policy across possible states, and the other players must reason about which policy is being followed from the actions they observe. That can create inefficient trade, misreporting incentives, strategic silence, and prices that encode information. The next problem is almost the inverse one. Instead of asking how rational players behave under a fixed auction, we can ask whether a designer can choose the rules so that reporting private information honestly is itself optimal.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A Bayesian game has players \(i\), type spaces \(\Theta_i\), action sets \(A_i\), common prior \(P\) over \(\Theta=\prod_i\Theta_i\), and utilities \(u_i(a,\theta)\). A pure strategy maps types to actions: \(s_i:\Theta_i\to A_i\). A Bayesian Nash equilibrium satisfies, for each player and each relevant type \(\theta_i\),
\[
\mathbb E[u_i(s_i(\theta_i),s_{-i}(\theta_{-i}),\theta)\mid\theta_i]
\ge \mathbb E[u_i(a_i,s_{-i}(\theta_{-i}),\theta)\mid\theta_i]
\quad\text{for all }a_i\in A_i.
\]
With continuous types, pay attention to regular conditional probabilities and almost-sure interpretation.

**Exogenous signal example.** Prior \(P(H)=2/5\), likelihoods \(P(G\mid H)=3/4\), \(P(G\mid\neg H)=1/5\). Then
\[
P(H\mid G)=\frac{(2/5)(3/4)}{(2/5)(3/4)+(3/5)(1/5)}=\frac57.
\]
A project giving \(+4\) in state \(H\) and \(-3\) otherwise has expected value \(7p-3\); threshold \(p=3/7\). The prior \(2/5\) is below the threshold; the posterior \(5/7\) is above.

**Two-bidder first-price equilibrium.** Private values \(v,w\overset{iid}{\sim}\mathrm{Uniform}[0,1]\). The candidate symmetric strategy is \(\beta(v)=v/2\). For deviation bid \(0\le b\le1/2\),
\[
\Pr(\beta(w)<b)=2b,\quad U_v(b)=2b(v-b),\quad U'_v(b)=2v-4b,\quad U''_v(b)=-4.
\]
Optimal bid is \(b=v/2\), payoff \(v^2/2\). For \(b>1/2\), payoff \(v-b\le v-1/2\le v^2/2\), since \(v^2/2-v+1/2=(v-1)^2/2\). Therefore \(\beta\) is a symmetric Bayesian Nash equilibrium.

**Exercises and solutions.** (1) Find the prior probability of a Good test. *Solution:* \(0.3+0.12=0.42\). (2) What bid does a value-0.6 player submit at the symmetric first-price equilibrium? *Solution:* 0.3. Winning probability 0.6 and expected utility 0.18. (3) Why does the auction proof check bids above one half? *Solution:* The derivative calculation used only the range where winning probability is \(2b\); outside it the probability saturates at one. (4) Can an uninformative public coin replace hidden type information? *Solution:* no; a public coin does not tell a player which private valuation was drawn and does not alter the type-conditioned payoff.

### Sources and reading

- MIT OpenCourseWare, *Economic Applications of Game Theory*, Chapters 14-16 and Lectures 16-18 (Fall 2025): https://ocw.mit.edu/courses/14-12-economic-applications-of-game-theory-fall-2025/resources/lecture-notes/
- Open Yale Courses, Ben Polak, *Game Theory*, Lectures 23-24 on signaling and auctions: https://oyc.yale.edu/economics/econ-159
- MIT OpenCourseWare, *Game Theory with Engineering Applications*, course scope and auction applications: https://ocw.mit.edu/courses/6-254-game-theory-with-engineering-applications-spring-2010/pages/syllabus/

The reliability signal, posterior threshold, and auction derivation are independently calculated examples.
