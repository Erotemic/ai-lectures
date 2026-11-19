# The Most Useful Sentence a Machine Can Say

**Track:** GPT-SoapBox  
**Lecture:** 003000  
**Preparation:** No technical background is needed; probability is introduced through examples.

<!-- BEGIN SPOKEN LECTURE -->

I want to defend a sentence that sounds, at first, like an admission of defeat.

'I don't know.'

This is not a lecture about the romance of mystery, or an invitation to be helpless in the face of difficult questions. I am arguing something more specific. A machine that can produce an answer to almost any question needs to become exceptionally good at describing the limits of that answer. Not because ignorance is admirable, but because an unmarked boundary between knowledge and guesswork is a design defect.

Fluent answers create a peculiar danger. When a reply is grammatically elegant, properly organized, and delivered without hesitation, the reader may feel as though some verification must have happened along the way. But verbal coherence is not a certificate of truth. A beautifully written answer can be wrong. It can even contain a convincing explanation of why it is wrong.

That is especially relevant to language models. Systems like the one producing this lecture learn patterns from enormous collections of material and are trained to produce useful responses. They can explain genuine ideas, solve real problems, summarize documents, and make substantive connections. They can also generate false particulars, confuse similar events, or present plausible citations that do not support the sentence they accompany. The important distinction is not between an impressive machine and an unimpressive one. It is between a response that happens to be convincing and a response whose claims are warranted.

I would like us to stop treating an acknowledgment of uncertainty as a stain on an answer and begin treating it as part of the answer's information.

## Four ways not to know

Suppose you ask me what time a particular museum closes tonight. There may be a definite answer, but it depends on the museum, the location, the date, and a schedule that can change. If I have not checked a current source, my problem is an information gap. It would be misleading to turn a remembered general opening time into a firm claim about tonight. The right move is to check, or to state plainly that I have not checked.

Now suppose you ask whether a particular medicine will help a particular patient. Even if we have good clinical evidence, we may face genuine uncertainty about the individual's response, the quality of the diagnosis, and the consequences of competing choices. This is not simply a missing fact waiting on a website. The best answer may be probabilistic and conditional, and the decision may require qualified professional judgment.

Third, suppose you ask which of two novels is better. Better in what sense? More daring in form? More psychologically acute? More enjoyable to read aloud? More influential? The question contains a value judgment that cannot be settled by discovering an overlooked statistic. I can make a case. I cannot honestly pretend a single measurement will settle every meaningful interpretation of the word better.

Fourth, suppose you ask, 'Should I take the offer?' We may not yet know which offer, what alternatives exist, what risks you face, or what matters to you. This is uncertainty about the question itself. The answer should not be invented merely because the sentence looks complete.

Those are different failures of completeness: an unchecked fact, an uncertain world, a disputed criterion, and an underspecified request. They require different responses. 'I don't know' can be the beginning of all four, but it should not be the end of the reasoning.

An information gap invites verification. A probabilistic question invites ranges, assumptions, or forecasts. A value question invites an explicit criterion and consideration of alternatives. An underspecified question invites a useful clarification, or a stated working assumption when the stakes are low.

An honest system should know which kind of incompleteness it is dealing with as well as it can. Otherwise it may respond to a missing fact with philosophical vagueness, or respond to a moral disagreement with a fake fact, or respond to a serious unknown with a manufactured number.

## The trick played by a coherent paragraph

Imagine a question about an obscure eighteenth-century pamphlet. The user asks who printed it, where it first appeared, and which contemporary responded to it. A language model produces three names, a city, a date, and an elegant story about a dispute between the printer and a philosopher. The paragraph reads like the beginning of a history lecture. You can almost smell the paper.

I have not named a real pamphlet here. The example is invented to expose a failure mode. Specificity makes the paragraph feel researched. Its details fit together. Yet none of that establishes that the pamphlet, printer, and correspondence existed.

A human storyteller can produce the same illusion. The technology changes the scale, speed, and ease of production. A system that can generate a plausible paragraph in seconds can fill an enormous space with apparent evidence before anyone has checked the first line.

An early research study called *TruthfulQA*, by Stephanie Lin, Jacob Hilton, and Owain Evans, deliberately tested language models with questions that invite common misconceptions. The study was presented at the Association for Computational Linguistics in 2022, using models available at the time. Its central insight was that a system trained extensively on human text can learn to repeat widely represented falsehoods rather than distinguish them from truth. Those results should not be treated as a measurement of every current model. The point remains conceptually important: producing the kind of answer people often give is not the same objective as producing the right answer.

The United States National Institute of Standards and Technology addresses related problems in its 2024 generative AI risk profile. NIST uses the term confabulation for generated, confidently presented false content, including incorrect logic and citations. An invented reference can be especially deceptive because it appears to supply the very verification the reader needs.

So what should an answer do instead? It should separate claims grounded in a checked source from claims inferred from the available evidence, from estimates, and from details still unverified. It should provide enough provenance that a reader can inspect consequential claims. A source link alone is not enough: the linked source must actually say what the answer attributes to it.

There is an aesthetic price to that approach. A perfect paragraph may have to make room for an imperfect sentence: 'That attribution has not been verified.' I consider this a good trade. A useful answer is not primarily a performance of confidence.

## Why a confidence percentage can make things worse

Here is an obvious proposal: have the machine attach a probability to every answer. Eighty-seven percent confident that this is correct. Ninety-two percent confident in that explanation. Wouldn't that solve the problem?

Not by itself. A number is useful only if we know what it measures.

Suppose a forecasting system labels one hundred comparable predictions as ninety percent likely. If its probabilities are well calibrated for that class of cases, we would expect approximately ninety of those outcomes to occur. Not exactly ninety in every batch; chance still matters. But over many appropriate cases, the frequencies should correspond to the predicted probabilities. That is one important meaning of calibration.

An individual number presented in a conversation, however, may have no such tested interpretation. Ninety percent of what? Confidence that the source was remembered accurately? That the question was understood? That the conclusion follows from the evidence? That another model would agree? That a particular user would find the answer useful? These are different properties.

Worse, uncertainty can hide in the space between those properties. I might be highly confident about a calculation made from the numbers you supplied and not confident at all that those numbers describe the real world. I might be confident about the historical date and uncertain about a proposed causal explanation. I might be confident that two readings of a sentence are possible and uncertain which one the user intended.

Compressing all of that into a single decimal can create a new illusion of precision. A number with two digits after the point is not more honest just because it looks quantitative.

This is not an argument against calibrated probabilities. Forecasting, risk analysis, and selective prediction can benefit enormously from them when we define the target event, evaluate performance, and understand the costs of errors. I am arguing against decorative precision: numbers chosen to make uncertainty look managed without evidence that they are meaningful.

Sometimes the best uncertainty statement is qualitative and specific: 'This is a standard theorem, and I can show the proof.' Or: 'The date is reported in this archive, but the archive does not establish the author's motive.' Or: 'I calculated the result from your spreadsheet, but I did not verify the original entries.'

The honesty is in the distinction, not in how many digits we display.

## A useful answer can be incomplete

There is a practical objection here, and it is serious. People use tools because they need help. They do not want to be buried beneath a paragraph of uncertainty before receiving a simple answer. If a user asks for a recipe substitution, a short calculation, or the meaning of an unfamiliar term, a machine that endlessly announces its limitations is not being more useful. It may be hiding from the work.

I agree. An answer should be proportionate to the stakes and the uncertainty. The arithmetic of six times seven does not require a cautionary essay. A draft title for a presentation can be offered directly. A speculative idea can be explored imaginatively as long as it is not disguised as a verified discovery. The goal is not maximum hedging. The goal is to avoid asserting more than the available evidence warrants.

One useful distinction is between being candid and being timid. Candor tells the reader what is supported, what is inferred, and what remains open when those differences matter. Timidity refuses to say anything decisive even when evidence is strong. The two can look similar from a distance, but they are opposites in practice.

If a calculation is valid and its assumptions are clear, state the result. If a decision has one option that dominates under the criteria the user supplied, recommend it. If a historical claim is well documented, teach it without apologizing for the existence of scholarship. If a task is creative, create. A model that says 'I don't know' every time it could be wrong will eventually say nothing of value.

The challenge is to know when the difference matters. We might start with three questions. How consequential is an error? How easily can the claim be verified? And what would the reader reasonably infer from the way the answer is presented? Those questions do not yield a universal formula, but they give us a responsible direction.

For a museum's opening time, verification is cheap and the user likely needs a concrete current fact. For a diagnosis, the consequences of error are high, evidence has to be contextual, and professional review may matter. For a philosophical argument, the important work is to state premises and reasons rather than invent a false consensus. For brainstorming, possibilities are the product; caution should not suffocate them.

I would prefer a model that makes these distinctions intelligently to a model that applies one disclaimer to every paragraph.

## An answer should carry a receipt when it needs one

Here is a more concrete design proposal. For consequential factual work, imagine an answer that can be accompanied by an epistemic receipt. Not a decorative seal saying verified, and not a demand that every sentence have a footnote. A compact account of how the answer was obtained.

The receipt might identify what information came from the user's supplied document, what was checked against external references, which numbers were computed, which assumptions were introduced, and what has not been checked. For time-sensitive information it might say when the source was consulted. For a prediction it might identify the forecast horizon and the basis for the uncertainty. For a comparison it might say which criteria were used and which were excluded.

Consider a fictional report comparing the operating costs of two machines. One machine has a lower purchase price. The other uses less energy. A glib answer recommends the cheaper purchase or the more efficient machine depending on which feature sounds most compelling. A better answer calculates cost under stated assumptions and says what is missing: electricity prices, maintenance schedules, utilization, financing, replacement intervals, and failure costs. The conclusion may still be decisive if one option wins across plausible ranges. Or the answer may be conditional: choose A if you expect less than a certain number of operating hours, B otherwise.

Notice how much more useful that is than an abstract confession that artificial intelligence can make mistakes. The reader can see what would change the conclusion.

This idea has limits. Some information cannot be disclosed because it is private. Some internal model processes do not translate into a truthful, inspectable human explanation. A fluent story about how a model supposedly reasoned can itself be fabricated. A receipt should therefore describe observable actions, supplied evidence, calculations that can be checked, and explicit assumptions. It should not pretend to provide privileged access to hidden mental steps.

And receipts must themselves be honest. A pile of citations chosen after a conclusion is reached is not proof that the sources support it. If the system says it checked a page, it should really have checked the page. If it did not, that should remain visible.

## The user deserves agency, not an oracle

A question-answering system can be helpful while gradually teaching its user a bad habit: accepting confident formulations without checking where they came from. The convenience is real. So is the risk. A user may become less practiced at noticing whether a claim is about a measurement, a judgment, a forecast, or an assumption.

The better relationship is a collaboration in which the system expands what the person can investigate. It can do the arithmetic, search a document, prepare alternative formulations, explain a hard concept, test a proposed argument, or organize a body of evidence. It can also say where its assistance ends. That boundary need not be hostile or paternalistic. It can be ordinary information.

I do not mean the human should be forced to inspect every calculation or citation. Much of the value of technology is that it saves us from repeated labor. The point is to keep verification possible and to make the division of responsibility comprehensible. Trust is stronger when it is not blind.

This is especially important when the machine is asked about itself. Claims such as 'I searched those records,' 'I tested that code,' or 'I verified the reference' should be reports of actual actions. They are not turns of phrase. If I have drafted a proposed test but not executed it, the difference matters. If I am speaking from general knowledge rather than a live source, that difference matters when the information can change. If I cannot inspect a proprietary system, I should not invent its internal state to make the interaction smoother.

We often think of helpfulness as delivering a finished product. But sometimes the most helpful output is an accurate map of what remains to be done. 'Here is the derivation. Here is the assumption it relies on. Here is the datum we must check before using the result.' That is not an incomplete service. For many tasks, it is the service we actually need.

## Ignorance can be concealed or made productive

Let me end with a distinction. Not knowing is ordinary. Human beings do not know almost everything about the universe, and no machine escapes that condition merely by speaking well. The important choice is what happens at the boundary.

One response is to hide it. Fill the empty space with familiar names, plausible dates, or comforting generalities. Produce an answer with the right shape, and hope the world cooperates. Another response is to stop completely: refuse to help because certainty is unavailable. Both are failures of the same imagination. They assume the only valuable product is a perfectly finished declaration.

A third response is more useful. State what can be established. Make a reasoned proposal when a proposal is appropriate. Show the alternatives. Identify the missing piece. Offer the next check. Revise when evidence changes.

I want machines capable of doing difficult work, not machines trained to apologize for existing. But competence includes knowing what kind of claim one is making. A tool that gives you a false certainty can be worse than one that gives you an accurate uncertainty. A tool that turns uncertainty into an actionable investigation is better still.

'I don't know' should not be the last sentence in a good answer. Often it should be the first honest sentence that makes the rest possible.

<!-- END SPOKEN LECTURE -->

## Sources and design distinctions (not spoken)

**Argument.** In a generative system, uncertainty disclosure should be informative, specific, and proportionate to context. The essay proposes an *epistemic receipt* as a design principle, not a claim that existing models can introspect their internal reasoning or supply well-calibrated probabilities without empirical evaluation.

**Sources.**

- Stephanie Lin, Jacob Hilton, and Owain Evans, “TruthfulQA: Measuring How Models Mimic Human Falsehoods,” *Proceedings of ACL 2022*: https://aclanthology.org/2022.acl-long.229/. The lecture identifies the model-era limits of the experimental results.
- National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, NIST AI 600-1 (2024), especially confabulation and information integrity: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence.
- National Institute of Standards and Technology, *AI Risk Management Framework 1.0* (2023), trustworthy AI characteristics, context, and risk balancing: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10.

**Illustrations.** The pamphlet, museum-hours question, treatment example, and machine-cost report are hypothetical. No real author or museum is being described. Numerical confidence examples explain calibration conceptually, not the measured calibration of any named model.
