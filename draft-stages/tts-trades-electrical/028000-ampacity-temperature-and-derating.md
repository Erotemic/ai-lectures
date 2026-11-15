# 028000 - Ampacity: Heat, Installation Method, and Derating

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** simplified thermal models, installation-method drawings, manufacturer tables, and paper calculations.

<!-- BEGIN SPOKEN LECTURE -->

# Ampacity: Heat, Installation Method, and Derating

Picture two identical copper conductors carrying the same current. One hangs in open air where a breeze can remove heat. The other is enclosed with several loaded conductors inside thermal insulation. Would you expect them to reach the same temperature?

There is no reason they should. Their electrical resistance may be identical at the start, but their ability to reject heat is different. That observation is the foundation of ampacity: the current that a conductor is permitted to carry under stated conditions is not simply a number stamped onto the metal.

A conductor has an electrical resistance. A wiring installation has a thermal environment. Ampacity joins the two.

## A wire is a heater and a heat exchanger

Whenever current passes through resistance, the conductor generates heat. For a waveform characterized correctly by its root-mean-square current and a compatible resistance model, the familiar approximation is current squared times resistance.

Double the current and, if resistance is held fixed, the heating becomes four times as large. Current is therefore a powerful thermal variable. A small increase near an installation's limit can matter more than intuition suggests.

But a conductor is not thermally isolated. It sends energy to its insulation, the neighboring cables, the conduit, the building material, the ground, and the surrounding air. The steady operating temperature occurs where heat production and heat removal balance. If the environment becomes hotter, the temperature difference driving heat removal shrinks. If more loaded conductors are placed together, each may warm its neighbors and make the shared region less effective at shedding heat.

A simple classroom model expresses this as a thermal resistance from conductor to ambient. Temperature rise equals power dissipation times thermal resistance. The model is useful because it shows why the same electrical loss can produce different conductor temperatures. A bundled or insulated installation may have greater effective thermal resistance than a freely cooled one.

This is a model, not the general formula for a wiring code's ampacity tables. Real cables have multiple heat-flow paths and construction details; buried circuits also depend on soil properties. Standards and validated engineering methods account for those effects more carefully.

## What an ampacity table assumes

Open an ampacity table and you will find a current value associated with conductor material, area, insulation temperature class, and some installation conditions. That value is meaningful only with its table headings, footnotes, reference conditions and adjustment rules.

One table may assume conductors in air at a specified ambient temperature. Another describes a reference installation method, such as conductors in conduit in a thermally insulated wall, in conduit on a surface, in free air on a tray, or buried in the ground. The IEC installation guidance groups these into different reference methods because their heat transfer differs.

Consider an air-cooled cable in a hot rooftop conduit. A reference current rating determined at thirty degrees Celsius does not describe that hotter condition without an adjustment. Likewise, taking several separately rated circuits and tightly grouping them in a raceway changes their thermal situation. Some of the reference tables assume two loaded conductors; others assume three. Whether a neutral carries significant current under the actual waveform can also change the analysis.

This is what engineers mean by **correction factors** and **adjustment factors**. We begin with a rating under specified reference conditions and modify that rating to account for conditions that differ. In some standard methods the factors multiply; in other applications additional constraints and special rules intervene. It is a mistake to treat one simple product as a complete design algorithm.

## The physical meaning of derating

Suppose a conductor has a hypothetical reference ampacity of thirty amperes in a given reference installation. The environment has a temperature correction factor of zero point nine one, and the grouping of circuits has a factor of zero point eight. In the simplified model, thirty times zero point nine one times zero point eight is twenty-one point eight four amperes.

That arithmetic says only this: under those hypothetical factors, the adjusted value is lower than the reference value. It does not establish that any real thirty-ampere conductor is suitable for twenty-one point eight four amperes in an actual building. We have not established its insulation type, terminal limits, protection, conductor count, wiring method, product marking or adopted jurisdictional rules.

The lesson is the shape of the reasoning. A cable that looks large enough from its printed size can be underspecified after accounting for its thermal environment. Conversely, simply multiplying generic factors found online can be just as wrong if they belong to a different cable family or reference method.

There is another nonobvious feature. The applicable conductor's insulation rating may be ninety degrees Celsius, while an equipment termination accepts only a lower temperature condition. You cannot automatically carry the highest column value all the way through to the terminal. Table methods sometimes allow the higher insulation temperature to be used as the starting basis for adjustment while separately enforcing a lower terminal limit. That distinction is subtle and edition-sensitive; its exact implementation belongs to the adopted code and connected equipment instructions.

## Geometry and loaded conductors

Why does grouping matter? Imagine a single wire losing heat to the surrounding air. Now imagine four loaded circuits crowded into a small raceway. Their total heat production raises the temperature of the raceway and its contents. The innermost conductor may have no direct exposure to cool air. Each conductor changes the others' boundary conditions.

The correct number of **current-carrying conductors** is an electrical question, not simply a visual count of colored wires. A protective conductor is not normally intended to carry load current. A neutral may carry only imbalance in some balanced linear three-phase situations, but nonlinear loads can send harmonic currents through it, and special arrangements can make the neutral heavily loaded. You cannot declare every white or blue conductor thermally irrelevant just because of its color.

Physical arrangement matters as well. Cables lying separately on a ventilated ladder, a tight bundle in a wall cavity, and cables inside a buried duct can have very different thermal behavior. Even where the same cable is used, a change of routing may require the current-carrying assessment to be repeated.

## Buried cable is a thermal problem in soil

With buried conductors, heat has to move through a duct or cable jacket and into soil. Soil thermal resistivity matters. Dry, poorly conducting soil can hold heat near a cable; soil moisture and temperature can vary seasonally and around energized installations. A wet trench on installation day is not a guarantee of that soil's behavior years later.

IEC-oriented guidance accordingly distinguishes air temperature from ground temperature, installation depth, grouping and soil thermal properties. More advanced methods, including the IEC 60287 cable-current-rating series, model thermal paths in greater detail. That is particularly important for large or critical cable systems.

It is tempting to say that underground means cool. Sometimes it does. But a buried cable is not automatically better cooled than one in free air. The answer depends on the actual thermal path and operating conditions.

## The current varies with time

So far we have described a steady-state heating model. Real loads are intermittent. Motors draw starting currents, thermostats cycle, and electronically controlled equipment changes operating states. A conductor and its surroundings have thermal mass, so temperature does not jump instantly to the steady-state value at each current fluctuation.

A simple thermal-capacitance model captures that lag. The rate of temperature change depends on the difference between heat being generated and heat escaping. This explains why a brief pulse and the same current applied continuously can have very different thermal outcomes.

But an installation's allowable loading cannot be invented from that observation alone. Protection devices, cable insulation, terminals, equipment standards, and code-defined continuous-load treatments create conditions that must all be respected. A current rating for continuous operation cannot be casually reinterpreted as a permission to overload a circuit for an arbitrary fraction of each hour.

The deeper principle is that **time, temperature and current belong together**. A realistic load study records both peak current and the duration and repetition of those peaks.

## Ampacity is not the whole cable design

Imagine a thirty-meter run and a very long two-hundred-meter run built from the same conductor, under similar thermal conditions, carrying the same current. Their per-meter heat generation might be similar, so the reference ampacity model might permit the same continuous current. But the long circuit has much more total resistance. Its voltage drop can be far greater.

That means there are at least two independent sizing checks: can the conductor carry the current within its thermal and product limits, and can it deliver suitable voltage at the load under expected operating conditions? Other checks include fault protection and withstand, mechanical strength, terminal compatibility, and available installation space.

Those requirements need not point to the same wire size. A conductor sized by ampacity may be too small for voltage regulation over a long route; a conductor enlarged to reduce voltage drop may create an equipment-termination compatibility question.

An engineer therefore does not ask merely, 'What is the ampacity of this gauge?' The useful question is, 'What is the allowable current of this **wiring system** under its actual thermal environment and applicable constraints?'

When you understand that distinction, cable tables become much less mysterious. They are compressed models of electrical heating, heat flow, materials and installation geometry. Reading them well requires restoring the assumptions that made each number meaningful.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Simplified lumped thermal model

\[
P_{\text{heat}}=I_{\mathrm{rms}}^2R(T), \qquad
\Delta T=P_{\text{heat}}\,\Theta_{\text{thermal}},
\]

where `Θ_thermal` is an idealized thermal resistance in K/W. For transients:

\[
C_{\text{thermal}}\frac{dT}{dt}=P_{\text{heat}}(t)-\frac{T-T_a}{\Theta_{\text{thermal}}}.
\]

This model is explanatory. It does not replace IEC 60287, IEC 60364-5-52, NEC ampacity rules, manufacturer specifications, or circuit-protection coordination. Temperature feedback enters through `R(T)`.

### Derating example with deliberately hypothetical coefficients

A **fictional** base table gives `I_ref = 30 A`. Invented correction factors are `k_ambient = 0.91`, `k_grouping = 0.80`. Then:

`I_adjusted = 30 × 0.91 × 0.80 = 21.84 A`.

The factors demonstrate multiplication but are **not a selected code table row** and cannot authorize a 21.84 A field loading. Schneider Electric's published IEC-oriented guide shows genuine variation by installation method, ambient temperature, grouping, and thermal-resistivity assumptions. IEC's official public catalogue documents standard scope, not the detailed calculation tables themselves.

### Thermal and electrical constraints are separate

| Design question | Relevant inputs | Common failure of reasoning |
|---|---|---|
| Reference ampacity | Conductor material, area, insulation, installation method | Taking the number without the table heading |
| Environmental correction | Ambient, cable grouping, soil, thermal insulation | Assuming every route is open air |
| Terminal temperature | Equipment and connector ratings | Treating a 90°C insulation label as a 90°C terminal permission |
| Load current | Waveform, duty, harmonics, simultaneous operation | Treating all neutral currents as zero |
| Voltage regulation | Circuit length, hot resistance, reactance, load behavior | Confusing ampacity with acceptable voltage drop |
| Fault behavior | Fault current, withstand time, device operation | Inferring protection solely from a normal-current table |

### Exercises with answers

1. **Power scale:** Double current with fixed resistance. **Answer:** four times heating.
2. **Factor sensitivity:** Apply a hypothetical `0.85` factor to `40 A`. **Answer:** `34 A` in that simplified model.
3. **Combined factor:** Why do `0.80 × 0.90` and `0.80 + 0.90` answer different questions? **Answer:** these factors multiply dimensionless reductions; addition is not a valid derating operation.
4. **Route comparison:** Which is likely to have higher thermal resistance: one freely ventilated cable or the same cable in a tightly insulated wall cavity? **Answer:** generally the insulated cavity, but actual ratings depend on the specified construction.
5. **Why isn't longer always hotter per meter?** **Answer:** if conductor size, per-meter resistance, current, and local heat-flow conditions are unchanged, local heating may be similar; total voltage drop grows with total length.
6. **Why does a neutral count require electrical analysis?** **Answer:** actual current and harmonic content, not insulation color alone, determine whether it produces material heating in the grouping model.

### Attribution and jurisdiction note

The equations follow standard electrical and heat-transfer reasoning; OpenStax gives the electrical power and temperature dependence, and Schneider Electric's public *Electrical Installation Guide* provides IEC-style reference-method and correction-factor examples. The applicable IEC standard is produced by IEC TC64. NFPA NEC requirements are the work of NFPA code-making committees and must be evaluated for their adopted edition; OSHA 1910.305 supplies workplace wiring context, not a general homeowner ampacity table. No full IEC normative clauses or local NEC edition were examined for installation decisions.

## Claim-level source map

| Claim ID | Consequential claim | Source and exact support role | Limits / review |
|---|---|---|---|
| E028000-01 | I-squared-R heating increases quadratically with current at fixed resistance | [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (§9.5 electrical power; physics) | Current RMS and resistance model must be appropriate to waveform. |
| E028000-02 | Ampacity combines internal heat generation and external heat removal | [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (Joule heating basis; physics); [electrical-iec60287-2023](https://webstore.iec.ch/en/publication/68118) (steady-state current rating and losses scope; engineering_standard_context) | Lumped thermal model is original synthesis, not a standard calculation procedure. |
| E028000-03 | Reference ampacity depends on insulation type and installation method | [electrical-se-cable-sizing](https://www.electrical-installation.org/enwiki/General_method_for_cable_sizing) (reference methods A-G and insulation temperature chart; public_engineering_guide); [electrical-iec60364-552-2024](https://webstore.iec.ch/en/publication/103734) (standard selection/erection scope; standard_scope) | Published guide may rely on specific earlier tables; adopted full clauses not checked. |
| E028000-04 | Ambient temperature can require correction of reference current ratings | [electrical-se-cable-sizing](https://www.electrical-installation.org/enwiki/General_method_for_cable_sizing) (air temperature corrections reference 30°C; public_engineering_guide) | Not universal across every cable standard or application. |
| E028000-05 | Grouping loaded circuits can reduce permissible continuous current | [electrical-se-cable-sizing](https://www.electrical-installation.org/enwiki/General_method_for_cable_sizing) (group reduction factors and installation differences; engineering_guide); [electrical-osha303](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.303) (heating effects considered in suitability; independent_workplace_context) | No actual group factor selected for field use. |
| E028000-06 | Loaded neutral status may depend on harmonics and waveform, not insulation color | [electrical-se-neutral-sizing](https://www.electrical-installation.org/enwiki/Sizing_the_neutral_conductor) (neutral and harmonic sizing discussion; engineering_guide); [electrical-se-cable-sizing](https://www.electrical-installation.org/enwiki/General_method_for_cable_sizing) (grouping of current-carrying conductors; same_publisher_context) | Product and rule-specific conductor-count treatment not independently checked. |
| E028000-07 | Buried cable heat rejection depends on soil temperature and thermal resistivity | [electrical-se-cable-sizing](https://www.electrical-installation.org/enwiki/General_method_for_cable_sizing) (ground conditions and soil resistivity correction; engineering_guide); [electrical-iec60287-2023](https://webstore.iec.ch/en/publication/68118) (buried and ducted steady-state cables in scope; independent_standard_scope) | Actual soil properties, drying and transient thermal behavior need site-specific study. |
| E028000-08 | IEC 60287-1-1:2023 uses steady-state cable current-rating equations at 100% load factor | [electrical-iec60287-2023](https://webstore.iec.ch/en/publication/68118) (official catalogue abstract; publisher_scope_only) | Cannot reproduce normative methods from publisher summary. |
| E028000-09 | Terminal restrictions can limit use of high-temperature insulation ratings | [electrical-osha303](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.303) (equipment heating, ratings, instructions; workplace_rule); [electrical-se-cable-sizing](https://www.electrical-installation.org/enwiki/General_method_for_cable_sizing) (insulation conductor temperature classes; engineering_context) | Specific code column and allowed correction basis depends on edition and device. |
| E028000-10 | Thermal mass delays temperature response to a transient current | [electrical-iec60287-2023](https://webstore.iec.ch/en/publication/68118) (steady-state versus other regimes explicit; standard_scope); [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (electrical heat generation; physics_context) | Thermal capacitance ODE is original teaching model, not verified cable transient standard. |
| E028000-11 | Conductor length affects total resistance and voltage drop even if local heat rate is similar | [electrical-openstax-resistivity](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance) (R proportional to length; physics); [electrical-se-voltage-drop](https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions) (voltage drop formula and length; independent_engineering_guide) | Local cooling uniformity assumed; cables in varying conditions may have different ratings. |
| E028000-12 | Ampacity check is distinct from fault withstand and voltage delivery | [electrical-se-cable-sizing](https://www.electrical-installation.org/enwiki/General_method_for_cable_sizing) (thermal sizing criteria; engineering_guide); [electrical-se-voltage-drop](https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions) (separate voltage-drop analysis; same_publisher_context); [electrical-osha303](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.303) (interrupting rating and heating requirements; independent_us_workplace_rule) | Specific fault withstand and protective coordination not calculated. |
