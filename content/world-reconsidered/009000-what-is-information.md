# 009000 — What Is Information? Messages, Uncertainty, and the Limits of Meaning

**Track:** The World Reconsidered. **Theme:** Claude Shannon, coding, entropy, transmission, and semantic boundaries. **Background:** fractions and logarithms explained in speech. **Form:** standalone question-centered lecture.

<!-- BEGIN SPOKEN LECTURE -->

# What Is Information? Messages, Uncertainty, and the Limits of Meaning

A person sends a message saying that a train will arrive at noon. Another sends a thousand random letters. Which message contains more information? The answer depends on what we mean by information. If we mean useful news for someone waiting at a station, the first message may be far more valuable. If we mean how many distinct possibilities must be distinguished to reproduce a sequence exactly, the random letters may require much more description. The same word points to two different questions.

Information has become part of almost every scientific explanation. Biologists speak of genetic information, engineers speak of data rates, neuroscientists study signals, and ordinary people talk about information overload. Yet one of the most important mathematical theories of information became powerful by refusing to answer what a message means. It asked instead: how much uncertainty does a message resolve, and how efficiently can it be carried through a noisy channel?

The man who posed that question with extraordinary clarity was Claude Shannon. He worked at Bell Laboratories, where communication was both a technical business and a source of mathematical puzzles. A telephone company needed to move voices over wires. Telegraph operators had to distinguish symbols. Engineers wanted to transmit more messages without losing their content to noise. Shannon found a framework connecting these problems, and it changed electronics, computing, and much of modern science.

## A mathematician who liked machines

Claude Elwood Shannon grew up in Michigan, studied mathematics and electrical engineering, and developed an early attraction to circuits and mechanical contraptions. At the Massachusetts Institute of Technology he wrote a master's thesis connecting Boolean algebra to relay and switching circuits. The insight was practical and conceptual: the operations of a circuit could be analyzed in the language of logic.

His later years at Bell Labs were filled with mathematical work and playful engineering. He constructed devices that performed limited tasks in surprising ways, including a mouse named Theseus that could traverse a maze through a mechanism hidden beneath the board. The mouse appeared to find its route by intelligence. In fact, a controlled system of switches and mechanisms supplied its memory and movement. Shannon delighted in such boundaries between appearance, mechanism, and description.

He also rode a unicycle and enjoyed juggling. These facts can become little more than decorative stories if detached from his work. But they point toward a persistent fascination with building things, testing their limits, and turning abstract puzzles into physical demonstrations. An engineer can learn a great deal by making a machine fail in a way the theory predicts.

In 1948 Shannon published *A Mathematical Theory of Communication* in the *Bell System Technical Journal*. Its opening distinguished the engineering problem from the semantic question of what a message refers to. That did not mean meaning was unimportant to people. It meant that the engineering task could be made precise without solving every philosophical difficulty about meaning.

The separation was liberating. A telephone line need not understand what a speaker is saying in order to transmit their voice with acceptable fidelity. The line must support reliable distinctions among signals. The same analysis can apply to letters, electrical pulses, digitized sound, or a stream of measurements.

## Start with a coin

Imagine somebody tosses a fair coin and tells you the result. Before hearing it, you consider two possibilities, heads and tails, equally likely. After hearing it, one possibility remains. In Shannon's framework, the message has resolved one bit of uncertainty.

A bit is a unit that distinguishes two equally likely alternatives. We can represent heads as zero and tails as one. Those labels are arbitrary; the important property is that one binary choice distinguishes two cases. Two binary choices distinguish four combinations: zero-zero, zero-one, one-zero, and one-one. Three distinguish eight. Ten binary choices can distinguish one thousand twenty-four alternatives.

Now imagine the coin is strongly biased: ninety-nine times out of a hundred it lands heads. The result still takes one binary symbol to report if we send each toss separately using a fixed code, but the average uncertainty before learning the result is smaller. Heads is expected. Tails is surprising. Over many tosses, we might compress a sequence of such outcomes by exploiting their regularity.

Suppose a friend tells you that the sun rose this morning. The statement may be true and emotionally welcome, but it resolves little uncertainty for someone who expected it. Learning that a rare eclipse occurred resolves more uncertainty. This is not an ethical or poetic comparison. It is an attempt to quantify the reduction in uncertainty about an event under a stated probability model.

The word model is essential. Surprise depends on what the receiver expected. If your friend has reason to think they are on a planet with different conditions, their probabilities may differ. Shannon entropy belongs to a distribution of possibilities, not to a sentence floating free of context.

## How to calculate uncertainty

For a set of possible outcomes with probabilities, Shannon's entropy is the average number of binary questions needed in an idealized coding sense. More precisely, it is the expected information content, measured in bits, when we use logarithms to base two.

The information content of an outcome with probability one half is one bit. An outcome with probability one quarter has two bits, because one quarter is one in four equally likely alternatives. An outcome with probability one eighth has three bits. This is captured by taking the negative logarithm of probability to base two.

Let's use a simple distribution. A source emits letter A half the time, B one quarter of the time, and C and D one eighth each. A carries one bit of surprise. B carries two. C and D carry three each. The average is one half times one, plus one quarter times two, plus one eighth times three, plus one eighth times three. That sums to one and three quarters bits per symbol.

The source has four possible symbols, so a fixed two-bit code could represent every symbol. But its average uncertainty is only one and three quarters bits. Over long messages, a suitable coding scheme can move toward that lower average, subject to coding constraints.

We must be precise about what this means. A single symbol cannot be represented by one and three quarters physical bits. Individual codewords have whole numbers of bits. The average can be fractional because common symbols get short descriptions and rare ones longer ones, or because coding across many symbols approaches the theoretical limit.

Shannon's entropy is powerful because it provides a quantitative lower bound for average lossless representation under specified assumptions. It does not tell us whether A represents a desperate warning, a joke, or a completely meaningless token. The probabilities matter to the compression problem; semantic value is a separate question.

## Give the common symbol the short code

We can actually construct a code for the distribution. Assign A the single bit zero. Assign B the two bits one-zero. Assign C the three bits one-one-zero. Assign D the three bits one-one-one.

No codeword is the beginning of another. That property makes the code immediately decodable: when a receiver sees zero, the symbol must be A. When the receiver sees one, it waits for another bit. One-zero means B; one-one means wait once more to distinguish C from D. This is a prefix code.

Its average length is one half times one, plus one quarter times two, plus one eighth times three, plus one eighth times three, which is exactly one and three quarters bits per symbol. In this deliberately chosen distribution, a simple prefix code reaches the entropy bound.

Now compare a uniform distribution over four symbols. Each symbol appears one quarter of the time. All four are equally surprising, and the entropy is two bits. There is no average improvement available from giving one symbol a shorter code unless another gets longer in a way that loses the benefit. The structure of the probabilities determines the compressibility.

What looks like waste in a message may therefore be structure. Repeated spaces, predictable letters, familiar patterns, and correlations can make data compressible. A genuinely unpredictable source offers fewer such savings. Compression does not require understanding a message's human significance. It requires detecting statistical regularity.

This is why a long repeated string can be described briefly. A million copies of the letter A are a million characters, but the instruction 'repeat A one million times' is short. The physical message can be large while the description is compact. However, the exact relationship between Shannon entropy of a source and algorithmic description length of an individual string involves different mathematical concepts. They should not be treated as interchangeable.

## Why noise changes the problem

A message rarely passes through an ideal channel. Electrical signals are disturbed, optical fibers lose photons, wireless signals encounter interference, and human voices are masked by background sound. The sender chooses a signal; the receiver observes a modified version. The engineering task is to recover the intended distinctions reliably enough for the application.

Suppose one bit is transmitted through a channel that independently flips it with probability one in ten. If we send a zero, the receiver sees a one ten percent of the time. If we send a one, it likewise sometimes arrives as zero. Sending each bit just once creates errors.

A naive defense is repetition. Send each bit three times: zero-zero-zero or one-one-one. If a receiver sees zero-one-zero, it can guess that the intended bit was zero because two of the three observations agree. Under independent ten-percent flip noise, this majority vote fails only when at least two of the three copies are flipped.

Calculate that probability. Exactly two flips can occur in three ways, and each particular pattern has probability one tenth times one tenth times nine tenths, or nine thousandths. Three ways give twenty-seven thousandths. All three flips have probability one thousandth. Together that is twenty-eight thousandths, or two point eight percent.

Our error probability dropped from ten percent to two point eight percent, at the cost of using three channel bits to convey one source bit. We purchased reliability by spending transmission capacity. Better error-correcting codes can do substantially better than repeating every bit, because they spread structured redundancy across messages.

Redundancy is therefore context dependent. A repeated phrase may be wasteful for compression but protective in a noisy channel. The right design depends on whether bandwidth or reliability is scarce, and on the nature of errors.

## Shannon's surprising promise

Shannon's noisy-channel coding theorem established something deeper than the usefulness of repetition. Under a given channel model, there is a capacity: a maximum rate below which reliable communication can be made possible with sufficiently sophisticated coding and sufficiently long blocks. Above capacity, arbitrarily reliable transmission is impossible under the theorem's assumptions.

This result can sound like magic. How can carefully designed redundancy overcome a stream of random errors? Think of a large family of possible codewords chosen so that noise-corrupted versions of different codewords are distinguishable with high probability. The receiver uses the structure of the code to identify the intended member of the family.

The theorem does not say the errors disappear physically. It says that decoding error probability can be made small while maintaining a positive communication rate, provided the rate stays below capacity and the channel behaves as modeled. Real systems balance block length, latency, computational cost, and changing channel conditions. Infinite-length idealization is a guide to design, not a ready-made telecommunications product.

For a binary symmetric channel that flips each bit independently with probability one tenth, the capacity is one minus the binary entropy of one tenth. The binary entropy at one tenth is approximately zero point four six nine bits. Capacity is therefore about zero point five three one bits of information per channel use.

This tells us that the triple-repetition scheme, whose rate is one third, is far from the best possible rate at this error level. Coding theory developed methods capable of approaching channel limits while controlling errors, though practical code performance depends on how much delay and processing we can afford.

An engineering problem that once looked like a collection of tricks had become a theory with a quantitative frontier. Shannon gave people a way to distinguish impossible demands from designs that might be improved.

## A message with no meaning and a message that changes a decision

Return to our original puzzle. A random string of characters can have high Shannon entropy if its symbols are hard to predict. A single sentence telling a rescue team where survivors are located may have modest length and enormous practical value. The entropy calculation is not mistaken; it measures a different property.

Shannon explicitly bracketed semantic aspects of communication from the engineering problem he analyzed. We should respect that deliberate scope. Information theory does not provide an automatic measure of truth, wisdom, beauty, usefulness, or human importance.

Consider two weather reports. One says rain is likely, the other says no rain is likely. Both can be encoded into the same number of bits. If one is accurate and the other fabricated, their engineering transmission requirements may be identical. The farmer deciding whether to harvest may face profoundly different consequences. The distinction between conveying a symbol and conveying reliable knowledge remains essential.

In modern life this gap appears whenever a computer successfully transmits false information. A flawless network can deliver misinformation at tremendous speed. Better bandwidth does not automatically improve epistemic quality. Establishing trust requires evidence about the source, verification methods, incentives, and error correction in a broader human sense.

The language of information becomes most useful when we ask what uncertainty we are measuring, what probability distribution we assume, and what task the message is supposed to support.

## From telephone signals to genetic sequences

Biology uses a code of a different kind. DNA is a molecular sequence containing bases that participate in the production of proteins and the regulation of cellular processes. Scientists can examine how sequences are copied, mutated, transmitted, and interpreted through biological mechanisms. Information-theoretic methods can quantify variability, mutual dependence, and other properties of these sequences.

But saying DNA contains information does not turn an organism into a simple message receiver. Development depends on cells, chemistry, physical environments, regulatory networks, and evolutionary history. The metaphor of a genetic program is sometimes useful and sometimes misleading. A sequence has causal roles because cellular machinery interacts with it.

Likewise, neurons exchange signals, but a brain is not merely a telephone network. It learns, acts, predicts, and is affected by its body and surroundings. Information theory can help analyze uncertainty and signals without replacing neuroscience, psychology, or philosophy.

A useful question is what the messages can predict. If knowing a sequence reduces uncertainty about a protein, information-theoretic measurements may capture something real. If somebody claims to have measured how meaningful a thought is using only its compressed length, we should ask what theory connects that length to meaning. Technical vocabulary cannot fill a missing causal argument.

## The inventor and the boundary of his invention

Shannon's fascination with devices also makes this point vivid. Theseus the mechanical mouse did not understand mythology because it was named for a Greek hero. It performed a particular maze task using a particular mechanism. Describing that mechanism honestly made the demonstration more impressive, not less. It showed that a limited form of adaptation could be embodied in circuitry and mechanical movement.

A story about an ingenious machine can tempt us to give it every quality associated with a living creature. Shannon's work suggests a better approach: define the task, describe the representation, measure performance, and recognize the distinction between competence in one problem and general understanding.

This methodological discipline is part of his legacy. Boolean switching circuits, entropy, source coding, and channel capacity gave engineers specific questions that could be answered mathematically. Philosophical questions about consciousness and meaning remained open. The theory succeeded because it did not pretend to solve them by definition.

Bell Labs itself mattered to the story. Telecommunications researchers worked within an institution facing real constraints of cost, noise, equipment, and scale. Shannon's abstractions arose from an environment in which elegant mathematical theory had to explain something a working engineer could measure. The institution did not supply all the answers, and the individual did not work outside history.

## A model for everyday information overload

Suppose you receive one hundred notifications in an hour. The number of notifications says little about whether you have learned anything important. If ninety-nine repeat what you already know, they add few new distinctions. If one reports a time-critical change of plans, it can have far more practical value than the rest combined.

Information theory gives us one language for redundancy and predictability. Decision theory provides another for the consequences of acting on a message. Epistemology asks whether the message is justified or true. Attention research asks how a human being can process it. These are distinct pieces of the explanation.

We can use them together without reducing one to another. In a communication system, increasing redundancy may make a message more resilient. In a human organization, too much repetition can crowd out important details. In a crisis, repeating an instruction might prevent misunderstanding. The same design feature can be helpful or harmful depending on the channel, task, and receiver.

The practical habit is to distinguish transmitting, understanding, and trusting. Was the message delivered accurately? Did the receiver interpret it as intended? Is its content supported by evidence? Would acting on it serve the intended goal? A system can succeed at one of these and fail at another.

## What two variables reveal about each other

So far we have examined the uncertainty in one source. But much of the power of information theory comes from comparing variables. Suppose a weather forecast predicts either rain or no rain, and the next day either rains or does not. How much does the forecast tell us about the outcome?

We can imagine a perfectly accurate forecast in a world where rain occurs half the time. Before hearing the forecast, there is one bit of uncertainty about tomorrow's weather. After hearing an accurate forecast, there is none. The forecast provides one bit of information about the outcome under that model.

Now imagine a forecast that always says rain regardless of the weather. It might occasionally be correct, but it does not reduce uncertainty about which outcome will occur. Knowing the forecast tells us nothing we could not already infer from the base rate. Its information about the weather outcome is zero in this simple setting.

Shannon's framework can quantify this relationship through mutual information. Mutual information asks how much uncertainty about one variable is reduced on average by observing another. It is zero when the variables are statistically independent, and it is larger when observing one genuinely helps distinguish the other.

This provides a useful way to think about tests and measurements. A sensor can produce lots of data but little information about the condition we care about. Another sensor may produce a small signal that predicts a crucial event. Counting transmitted bits tells us how much description moves through the channel; measuring mutual information asks how much one signal predicts a specified target.

The phrase specified target is essential. A thermometer reading may carry information about room temperature and almost none about whether a nearby book is worth reading. Information is always relative to a model of variables and observations when used in this statistical sense.

## Why exact transmission and useful decisions differ

Consider two medical laboratories. Laboratory A transmits every test result with no communication error, but the test itself is poorly associated with the disease. Laboratory B uses an accurate test but occasionally sends results to the wrong patient. Both systems need correction. The first has a measurement problem; the second has a communication and identity problem.

Information theory can help analyze the second system's transmission reliability. Statistical inference can help analyze the first system's diagnostic accuracy. Ethics and clinical practice determine what should happen when a patient receives a result. A solution at one layer does not automatically solve the others.

The distinction becomes sharper with a prediction system. Suppose a model confidently predicts a person's behavior based on biased historical records. It may encode the records faithfully and compress them efficiently while reproducing their distortions. Good compression is compatible with bad evidence. Accurate transmission is compatible with unjust decisions.

Shannon's abstraction is therefore more valuable when we protect its boundaries. It makes precise a domain where precision is possible. It also shows us where additional theories are required: semantics, causation, truth, fairness, and action.

## The cost of waiting for an answer

Long-block error-correcting codes can approach theoretical channel capacity, but real receivers have deadlines. A video call cannot always wait for a huge block of data to be collected before decoding. A spacecraft may have severe power limits. A medical sensor may need to warn immediately when a measured signal changes.

This creates engineering tradeoffs. A short code can have low delay but may need more redundancy for the same error rate. A long code can use statistical regularity more efficiently but requires memory and processing. Changing channel conditions can make yesterday's optimal code a poor choice today.

The mathematical theorem is a boundary on possibility under assumptions, not a command to use one universal algorithm. Practical systems integrate probability models, physical equipment, energy budgets, computational constraints, and human needs. The engineer who understands the theorem must still design a product.

Think again of Theseus, Shannon's maze-solving mouse. The mechanism under the maze succeeded at a well-defined task. Its limited competence was meaningful because the test was specified. Likewise, a communications system can be judged by bit error rate, speed, power, and resilience to noise. We should resist the urge to promote success on those measures into an assertion about every form of intelligence or understanding.

Shannon's work is a reminder that deep mathematical progress often comes from asking a smaller question with great care. We learn a limit that can be proved, use it to build new tools, and remain free to investigate the larger questions it leaves unanswered.

There is one more distinction between information and knowledge worth practicing. Imagine receiving a long spreadsheet containing ten thousand measurements. It may have high informational content and require substantial storage. Yet without labels identifying the instruments, units, dates, and sampling process, it may be impossible to make a trustworthy inference. Metadata about how observations were produced can be more consequential than a great many additional rows.

A dataset can also contain highly predictable errors. If a faulty sensor always reports the same temperature, its output is very easy to compress. The low entropy is not a sign that the measurement is reliable. On the other hand, a noisy sensor may generate many unpredictable bits while adding little understanding of the physical quantity of interest. The distinction between entropy of the signal and information about the target clarifies the problem.

That lesson has consequences for scientific communication. Researchers need to report uncertainty, calibration, selection procedures, and limitations alongside results. Transmitting the numbers flawlessly does not establish how they were obtained. Information theory supplies tools for designing the channel; careful scientific practice supplies ways to evaluate whether the content supports the claim being made.

The next time someone says that a system processes enormous amounts of information, ask what is being measured. Are they describing bytes stored, symbols transmitted per second, reduction in uncertainty about a target, or practical usefulness to a decision-maker? Each measure can be legitimate. They should not be mistaken for the same achievement.

## What one bit can teach

The fair coin was our smallest example. It showed why one binary choice corresponds to one bit. A biased coin showed that average uncertainty depends on probabilities. A four-symbol alphabet showed how variable-length codes exploit statistical regularity. A noisy channel showed why controlled redundancy can rescue reliability. Each small step developed a part of a theory of communication.

Yet the opening question remains a useful warning. A message that saves a life does not need to contain many bits. A giant file of random noise can be difficult to compress and still be worthless to its reader. The richness of human communication involves meaning, evidence, purpose, and consequences in addition to uncertainty.

Shannon's achievement was to make a difficult portion of that world precise. His theory tells us what rates of representation and transmission are possible under defined conditions. It does not dictate what is worth saying. Learning where a powerful theory stops is part of learning what it can genuinely explain.

<!-- END SPOKEN LECTURE -->

## Mathematical and historical companion (display only)

### Source entropy and prefix code

Synthetic source \(P(A,B,C,D)=(1/2,1/4,1/8,1/8)\). Entropy \(H=-\sum p_i\log_2p_i=1.75\) bits per symbol. Code \(A=0,B=10,C=110,D=111\) is prefix-free and expected length 1.75 bits, matching entropy for this distribution.

### Triple repetition under independent noise

For bit flip probability \(p=0.1\), majority decoding three copies fails with probability \(3p^2(1-p)+p^3=3(0.01)(0.9)+0.001=0.028\). Independent identical errors are assumed; correlated errors change performance.

### Binary symmetric channel capacity

\(C=1-H_2(p)\) bits per channel use, where \(H_2(p)=-p\log_2p-(1-p)\log_2(1-p)\). At \(p=0.1\), \(H_2\approx0.468996\), \(C\approx0.531004\). The coding theorem is asymptotic and has modeling assumptions.

### Reading and research references

1. Claude E. Shannon, *A Mathematical Theory of Communication* (1948), full reprint: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
2. Original Bell System Technical Journal, July part: https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
3. Original Bell System Technical Journal, October part: https://doi.org/10.1002/j.1538-7305.1948.tb00917.x
4. IEEE Spectrum, *Claude Shannon: Tinkerer, Prankster, and Father of Information Theory*: https://spectrum.ieee.org/claude-shannon-tinkerer-prankster-and-father-of-information-theory
5. Massachusetts Institute of Technology Libraries, Claude Shannon papers: https://archivesspace.mit.edu/repositories/2/resources/688
6. David J. C. MacKay, *Information Theory, Inference, and Learning Algorithms*, free text: https://www.inference.org.uk/mackay/itila/book.html
