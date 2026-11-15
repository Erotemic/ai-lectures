# 002000 — Electricity Can Hurt: The Hazard Model and the Safe-Work Boundary

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Background:** voltage, current, and power at an introductory level. **Purpose:** distinguish mechanisms of harm and explain why an educational explanation is not sufficient field qualification.

<!-- BEGIN SPOKEN LECTURE -->

# Electricity Can Hurt

Imagine two electrical failures. In the first, a person touches a damaged metal appliance and receives a shock. In the second, nobody touches a live conductor, but a poor connection inside a wall grows hot enough to damage insulation and ignite nearby material. Both events are electrical hazards, yet they follow different physical paths and require different protective designs.

The most serious mistake in thinking about electrical safety is to imagine a single scale with 'low voltage' at one end and 'high voltage' at the other, as though a number by itself settled the question. Voltage matters, but it is not the entire hazard. A dangerous event depends on the available source energy, the path through which that energy can act, the duration of contact or fault, the environment, and the devices or structures that prevent exposure.

We can learn the hazard mechanisms without putting ourselves in their presence. That distinction is foundational to this course. Knowing why a switch might be hazardous does not require opening the box to confirm it. Knowing what a fault-current path is does not require producing a fault. Electrical trades require physical skills acquired under controlled conditions, and some risks belong exclusively to qualified people using procedures and equipment matched to the installation.

## Electric shock: the body becomes part of a circuit

A shock occurs when current flows through the body. The severity depends on multiple variables: the current's magnitude, duration, frequency, path through the body, contact area and condition of the skin, individual circumstances, and the surrounding environment. Wet skin can reduce contact resistance. A fall caused by involuntary muscle movement can add a second injury. A shock that does not leave an obvious burn can still be medically serious.

The crucial point is that the body is not an abstract resistor with one fixed value. Body impedance varies with conditions, and its tissue response is not captured by a single universal current threshold. An insulating surface that seems protective when dry may not behave the same way when wet. A voltage measurement made between two different points can change the estimated touch hazard. For that reason, safe practice does not use a casual calculation about the body to declare a live circuit touchable.

People sometimes describe the earth as though it were the normal destination of every electrical current. That can mislead. Current needs a complete path back to a source, not necessarily a route through soil. Contact with an energized conductor and a grounded metal surface can create such a path. Contact with two conductors at different potentials can also create one, even without touching the earth. Protective grounding and bonding are not mystical ways to make all voltage disappear; they are engineered parts of a broader fault-control strategy.

## Heating and fire: small resistances can matter

An appliance drawing normal current can still be dangerous if a connection is poor. Suppose a contact has an added resistance of a fraction of an ohm. Current passing through that contact converts electrical energy to heat there. With enough current, heat is concentrated in a very small region. An enclosure can conceal damage from view. Heat may degrade insulation and make the contact worse, leading to a feedback process.

A standard overcurrent device is often designed primarily to protect conductors and interrupt large fault currents under defined conditions. It does not guarantee that every hot connection will draw enough current to trip. An arcing-fault protective device may detect some dangerous arcing signatures; it does not eliminate every possible fire mechanism. A residual-current device detects imbalance under its design conditions; it is not a temperature monitor. Protection is layered because failures are physically different.

That makes an outward symptom important. A switch plate that becomes unexpectedly warm, a burning smell, discoloration, repeated unexplained tripping, or intermittent crackling can be evidence that an installation needs qualified assessment. The useful skill for a homeowner is often to recognize a warning early, stop using affected equipment, isolate it where this can be done without exposure, and call someone equipped to investigate safely. Repeatedly resetting a protective device without understanding why it operated is not troubleshooting.

## Arcing and arc flash: dangerous energy without body contact

Electricity can cross a gap as an arc. Some arcs are part of a device's intended operation, but an uncontrolled arc can release intense heat, light, sound, pressure, and molten material. A person does not have to become part of a conducting path to be injured by that release.

The risk is especially important near high-energy sources and distribution equipment. It is a mistake to assume that common household voltage makes an exposed service compartment safe to work in. The available fault current and how rapidly protective equipment operates can determine how much energy an arc releases. A home's upstream source may be capable of delivering very high current even when a particular appliance normally draws very little.

Workplace rules and technical guidance therefore treat electrical arc hazards separately from shock. Personal protective equipment can reduce certain consequences when correctly selected and used by trained workers, but it is not a substitute for arranging the work so that energized exposure is absent. We will teach the principles behind those practices; this lecture is not training for energized work.

## What protective devices can and cannot do

Consider the ordinary circuit breaker. Its job is to open a circuit under certain overcurrent conditions. A breaker must be matched to the circuit design and the faults it could interrupt. Its handle position and trip behavior tell us something about the system, but not everything. A breaker that did not trip does not prove a circuit harmless; a breaker that did trip does not prove the fault has gone away.

A ground-fault circuit interrupter, called a GFCI in U.S. practice, compares current going out on protected conductors with current returning through the intended paths. An unexpected imbalance can indicate leakage through an unintended path, possibly a person. The device is designed to disconnect rapidly under the conditions specified by its rating. In many other regions, similar protective functions are provided by residual-current devices, often abbreviated RCD. The devices and trip criteria are not automatically interchangeable in every application.

A GFCI cannot be expected to protect someone who becomes part of a current path between two conductors while the current returning through the device remains balanced. Nor does it provide overcurrent protection unless combined with a suitable overcurrent device. An arc-fault circuit interrupter, or AFCI, targets some dangerous arcing patterns that can create fire hazards. Protection features are not interchangeable simply because their names contain the word 'fault.'

Equipment grounding and bonding address another concern: if a normally non-current-carrying metal case becomes energized because of an internal failure, the system should keep the accessible metal at safer relative potentials and, for designs based on rapid fault disconnection, provide an effective return path so a protective device can operate. The exact arrangement varies with the source and earthing system. A grounding electrode driven into soil is not a substitute for an effective fault-current return path to the source.

## The most important safety skill: knowing what is not isolated

Think about an electric appliance that has been turned off by its normal power button. It might still contain energized components upstream of the button. A switch may interrupt only one conductor. A device may have stored energy in capacitors after its supply is removed. A solar array can generate voltage when illuminated. A backup source or incorrectly connected circuit may energize conductors unexpectedly. Even a circuit label may be wrong.

This is why 'off' and 'verified de-energized' are not synonyms. Professional safe-work practice involves correctly identifying all electrical sources, establishing an appropriate isolation boundary, preventing inadvertent re-energization, and confirming the actual absence of hazardous energy at the work location with suitable test equipment and qualified procedures. In U.S. workplaces, OSHA's electrical safe-work provisions expressly address de-energizing, lockout or tagging, and verification by qualified personnel. Other jurisdictions have their own detailed rules.

We are not going to translate that into an oversimplified instruction like 'flip the breaker and touch the wire.' That would erase the very failure modes the procedure is meant to control. Even when a homeowner is legally allowed to do some wiring, permission and competence are not the same thing. A noncontact voltage indicator can be useful for preliminary awareness, but it cannot alone establish that every relevant conductor is safe to touch. Test instruments themselves have voltage and measurement-category ratings, lead requirements, inspection needs, and modes of failure.

Some equipment remains dangerous even after a customer disconnect has been opened. Service conductors or upstream portions of a panel can remain energized. Power electronics and storage systems introduce additional sources of energy. Anyone planning work must understand the precise equipment and its isolation design, not rely on general statements about what a main switch usually does.

## What can you learn safely before learning the physical trade?

You can learn to read a nameplate and identify whether a device is rated for the available voltage and frequency. You can calculate normal power and energy requirements. You can diagram where protective devices would belong in a conceptual circuit. You can understand the difference between a line conductor, neutral, and protective earth without touching any of them. You can learn to identify damaged extension cords, compromised plugs, blocked equipment ventilation, and inappropriate reliance on adapters. You can ask a contractor whether the intended connection is approved for the equipment and what testing will establish that the finished installation is safe.

A current-limited educational electronics kit can also be useful. It lets a learner explore resistance, voltage and simple switching on a low-energy supply designed for training. Such a kit still needs appropriate instructions and adult oversight where applicable; even small batteries can overheat if shorted, and some power sources or capacitors can deliver hazardous currents. We do not use exposed household wiring as a laboratory.

For field work, the ladder of competence is different. A person must learn to recognize hazards on site, identify and verify isolation, choose correctly rated equipment, maintain physical workmanship, and document inspections and tests. That learning requires demonstrations, supervision, feedback, and an understanding of the applicable law. Listening prepares questions and judgment; it does not confer an electrician's skills.

## What to do when someone may have been injured

An electrical incident can remain hazardous to rescuers. Do not grab a person who may still be in contact with an energized source. Contact emergency services and arrange isolation of the source only if it can be done without exposing yourself. Follow emergency dispatcher guidance; trained responders may need to perform cardiopulmonary resuscitation or use an automated external defibrillator after the area has been made safe. If someone may have received an electric shock, call emergency services or other emergency medical help. Never touch a person who may still be in contact with an energized source. Electrical injury can be serious even without a visible burn.

This is also part of the craft: safe work includes what happens before work, during it, and after something goes wrong. The skill is not bravery near energized equipment. It is designing the job so that nobody has to be brave near energized equipment.

## A lasting way to think about risk

Every electrical hazard has a source of energy, a possible path to a person or combustible material, and a set of barriers or controls. A good protection system interrupts at least one dangerous link. Better systems build redundancy, make failure visible, and fail in predictable ways. A device label, breaker, enclosure, or inspection record gives useful evidence, but none excuses ignoring the others.

There is no single protective trick that makes electrical work safe. There is a disciplined way of reasoning about electrical energy, an increasingly precise vocabulary for what could happen, and a boundary between understanding a system and being qualified to alter it. That boundary is the first practical lesson this subject must teach.

<!-- END SPOKEN LECTURE -->

## Technical companion — display only

### Fault/hazard matrix

| Failure mechanism | Hazard | Representative engineered controls | What the control does *not* guarantee |
|---|---|---|---|
| Insulation damage, accessible energized conductor | Shock and secondary injury | Insulation, barriers, isolation, suitable RCD/GFCI and earthing strategy | RCD cannot make all contact paths harmless |
| Sustained conductor overcurrent | Heating and fire | Proper cable ampacity, protective device with appropriate rating | An ordinary breaker is not a detector of every poor connection |
| High-resistance termination | Local heat | Approved connection, correct materials and terminations, inspection | A circuit might remain below an overcurrent trip threshold |
| Sustained electrical arcing | Fire and burn | Suitable protective devices, enclosure, work isolation | An AFCI does not detect every arc; an enclosure does not eliminate exposure |
| Unexpected backfeed or stored energy | Shock/arc during work | Source identification, isolation, verification, qualified safe-work procedure | Control switch position is not proof of dead conductors |

### Case-study questions (desk-only)

1. A circuit breaker does not trip while a receptacle discolors. Does that prove there is no fault? **No.** Heating at a poor contact may exist below the breaker's trip threshold.
2. Someone turns an appliance off using the power button. What might remain energized? **Input terminals, filters, capacitors, upstream wiring, or other connected supplies**, depending on design.
3. What specific hazard does an RCD/GFCI principally address? **Unintended leakage current and resulting shock risk**, not every overcurrent, fire mechanism, or balanced line-to-neutral shock.
4. Is a grounding rod alone a reliable way to open a breaker after a line-to-case fault? **No.** The entire fault-return impedance and protective-device strategy matter.

**Practice classification:** desk-only and visual-only observation of accessible equipment with covers closed. Do not open live enclosures or perform live instrument testing as part of this exercise.

### Primary references

- OSHA 29 CFR 1910.333 — qualified de-energization and verification (`electrical-osha333`). These are U.S. *workplace* rules, not a universal DIY permit.
- OSHA 29 CFR 1910.334 — test instruments, portable cords and inspection (`electrical-osha334`).
- OSHA — arc-flash hazards at ordinary distribution voltages (`electrical-osha-arc`).
- ESFI — shock protection and leakage-current detection (`electrical-esfi-gfci`).
- ESFI — arc-fault protection (`electrical-esfi-afci`).
- OSHA grounding incident guide (`electrical-osha-ground`).

### Claim-level source map (editorial review: 2026-11-15)

Each claim has a stable evidence ID in `metadata/002000.json`. The entries below identify the supporting source, a precise section when available, and its **role**. A publisher abstract supports only a standard's edition and scope, not the detailed requirements of its normative clauses. The reader-facing lecture is not an installation authorization.

| Evidence ID | Narrow claim | Evidence links, exact location, and role |
|---|---|---|
| E002000-01 | Shock depends on current path and exposure, not a magic safe household voltage | [OSHA (U.S. Department of Labor)](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) — §1910.333(a): direct/indirect contact hazard (main; `electrical-osha333`); [Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-from-electrical-hazards.html) — supporting overview (not an independent clause audit) (contextual_source_only; `electrical-cdc-firstaid`) |
| E002000-02 | A low-voltage installation can present major arc-flash risk | [OSHA (U.S. Department of Labor)](https://www.osha.gov/electrical/flash-hazards) — Arc flash at 120/208 V (main; `electrical-osha-arc`) |
| E002000-03 | Ordinary breaker/fuse overcurrent function is not GFCI personnel protection | [U.S. Department of Labor, OSHA](https://www.osha.gov/etools/construction/electrical-incidents/ground-fault-circuit-interrupters) — GFCI function and line-contact limits (main; `electrical-osha-gfci`); [Electrical Safety Foundation International (ESFI)](https://www.esfi.org/ground-fault-circuit-interrupters-gfci) — supporting overview (not an independent clause audit) (contextual_source_only; `electrical-esfi-gfci`) |
| E002000-04 | GFCIs compare outgoing and returning current and may not interrupt balanced contact | [U.S. Department of Labor, OSHA](https://www.osha.gov/etools/construction/electrical-incidents/ground-fault-circuit-interrupters) — Line-contact limitation (main; `electrical-osha-gfci`); [Electrical Safety Foundation International (ESFI)](https://www.esfi.org/ground-fault-circuit-interrupters-gfci) — supporting overview (not an independent clause audit) (contextual_source_only; `electrical-esfi-gfci`) |
| E002000-05 | AFCIs and GFCIs address different failure classes | [Electrical Safety Foundation International (ESFI)](https://www.esfi.org/arc-fault-circuit-interrupter-afci-advanced-electrical-fire-protection-for-the-home/) — AFCI vs GFCI Q&A (main; `electrical-esfi-afci`); [Electrical Safety Foundation International (ESFI)](https://www.esfi.org/ground-fault-circuit-interrupters-gfci) — supporting overview (not an independent clause audit) (contextual_source_only; `electrical-esfi-gfci`) |
| E002000-06 | The equipment grounding path must be maintained and effective | [U.S. Department of Labor, OSHA](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) — §1910.304(g)(5),(8) (main; `electrical-osha304`); [OSHA (U.S. Department of Labor)](https://www.osha.gov/etools/construction/electrical-incidents/grounding) — supporting overview (not an independent clause audit) (contextual_source_only; `electrical-osha-ground`) |
| E002000-07 | Personnel GFCI/RCCB does not automatically provide overcurrent protection | [International Electrotechnical Commission, SC 23E](https://webstore.iec.ch/en/publication/67980) — Device class title: without integral overcurrent protection (main; `electrical-iec61008`) |
| E002000-08 | Workplace de-energization includes lockout/tagout and qualified verification | [OSHA (U.S. Department of Labor)](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) — §1910.333(b)(2)(iv) (main; `electrical-osha333`); [NFPA 70E technical committee / NFPA](https://www.nfpa.org/codes-and-standards/nfpa-70-standard-development/70E) — supporting overview (not an independent clause audit) (contextual_source_only; `electrical-nfpa70e`) |
| E002000-09 | Testing equipment needs correct rating and qualified operation | [OSHA (U.S. Department of Labor)](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.334) — §1910.334(c)(1)-(3) (main; `electrical-osha334`) |
| E002000-10 | After a suspected electrical shock, summon emergency medical help and avoid contact with an energized person | [Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-from-electrical-hazards.html) — Key points and First aid, steps 1–2 (main; `electrical-cdc-firstaid`) |

**Editorial limitation:** The citations identify evidence and its intended use. Not all consequential claims have two independent sources, and full locally adopted code clauses and equipment listing conditions have not been checked. A qualified safety/electrical review remains **pending**; the track is currently an educational draft, not a certified field manual.
