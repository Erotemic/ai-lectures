# 025000 - When Comparisons Mislead: Confounding and Observational Studies

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** conditional probability, averages, and basic study design. **Theme:** confounding, Simpson's paradox, stratification, selection, and the difference between association and causation.

<!-- BEGIN SPOKEN LECTURE -->

# When Comparisons Mislead: Confounding and Observational Studies

Two treatments are compared in a hospital. Among patients who received treatment A, twenty-nine of one hundred and ten recovered. Among patients who received treatment B, eighty-one of one hundred and ten recovered. If you stop here, B seems vastly better. The recovery rates are about twenty-six percent for A and seventy-four percent for B.

Now suppose that patients came to the hospital with very different initial conditions. Some had mild illness, others severe illness. Treatment A was more often given to the severe cases; treatment B was more often given to the mild ones. The two overall recovery rates mix up treatment with the kind of patient who received it.

The next calculation is deliberately constructed, not historical hospital data. It shows something that can really happen in observational data. Among mildly ill patients, nine out of ten receiving A recovered, while eighty out of one hundred receiving B recovered. A has ninety-percent recovery against eighty percent. Among severely ill patients, twenty out of one hundred receiving A recovered, while one out of ten receiving B recovered. A has twenty percent against ten percent. Treatment A has the higher recovery rate in *both* severity groups, yet the overall average makes it look far worse.

This is Simpson's paradox: an association can reverse when we combine groups with different compositions. Nothing mysterious has happened to arithmetic. The averages answer different questions, and the patient populations being averaged are not comparable.

## What was mixed into the treatment comparison?

Look closely at the sample sizes. Treatment A was given to only ten mild patients but one hundred severe patients. Treatment B was given to one hundred mild patients but only ten severe patients. More A patients began with the disadvantage of severe illness. More B patients began with the advantage of mild illness.

The observed overall difference mixes two things: variation in treatment outcomes within severity groups, and variation in which severity groups received each treatment. If the selection mechanism were not recorded, the average would tempt us to attribute both effects to the treatment.

Severity is a confounder in this example because it is associated with the treatment received and predicts recovery independently of that treatment. It is a pre-treatment variable that creates a backdoor association between treatment and outcome. A clinician may prescribe A precisely because a patient seems likely to do badly without it. In that case, comparing treated and untreated patients can make a genuinely helpful treatment look harmful.

We should be careful with the word confounder. The mere fact that a variable is correlated with treatment and outcome does not prove that adjusting for it fixes a causal estimate. We need a story of when variables were measured, how treatment was chosen, and which relationships might have been left out.

## Standardizing to the same mixture

We can ask a more comparable descriptive question. What would the treatment-specific recovery rates look like if both groups had the same proportion of mild and severe patients?

For the purpose of this demonstration, choose a population that is half mild and half severe. We give each severity-specific rate a weight of one half. For A, ninety percent and twenty percent average to fifty-five percent. For B, eighty percent and ten percent average to forty-five percent. On this common severity mixture, A is ten percentage points higher than B.

Notice exactly what has been accomplished. We have corrected the descriptive imbalance in the one recorded variable, severity. We have not proved that the treatment itself caused the entire ten-point difference. If within the mild group, the A patients were younger or arrived earlier, those differences might also matter. If the severe patients treated with A were selected for some unrecorded reason, adjusting only for coarse severity may leave confounding behind.

This is the fundamental difference between a standardized association and a causal effect. Standardization compares rates on a shared distribution of recorded covariates. To interpret it causally, we also need sufficiently strong assumptions about unmeasured causes, selection, and the consistency of treatment definitions.

## The counterfactual question

Causation asks what would change for the same patient under different treatment assignments. In the potential-outcomes language, the treatment effect is the difference between the outcome under A and the outcome under B. We cannot observe both outcomes for one patient, so we need a design or an identification argument to estimate the average difference.

In a randomized experiment, assigning treatment at random helps break systematic associations between treatment and pre-treatment causes of the outcome. In an observational study, clinicians or patients choose treatment. The causal contrast may still be estimable, but we must argue that the recorded covariates account for the relevant differences in treatment selection.

One common condition is conditional exchangeability: once we condition on the measured pre-treatment covariates, the treatment assignment no longer contains information about the potential outcomes. Another is positivity: for each relevant covariate profile, there must be a genuine possibility of receiving either treatment. If every severe patient receives A and never B, no amount of reweighting can tell us directly how B would perform among severe patients. The data lack the necessary comparison.

Consistency matters too. If treatment A actually refers to many substantially different procedures, each with different effects, then saying someone received A may not define the counterfactual we want. The variables in the table must correspond to a meaningful intervention.

These conditions are not normally established by a single significance test. They are scientific assumptions about the process that generated the data.

## Why controlling for every variable is not always wise

Suppose treatment affects a patient's blood pressure, and blood pressure in turn affects recovery. If we want the total effect of treatment on recovery, controlling for post-treatment blood pressure can remove part of the very effect we hoped to measure. The analysis could answer a different question: how outcomes differ at a fixed value of a mediator. That may be interesting, but it is not the same as the total effect.

An even subtler problem is selection through a common effect. Imagine that both strong treatment effects and unexpectedly good baseline prognoses increase the chance that a patient returns for follow-up. If we analyze only people who returned, we have conditioned on a variable influenced by both the treatment-related process and prognosis. In certain causal structures this opens a spurious association. Such a variable is called a collider. Conditioning is not automatically helpful merely because it creates more homogeneous-looking groups.

The safest way to approach a proposed adjustment is to ask the time order and causal role of each variable. Was it measured before assignment? Does it influence treatment choice? Does treatment influence it? Could inclusion in the dataset depend on it? That reasoning comes before choosing columns for a regression.

## Regression does not automatically solve confounding

We can fit a regression model predicting recovery from treatment and severity. The coefficient on treatment may summarize within-severity associations. If we include age, baseline blood pressure, and other covariates, the coefficient may change again. This can be useful, especially when the form of the model is suitable and the covariates were chosen sensibly.

But the regression algorithm is only performing a mathematical adjustment. It does not know which variables are confounders, which are mediators, and which are colliders. It does not know whether a patient with a given profile could ever have received the other treatment. And it cannot check an unmeasured variable simply by looking harder at the variables we did record.

Furthermore, different models can answer different questions. A coefficient in a logistic regression is a change in log odds holding other covariates fixed. It is not automatically the same as a percentage-point change in recovery probability. When we want a population-average risk difference, we may need to calculate model predictions under each treatment for the same covariate distribution and then average those predicted risks.

## Selection can start before the study

Sometimes the key imbalance is not between the treatment groups but between the people who entered the dataset and those who did not. A survey distributed only to satisfied customers can yield extremely precise estimates about respondents without representing all customers. A medical record system may omit patients who received care elsewhere. Repeated measurements from the same clinic may look plentiful but reflect one local protocol.

The distinction between measurement precision and validity is essential. Adding more observations to a biased comparison can make its confidence interval narrower without moving its center toward the causal truth. Smaller sampling error is not a cure for systematic selection.

Nor does every observational study become useless because of possible confounding. Good studies can exploit rich pre-treatment records, natural assignment mechanisms, credible instrumental variables, discontinuities in eligibility rules, or longitudinal designs. Each method has its own assumptions. Observational evidence becomes persuasive when the comparison mechanism and its limitations are investigated, not merely when the sample size is large.

Return to the constructed hospital table. The aggregate comparison says B has the higher raw recovery rate among the patients who happened to receive it. The within-severity comparison says A has the higher rate in both observed severity groups. The standardized comparison says A is higher after using the same fifty-fifty mixture. None alone is a randomized causal trial.

Before trusting a fitted model, draw the table, identify who was eligible for each treatment, and ask what made one patient different from another before either treatment began. The important statistical question is not only how much the outcomes differ. It is whether the observations give us a credible comparison for the question we want to answer.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — Simpson reversal and identification assumptions

### Exact constructed table

| Severity | A recovered / total | A rate | B recovered / total | B rate |
|---|---:|---:|---:|---:|
| Mild | 9/10 | 0.90 | 80/100 | 0.80 |
| Severe | 20/100 | 0.20 | 1/10 | 0.10 |
| Combined | 29/110 | 0.263636... | 81/110 | 0.736363... |

With target severity weights \(w_\text{mild}=w_\text{severe}=1/2\), standardized A rate is \(0.5(0.90)+0.5(0.20)=0.55\); standardized B rate is \(0.5(0.80)+0.5(0.10)=0.45\). The standardized risk difference is \(+0.10\) in favor of A. These are constructed conditional frequencies, not a demonstration of identified causal treatment effects.

### Causal estimand and identification

Let \(T\in\{A,B\}\), observed baseline covariates \(X\), and potential outcomes \(Y(A),Y(B)\). The average treatment effect is \(E[Y(A)-Y(B)]\). Under consistency, no interference, positivity, and conditional exchangeability \((Y(A),Y(B))\perp T\mid X\),
\[
E[Y(t)]=\int E[Y\mid T=t,X=x] \;dF_X(x),\quad t=A,B.
\]
The resulting identification is conditional on assumptions about observational treatment assignment. It is not established by the numerical standardization exercise alone.

### DAG examples

- Confounder: \(X\to T\), \(X\to Y\), \(T\to Y\). Adjustment for observed pre-treatment \(X\) may help close the backdoor path.
- Mediator: \(T\to M\to Y\). Conditioning on \(M\) generally changes a total-effect estimand.
- Collider: \(T\to S\leftarrow U\to Y\). Conditioning on \(S\), which is affected by \(T\) and unmeasured \(U\), can open a noncausal association.

### Exercises with worked answers

1. **Aggregate reversal.** Which treatment has higher total recovery in the constructed table? **Answer:** B, by \(81/110\) versus \(29/110\). Within both severity strata A is higher.
2. **Standardization.** If the target population is 30% mild and 70% severe, compute both standardized rates. **Answer:** A is \(0.3(0.9)+0.7(0.2)=0.41\); B is \(0.3(0.8)+0.7(0.1)=0.31\).
3. **Positivity.** Why is observing no B-treated severe patients a problem? **Answer:** the data do not directly identify their B outcome distribution; model extrapolation cannot replace positivity without extra assumptions.
4. **Adjustment choice.** Should a variable created by treatment always be included as a control when estimating its total effect? **Answer:** no; it may mediate that effect.
5. **Interpretation.** Does conditional exchangeability follow from controlling for severity in regression? **Answer:** no. It is an assumption about all relevant causes of treatment choice and outcomes.

### Reading and attribution

- Penn State STAT 503, *Design of Experiments*, https://online.stat.psu.edu/statprogram/stat503.
- Penn State STAT 501, *Regression Methods*, https://online.stat.psu.edu/stat501/.
- Miguel A. Hernán and James M. Robins, *Causal Inference: What If*, https://miguelhernan.org/whatifbook.
