# 029000 - Voltage Drop, Distance, and the Cost of Current

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** one-line routes, hot-resistance calculations, phasor sketches, efficiency comparisons and load scenarios.

<!-- BEGIN SPOKEN LECTURE -->

# Voltage Drop, Distance, and the Cost of Current

A building can have a circuit that never overheats and still performs poorly. A long feeder may deliver enough current without exceeding its thermal rating, yet the voltage at its far end may sag whenever a large load starts. Lights may flicker, a motor may struggle to accelerate, or an electronic converter may change the current it draws.

Nothing about this contradicts the ampacity calculation. Ampacity asks whether the wiring can carry current under its thermal conditions. Voltage drop asks how much of the source's voltage is consumed by impedance along the path before the load receives its share.

Both questions concern the same conductor, but they lead to different sizing constraints.

## Trace the complete current loop

Imagine a direct-current source supplying a resistor at the end of a long pair of wires. Current travels out along one wire and returns along the other. Each wire has resistance. Their resistances add around the loop.

Suppose the distance to the load is thirty meters. For a two-conductor circuit whose supply and return use equal paths, the current traverses sixty meters of conductor in total. In a simplified resistance calculation, using thirty meters only once would miss half of the wiring's resistance.

That is why the first step is to draw the current path. In a North American center-tapped system, a load connected line to neutral has a particular supply-and-return geometry; a load connected between the two outer conductors has another. In a balanced three-phase circuit, current flows through multiple phase conductors and is described with phasors rather than a single two-wire loop. A neutral's presence on the drawing is not proof that it carries the same current as a phase conductor in every operating condition.

The calculation must follow the actual circuit topology. There is no universal 'multiply length by two' rule that applies unchanged to every three-phase or multiwire circuit.

## Resistance turns into voltage loss

For a simple DC or predominantly resistive circuit, the voltage lost along a wire is current times wire resistance. The conductor's resistance is its resistivity times length divided by metallic cross-sectional area.

Put these together and several trends become immediate. Double the run length, and resistance and voltage drop double if everything else remains the same. Double the metallic cross section, and both are approximately halved. Double the current, and the voltage drop doubles at fixed resistance—but the power lost as heat becomes four times as large.

This last relationship is important when looking at efficiency. Voltage drop tells you how much voltage is missing at the load. Current squared times resistance tells you the power being dissipated along the cable. That lost energy has to go somewhere: it becomes heat distributed along the wiring and associated connections.

A circuit can therefore waste substantial power even when it remains within its permitted thermal loading. That is especially relevant to systems operating for many hours, where small continuous losses become meaningful energy costs.

## Work through a hypothetical long run

Consider a pure resistive model at twenty degrees Celsius. The conductor metal has a resistivity of approximately one point six eight times ten to the minus eight ohm meters, a value commonly used for copper in introductory physics. A two-wire circuit has a thirty-meter one-way run. Each conductor has a metallic cross section of two point five square millimeters. Let the current be twelve amperes.

The total loop length is sixty meters. The approximate loop resistance is zero point four zero three ohms. Multiply by twelve amperes and the voltage drop is about four point eight four volts. Relative to a nominal one-hundred-twenty-volt supply, that is about four percent. The total heat dissipated along both conductors is about fifty-eight watts.

Now keep the current and length fixed, but increase the metallic area to four square millimeters. The loop resistance falls in proportion to area, and the idealized drop becomes about three volts. This is an electrical comparison, not a recommendation to select either size for a building. The hypothetical example has not established ampacity, cable type, permitted conductor sizes, connection compatibility, or local voltage-drop criteria.

Notice the larger lesson: the conductor area that carries a current safely can be smaller than the conductor area that delivers acceptable voltage to a distant load. In a long system, the voltage criterion may become the stronger constraint.

## A warm conductor drops more voltage

The earlier calculation used reference-temperature copper resistance. But current heats a conductor, and copper's resistance increases as it warms. If the metal temperature rises from twenty degrees to seventy degrees Celsius, a simple linear approximation using a temperature coefficient near zero point zero zero three nine per degree gives an increase of about nineteen and a half percent in resistance.

At the same twelve-ampere current, the hypothetical four point eight four volt loss becomes about five point seven eight volts. The precise number in a real cable depends on the metal alloy, actual temperature distribution, manufacturing tolerance, and termination effects. But the direction is reliable: a cold-conductor calculation tends to understate resistance-related drop at hotter operating temperatures.

The calculation and the thermal design are coupled. Current creates heat. Heat changes resistance. Resistance changes the voltage drop and loss. This is one reason careful conductor sizing uses temperature assumptions that match the installation, not merely convenient room-temperature values.

## Alternating current adds phase

At mains frequency, copper conductors still have resistance, but the complete electrical behavior of a cable also includes reactance. Alternating current creates time-varying magnetic fields. A conductor arrangement has inductance, and that inductance creates a voltage component that is not simply in phase with the current.

The general object is the circuit's complex impedance. For a sufficiently simple linear sinusoidal model, impedance has a real part, resistance, and an imaginary part, reactance. The load has a power factor that describes the relationship of its fundamental current to voltage, although harmonics require additional care.

For many short, relatively small building circuits at ordinary mains frequency, the resistive component is dominant enough that a first approximation based on resistance is useful. As circuits become longer, conductor sizes larger, or current and phase characteristics different, reactance may matter. Schneider Electric's installation guide provides separate single-phase and balanced three-phase formulas that include resistance, reactance, current, circuit length and phase angle.

A balanced three-phase system also has a geometric factor: its voltage relationships are not simply those of a two-conductor loop. Engineers often see a square-root-of-three factor in three-phase line-to-line voltage-drop approximations. That factor arises from phasor geometry under stated balance and waveform assumptions. It must not be pasted into a DC calculation or an unbalanced nonlinear waveform without reconsidering the model.

## The source itself can sag

Imagine that measurements at a distribution panel already show reduced voltage when a large motor starts. The motor circuit adds some additional voltage drop along its cable. Improving only that cable cannot restore the voltage lost upstream in the service transformer, feeder, utility system, generator or inverter.

To analyze voltage at the load, separate source voltage from downstream line impedance. At a given instant, the receiving equipment sees the voltage remaining after the current-dependent drops along the route. The source may also change its terminal voltage with load.

A motor can complicate the story because its starting current may be much higher than its steady running current. Starting current increases the drop, which reduces the voltage available to create starting torque. The outcome depends on the motor, control method, source stiffness and mechanical load. An inverter-driven motor or electronically regulated appliance may behave differently from an across-the-line induction motor.

It is also unsafe analytically to assume every load keeps current fixed as voltage changes. A simple resistance draws less current at lower voltage. A constant-power converter, over its regulated operating range, tends to draw more current when input voltage falls. Real equipment has limits and protection behavior. Different load models can therefore produce different predictions from the same wiring resistance.

## Voltage-drop criteria are not one eternal percentage

You may have heard that a branch circuit should stay below three percent voltage drop, or that feeder plus branch should stay below five percent. Those figures appear in editions and commentaries associated with North American code guidance, often as efficiency-oriented informational notes rather than a universal enforceable rule for every circuit. Other applications and jurisdictions use different criteria, and some equipment requires a tighter voltage tolerance for reliable operation.

The IEC 60364-5-52 family addresses voltage drop in wiring-system selection. Its consolidated 2024 publisher description notes changes to Clause 525 and references the applicable annex. That scope statement is not enough to determine an installed system's permitted percentage without reviewing the relevant complete adopted text.

The technically useful habit is to state a criterion together with its source and scope: the equipment's permitted voltage range, the power system's operating profile, the chosen engineering guide, and the actual adopted local requirement. A percentage without its context is less valuable than the load behavior it was intended to protect.

## Size for the system, not for one formula

An engineering comparison should check at least four different dimensions. First, the conductor's thermal current-carrying capability under its installation conditions. Second, the voltage it delivers under normal, starting, and other relevant load states. Third, its ability to withstand and permit proper clearing of faults in the actual source and protective-device arrangement. Fourth, mechanical and connection compatibility, including size, flexibility, raceway or cable construction, and terminal limits.

Energy efficiency adds an economic dimension. Enlarging a conductor can reduce resistive losses, but increases material cost, space and possibly installation complexity. The best tradeoff depends on duty cycle, energy price, material costs and expected service life. The math is not reducible to choosing the largest conductor that fits.

The conceptual shift is to stop thinking of a wire as a perfect line on a diagram. It has resistance, impedance, temperature, geometry and cost. When current flows, it changes the voltage available to everything downstream. Understanding that relationship turns voltage drop from a mysterious complaint into a calculable property of the whole current path.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Resistive single-phase/DC loop model

For a two-wire supply/return route with identical conductor material and area and one-way length `L`:

\[
R_{\text{loop}}(T)=2\rho(T)\frac{L}{A},\qquad
\Delta V\approx I R_{\text{loop}},\qquad
P_{\text{loss}}=I^2R_{\text{loop}}.
\]

The factor two accounts for outgoing and returning conductors in this specific topology. It is not a universal formula for all multiwire or three-phase systems.

### Calculated example, equal current, 20°C reference

Take `ρ_Cu=1.68×10^-8 Ω·m`, `L_one_way=30 m`, `A=2.5 mm² =2.5×10^-6 m²`, `I=12 A`, `V_nominal=120 V`.

- `R_loop = 1.68e-8 × 60 / 2.5e-6 = 0.4032 Ω`.
- `ΔV = 12 × 0.4032 = 4.8384 V`, or `4.032%` of 120 V.
- `P_loss = 12² × 0.4032 = 58.0608 W`.
- At `A=4.0 mm²` instead, `R_loop = 0.252 Ω`, `ΔV=3.024 V`, `P_loss=36.288 W`.
- With `α=0.0039/°C` and hypothetical metal temperature `70°C`, the 2.5 mm² reference resistance becomes `0.4032 × 1.195 = 0.481824 Ω`, `ΔV=5.781888 V`, `4.81824%`.

These are reference-temperature *material* calculations, not standardized wire sizes, allowable currents, or an approved installed cable design. The chosen 12 A is held fixed to expose changes in geometry and temperature.

### Balanced sinusoidal AC approximation

For a balanced three-phase route, using `R` and `X` **per conductor per unit length** at the relevant operating temperature:

\[
\Delta U_{LL}\approx \sqrt{3}\,I\,L\,(R\cos\varphi+X\sin\varphi).
\]

A single-phase two-wire approximation has the analogous factor 2 for its two conductors. Source: Schneider Electric *Electrical Installation Guide*, *Calculation of voltage drop in steady load conditions*. These are approximate phasor formulas for stated conditions and do not fully describe unbalanced, nonlinear or dynamic equipment.

### Competing load models

| Model | Current change when received voltage falls | Caveat |
|---|---|---|
| Constant resistance | Current falls approximately with voltage | Resistance may vary with temperature |
| Constant current | Current remains approximately fixed | Only over device operating range |
| Constant input power | Current rises approximately as inverse voltage | Control limits, power factor and harmonics affect the result |
| Direct-on-line motor during start | Potentially large, dynamic current | Source, motor, torque-speed and load models required |

### Exercise: source versus line loss

A hypothetical source is `118 V` at the feeder origin under load; the cable drops `3 V`. The receiving voltage is approximately `115 V`. Replacing the cable with one that drops `1 V` raises receiving voltage to `117 V` **only if source voltage and load current remain the assumed values**. It cannot automatically recover a missing two volts caused upstream, and a real load could change its current after the replacement.

### Additional questions

1. At fixed current, how do resistive drop and cable loss scale with doubled length? **Answer:** both double.
2. At fixed length and area, how does doubled current affect voltage drop and loss? **Answer:** drop doubles, loss quadruples in the fixed-resistance approximation.
3. A conductor passes its thermal check but fails the voltage-delivery objective. Is the thermal check contradicted? **No:** they are separate constraints.
4. Why calculate resistance at operating temperature? **Because:** metal resistivity changes with temperature, affecting drop and loss.
5. Why is a three-percent target not a universal rule? **Because:** its authority, edition, application and enforceability differ, while equipment voltage requirements vary.
6. Does adding an extra neutral guarantee lower drop for a phase-to-phase load? **No:** first establish the actual current path and circuit topology.

### Standards and attribution boundaries

OpenStax §9.3 is used for material resistivity and the temperature model. Schneider Electric publishes the engineering formulas for AC voltage drop and distinguishes conductor sizes, resistance, reactance and phase conditions. IEC 60364-5-52 is the IEC TC64 wiring-system standard; the publicly available IEC catalogue states scope and revision notes but not fully adopted clause content. Publicly accessible older U.S. guidance from Schneider reproduces the familiar three/five-percent informational-note language for a particular code edition; it is **not** treated as a universal NEC requirement or proof of the 2026 adopted text. Product tolerances must come from relevant equipment specifications.

## Claim-level source map

| Claim ID | Consequential claim | Source and exact support role | Limits / review |
|---|---|---|---|
| E029000-01 | Two-wire supply-return geometry uses total loop length for DC/resistive drop | [electrical-openstax-resistivity](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance) (R proportional to conductor length and inverse area; physics); [electrical-openstax-ohm](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) (Ohm law; same_textbook_equation) | Only valid for explicitly stated symmetric two-wire loop geometry. |
| E029000-02 | Resistive voltage drop grows with current and length at fixed area and resistivity | [electrical-openstax-ohm](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) (Ohm law; physics); [electrical-openstax-resistivity](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance) (resistivity expression; same_publisher_physics) | Not a complete dynamic source/load network model. |
| E029000-03 | Dissipation increases with square of current while idealized drop grows linearly | [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (P=I²R; physics); [electrical-openstax-ohm](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) (V=IR; same_textbook_physics) | Resistance and source/load states held fixed. |
| E029000-04 | Reference resistivity and temperature coefficient determine hypothetical hot-loop resistance | [electrical-openstax-resistivity](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance) (20°C table and linear temperature relation; physics) | Actual cable composition, hot spots and temperature vary. |
| E029000-05 | Thermal ampacity and voltage-drop criteria are different sizing constraints | [electrical-se-cable-sizing](https://www.electrical-installation.org/enwiki/General_method_for_cable_sizing) (reference current ratings; engineering_guide); [electrical-se-voltage-drop](https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions) (steady voltage-drop analysis; same_publisher_other_guide) | Independently check installed code, equipment voltage tolerance, fault and terminal constraints. |
| E029000-06 | In AC wiring the resistive and reactive components of impedance affect voltage drop | [electrical-se-voltage-drop](https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions) (R cos φ + X sin φ terms; engineering_guide); [electrical-openstax-ac-circuits](https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits) (phasor circuit impedance principles; independent_physics) | Sinusoidal steady-state conditions; nonlinear loads and transients may violate assumptions. |
| E029000-07 | Balanced three-phase voltage drop uses phasor geometry and a square-root-of-three factor | [electrical-se-voltage-drop](https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions) (balanced three-phase formula in public guide; engineering_guide); [electrical-openstax-ac-sources](https://openstax.org/books/university-physics-volume-2/pages/15-1-ac-sources) (AC phase relationships; independent_physics) | Not for arbitrary unbalanced harmonics, or single-phase DC. |
| E029000-08 | Upstream source sag must be distinguished from losses in downstream cable | [electrical-se-voltage-drop](https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions) (guide example includes upstream distribution-board drop; engineering_guide); [electrical-openstax-kirchhoff](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules) (loop voltage conservation; independent_physics) | Requires load-current and source-impedance model for quantitative diagnosis. |
| E029000-09 | Load voltage dependence differs between fixed resistance and regulated constant power | [electrical-openstax-ohm](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) (resistance current-versus-voltage relationship; physics); [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (power/current relation; same_textbook_physics) | Constant-power behavior only over converter regulation range; actual equipment specs needed. |
| E029000-10 | Common U.S. 3% branch and 5% feeder-plus-branch guidelines are not universally mandatory | [electrical-se-nec21019-historic](https://www.productinfo.schneider-electric.com/na-std-ref/5c0fee4b347bdf0001de4d55/Conductor%20Ampacity%20Tables/English/Data%20Bulletin%20-%20Conductor%20Ampacity%20Tables%20%28bookmap%29_0000264293.ditamap/%24/NEC210.19ConductorsMinimumAmpacityA-F20BBAC1) (NEC 210.19 Informational Note excerpt, historical 3% and 5% guidance; secondary_historical_code_excerpt); [electrical-se-voltage-drop](https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions) (engineering performance criteria context; engineering_guide); [electrical-iec60364-552-2024](https://webstore.iec.ch/en/publication/103734) (IEC Clause 525 catalogue changes and annex reference; separate_standard_scope) | This secondary excerpt documents an older NEC informational note, not the 2026 NEC text or a binding universally adopted limit; local code and equipment requirements differ. |
| E029000-11 | IEC 60364-5-52 scope covers wiring-system voltage drop and a 2024 clause revision | [electrical-iec60364-552-2024](https://webstore.iec.ch/en/publication/103734) (official catalogue Clause 525 change note; publisher_scope_only) | Publisher summary not full adopted annex; local requirements unknown. |
| E029000-12 | Conductor upsizing trades resistance and loss against material, route and terminal constraints | [electrical-openstax-resistivity](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance) (R decreases with area; physics); [electrical-ul486-2025](https://www.shopulstandards.com/ProductDetail.aspx?ShowFreeviewModal=1&UniqueKey=48038) (connector material and size scope; separate_product_standard_context) | No life-cycle economic or field-sizing conclusion without duty and product info. |
