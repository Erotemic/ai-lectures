# 002000 - Counting, Conditioning, and Independence: How Evidence Changes the Sample Space

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** fractions and elementary probability. **Theme:** sample spaces, conditional probability, counting, independence, and selection mechanisms.

<!-- BEGIN SPOKEN LECTURE -->

# Counting, Conditioning, and Independence: How Evidence Changes the Sample Space

A colleague tells you that a family has two children and at least one is a boy. What is the probability that both children are boys? Before answering, ask how your colleague learned this information. Did they inspect a randomly selected family and report that at least one child was a boy? Or did they meet one randomly chosen child and observe that this child was a boy? Those two procedures can lead to different answers, even though the spoken phrase sounds nearly identical.

This is one of probability's most important lessons. Evidence is not merely a sentence added to our knowledge. It arrives through a process. The process determines which possibilities are still eligible and how much weight they carry. Conditional probability gives us a language for updating a sample space, and careful counting gives us a way to perform the update without fooling ourselves.

We will examine the geometry of events inside a sample space, derive the counting rules that make conditional probability work, and distinguish genuine independence from the appearance of independence. We will also investigate a famous game-show puzzle, not as a trick question, but as a lesson about the information carried by a selection procedure.

## What did we count in the first place?

Imagine tossing two fair coins. We can list four equally likely outcomes: heads-heads, heads-tails, tails-heads, and tails-tails. Order is part of the modeled outcome because the first toss and second toss are distinguishable positions. The event "exactly one head" contains two outcomes. The event "at least one head" contains three. This simple sample space lets us see where denominators come from.

When we assign probabilities by counting favorable outcomes divided by total outcomes, we are relying on a strong assumption: the elementary outcomes are equally likely. That is true for two independent fair tosses in this model. It is not automatically true for arbitrary labels on outcomes. If we group heads-heads and tails-tails into one category but leave the mixed outcomes as two separate categories, the resulting three named categories are not equally likely.

A general probability space assigns probabilities to events in a way that respects nonnegativity, total probability one, and additivity for disjoint events. Equal counting is a convenient special case. A counting argument is valid only after we have justified the sample space and its weights.

Now let A be the event that the first toss is heads, and B the event that at least one toss is heads. The event A contains two of the four outcomes. Event B contains three. The intersection of A and B is just A, because any first-toss head satisfies the at-least-one-head condition. If we learn B, our eligible outcomes shrink from four to three; among those three, two satisfy A. Therefore the conditional probability of A given B is two-thirds.

This is the definition in action: probability of A and B together, divided by probability of B, provided B has positive probability. The numerator measures the part of B where A also holds. The denominator renormalizes the reduced world B so that its total probability is one.

## Why intersections must be handled carefully

Suppose two events A and B can occur together. The probability that A or B occurs is the probability of A plus the probability of B, minus their overlap. Otherwise the outcomes in both A and B are counted twice. This is inclusion-exclusion for two events.

Think of a survey asking whether people use either of two software tools. If sixty percent use the first and fifty percent use the second, we cannot conclude that one hundred and ten percent use at least one. We need to know how many use both. If twenty percent use both, the proportion using at least one is ninety percent. The repeated twenty percent must be subtracted once.

For three events, the adjustment continues: add the three individual probabilities, subtract each pairwise overlap, then add the triple overlap back. The alternating signs arise from correcting overcounts. If a single outcome lies in all three events, it was counted three times, then removed three times through pairwise intersections, so the triple term restores it once.

There is an intuitive connection to combinatorics. Counting does not merely enumerate objects. It organizes which objects have been counted and how often. That discipline is especially important when rare events arise through many possible routes. The union bound, a simpler inequality, says the chance of at least one among several events is no greater than the sum of their individual probabilities. It does not require independence and is often useful when exact overlaps are difficult to calculate.

## Return to the two-child family

Assume, solely for the model, that child sexes are independent and each child is equally likely to be categorized as a boy or a girl. Also assume we distinguish older and younger child. Then the four family outcomes are boy-boy, boy-girl, girl-boy, and girl-girl, each with probability one-quarter.

If we select a family uniformly from the modeled population and are told the family has at least one boy, we rule out only girl-girl. Three equally likely family outcomes remain, and exactly one is boy-boy. The conditional probability that both children are boys is one-third.

But suppose instead we randomly select one of the two children and observe that the selected child is a boy. There are now eight equally likely outcomes if we record both family composition and which child was selected. The observation favors families containing two boys: such a family always yields a boy upon selection, while a mixed family does so only half the time. Conditioned on having observed a boy, the posterior probability of boy-boy is one-half.

Neither calculation is a universal answer to a bare phrase about two children. Real families also depart from the idealized assumptions. The point is to track the sampling and reporting mechanism. If a question leaves that mechanism unspecified, a confident numerical answer may conceal an invented assumption.

The same issue arises in research. Patients who enroll in a study may be selected because of symptoms. People who answer a survey may differ from those who ignore it. Events that appear rare in the whole population may be common in a database constructed by selecting particular categories of cases. Before updating probabilities, identify how observations entered the dataset.

## Independence is a statement about joint behavior

Two events A and B are independent when the probability of their intersection equals the product of their separate probabilities. When B has positive probability, this is equivalent to saying that learning B does not change the probability of A. Independence concerns the probability model, not a vague feeling that two things are unrelated.

For two fair coin tosses, "first toss is heads" and "second toss is heads" are independent. Each has probability one-half, and both occur with probability one-quarter. Learning the second toss does not change the probability of the first. But "first toss is heads" and "at least one toss is heads" are not independent. Knowledge of the second event changes the probability of the first from one-half to two-thirds.

A frequent mistake is to confuse independence with being mutually exclusive. If two events cannot occur together, their intersection has probability zero. If both have positive probability, the product of their separate probabilities is positive. Thus two mutually exclusive events with positive probability cannot be independent. Knowing one occurred tells us the other did not occur, which is maximal dependence in that direction.

Another mistake is to conclude that because every pair among three events is independent, all three are jointly independent. That is false. Toss two fair coins and define three bits: the first toss, the second toss, and whether the two tosses agree. Each bit can be represented as a zero-or-one event. Any pair is independent, yet the third is determined by the first two. Pairwise independence does not ensure mutual independence.

This example is mathematically compact but conceptually deep. Pairwise tests do not capture all dependence structures. In data science, checking individual correlations between variables may miss relationships involving several variables together. Independence is a structural property of joint distributions, not a synonym for zero linear correlation or a lack of visible pairwise association.

## Conditioning can create dependence

There is an even more surprising phenomenon. Two variables can be independent before we condition, yet become dependent after we restrict attention to a selected group. Imagine two independent causes that can each make an alarm ring. Suppose we learn that the alarm has rung. If we then discover that the first cause occurred, the second cause becomes less necessary as an explanation. Within the alarmed group, the causes are negatively associated even if they were independent in the full population.

We can build a finite model. Toss two independent fair coins. Define an alarm that rings if either coin is heads. Before learning about the alarm, the coin outcomes are independent. Given that the alarm rang, three outcomes remain: heads-heads, heads-tails, and tails-heads. Within this reduced sample space, learning that the first coin is heads reduces the chance that the second is heads from two-thirds to one-half. Without the first-coin information, the chance of second heads in the alarmed group is two-thirds, while with first heads it is one-half.

The correct conditional numbers reveal the effect. Among the three alarmed outcomes, two have second heads, so its conditional probability is two-thirds. Among the two alarmed outcomes with first heads, only one has second heads, so its conditional probability drops to one-half. The conditioning event has opened a statistical relationship that did not exist beforehand.

This phenomenon is often called selection or collider bias. It is a reason that correlations in admitted hospital patients, applicants who passed a screening stage, or articles accepted by a journal may not reflect associations in the broader population. The selected group may have been constructed partly by the variables we are trying to compare.

The practical remedy is to model selection, not to memorize one slogan about bias. What is the population? What event has been conditioned on? Which variables influence inclusion? Independence statements must always specify the underlying probability distribution and any conditioning information.

## A game-show host who knows where the prize is

Consider three closed doors. One conceals a prize. You choose a door, but it remains closed. The host knows where the prize is and opens one of the two doors you did not choose, revealing a door without a prize. The host then offers you the chance to switch to the remaining unopened door. Should you switch?

Under the standard rules, the host must always open a losing door, must never open your chosen door, and must always offer the switch. Your first choice is correct with probability one-third. It is wrong with probability two-thirds. If it is wrong, the host's required action leaves the prize behind the only other unopened door. Switching wins in precisely those original wrong-choice cases. So switching succeeds with probability two-thirds.

Why does this feel counterintuitive? After a door opens, two closed doors remain. It is tempting to call them equally likely. But one is your original selection, made before the host revealed anything. The other was selected by a host whose action was constrained by knowledge of the prize. They do not have symmetric histories.

We can check the claim by listing the three prize locations relative to your initial pick. If the prize is behind your chosen door, switching loses. If the prize is behind either of the other two doors, the host must reveal the remaining losing door and switching wins. Two of the three equally likely prize locations favor switching.

Change the host's behavior and the answer can change. Suppose the host sometimes opens a door at random and accidentally reveals the prize. Or only offers a switch on certain occasions. Then the event that you saw a losing door opened and received an offer carries additional information about the prize location. A careful probability calculation must incorporate the host's policy. The familiar two-thirds result belongs to the specified mechanism, not to the superficial picture of two remaining doors.

## Why conditional probability became a mathematical subject

Many early probability problems concerned games in which a fair division of stakes had to be decided before the game finished. In their 1654 correspondence, Blaise Pascal and Pierre de Fermat investigated such problems, helping to establish systematic reasoning about possible continuations. The human situation was familiar: people were disputing what a partially completed game was worth. Mathematics could replace intuition with a consistent accounting of possible outcomes.

Later work on probability moved well beyond gambling. Thomas Bayes's essay on probability was communicated after his death by Richard Price and appeared in 1763. The paper addressed reasoning from observed results toward unknown chances under specified assumptions. Modern Bayesian inference is much broader than that one essay, but the historical example reminds us that using evidence to revise probability requires a mathematical description of how evidence could have arisen.

The mathematical developments unfolded across several traditions and centuries. Counting methods, analytic probability, statistical inference, and measure-theoretic probability are related but distinct achievements. The value of the early stories is that they put human decisions behind the abstractions: dividing a wager, estimating a hidden chance, deciding whether a pattern is evidence.

## Independence as a model to be tested

We should not treat independence as the default condition of nature. If two measurements share a sensor, a weather influence, or a selection process, their errors may be dependent. If a randomized experiment assigns treatment independently of baseline characteristics, that independence comes from a designed mechanism rather than from wishful thinking. Even then, sampling error can produce accidental imbalances in a finite dataset.

Sometimes conditional independence is the right statement. A medical symptom and a test result may be dependent overall because both respond to an underlying disease state. Within each disease category they might be modeled as independent, although that assumption must be justified. Graphical models use such conditional independence relationships to organize large probabilistic systems.

The most important habit is to say what is being held fixed. "A and B are independent" refers to an unconditional joint distribution. "A and B are independent given C" refers to the distributions obtained after conditioning on C, when those conditional probabilities are defined. Neither implies the other in general.

This clarity is essential when deriving algorithms. An inference method that multiplies probabilities of observations is making an independence assumption, often conditional on some latent state. That assumption may yield a very efficient computation. It may also be the model's principal source of error. Once written explicitly, it can be challenged, tested, or replaced.

## The birthday calculation and the value of a complement

Suppose twenty-three people independently have birthdays uniformly distributed among 365 days, ignoring leap days and seasonal effects. What is the chance that at least two share a birthday? Directly counting every pattern with one or more matches is awkward. Instead, count the complementary event: all birthdays are different.

The first person may be born on any day, so the chance that the first birthday introduces no collision is one. The second person must avoid the first person's day, giving a factor of 364 over 365. The third must avoid two occupied days, giving 363 over 365. Continue until the twenty-third person, who must avoid twenty-two occupied days, giving 343 over 365. Multiply those factors to obtain the probability of no shared birthday, then subtract from one.

The result is a little more than fifty percent. This surprises people who imagine matching their own birthday, but that is a different event. With twenty-three people, there are 253 distinct pairs of people who could match. Pair events overlap and are not independent, so simply adding 253 copies of one over 365 would not be an exact probability. The complement method handles those dependencies through a sequence of conditional probabilities.

The number 365 and the assumption of equal independent birthdays are part of the model. Real birth dates have seasonal patterns and demographic structure, so the exact percentage changes in real populations. The mathematical lesson survives: when a union of many overlapping events is difficult to count, the complement may have a simple sequential structure.

## Diagnostic testing and the base-rate denominator

Suppose a condition affects one person in a hundred. A test is positive in ninety percent of people who have the condition and in ten percent of people who do not. What is the probability that a person with a positive test actually has the condition?

Imagine testing ten thousand people. About one hundred have the condition, and ninety of those test positive. The remaining nine thousand nine hundred do not have the condition, and about nine hundred ninety of those test positive. There are about one thousand eighty positive tests altogether, only ninety of which came from people with the condition. The probability of the condition among positive tests is therefore ninety out of one thousand eighty, or one-twelfth, about eight point three percent.

The sensitivity of the test is ninety percent, but the positive predictive probability is much smaller. The denominator includes every way the positive result can arise. The low prevalence of the condition gives many more opportunities for false positives than for true positives. Bayes' rule expresses the same reasoning algebraically; the population-count version makes the underlying mechanism easier to inspect.

If we select people with symptoms rather than at random, the relevant prevalence may change. If test accuracy differs by age or other covariates, the simple model may need refinement. A conditional probability is only as meaningful as the population and observation process used to calculate it. That is why a base-rate question cannot be answered by reporting test sensitivity alone.

## The question beneath every conditional answer

Probability makes it possible to quantify uncertainty, but it does not tell us automatically how an observation was selected. The denominator of a conditional probability represents the event we learned occurred. If we define that event incorrectly, every subsequent calculation can be internally consistent and still answer the wrong question.

We began with a two-child family and ended with a game-show host, but the lesson is the same. Identify the possible worlds. Specify how each world is weighted. State what observation was made and how it could have been produced. Restrict the probability space accordingly. Only then count or integrate the favorable outcomes.

Independence can simplify the calculation; selection can destroy it; conditioning can create a new dependence. The mathematics is rigorous when the model is explicit. The reasoning becomes reliable when we refuse to let an ambiguous story choose the model for us.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Basic identities

For `P(B)>0`, `P(A|B)=P(A intersect B)/P(B)`. Inclusion-exclusion: `P(A union B)=P(A)+P(B)-P(A intersect B)`. Independence: `P(A intersect B)=P(A)P(B)`.

### Two-child sample mechanisms

Uniform families in `{BB,BG,GB,GG}` given at least one boy: `P(BB | at least one B)=1/3`.

Select one child uniformly at random from a random family and observe that selected child is a boy: `P(BB | selected child is B) = (1/4)/(1/2)=1/2`.

### Collider example

Let independent fair bits be `X,Y`; select if `S=(X=1 or Y=1)`. Then `P(Y=1|S)=2/3`, but `P(Y=1|X=1,S)=1/2`, so conditional independence fails.

### Monty Hall

Under obligatory informed opening and obligatory switch offer, `P(switch wins)=2/3`, `P(stay wins)=1/3`.

### Exercises and answers

1. **Two events:** If `P(A)=0.6`, `P(B)=0.5`, `P(A intersect B)=0.2`, what is `P(A union B)`? **Answer:** 0.9.
2. **Mutual exclusion:** Can two disjoint positive-probability events be independent? **Answer:** No; their intersection is 0 but the product is positive.
3. **Independence:** Give pairwise-independent variables that are not mutually independent. **Answer:** Two fair bits and their XOR.
4. **Selection:** Why does the two-child answer depend on how a boy was observed? **Answer:** Family selection and child selection induce different conditional weights.

### References

- Joseph Blitzstein and Jessica Hwang, *Introduction to Probability*, Harvard Stat 110 materials: https://stat110.hsites.harvard.edu/
- MIT OpenCourseWare, Probability and Random Variables 18.600: https://ocw.mit.edu/courses/18-600-probability-and-random-variables-fall-2019/
- Pascal-Fermat correspondence (translated), University of York History of Statistics: https://www.york.ac.uk/depts/maths/histstat/pascal.htm
- Thomas Bayes, "An Essay towards solving a Problem in the Doctrine of Chances" (1763), communicated by Richard Price: https://bayes.wustl.edu/Manual/an.essay.pdf
