# 013000 — Protective Devices Have Different Jobs: GFCI, RCD, AFCI, Fuses, Breakers, and Surge Protection

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Practice boundary:** published device markings, product literature, paper scenarios and visual-only observations. No live test setups, induced faults, panel opening, protective-device bypass or installation recipe. Product selection and commissioning need qualified application-specific review.

<!-- BEGIN SPOKEN LECTURE -->

# Protective Devices Have Different Jobs: GFCI, RCD, AFCI, Fuses, Breakers, and Surge Protection

Walk through a hardware store and you may see breakers, ground-fault interrupters, arc-fault interrupters and surge protectors. Some products combine several functions in one housing. Their names sound similar, and all may be sold under the banner of electrical safety. But a device that responds well to one failure might not detect another at all.

The central question is not 'Does this device protect me?' It is 'Which physical event does it detect, under what conditions, and what remains dangerous even if it works exactly as designed?' That question is essential to homeowners evaluating a new circuit, a nuisance trip, an older installation or a proposed upgrade. It is also a good way to distinguish an engineering purpose from the particular code rule that requires protection in a particular location.

## Begin with an ordinary fuse or circuit breaker

A fuse or overcurrent circuit breaker primarily protects conductors and connected equipment from current beyond their intended safe operating conditions. A fuse contains a sacrificial element that opens under defined electrical stress. A resettable breaker has a mechanism to open its contacts. The time-current characteristics may accommodate brief inrush but act on sustained overload and large faults. Its interrupting rating and suitability for the available fault current are separate engineering requirements.

Neither is a universal shock detector. Dangerous current passing through a person's body can be far below a conventional branch breaker trip threshold. A poorly connected terminal can heat while total circuit current looks normal. An ordinary breaker can be performing exactly as designed while another hazard remains. Resetting or up-rating it without explaining the cause is not a solution.

## Residual current is a difference, not a label on a wire

Now imagine a circuit with one line conductor delivering current and a neutral returning it. Under normal conditions the current entering and leaving the monitored conductors balances. A residual-current device observes the vector sum of currents through the conductors that carry normal load. If some current leaves the intended path—for example through a person, wet surface or faulty enclosure—and returns by another route, the monitored currents no longer balance. A device designed for that kind of residual current can open the circuit.

In North American residential language, a ground-fault circuit interrupter, or GFCI, is an important device for personnel protection. In much international practice the broader terms residual-current device and RCD are used. Specific product families include residual-current circuit breakers without integral overcurrent protection, often abbreviated RCCB, and combined residual-current plus overcurrent devices, often called RCBO. Names, available types, waveforms detected, wiring arrangements and required applications differ among standards and manufacturers.

The distinction between a residual-current trip rating and a human safety threshold matters. You may see a thirty-milliampere residual-current rating associated with a common form of additional protection in some systems. That number describes an equipment characteristic within a defined standard, not a statement that thirty milliamperes through the human body is safe. U.S. personnel GFCI classifications are governed by different product standards. Never translate one device label into another country's installation rule by swapping numbers.

The residual-current principle has a specific limitation: a person touching line and neutral together may draw current that leaves and returns through the two monitored conductors. The balance can remain approximately zero even as the person is injured. Similarly, a residual-current device is not necessarily an overcurrent breaker; an RCCB without integral overcurrent function still needs appropriate overcurrent protection elsewhere. And an electrical source may have a circuit arrangement in which a particular device type is not suitable. Approval and compatibility cannot be inferred solely from the word RCD.

## What ground fault does not mean

It is tempting to imagine a GFCI searching for a missing ground wire. The device instead detects current imbalance. A properly applied GFCI may operate for an appropriate fault even where a conventional equipment grounding conductor is absent; that does not make the conductor suddenly appear. Conversely, protective earthing and bonding serve functions that a residual-current detector does not replace. They can maintain accessible metal parts near a safe potential and support other methods of disconnection.

Some official safety descriptions use very confident language about the speed of GFCI operation. That confidence must stay within the device's tested fault conditions and a particular system. A residual-current device can fail, be miswired, be incompatible with the waveform, or be unable to interrupt a path that does not create an imbalance. Even a correctly operating protective device may permit some shock exposure before clearing. This is why the British Health and Safety Executive describes RCD protection as an additional protection layer, not a reason to work on energized equipment.

## An arc-fault device is looking for a different signature

An arc is a current path through ionized gas. A damaging arc can occur across damaged insulation or between conductive parts with a poor connection. Some arcs produce characteristic changes in the current waveform. Arc-fault circuit interrupters—AFCIs in much U.S. language, AFDDs in some other jurisdictions—use sensing and decision logic to detect specified hazardous arcing conditions and disconnect.

These devices target a subset of fire-ignition risks. The U.S. Consumer Product Safety Commission explains that ordinary fuses and breakers may not react to early arcing conditions in house wiring. That gives a reason for adding arc-fault protection. But it does not imply that every high-resistance connection, every spark or every overheating terminal will be detected. The published scope of UL 1699 explicitly excludes an expectation of detecting glowing connections. This is a vital limitation: a loose connection may be dangerously hot with no qualifying arc signature.

Some units combine AFCI and GFCI capabilities. That combination is not proof that the two functions are identical, nor does every device with an AFCI label include GFCI personnel protection. The marking and applicable certification determine what protection has actually been evaluated. An arc-fault device also does not eliminate the need for proper conductor sizing, workmanship, protective enclosures or compatible breakers.

## Transient surges are a third problem

A surge protective device, or SPD, is intended to limit specified transient overvoltages. It is a response to relatively short disturbances such as certain switching events or externally coupled surges. Its job is different from a fuse that opens on sustained overcurrent, a GFCI that detects residual current or an AFCI that analyzes arcing signatures. Surge devices have their own voltage, surge-current, installation and coordination limits. A generic plug-in strip with an SPD label is not a guarantee that every electronic appliance will survive any lightning event.

In many electrical systems the surge protective device itself needs an appropriate connection to the installation's protective system and coordination with other protection. The general physical rationale is that the energy and voltage of a transient must be managed before they damage insulation or electronics. But selecting an SPD for a particular service, panel, PV source or communications line requires specific approved instructions and local requirements. The lecture supplies no wiring procedure.

## Device standards describe scope, not a universal approval

Consider several concrete standard families. UL 943 covers specified U.S.-market Class A GFCIs for personnel protection on certain grounded-neutral AC systems. IEC 61008-1 addresses household residual-current circuit breakers **without** integral overcurrent protection within its published scope. UL 1699 addresses specified arc-fault circuit interrupters intended to mitigate certain arcing-fire risks; its 2025 edition explicitly says these devices are not intended to detect glowing connections. UL 1449 concerns surge protective devices. Each source tells you which class of product is under discussion.

A standard's catalog page may publish the title, edition and scope, but that is not the same as verifying every performance clause, every exception or the product's compliance. An actual installation must consider the adopted national or local code, permitted device types, the particular panel or equipment listing, line arrangement, frequency, available short-circuit current and instructions. Manufacturer claims are useful engineering evidence, but one vendor repeating its own data is not independent corroboration.

## A nuisance trip is a symptom, not an invitation to defeat protection

An RCD or GFCI can trip because of an actual leakage path, moisture or damaged equipment. Some power electronics can also create leakage or waveform conditions that require a compatible device type. An AFCI may trip for reasons that must be diagnosed, and a breaker may interrupt an overload. These mechanisms differ; the tripped-device type alone does not identify the exact cause.

Do not repeatedly reset an unexplained trip, remove a protective conductor, swap a protective device for another model because it fits, or defeat a feature to keep a load running. Product test buttons are intended to exercise particular internal functions according to instructions. They do not prove that the complete wiring and fault-return arrangement are correct, and they are not an electrical safe-work isolation procedure. An installation that requires a qualified assessment has not become a classroom exercise merely because the protective device is visible on a wall.

## A matrix for informed questions

Here is a useful mental matrix. For persistent excess current, ask about the fuse or overcurrent breaker and the conductor it protects. For current escaping the intended line-and-return path, ask about GFCI or RCD protection and the fault arrangement. For some damaging arcing conditions, ask about AFCI or AFDD protection and its detection limits. For a short transient overvoltage, ask about surge protective devices. For an exposed conductive enclosure that might become live, ask about insulation, protective bonding, the fault-current loop and disconnection method. None of these questions is answered completely by an equipment logo.

The listener's objective is not to become a one-person standards committee. It is to understand that protection is the coordination of several mechanisms with different evidence behind them. When you know what each one measures and where it can fail, you can ask much better questions before work begins—and recognize an answer that is only a slogan.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Protection-function table (scope, not installation selection)

| Device family | Primary detectable condition | Important limitation |
|---|---|---|
| Ordinary fuse / overcurrent breaker | Overload and specified fault-current levels | Does not reliably detect all harmful body currents, leakage, glowing connections or arc signatures |
| GFCI / RCD | Residual imbalance through monitored live conductors | May not trip on balanced line-to-neutral body contact; no universal protection from shock |
| RCCB | Residual-current function without integral overcurrent protection | Requires separately coordinated overcurrent protection |
| RCBO / combination functions | Multiple specified protection functions | Exact capabilities depend on listing, markings, model and intended system |
| AFCI / AFDD | Specified arcing-current signatures | Not all hot loose contacts; UL 1699 expressly excludes glowing-connection detection |
| SPD | Specified transient overvoltages | Does not perform the jobs of an RCD, AFCI or standard overload protection |

### Worked conceptual example

If 8.00 A RMS enters via one monitored conductor and 7.98 A RMS returns along the intended opposite conductor with compatible waveforms, a simple arithmetic illustration gives a 0.02 A residual. **This does not predict a real GFCI trip**: timing, waveform, device type, calibration and the system topology are unspecified. Never produce such an imbalance by applying a real electrical fault.

### Desk exercises with answers

1. **Choose the question.** A device has a local overheated terminal but normal total load current. Which protection might miss it? **Answer:** Ordinary overcurrent protection may not see an overload; an AFCI also may not detect a glowing connection. Proper workmanship and assessment remain essential.
2. **Balanced contact.** Someone bridges line and neutral with their body. Does a residual-current detector have to operate? **Answer:** No; the monitored sum may remain balanced. The contact is still dangerous.
3. **Two functions.** A published product is called an RCCB without integral overcurrent protection. What else must the designer consider? **Answer:** Suitable overcurrent protection and coordination, among other product/system-specific requirements.
4. **Surge question.** Does a surge-strip listing prove it can prevent every fire or shock? **Answer:** No. Surge limitation is distinct from overcurrent, residual-current and arc-fault protection.
5. **Standards literacy.** A website advertises UL 1699. Can you conclude a particular panel accepts that breaker? **Answer:** No. Exact listing, model, panel compatibility and locally adopted requirements must be checked.

## Claim-level source map

| Claim | Consequential statement | Supporting evidence, exact source location, and role | Unresolved scope / limitation |
|---|---|---|---|
| E013000-01 | Fuses and ordinary breakers handle overcurrent, not every shock/arc hazard | [`electrical-osha304`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) (§1910.304(f); main); [`electrical-cpsc-afci`](https://www.cpsc.gov/s3fs-public/5133.pdf) (p.1 AFCI vs GFCI, ordinary protection limitations; independent_context) | Actual combination devices may offer more than one function. |
| E013000-02 | GFCI/RCD measures imbalance through monitored load conductors | [`electrical-osha-gfci`](https://www.osha.gov/etools/construction/electrical-incidents/ground-fault-circuit-interrupters) (How it works and limitations; main); [`electrical-hse-rcd`](https://www.hse.gov.uk/electricity/electricequip.htm) (RCD protection purpose and limitation; independent_regulator_context) | Exact sensing type, wiring and response time require full product docs. |
| E013000-03 | Balanced line-neutral body contact may evade residual detection | [`electrical-osha-gfci`](https://www.osha.gov/etools/construction/electrical-incidents/ground-fault-circuit-interrupters) (Line contact hazard examples; main) | Independent mechanism-specific corroboration not reviewed; safety-critical limitation remains true under specified balance hypothesis. |
| E013000-04 | RCD is supplemental; it cannot prevent every electric shock | [`electrical-hse-rcd`](https://www.hse.gov.uk/electricity/electricequip.htm) (Use an RCD section; main); [`electrical-osha-gfci`](https://www.osha.gov/etools/construction/electrical-incidents/ground-fault-circuit-interrupters) (Line contact limitation; independent_corroboration) | No recommendation to work energized or deliberate testing by shock. |
| E013000-05 | IEC RCCB scope excludes integral overcurrent protection | [`electrical-iec61008`](https://webstore.iec.ch/en/publication/67980) (IEC 61008-1:2024 public abstract, device class; main) | Full normative text not inspected; application-specific design pending. |
| E013000-06 | UL 943 scope refers to specified Class A personnel GFCIs | [`electrical-ul943`](https://www.shopulstandards.com/ProductDetail.aspx?ShowFreeviewModal=1&productId=UL943) (§1 Scope, published public abstract; main) | Scope only; full test requirements and individual certification not checked. |
| E013000-07 | AFCI addresses some arcing fire mechanisms distinct from GFCI | [`electrical-cpsc-afci`](https://www.cpsc.gov/s3fs-public/5133.pdf) (p.1 AFCI vs GFCI distinctions; main); [`electrical-ul1699`](https://www.shopulstandards.com/ProductDetail.aspx?UniqueKey=49312) (§1.1 intended arc fire mitigation; independent_standard_scope) | Device performance conditional and intended application limited. |
| E013000-08 | UL 1699:2025 excludes glowing connection detection | [`electrical-ul1699`](https://www.shopulstandards.com/ProductDetail.aspx?UniqueKey=49312) (§1.3 explicitly says not intended to detect glowing connections; main) | Direct public scope statement; full standard not inspected; not a promise of behavior of every product. |
| E013000-09 | UL 1449 covers designated transient surge limiting devices | [`electrical-ul1449`](https://www.shopulstandards.com/ProductDetail.aspx?productId=UL1449) (§1.1 published scope; main) | Publisher scope only; no actual SPD selection/voltage claim verified. |
| E013000-10 | Test button does not verify entire installation or safe absence of voltage | [`electrical-hse-rcd`](https://www.hse.gov.uk/electricity/electricequip.htm) (RCD user test guidance; main); [`electrical-osha333`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) (§1910.333(b)(2)(iv) qualified verification of deenergization; separate_regulatory_context) | Product instructions and qualified testing required; test button alone not safe-work verification. |
| E013000-11 | Code adoption, panel compatibility and listing are separate requirements | [`electrical-osha303`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.303) (§1910.303(b)(2) equipment instructions; main); [`electrical-iec60364`](https://webstore.iec.ch/en/publication/63699) (Published IEC 60364 general scope only; region_context) | Occupational rule does not prove private-household permission; exact local adopted codes and product list required. |
| E013000-12 | A tripping device is a symptom not an assured diagnosis | [`electrical-hse-rcd`](https://www.hse.gov.uk/electricity/electricequip.htm) (RCD testing and faulty devices; main); [`electrical-osha333`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) (Safe-work / qualified exposure rules; limited_context) | Specific trip cause must be investigated by competent personnel; not DIY diagnostics. |
| E013000-13 | Illustrative 8.00 vs 7.98 ampere residual equals 20 mA | [`electrical-osha-gfci`](https://www.osha.gov/etools/construction/electrical-incidents/ground-fault-circuit-interrupters) (Differential-current principle; concept_source) | Arithmetic only: no trip-time or waveform prediction and no intentional fault test. |

**Audit status:** Source-audited educational draft, not independently reviewed or approved by a qualified electrician, engineer, medical clinician or local authority. Full locally adopted code and product listing documents have not been reviewed. A claim may have one authoritative line of evidence without independent corroboration; see the individual ledger entry rather than treating source count as a validation score.
