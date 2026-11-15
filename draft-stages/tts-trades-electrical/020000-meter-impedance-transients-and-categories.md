# 020000 — Why a Meter Can Mislead: Input Impedance, Ghost Voltage, and Measurement Categories

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** paper measurement models, instrument manuals and simulations. Distinguish meter specifications from safety verification of an actual installation.

<!-- BEGIN SPOKEN LECTURE -->

# Why a Meter Can Mislead: Input Impedance, Ghost Voltage, and Measurement Categories

A meter says sixty volts on a conductor that seems disconnected from its source. Is the conductor energized by a substantial power supply? Is it floating beside another conductor and being coupled through a small capacitance? Is the meter responding to a waveform it does not measure accurately? Is the reading caused by a reference or instrument problem? The display alone does not tell us.

The central skill in this lecture is to stop treating an electrical meter as a transparent window. A meter is a component inserted into a circuit, built to survive a particular environment, with specified limits on what its displayed numbers mean. It has input impedance, bandwidth, protection features and measurement categories. These are not obscure footnotes; they are the physics of whether the evidence is trustworthy.

## A measuring instrument creates a new circuit

Start with a voltmeter. An ideal voltage measurement draws zero current, but a real input offers finite resistance and capacitance. When the circuit under test has a low source resistance, a ten-megohm input often hardly changes the voltage. When the circuit has a high source resistance, that same input can be a significant load.

Imagine a source modeled as eighty volts through a two-megohm series resistance. A ten-megohm voltmeter across the output reports about sixty-six point seven volts. Replace the meter with a one-hundred-kilohm input, and the modeled voltage drops to about three point eight volts. Both instruments would be measuring a *different loaded circuit*. Those two numbers do not require the source to have changed internally.

This example is an ordinary resistive Thevenin model. It is not a realistic universal equivalent circuit for all stray or induced voltages, many of which involve capacitances with frequency-dependent impedance. But it makes the important point: the impedance of the measurement is part of the answer.

The National Institute of Standards and Technology's multimeter performance report by T. F. Leedy and colleagues describes input impedance, common-mode rejection and protection as specifications that shape the measurement. Keysight's instrument notes provide a manufacturer-specific example in which an alternating-current voltage input behaves like a resistor in parallel with capacitance. As frequency rises, the effective impedance changes. A meter that is minimally intrusive at direct current can perturb a higher-frequency signal much more.

## A high reading from a weakly coupled source

Two nearby conductors can exchange tiny displacement currents through capacitance. A conductor with no firm low-impedance connection to a source can acquire an alternating potential relative to a chosen reference. Because a high-input-impedance meter requires little current, it may display a substantial voltage even though the coupling cannot supply the same voltage under a much larger load.

This phenomenon is often called **phantom voltage** or **ghost voltage**. Those names are convenient but can be misleading. There is a real electrical interaction; the word ghost only indicates that the apparent source may have high impedance and little available current under the modeled conditions. It is not a promise of harmlessness, and the term does not identify the mechanism in any particular installation.

An instrument with a designed low-impedance voltage mode can deliberately load the measured circuit to help distinguish a high-impedance coupled source from a low-impedance supply. Keysight describes that principle in its technical discussion of ghost-voltage measurements. But this is a diagnostic technique with its own equipment, ratings and conditions—not a proof of safe absence of energy. A real live source can also be high impedance, and a low-impedance connection can disturb sensitive electronics or demand more current than the measurement setup can safely accommodate.

The right question is not “Is a nonzero value a ghost?” It is “Which source model and measurement method could produce this reading, and what evidence distinguishes those possibilities?”

## Transients and the reason a meter needs more than a voltage rating

Electrical systems experience short-duration overvoltages. Switching inductive loads, faults and externally coupled disturbances can briefly push a circuit far above its nominal operating voltage. Those transients may be too fast for the ordinary display to report, yet they affect insulation stress and the internal protection required of measuring equipment.

For this reason, electrical test instruments are not characterized solely by a number such as six hundred volts. Under IEC measurement-equipment standards, a **measurement category** and its rated voltage jointly describe an environment and related transient withstand expectations. You will encounter CAT II, CAT III and CAT IV markings. In general explanatory terms, CAT II often concerns suitable utilization-side loads, CAT III concerns parts of fixed installation distribution, and CAT IV concerns the origin or service side of certain low-voltage installations. The categories are not simply steps of greater continuous voltage. They relate to installation context and available transient energy.

An important nuance: a catalog table that associates a category with a familiar location is a guide, not authority to assign a particular unseen terminal a rating. The controlling instrument manual, tested marking, actual measurement environment and applicable standard matter. A meter with an impressive CAT number but an inadequate voltage rating, incompatible leads or damaged protection is not made appropriate by the category name alone.

The IEC 61010-2-030:2023 standard addresses safety requirements for equipment whose measuring circuits connect to external circuits. Its official public catalog describes scope and edition. The full test requirements were not reviewed for this lecture, so we do not turn a publisher abstract into detailed performance promises. Manufacturer technical explanations can help users understand the categories, but they are not substitutes for independent certification or the normative standard.

## Leads, terminals, and the instrument's internal architecture

A meter is a system of case, inputs, rotary switch or electronic configuration, leads, probes, protective components and firmware. Its measurement category applies to a specified arrangement, not to a loose collection of parts with unrelated ratings. The weakest-rated or compromised component in the path can dominate the practical limit.

Voltage and current inputs differ sharply. The voltage input normally aims for a high impedance. The current input normally has a low-resistance shunt and protective fuse. A lead left in a current jack while a person believes the instrument is in voltage configuration can create an unintended low-impedance path. This is a design failure mode, not a fine point about how to hold the probes. The UK Health and Safety Executive's guidance GS38 addresses equipment selection, probe construction, leads, voltage detection, and when dead testing is more appropriate than live testing.

Some voltage detectors are purpose-built to establish whether a circuit is energized under a controlled safe-work method. A noncontact detector responds to an electrical field and can sometimes indicate the presence of an alternating field without a metallic connection. Its sensitivity and geometry also mean it may not indicate all energized states. An “off” indication on such a device cannot be treated as verified absence of voltage in every context.

When the question is a formal safe-isolation verification, the equipment and procedure are selected for that purpose. For example, OSHA's U.S. workplace regulation 29 CFR 1910.333 requires qualified verification of de-energization and checking for possible induced voltage or backfeed in the covered work circumstances. British guidance has its own approach and equipment conventions. Those are important examples of the engineering problem; they are not interchangeable residential codes.

## Frequency, crest factor, and a true-RMS label

The quantity most meters call alternating voltage may be an RMS value, but **RMS** is mathematically defined for a waveform over a specified time interval. The instrument may use AC coupling that excludes direct current, have limited frequency response, reject some common-mode voltage imperfectly, or sample too slowly for a brief transient.

A so-called true-RMS meter is not an infinite-bandwidth waveform analyzer. A nonlinear power supply can draw narrow current pulses whose peak is high relative to RMS. That ratio is called **crest factor**, and it matters to the measurement chain. Even a true-RMS display can lose accuracy if the waveform exceeds the instrument's crest-factor or frequency limits, clips its range, or contains energy the meter's filter suppresses.

Likewise, a brief voltage sag or an intermittent event may occur between display updates. A steady number on the screen is evidence of the conditions the meter averaged or sampled, not a complete recording of the past minute. A suitable logger or waveform recorder can be more informative when the event being investigated is short or rare. But a data logger also has sampling and trigger limits.

## Resolution is not authority

The number of digits on an LCD is not the same as the quality of the measurement. Accuracy specifications depend on range and conditions; some manufacturers state limits as a percentage of reading plus display counts. Calibration and uncertainty statements address other questions. The authors Barry N. Taylor and Chris E. Kuyatt, in NIST Technical Note 1297, distinguish the quantity being measured, the uncertainty of the result, and the method used to estimate that uncertainty.

A precise-looking result may be poorly connected to the question that motivated the test. Suppose a meter reads one hundred twenty point zero volts at a receptacle. That can be consistent with normal supply at that instant. It does not tell you the circuit's fault-clearing performance, connector temperature under load, available fault current, insulation condition, or what happens when a motor starts. Each of those is a different measurand or engineering question.

This is why electrical test programs use more than one technique. IEC 61557-1 specifies general requirements for certain equipment used in testing and monitoring protective measures in low-voltage distribution systems. Its scope is not the same thing as giving a homeowner a universal test checklist. The applicable parts of the series, actual installation type and local commissioning requirements determine the appropriate methods.

## Compare hypotheses using instrument models

Return to the initial report of an unexpected voltage on an apparently disconnected conductor. Before choosing the explanation, the competent analyst asks which two points were compared, what the source arrangement is, whether the meter is high impedance, whether there could be another source or capacitive coupling, and what kind of evidence would distinguish these possibilities.

Notice that the intellectual task is largely the same whether the work concerns a small battery system, an industrial control circuit, or building distribution: identify the circuit, identify the instrument's coupling to it, model what it measures, and make the uncertainty explicit. The danger and required controls are different in each environment, and that affects who conducts the measurement and with what equipment. The reasoning remains valuable even when a direct measurement is not the next sensible action.

A measurement is not the truth delivered by a box. It is an interaction with a physical system whose result must be interpreted. Good instrumentation makes that interaction predictable. Good electrical reasoning remembers that it happened.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Two models, two interpretations

**Resistive model:** An ideal `80 V` source has Thevenin resistance `R_s = 2 MΩ`. A voltage-measuring input `R_m` reads `V_m = 80 * R_m / (2 MΩ + R_m)`. At `10 MΩ`: `66.67 V`; at `100 kΩ`: `3.8095 V`. The load imposed by the meter produces the change. This example is a resistor network; capacitive coupling needs an AC impedance model.

**Capacitive-coupling model:** `I_C = C * d(V_source - V_floating)/dt`. A useful circuit model includes `C_c` from an energized conductor to a floating one and a meter with `R_m || C_m` from that floating conductor to a reference. The phase and magnitude depend on frequency and all impedances. No single resistance represents every real-world phantom-voltage case.

### Measurement-category interpretation

- `IEC 61010-2-030:2023` is an equipment-safety standard for testing/measuring circuits; this source review covered the **official public scope only**, not the test clauses.
- `CAT II/III/IV` are installation-context ratings with rated working voltage; manufacturer tables provide examples, not a universal boundary map.
- Meter body, probes, leads, input terminal selection and condition all matter; category markings do not establish suitability for every high-energy source.
- `IEC 61557-1:2019+AMD1:2024` addresses a different series for test/measurement equipment used to assess protective measures; it is not an alternative definition of CAT ratings.

### Exercises — paper and instrument documentation

1. Calculate both modeled voltages above and the ratio `V_high-Z/V_low-Z`. **Answer:** approximately `17.50`; the source and reference assumptions are unchanged.
2. Why is a true-RMS label insufficient to certify pulse-train measurements? **Answer:** frequency response, crest factor, coupling, sampling and range remain limited.
3. Does a `CAT III 600 V` marking imply suitability at any point inside a building? **Answer:** No. Evaluate context, exact rated configuration, accessories, equipment condition and intended use.
4. A high-Z reading differs sharply from a low-Z reading. Is the circuit therefore safe to touch? **Answer:** No. The readings distinguish loading behavior under test conditions but do not establish all source, transient or fault conditions.
5. A fast transient appears in an event logger but not the meter display. What is the most informative inference? **Answer:** The instruments observed different signal features and/or time windows. Check each device's bandwidth, trigger and acquisition limits.

### Attribution and source boundaries

- **IEC TC 66 and other relevant standards committees** govern the cited IEC measurement-equipment standard families; the official public pages establish their scope and edition, not their full internal performance clauses.
- **T. F. Leedy, K. J. Lentner, O. B. Laug and B. A. Bell** authored the NIST handbook study of multimeter loading and limits. **Barry N. Taylor and Chris E. Kuyatt** authored NIST TN 1297 on measurement uncertainty.
- **Keysight and Fluke** provide manufacturer-origin explanations and product examples, which must be identified as such. **HSE and OSHA** are distinct UK and U.S. occupational authorities; their published procedures do not determine every homeowner's local legal duties.

## Claim-level source map

| Claim ID | Consequential claim | Evidence location and role | Limitations / pending checks |
|---|---|---|---|
| E020000-01 | High input impedance and source impedance form a loaded measurement divider (physics) | [`electrical-nist-dmm-1988`](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir88-4021.pdf) (§4.1 input characteristics; main); [`electrical-keysight-ac-loading`](https://www.keysight.com/zz/en/lib/resources/training-materials/tip-4-measuring-high-frequency-signals--loading-errors-471570.html) (loading error equations; independent_manufacturer_example) | Resistive Thevenin approximation, not a general capacitive coupling model. |
| E020000-02 | The 80V/2M source gives 66.67 V at 10M input and 3.81 V at 100k input (derived_calculation) | [`electrical-nist-dmm-1988`](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir88-4021.pdf) (§4.1 input loading model; method) | Idealized values, arithmetic checked; not a real safe-voltage assertion. |
| E020000-03 | Capacitive coupling can produce apparent ghost voltage on high impedance inputs (engineering) | [`electrical-keysight-ghost`](https://www.keysight.com/us/en/use-cases/eliminate-ghost-voltage-measurements.html) (ghost voltage mechanism; main); [`electrical-keysight-ac-loading`](https://www.keysight.com/zz/en/lib/resources/training-materials/tip-4-measuring-high-frequency-signals--loading-errors-471570.html) (frequency-dependent loading; same_manufacturer_support) | No universal available-current claim from display alone. |
| E020000-04 | Low impedance mode changes loading, not necessarily proof that no hazardous energy exists (safety) | [`electrical-keysight-ghost`](https://www.keysight.com/us/en/use-cases/eliminate-ghost-voltage-measurements.html) (low impedance mode principle; method); [`electrical-osha333`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) (§1910.333(b)(2)(iv), qualified verification and backfeed; independent_regulatory_context) | Field measurement selection and qualification remain site dependent. |
| E020000-05 | Short transients may stress meter insulation without stable display indication (engineering) | [`electrical-fluke-cat`](https://www.fluke.com/en-us/learn/blog/safety/safe-test-tools-real-world-use) (transient discussion; main); [`electrical-iec61010-2-030`](https://webstore.iec.ch/en/publication/75915) (public equipment safety scope; standards_context) | Full IEC transient test clauses not verified in this review. |
| E020000-06 | Measurement category combines application environment and working voltage rating (standards_scope) | [`electrical-fluke-cat`](https://www.fluke.com/en-us/learn/blog/safety/safe-test-tools-real-world-use) (CAT II/III/IV explanation; manufacturer_example); [`electrical-iec61010-2-030`](https://webstore.iec.ch/en/publication/75915) (published scope, 2023 edition; independent_standard_scope) | No particular measurement location/category adjudicated; full text not reviewed. |
| E020000-07 | IEC 61010-2-030:2023 scope covers equipment with measuring circuits connected externally (standards_scope) | [`electrical-iec61010-2-030`](https://webstore.iec.ch/en/publication/75915) (publisher abstract §1; main) | Scope verified only, not normative test details. |
| E020000-08 | Test leads, probes and selected terminals form part of instrument protection system (safety) | [`electrical-hse-gs38`](https://www.hse.gov.uk/pUbns/books/gs38.htm) (published GS38 guidance scope; main); [`electrical-fluke-cat`](https://www.fluke.com/en-us/learn/blog/safety/safe-test-tools-real-world-use) (equipment markings and lead ratings; independent_manufacturer_context) | Technical specifications and application-specific inspection needed. |
| E020000-09 | Current jack/shunt path differs from voltage jack and wrong configuration can cause a fault (safety) | [`electrical-nist-dmm-1988`](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir88-4021.pdf) (§3.1.4 and §4 current measuring circuit; physics); [`electrical-osha334`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.334) (§1910.334(c) equipment suitability; independent_workplace_regulation) | No live measurement procedure or product wiring instructions. |
| E020000-10 | Noncontact voltage indication alone is not comprehensive proof of absence (safety) | [`electrical-hse-gs38`](https://www.hse.gov.uk/pUbns/books/gs38.htm) (guide on voltage detector types and selection; main); [`electrical-osha333`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) (§1910.333(b)(2)(iv), verification; independent_workplace_context) | Specific instruments have distinct sensing modes and performance. |
| E020000-11 | True RMS meters remain subject to crest factor, bandwidth and range limits (engineering) | [`electrical-nist-dmm-1988`](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir88-4021.pdf) (§4.3.3–4.3.4; main); [`electrical-keysight-ac-loading`](https://www.keysight.com/zz/en/lib/resources/training-materials/tip-4-measuring-high-frequency-signals--loading-errors-471570.html) (frequency-dependent input behavior; independent_manufacturer_context) | A True RMS label does not characterize all transients. |
| E020000-12 | IEC 61557-1:2019 plus amendment 2024 sets general scope for testing protective measures (standards_scope) | [`electrical-iec61557-1`](https://webstore.iec.ch/en/publication/102414) (official IEC consolidated abstract; main) | Not a general instrument CAT rating and clauses/installation tests not reviewed. |
| E020000-13 | NIST frames uncertainty as part of meaningful reported measurements (metrology) | [`electrical-nist-tn1297`](https://www.nist.gov/pml/nist-technical-note-1297) (§2 and §7; main) | No numerical uncertainty estimates for the hypothetical instrument. |
| E020000-14 | OSHA verification rule covers U.S. workplaces and induced or backfed voltage (regulatory_scope) | [`electrical-osha333`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) (§1910.333(b)(2)(iv)(B); main) | Does not on its own determine homeowner permissions outside covered workplaces. |

