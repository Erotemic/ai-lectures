# 021000 — Electrical Diagnosis as Evidence: Symptoms, Hypotheses, and the Next Question

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** symptom logs, drawings, product manuals, recorded measurements and hypothetical fault trees. Site-specific field testing is governed separately by equipment and work conditions.

<!-- BEGIN SPOKEN LECTURE -->

# Electrical Diagnosis as Evidence: Symptoms, Hypotheses, and the Next Question

A kitchen light flickers. Someone says the breaker must be bad. Another person says it is a loose neutral. A third suggests that the LED lamp is failing. Those are not yet diagnoses; they are candidate explanations. A competent troubleshooter does not reward the most vivid story. They ask what observation would distinguish one explanation from another, and what action would produce the most useful evidence without introducing a disproportionate risk.

This is a way of thinking that applies across repair trades. You begin with what actually happened. You build a model of the system. You list plausible failure mechanisms. You distinguish symptoms from causes. Then you choose the next observation or measurement based on how much it will change your understanding.

We can make this systematic without pretending that every electrical fault is simple or that one checklist fits every installation.

## Separate the report from the interpretation

A homeowner reports, “The breaker keeps tripping.” The useful questions are more specific. Which protective device is it: an ordinary overcurrent breaker, a residual-current device, an arc-fault device, or a combined unit? What exactly indicates a trip? Does it happen immediately, after a motor starts, after rain, or at a random time? Which loads were operating? Has any wiring or equipment changed? Are other rooms or circuits affected? Is the device's product identification known?

One sentence of complaint can hide many different physical events. A ground-fault trip has a different detection mechanism from an overcurrent trip. A transient utility voltage sag may dim lights without opening any protective device. Some control systems intentionally shut down under low voltage, and some failures leave the protection untouched.

The first diagnostic product is therefore a precise **problem statement**. It includes the observed event, the affected scope, the time and conditions, and the evidence available. Keep the word “suspected” attached to suspected causes until there is evidence for them.

## Build the map before the tree

The drawings and circuit knowledge developed earlier now become practical. We want to know what is shared and what is independent. If one plug-in lamp flickers while everything around it remains steady, a local lamp, connector or driver hypothesis gains plausibility. If several unrelated loads change at the same instant, a common upstream supply or shared control deserves attention. Neither observation proves a single cause, but each helps prioritize.

Think of the installation as a graph of sources, conductors, connections, protective devices, controls and loads. Every branch has electrical properties and operating states. A fault can be in the source, a shared distribution path, an individual load, a control signal, or an interaction between several of them. A physically damaged connection is a different possibility from an automatic protective response, even though both can interrupt supply.

A diagram is only a starting hypothesis about the as-built system. A current panel schedule, a device manual and a maintenance record may refine it. Revisions matter. A drawing that predates a repair may support the wrong inference about which loads share a circuit.

## Construct a fault tree, then challenge it

One formal method is **fault-tree analysis**. Start with an unwanted event, such as “lamp output disappears,” and decompose it into possible necessary or sufficient conditions. The lamp can be unpowered, commanded off, internally defective, or subject to an environmental condition that prevents operation. “Unpowered” might be decomposed into upstream source loss, interrupted branch connection, a protective operation, or another cause. In a real system more than one failure can coexist, and an “or” diagram may fail to capture interactions unless we model them explicitly.

Fault-tree methods were developed within reliability and safety engineering, not invented for this lecture. The NASA *Fault Tree Handbook with Aerospace Applications* presents the deductive logic from an undesired event back toward causes. We borrow that logical structure as an educational method. We do not claim its aerospace risk models constitute a residential electrical code or a complete diagnosis of a particular house.

The main benefit is forcing yourself to consider alternatives. When someone insists a breaker is defective because power disappears, the fault tree asks whether power loss could also arise upstream, from a load connection, or from a control system. When someone insists a neutral is loose because lights change brightness, it asks what other mechanisms produce the same observation.

## Evidence should discriminate

Suppose two hypotheses predict that a lamp will dim when a refrigerator starts. Hypothesis A is a shared supply impedance; hypothesis B is a lamp driver sensitive to even small dips. Simply observing another episode of dimming does not necessarily distinguish them. A better discriminating observation might be whether multiple kinds of loads on the same documented supply path exhibit the same change, or whether the event is captured in an existing power-quality log.

For another example, imagine a device that stops after forty minutes. A thermal protection event, a timed control program and an intermittent upstream connection can all mimic one another. A timestamped record of the device's internal error code, ambient temperature and operating mode can help separate them. Without that context, restarting it repeatedly may erase the most useful evidence.

The best next question is not always the most sophisticated instrument reading. It may be a nameplate, a product manual, an event history, a picture of an indicator state, a known maintenance date or a comparison across several observations. Sometimes the informative result is a negative one: other equipment sharing the supply continued normally. But a negative observation matters only if it was possible to see the relevant event at the relevant time.

## A reading can be accurate and irrelevant

Suppose a multimeter displays the expected voltage at a receptacle during a period when everything is working. That is a valid observation of a particular voltage difference at that time. It does not refute an intermittent connection that opens only under load, a driver that fails when warm, or a supply disturbance that lasts a fraction of a second. The instrument's sampling time, load imposed by measurement, reference points and range determine which hypotheses it can test.

In this sense, **test selection** is part of diagnosis. A continuity beep does not establish the quality of a connection at operating current. A high-impedance voltage reading may indicate capacitive coupling. A clamp around several conductors may report a net current near zero despite large individual currents. A logger with poor time resolution may miss the event. Before requesting a test, specify the condition that would count as evidence for or against each candidate explanation.

This point is also why protective-device identifiers and event logs matter. A breaker that looks like an ordinary switch may contain electronics with specific diagnostics. A generic label “power trip” could combine distinct events in a monitoring platform. The actual manufacturer's description determines what the indicator signifies.

## Use probabilities without fake precision

A diagnostic process is implicitly probabilistic. Some failures are common in particular equipment; some are possible but very rare. Conditions such as recent maintenance, humidity, load changes and equipment age can alter which explanations deserve attention. But no probability should be invented merely to make the analysis appear scientific.

One useful qualitative idea comes from Bayesian reasoning: evidence changes your confidence in a hypothesis according to how expected that evidence would be if the hypothesis were true, compared with how expected it would be under alternatives. If a symptom is equally likely under two explanations, seeing it does little to distinguish them. If one explanation strongly predicts an observation and the other does not, the observation may be valuable.

Sometimes the right distinction is not between competing diagnoses but between **uncertainties that matter to the next decision**. For example, if an accessible outlet face is visibly discolored and smells scorched, the decision to stop using the affected equipment and arrange assessment does not require identifying the microscopic origin of the damage. The later investigation can distinguish a damaged receptacle contact, a connection problem or another source of heating. Good judgment prevents false precision from delaying an appropriate response.

## Learn from the sequence of events

The U.S. Department of Energy's guidance on causal analysis emphasizes chronology, changes, evidence preservation and identifying corrective actions rather than merely naming someone responsible. A small homeowner maintenance log can use the same intellectual structure without imitating an industrial incident investigation. Record when a symptom began, what was operating, whether it is localized, and which changes preceded it. Distinguish what someone directly witnessed from what was inferred later.

A useful example is repeated tripping after installing a new appliance. The chronology says there is an association. It does not yet tell you whether the appliance is defective, the circuit is overloaded, a protective device is responding appropriately to leakage, an installation has a connection problem, or the new equipment requires a different protective-device compatibility. The causal explanation requires evidence about which type of protection operated and under what conditions.

When multiple changes occurred at once, “it started after the installation” is still weaker evidence. Correlation directs investigation; it is not automatic proof of root cause.

## The system has boundaries

Electrical diagnosis can straddle utility supply, building wiring, appliance electronics and software controls. A voltage sag may originate beyond the property. A smart appliance may report a fault based on an internal sensor. A solar inverter may alter operating modes because of an external grid condition. There is no single local instrument that sees the whole chain.

Record the boundary of each piece of evidence. A smart-plug report tells you what the smart plug sensed, not necessarily what occurred at the service entrance. A utility event log covers the utility's measuring point and time resolution, not every branch connection. A manufacturer's fault code describes a device's internal interpretation, whose meaning must come from the product documentation.

When a hypothesis spans multiple parties, a useful repair scope explains the evidence needed from each: device documentation, circuit identity, service records, applicable test results and observed conditions. That also makes discussions with electricians, equipment manufacturers and utilities much more productive.

## Stop when the evidence supports the next decision

A good diagnosis does not demand infinite investigation. It asks whether the remaining uncertainty changes the next safe and effective action. Sometimes the next step is a documented repair by a qualified person, sometimes replacement of a failed removable device, sometimes a utility investigation, and sometimes continued monitoring because the evidence is not yet strong enough to justify intrusive testing.

There is an important distinction between an **observed failure**, a **plausible fault model**, a **confirmed root cause** and an **accepted repair**. A repair can remove a symptom while leaving the underlying hazard or contributing cause intact. Conversely, a proposed fix can be soundly justified by a fault mechanism even before the exact microscopic failure has been reconstructed, provided the scope and validation are adequate.

Useful completion evidence may include an updated drawing, a written finding, manufacturer-compliant replacement details, recorded test results and a specified acceptance criterion. The required documentation varies with jurisdiction and job. The engineering principle does not: the resolution should be tied to the originally observed problem and the failure mechanism it was meant to address.

The difference between guessing and troubleshooting is not confidence. It is a chain of reasoning that another competent person can inspect: symptoms, system model, candidate causes, discriminating observations, uncertainty, and a decision that actually follows from the evidence. That is a skill worth carrying into every physical repair project.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Fault-tree example: light goes out intermittently

```text
TOP EVENT: light output disappears intermittently
    OR: power input is interrupted
        - source / distribution disturbance
        - branch connection or control interruption
        - protective device opens
    OR: load is powered but does not produce light
        - lamp/driver failure
        - heat-dependent shutdown
        - internal control commands OFF
```

The branches are hypotheses, not exhaustive or mutually exclusive truths. Fault-tree OR/AND gates become formal only with correctly specified events; this sketch is a pedagogical decomposition.

### A diagnostic evidence table

| Evidence | What it supports | What it does not establish |
|---|---|---|
| Multiple loads dim at the same instant | Shared upstream effect deserves consideration | Exact fault location or utility culpability |
| One lamp fails while neighboring lamps remain stable | Local lamp/driver/control hypothesis deserves consideration | Supply definitely fault-free |
| Existing meter/logger shows short voltage sag | A sag occurred at the observed point and sampled time | Its cause or behavior at every branch |
| Protective device reports trip/fault code | A device registered a defined event | Root cause without model-specific documentation |
| Voltage normal during symptom-free interval | That voltage was present during that observation | Absence of intermittent defect |

### Exercises — event logs and paper analysis

1. A refrigerator starts and two lamps dim simultaneously. List three materially different hypotheses. **Answer:** Shared supply impedance, upstream supply fluctuation, and distinct driver responses to the same modest dip are examples; none is confirmed.
2. A smart device logs an undervoltage warning. What would you request before assigning blame to the utility? **Answer:** Timestamp, device threshold and sampling method, whether other meters agree, installation topology and corroborating source logs.
3. A meter shows normal voltage at noon, but a device failed at dawn. Does the noon reading falsify an intermittent undervoltage hypothesis? **Answer:** No; conditions and observation time differ.
4. Draw a two-level fault tree for a motor not starting. **Answer:** Supply unavailable OR control inhibits start OR internal motor/driver fault; refine with mutually conditioned events and manufacturer data.
5. Distinguish a proposed repair from confirmation of root cause. **Answer:** A proposed repair is an intervention chosen for a plausible mechanism; root-cause confirmation requires evidence explaining the original failure and showing why it should not recur.

### Attribution and scope

This lecture borrows the **deductive structure** of fault-tree analysis from the NASA reliability handbook and the **evidence/chronology/cause/action distinction** from DOE causal-analysis documents. Their authorship belongs to those institutions and contributing technical teams, not to this course. Neither is a building electrical installation standard. The application to a household symptom diary and the illustrative examples are instructional synthesis, not claims that NASA or DOE approved these specific repair methods.

## Claim-level source map

| Claim ID | Consequential claim | Evidence location and role | Limitations / pending checks |
|---|---|---|---|
| E021000-01 | An observed symptom should be distinguished from an inferred cause (engineering) | [`electrical-doe-causal-2024`](https://www.energy.gov/documents/doe-std-1197-2024-finalpdf) (§5 incident investigation and causal analysis; main) | DOE industrial causal-analysis context is an adapted framework, not a residential rule. |
| E021000-02 | Different protective devices can signal physically distinct causes (engineering) | [`electrical-osha334`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.334) (§1910.334 general equipment usage context; workplace_context); [`electrical-iec61557-1`](https://webstore.iec.ch/en/publication/102414) (public scope for protective measure testing; standard_context) | Device-level diagnosis requires actual markings and manuals; neither source alone defines every device trip code. |
| E021000-03 | Shared loads experiencing synchronized symptoms support a common upstream hypothesis (inference) | [`electrical-mit-node-2006`](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/9d19116cbabeada1c98004a4367a0ee0_nodal_mesh_methd.pdf) (shared impedance and nodal currents method; physics); [`electrical-doe-causal-2024`](https://www.energy.gov/documents/doe-std-1197-2024-finalpdf) (change/event analysis method; independent_diagnostic_context) | Observation supports hypotheses but not precise fault location. |
| E021000-04 | Fault tree starts from undesirable top event and breaks down possible causes (engineering) | [`electrical-nasa-fault-tree`](https://extapps.ksc.nasa.gov/Reliability/Documents/Fault_Tree_Handbook_with_Aerospace_Applications_August_2002.pdf) (Ch.1 introduction, deductive fault-tree approach; main) | Pedagogical sketch is not a complete quantitative reliability model. |
| E021000-05 | Fault trees use AND/OR event logic and can omit interacting causes if modeled poorly (engineering) | [`electrical-nasa-fault-tree`](https://extapps.ksc.nasa.gov/Reliability/Documents/Fault_Tree_Handbook_with_Aerospace_Applications_August_2002.pdf) (Ch.2 fault tree structure and gates; main) | Example not exhaustive or mutually exclusive. |
| E021000-06 | Chronology, changes and preserving evidence help distinguish causal explanations (engineering) | [`electrical-doe-causal-2024`](https://www.energy.gov/documents/doe-std-1197-2024-finalpdf) (§5 and causal method summaries; main) | DOE report standards apply in DOE context; transferred reasoning only. |
| E021000-07 | Repeated symptoms do not distinguish hypotheses if predicted by all (inference) | [`electrical-bayes-sep`](https://plato.stanford.edu/entries/bayes-theorem/) (§1 likelihood and confirmation; general_theory) | Qualitative inference, no calibrated failure rates. |
| E021000-08 | A normal reading at a different time does not refute an intermittent event (engineering) | [`electrical-nist-dmm-1988`](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir88-4021.pdf) (§4.2 response time and measurement limitations; measurement_context); [`electrical-doe-causal-2024`](https://www.energy.gov/documents/doe-std-1197-2024-finalpdf) (timeline and evidence preservation; independent_diagnostic_context) | Exact instrument sampling and event duration determine informativeness. |
| E021000-09 | Meter connection and impedance determine whether a test is discriminating (engineering) | [`electrical-nist-dmm-1988`](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir88-4021.pdf) (§4.1 loading and §4.2 response; main); [`electrical-keysight-ghost`](https://www.keysight.com/us/en/use-cases/eliminate-ghost-voltage-measurements.html) (high/low impedance interpretations; independent_manufacturer_context) | Selection of actual field test must be matched to qualification and instrument. |
| E021000-10 | Bayesian reasoning compares support by likelihood rather than vividness (mathematics) | [`electrical-bayes-sep`](https://plato.stanford.edu/entries/bayes-theorem/) (§1 Bayes theorem; Bayes 1764 attribution; main) | No numerical priors or probabilities invented for electrical failures. |
| E021000-11 | A source-device log is limited to its sensing point, time and internal definitions (engineering) | [`electrical-nist-tn1297`](https://www.nist.gov/pml/nist-technical-note-1297) (measurement context and uncertainty; metrology_context); [`electrical-doe-causal-2024`](https://www.energy.gov/documents/doe-std-1197-2024-finalpdf) (evidence interpretation; diagnostic_context) | Product-specific event-code semantics not verified. |
| E021000-12 | Visual heat damage supports prompt risk control without a microscopic root cause (safety) | [`electrical-doe-causal-2024`](https://www.energy.gov/documents/doe-std-1197-2024-finalpdf) (graded causal analysis and risk context; general_method) | Aspirational safe decision principle; no building-specific inspection requirement given. |
| E021000-13 | Correction of symptoms and proof of root cause are distinct stages (engineering) | [`electrical-doe-causal-2024`](https://www.energy.gov/documents/doe-std-1197-2024-finalpdf) (causal analysis and corrective actions; main); [`electrical-nasa-fault-tree`](https://extapps.ksc.nasa.gov/Reliability/Documents/Fault_Tree_Handbook_with_Aerospace_Applications_August_2002.pdf) (analysis of causes and failure events; independent_analytical_context) | No repair acceptance standard for particular appliance is claimed. |
| E021000-14 | A documentation-based repair scope should tie observations to acceptance evidence (engineering) | [`electrical-doe-causal-2024`](https://www.energy.gov/documents/doe-std-1197-2024-finalpdf) (causal analysis and actions; general_method); [`electrical-doe-prints-v1`](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1016-93_VOL1.pdf) (revision and drawing records; independent_documentation_context) | Real job documentation is jurisdiction and product dependent. |

