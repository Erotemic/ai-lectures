# 023000 - Split-Phase, Three-Phase, and the Voltages Between Wires

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** phasor diagrams, paper load calculations and published nominal-voltage tables.

<!-- BEGIN SPOKEN LECTURE -->

# Split-Phase, Three-Phase, and the Voltages Between Wires

Suppose two houses each have receptacles described as one hundred twenty volts. A heating appliance in the first house receives two hundred forty volts between two outer supply conductors. A similar appliance in a small commercial building sees about two hundred eight volts between two conductors even though each conductor is also about one hundred twenty volts from the neutral. Those numbers are not a rounding discrepancy. They describe different alternating-current geometries.

The essential idea is that voltage is a **difference between two electrical potentials**. A number printed on one conductor's label makes sense only with its reference conductor. When several alternating voltages are available, the timing of their waveforms determines the voltage between them. This is where the vocabulary of split-phase, single-phase and three-phase power becomes useful.

## A split-phase source is one winding with a center reference

Consider a transformer secondary winding whose two ends we call L1 and L2. A connection at its midpoint is called a center tap. In a familiar North American nominal system, the voltage from L1 to that midpoint is about one hundred twenty volts RMS, and the voltage from L2 to the midpoint is also about one hundred twenty volts RMS. The entire winding provides two hundred forty volts between L1 and L2.

Imagine measuring a voltage waveform from L1 to the midpoint. Then imagine measuring from L2 to the same midpoint. With consistent polarity conventions, the two waveforms have opposite signs at a given instant. Their phasors are separated by one hundred eighty degrees. The voltage between the outer ends is their difference, and its magnitude is the sum of the magnitudes of the two equal half-winding voltages. That gives two hundred forty volts.

This arrangement is often called **split-phase** or **single-phase three-wire**. The description matters. It is not the same as taking two arbitrary phases from a three-phase system, and it does not create two independent three-phase supply phases. Both halves are part of one single-phase transformer secondary.

The center tap often serves as the grounded neutral, subject to the installation's grounding arrangement. A nominal one-hundred-twenty-volt load connects across one outer conductor and neutral. A two-hundred-forty-volt load connects across the two outer conductors. Some equipment uses both voltages, for example two hundred forty volts for a heating element and one hundred twenty volts for controls. The exact appliance design must be taken from its label and technical documentation, not guessed from its plug shape.

Why not simply distribute all loads at one hundred twenty volts? Higher voltage can transfer a given ideal real power with less current when power factor and conditions are comparable. If a resistive load consumes two thousand four hundred watts, a nominal one-hundred-twenty-volt model uses twenty amperes; a nominal two-hundred-forty-volt model uses ten. The reduced current can reduce conductor heating for a given resistance. But a voltage class alone does not dictate safe conductor sizing: connection ratings, operating conditions and code requirements enter the practical design.

## Neutral current in the center-tapped system

In a three-wire, center-tapped single-phase system, consider two resistive loads, each connected from an outer conductor to neutral. The neutral carries the vector sum of their return currents. Because those two source voltages are oppositely directed relative to the center tap, the neutral currents tend to cancel when comparable loads are placed on opposite halves of the supply.

If both loads draw eight amperes under the simple sinusoidal resistive model, the neutral carries zero current from this pair. If one draws eight and the other draws three, the neutral carries five amperes. The example is not a declaration that a real neutral is inactive or safe; neutral current depends on actual load balance, waveform shape, connections, and system integrity.

Now consider an open neutral in a circuit feeding two unequal series-connected loads from the outer conductors. The midpoint of the load pair is no longer held at the transformer's center reference. The two load voltages can shift drastically, with the higher-impedance load taking the larger share of the two-hundred-forty-volt supply. This is a physical explanation for why a missing neutral is not merely a loss of an optional return wire. It can expose equipment to damaging voltage and produce hazardous accessible potentials.

## Three-phase means three timed waveforms

In a balanced three-phase source, three sinusoidal voltages share the same frequency and are separated in phase by one hundred twenty degrees. You may label them A, B and C, or L1, L2 and L3. Their instantaneous sum, when modeled as equal sinusoidal phase-to-neutral voltages, is zero. Their vector geometry creates useful line-to-line voltages and a balanced transfer of power across the cycle.

In a **wye** or star connection, one end of each phase winding joins at a common point. That point may provide a neutral conductor when the design brings it out. If each phase-to-neutral voltage is one hundred twenty volts RMS, the line-to-line voltage in the ideal balanced wye model is one hundred twenty times the square root of three, or approximately two hundred eight volts. That arrangement is often marked two-hundred-eight Y slash one-hundred-twenty volts.

In a different common system, each phase to neutral is nominally two hundred thirty volts. Two hundred thirty times the square root of three is about three hundred ninety-eight volts, giving the familiar four-hundred slash two-hundred-thirty-volt designation. That voltage family is prominent in many countries and is described in international nominal-voltage references. The nominal labels do not imply exact instantaneous values or identical local supply tolerances.

A **delta** connection instead connects windings end-to-end around a closed triangle. There may be three lines without a neutral, or more complex arrangements with a grounded point or derived neutral. A four-wire high-leg delta configuration can provide multiple distinct line-to-neutral voltages and has special identification requirements where used. It is a good reminder that the word 'three-phase' does not identify the available neutral voltage or grounding method by itself.

## Two hundred eight is not two hundred forty

Return to the two buildings. A nominal one-hundred-twenty slash two-hundred-forty source is a center-tapped single-phase arrangement; two hundred forty appears between the outer winding ends. A nominal one-hundred-twenty slash two-hundred-eight wye supply has three phase-to-neutral voltages separated by one hundred twenty degrees; two hundred eight appears between any pair of phases.

For a hypothetical resistive heater with constant resistance, operating power scales with voltage squared. If the heater is designed to dissipate two thousand four hundred watts at two hundred forty volts and its resistance remains constant, moving the same resistance to two hundred eight volts gives about eighteen hundred watts. This calculation explains a performance difference, not whether a particular appliance is approved for either supply. Motors, electronically controlled appliances and constant-power supplies respond differently; their nameplate and instructions decide acceptable input ranges.

It also explains why a piece of equipment rated for a one-hundred-twenty slash two-hundred-forty split-phase source may not work correctly from two legs of a one-hundred-twenty slash two-hundred-eight wye source. The line-to-neutral labels look similar while the line-to-line voltage and phase relation differ.

## Three-phase power is not three times a single phase by accident

Balanced three-phase circuits are used for efficient power distribution, large loads and rotating machines. With a balanced sinusoidal load, total apparent power magnitude equals the square root of three times the line-to-line RMS voltage times line current. Real power adds the load's power factor. Thus the real-power expression is the square root of three times line voltage times line current times power factor.

For example, a balanced three-phase load at four hundred volts line-to-line and ten amperes line current has apparent power of approximately six point nine three kilovolt-amperes. At a power factor of zero point eight, real power is about five point five four kilowatts. Those figures assume balanced sinusoidal operation and compatible RMS measurements; they are not the correct universal calculation for highly distorted or unbalanced loads.

Three-phase motors can use the rotating electromagnetic field created by phase-separated currents to develop torque. That is a central reason three-phase service is prevalent in industrial and larger commercial facilities. But three-phase equipment is not inherently present in every dwelling, and the choice of supply must match the installed loads and local network.

## Neutral behavior differs in three-phase systems

In an ideal balanced three-phase wye system with sinusoidal equal loads, the three phase currents cancel as phasors at the neutral point. Real loads are often unbalanced, so a neutral can carry current. Electronic loads may also inject harmonic components. Certain harmonics that are multiples of three can add rather than cancel in the neutral of a four-wire three-phase system. A perfectly balanced load by fundamental-frequency amperage therefore need not have zero neutral current when its waveforms are distorted.

This is another place where simplified electrical arithmetic can mislead. 'The currents balance' must always specify which components, frequencies and circuit geometry are being balanced. Likewise, neutral conductor capacity is not a casual consequence of subtracting three displayed current magnitudes.

## Frequency and regional vocabulary

Many North American systems use sixty hertz; many other systems use fifty. Nominal household voltages, outlet arrangements, phase availability, permissible voltage variation, and conductor identification all depend on region and supply. IEC 60038 is a reference framework for standardized voltage levels. National installation rules and utility specifications determine which levels and connections actually apply.

An important principle survives those differences. Begin with the conductors and the voltage between each relevant pair. Determine whether the source is a center-tapped winding, a wye, a delta, or some other arrangement. Identify the intended grounded reference, any neutral and any protective conductor. Only then interpret an appliance rating or a branch-circuit drawing.

The vocabulary of phase is not decoration. It is a way to describe the geometry of alternating voltage. Once you can picture that geometry, two hundred eight, two hundred forty, and four hundred volts stop being disconnected numbers in a catalog. They become predictable relationships between wires in a particular source.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Phasor relationships

- Split-phase winding: with center tap N, `V_L1N = 120 angle 0 deg` and `V_L2N = 120 angle 180 deg`; `V_L1L2 = V_L1N - V_L2N = 240 V` in the ideal equal-winding model.
- Balanced wye: `V_AN = Vp angle 0 deg`, `V_BN = Vp angle -120 deg`, `V_CN = Vp angle +120 deg`. `|V_AB| = sqrt(3) Vp`.
- Balanced three-phase sinusoidal: `|S_3phase| = sqrt(3) V_LL I_L`; `P_3phase = sqrt(3) V_LL I_L cos(phi)`.
- Neutral in ideal split-phase with resistive unity-power-factor 120 V legs: `|I_N| = |I_L1 - I_L2|`. This special formula does not replace general current-waveform summation.

### Two counterexamples

1. A resistive 240 V, 2400 W element has `R = 240^2/2400 = 24 ohms`. At 208 V with constant resistance, `P = 208^2/24 = 1802.67 W`. A regulated power supply may instead try to keep constant power within its operating range.
2. An ideal equal pair of 120 V loads on opposite halves carries no neutral current from that pair. If the common neutral connection is broken, unequal load impedances can produce strongly unequal voltages. Zero neutral current in one operating state was never a statement about conductor touch safety or source isolation.

### Exercises - paper and simulation

- Derive `|V_AB| = sqrt(3) Vp` from the cosine law for two equal phasors 120 degrees apart. **Answer:** the squared magnitude is `Vp^2 + Vp^2 - 2 Vp^2 cos(120 degrees) = 3 Vp^2`.
- A single-phase 2400 W resistive load is rated 240 V. Compute ideal currents at 240 and 208 V using a constant resistance. **Answer:** 10 A and approximately 8.67 A.
- Why does a 120/208 V label not imply 240 V between two phases? **Answer:** those phase-to-neutral phasors differ by 120 rather than 180 degrees.
- Give one reason a three-phase neutral can carry current even if the fundamental components are balanced. **Answer:** in a nonlinear load, triplen harmonic components can add.

### Attribution

The phasor and transformer calculations follow established circuit theory taught by OpenStax and university engineering texts. The Schneider Electric Electrical Installation Guide is credited for its comparison of distribution arrangements and examples of standardized nominal voltages. IEC 60038 is a collectively authored standard; a published secondary summary of its voltages is not evidence that every region has adopted a particular voltage or wiring method. The worked examples in this lecture are original pedagogical calculations.

## Claim-level source map

| Claim ID | Consequential claim | Source and exact support role | Limits / review |
|---|---|---|---|
| E023000-01 | North American 120/240 V commonly arises from center-tapped single-phase transformer secondary | [electrical-se-lv-networks](https://www.electrical-installation.org/enwiki/Low-voltage_distribution_networks) (North and Central American residential distribution paragraph; technical_guide); [electrical-openstax-transformers](https://openstax.org/books/university-physics-volume-2/pages/15-6-transformers) (Section 15.6 transformer winding physics; independent_physics) | Not every North American building uses that source arrangement. |
| E023000-02 | Split-phase outer-to-midpoint voltages are opposite phasors, yielding 240 V outer-to-outer | [electrical-openstax-ac-sources](https://openstax.org/books/university-physics-volume-2/pages/15-1-ac-sources) (Section 15.1 AC sinusoidal voltage theory; physics_foundations); [electrical-se-lv-networks](https://www.electrical-installation.org/enwiki/Low-voltage_distribution_networks) (120/240 V center-tap description; engineering_example) | Ideal equal secondary assumption; real voltage regulation differs. |
| E023000-03 | Higher voltage at equal resistive power reduces current in the simplified model | [electrical-openstax-ohm](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) (Section 9.4 Ohm law; physics); [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (Section 9.5 power and Joule losses; independent_derivation) | Does not determine safe conductor size. |
| E023000-04 | Balanced split-phase resistive leg loads cause neutral-current cancellation in ideal model | [electrical-openstax-kirchhoff](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules) (Section 10.3 junction rule; physics); [electrical-se-lv-networks](https://www.electrical-installation.org/enwiki/Low-voltage_distribution_networks) (center-tapped secondary architecture; system_context) | Opposite leg phasors and unity-power-factor assumption required. |
| E023000-05 | Open center-tap neutral with unequal loads can lead to unequal series voltages | [electrical-osha-open-neutral](https://www.osha.gov/laws-regs/standardinterpretations/2003-07-07-1) (OSHA July 7 2003 open-neutral interpretation; primary_hazard_support); [electrical-openstax-kirchhoff](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules) (Voltage division and loop rules; independent_physics) | Fault voltages depend on topology and extra load paths. |
| E023000-06 | Balanced three-phase sinusoids have phase separation of 120 degrees | [electrical-openstax-ac-sources](https://openstax.org/books/university-physics-volume-2/pages/15-1-ac-sources) (General sinusoidal AC theory; physics); [electrical-se-voltage-ranges](https://www.electrical-installation.org/enwiki/Definition_of_voltage_ranges) (Three-phase system categories; engineering_context) | Three-phase angle model is standard phasor derivation; source specifically not a comprehensive 3-phase text. |
| E023000-07 | Balanced wye line-to-line voltage magnitude is sqrt(3) times phase-neutral voltage | [electrical-openstax-ac-sources](https://openstax.org/books/university-physics-volume-2/pages/15-1-ac-sources) (Sinusoidal phasor algebra context; physics); [electrical-se-voltage-ranges](https://www.electrical-installation.org/enwiki/Definition_of_voltage_ranges) (230/400 and 120/208 examples; secondary_standards_context) | Exactly true for balanced sinusoids; nominal rounding affects labels. |
| E023000-08 | 230/400 V and 120/208 V are standardized supply families but not global rules | [electrical-se-voltage-ranges](https://www.electrical-installation.org/enwiki/Definition_of_voltage_ranges) (IEC 60038 summary table; voltage_guide); [electrical-se-lv-networks](https://www.electrical-installation.org/enwiki/Low-voltage_distribution_networks) (regional architecture comparison; same_publisher_context) | Both Schneider sources are same publisher and do not count as independent corroboration. |
| E023000-09 | Delta connections and wye connections do not necessarily offer same neutral voltages | [electrical-osha304](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) (1910.304(g)(1)(iv) includes wye/delta systems; primary_us_regulation); [electrical-se-voltage-ranges](https://www.electrical-installation.org/enwiki/Definition_of_voltage_ranges) (Three-phase three-/four-wire voltage notation; engineering_context) | Detailed high-leg identification and application needs local code and equipment specifics. |
| E023000-10 | At fixed resistance, a 2400 W 240 V heater draws about 1803 W at 208 V | [electrical-openstax-ohm](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) (Section 9.4 Ohm law; physics); [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (Section 9.5 P equals V squared over R; physics) | Purely resistive fixed-temperature model, not equipment approval. |
| E023000-11 | Balanced three-phase sinusoidal real power is sqrt(3) V_LL I_L times power factor | [electrical-openstax-acpower](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (Section 15.4 AC power and power factor; physics); [electrical-se-voltage-ranges](https://www.electrical-installation.org/enwiki/Definition_of_voltage_ranges) (Three-phase voltage conventions; system_context) | Formula assumes balance and sinusoidal definition of power factor. |
| E023000-12 | Four-wire three-phase neutral can carry unbalance and triplen harmonic current | [electrical-se-neutral-sizing](https://www.electrical-installation.org/enwiki/Sizing_the_neutral_conductor) (Influence of harmonics on neutral sizing; technical_guide); [electrical-fluke-harmonics](https://www.fluke.com/en-us/learn/blog/power-quality/installation-harmonics) (Harmonic current discussion; independent_vendor_context) | Device and waveform specifics matter; instrument measurement required for actual values. |
| E023000-13 | Regional nominal voltage and frequency differ across systems | [electrical-se-voltage-ranges](https://www.electrical-installation.org/enwiki/Definition_of_voltage_ranges) (IEC nominal voltage summary table; technical_context); [electrical-se-lv-networks](https://www.electrical-installation.org/enwiki/Low-voltage_distribution_networks) (regional network comparison; same_publisher_context) | Precise voltage tolerance and frequency require actual utility and national rules. |
| E023000-14 | Source phasor compatibility matters to 120/240 versus 120/208 equipment | [electrical-se-voltage-ranges](https://www.electrical-installation.org/enwiki/Definition_of_voltage_ranges) (Voltage relationships table; technical_context); [electrical-openstax-ac-sources](https://openstax.org/books/university-physics-volume-2/pages/15-1-ac-sources) (AC phasor foundation; independent_physics) | Individual appliance allowable voltage is product specific. |
