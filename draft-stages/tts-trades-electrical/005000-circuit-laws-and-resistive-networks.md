# 005000 — Following the Current: Resistive Circuits and Kirchhoff's Laws

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Background:** voltage, current, power, and a closed circuit. **Practice boundary:** paper or simulated schematics; any optional physical demonstration must use a purpose-designed, isolated, current-limited educational kit under competent supervision. No work on building wiring or energized distribution equipment.

<!-- BEGIN SPOKEN LECTURE -->

# Following the Current: Resistive Circuits and Kirchhoff's Laws

Imagine a source, a lamp, and a switch. When the switch closes, the lamp lights. That simple picture is excellent for introducing a complete circuit. But it becomes less informative when there are three lamps, two branches, a source with internal resistance, and one connection whose resistance is rising as it ages. Which part sees which voltage? Where does current divide? Why could the load continue operating while one small region becomes hot?

To answer those questions, we need a way to account for every path through a network without relying on the appearance of the drawing. Two statements, traditionally named for Gustav Kirchhoff, give us much of that power. They are usually taught as algebraic rules. I want you to hear them first as conservation laws: electric charge does not simply vanish at a junction, and a completed accounting of potential differences around a loop must be consistent.

The rest is learning what a circuit model assumes, and when its assumptions stop being adequate.

## A model is not the wire itself

The drawings used in introductory circuit analysis are deliberately abstract. A wire becomes a line. A resistor becomes a small symbol, sometimes a zigzag. A source becomes a pair of terminals with a specified voltage. All points connected by ideal wire are treated as having the same potential. A component is treated as if its behavior can be described by quantities at its terminals, rather than by the entire field of electric and magnetic forces distributed through space.

This is the lumped-circuit model. It is immensely useful when the dimensions and time scales make those simplifications appropriate. It is not a declaration that real conductors have zero resistance, that switching happens without propagation time, or that rapidly changing magnetic fields can never induce voltage around a path. Those exceptions will matter later. For now, we will make the assumptions explicit so that the algebra has a definite meaning.

We begin with resistance. In its simplest model, a resistor has a voltage across it proportional to the current through it. Double that voltage, and the current doubles, if the resistance stays constant. This is Ohm's law for an ohmic element. It is not a universal description of every appliance. Filaments heat up, motors move, electronic power supplies switch, and many components change behavior with temperature or voltage. Nevertheless, networks of approximately ohmic elements are a valuable first language.

## One path: series

Suppose an ideal five-volt source is represented as feeding two resistors in series: one thousand ohms and two thousand ohms. Series means the current has no alternative branch between those components. The same current passes through both.

Their equivalent resistance is three thousand ohms. Divide five volts by three thousand ohms and you get one six-hundredth of an ampere, approximately one point six seven milliamps. The voltage across the first resistor is about one point six seven volts. Across the second, about three point three three volts. Add those two drops, and the five volts supplied are accounted for.

Notice what did not happen. We did not split the source voltage equally just because there were two resistors. They divide the voltage according to resistance, under these assumptions. Nor did the current disappear when it passed through the first resistor. The resistor transferred electrical energy to heat. The charge continued through the closed path.

Now check the power. Multiply the voltage across either resistor by the current through it. Each resistor receives a positive rate of energy transfer; together, the powers add to the rate supplied by the ideal source. That is a second accounting check. In this numerical example the power is only milliwatts. A different voltage or resistance can produce very different heat. Values on a chalkboard never certify that a physical component, connector, wire, or enclosure is adequately rated.

## Two paths: parallel

Now place the same two resistors across the same ideal five-volt source, with a separate branch for each. They are in parallel because both terminals of each resistor connect to the same two ideal nodes. Each branch sees five volts. The one-thousand-ohm branch draws five milliamps; the two-thousand-ohm branch draws two point five milliamps. The source provides seven point five milliamps in total.

So the parallel network draws more source current than either branch alone. Its equivalent resistance is less than either branch resistance. For these values it is about six hundred and sixty-seven ohms. You can derive that result by adding the branch conductances, the reciprocals of resistance.

The distinction between series and parallel is about topology: which nodes are connected. It is not about whether symbols appear next to one another or on separate lines of a page. A diagram can be redrawn without changing the circuit. A single junction that was hidden in a messy drawing can be made obvious in a clean one.

There is a useful but limited household connection. Many separate loads receive the same nominal supply voltage because they are connected in parallel through distribution circuits. That does not mean you can combine arbitrary branch currents and decide whether a building circuit is safe. Actual supply impedance, conductor ratings, overcurrent protection, simultaneous loading, temperature, product instructions, and locally adopted rules all matter. Our five-volt example is a model for reasoning, not an installation design.

## Kirchhoff's junction rule: conservation of charge

Choose a junction where three branches meet. Imagine two amperes arriving from one branch and current leaving by two others. If the currents are steady and no charge is building up at the junction, the leaving currents must sum to two amperes. One point two amperes in one branch leaves zero point eight amperes for the other.

That is Kirchhoff's current law, sometimes called the junction rule. The signed sum of currents at a node is zero. You may choose all currents entering as positive and all leaving as negative, or use the reverse convention. Be consistent. If you guess a direction and the solved current is negative, the mathematics tells you the actual current is opposite the arrow you selected. It does not tell you the calculation failed.

Why the condition about stored charge? In a time-changing circuit, charge can accumulate temporarily on conductors and capacitor plates. In circuit models, we keep the conservation law but include the appropriate capacitance and displacement-current effects rather than pretending the charge accumulation never happens. The simple statement is a steady-state description of a deeper conservation principle.

There is a larger moral. A conductor called a neutral is not a mathematical sink where current safely evaporates. A return path carries current, and the actual paths depend on the whole system and fault conditions. Circuit theory does not permit anyone to infer that a neutral wire, or an apparently disconnected conductor, is safe to touch.

## Kirchhoff's loop rule: consistent potential differences

Now travel around the five-volt series circuit and add the potential changes you encounter. Cross the ideal source from its lower-potential to its higher-potential terminal: add five volts. Cross the first resistor in the direction of the defined current: subtract roughly one point six seven volts. Cross the second: subtract roughly three point three three. The sum is zero.

This is Kirchhoff's voltage law in the usual lumped, quasistatic circuit model. It is often motivated by energy conservation. More precisely, it is a consistent accounting of scalar potential differences across the modeled elements. When magnetic flux through a physical loop changes, Faraday's law introduces induced electromotive force; a careless claim that every line integral of the electric field around every physical loop always vanishes would be wrong. Circuit models can include those induced voltages as elements, but we should not mistake a convenient schematic law for an unconditional statement about the fields.

A useful skill is to write the loop equation before putting numbers into it. Source rise, then component drops; or the same loop traced backward, with every sign reversed. Either description should lead to the same current. If the signs depend on how you drew the picture instead of how you defined the path, check the model again.

Together, the junction rule and the loop rule make it possible to solve networks that cannot be collapsed into one simple series or parallel equivalent. In engineering classrooms this develops into node-voltage analysis and mesh-current analysis: systematic ways of turning a circuit diagram into simultaneous equations. Their underlying ideas come from charge conservation and the potential relationships of the elements.

## An ideal short circuit is not a low-power load

It is tempting to think that because a resistor makes current smaller, removing resistance must make a device more efficient. But if a voltage source has an unintended path with very low impedance, current can rise dramatically. The ideal formula predicts infinite current for an ideal voltage source and zero resistance; real sources and wiring limit the current, but they can still deliver enough energy to damage equipment or start a fire.

An ideal short circuit is a limiting model, not a condition to experiment with. Never deliberately short a battery, power supply, or building circuit. Even a modest battery can deliver dangerous localized heat if its available current and protection are not understood.

At the opposite extreme is an open circuit: no conducting path through the modeled branch. An open branch may carry no steady current, yet the two ends can remain at a substantial voltage difference. No current in an open branch is not proof that its exposed terminals are harmless. The source may remain connected. Stored energy may remain. Induced or backfed voltage may be present. These are separate questions from the current of the simplified model.

## A tiny resistance at the wrong place

Imagine a connection that introduces an extra two-tenths of an ohm into a circuit carrying ten amperes. Its resistive heating, by the ideal equation current squared times resistance, is twenty watts, concentrated at the connection. In a real installation the temperature depends on contact geometry, surroundings, duration, changing resistance, and heat removal. The arithmetic is not a prediction that a particular connector will stabilize at any given temperature. It tells us why a small electrical resistance can matter greatly when substantial current flows through it.

This is one reason connection quality, suitable terminals, manufacturer-specified torque, and environmental protection exist in installation practice. The physical motivation is distinct from the exact terminal, conductor, rating, and testing requirements of a local code or a product's instructions. A listener cannot infer a safe termination method from the twenty-watt example.

## What a schematic can tell you, and what it cannot

If you are reading a schematic, ask four questions in order. What establishes the voltage or current? Which nodes are electrically the same in the model? Where can current split or rejoin? Where does each element transfer or store energy? These questions work for a battery-fed instrument, a lamp, a resistor network, or a drawing of a much more complex power system.

Then ask a fifth question before taking the model into the world: which physical effects did we leave out? A real wire has resistance and inductance. Connectors have ratings and failure modes. Sources have finite current limits, sometimes enormous ones. Insulation can fail. Protective devices respond to particular fault conditions and within particular time ranges. A clean circuit equation is the beginning of engineering judgment, not its substitute.

A good exercise is to work on paper. Draw a five-volt source, two resistors in parallel, and one resistor in series with that parallel pair. Label every node. Predict which branch has the larger current. Then calculate and check the voltage rises, the voltage drops, and the total energy transfer. Do not build the circuit unless it is part of a properly supervised, limited-energy teaching exercise.

Kirchhoff's laws give you something more durable than a wiring trick. They give you a disciplined way to ask where charge and energy are going. That skill will still be useful when the simple resistors are replaced by coils, capacitors, motors, electronic converters, and sources that change with time.

<!-- END SPOKEN LECTURE -->

## Technical companion — display only

### Idealized examples and dimensional checks

For an ohmic element, \(v=iR\). With signed current convention, the instantaneous absorbed power is \(p=vi\); for a passive resistor it is \(p=i^2R\). The ideal lumped network uses \(\sum i_{\mathrm{node}}=0\) and \(\sum v_{\mathrm{loop}}=0\) for branch voltage assignments. **Limit:** when time-varying flux links a physical path, use Faraday's law / appropriate induced-emf elements rather than a field-level assertion that circulation vanishes.

| Model | Calculation | Check |
|---|---|---|
| 5 V, 1 kΩ and 2 kΩ **series** | \(R_{eq}=3\,\mathrm{k\Omega}, I=1.6667\,\mathrm{mA}\) | Drops 1.6667 V and 3.3333 V; power 8.333 mW total |
| 5 V, 1 kΩ and 2 kΩ **parallel** | \(1/R_{eq}=1/1000+1/2000\), so \(R_{eq}\approx 666.67\,\Omega\) | Branches 5 mA + 2.5 mA = 7.5 mA; power 37.5 mW total |
| Local connection of 0.2 Ω at 10 A (hypothetical) | \(P=I^2R=20\,\mathrm{W}\) | Indicates concentrated heating possibility, not a temperature or compliance determination |

### Exercise with solution — desk only

**Question.** An ideal 9 V source supplies a 1 kΩ resistor in series with two 2 kΩ resistors in parallel. Find equivalent resistance, source current, parallel-branch current and total absorbed power. **Answer.** The parallel part is 1 kΩ, giving 2 kΩ total. Source current is 4.5 mA. The parallel branch voltage is 4.5 V, so each 2 kΩ branch carries 2.25 mA. Total power is \(9\times 0.0045 = 0.0405\,\mathrm{W}\). Verify KCL at the split and KVL around either branch loop. This ideal network does **not** specify physical component ratings.

**Model boundaries:** parasitic resistance/inductance, heating, source current limits, fault current, transients, displacement currents, magnetic induction, insulation, product ratings and adopted installation requirements are excluded from these calculations. No energized work is included.

### Claim-level source map (educational editorial check, 2026-11-15)

The IDs below correspond to structured records in `metadata/005000.json`. Citations specify a narrow claim; an engineering course does not establish legal installation permission.

| ID | Supported claim | Sources and limitations |
|---|---|---|
| E005000-01 | Lumped circuit analysis is an approximation of distributed fields | [`electrical-mit-6002-course`](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) (MIT 6.002 course overview), [`electrical-mit-6002-lecture2`](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/c7c33e6a7c168cda50ff54f99c45e041_6_0022007L02.pdf) (Lecture 2 transcript, KCL/KVL abstraction) |
| E005000-02 | Ohm's law is an element model, not universal for devices | [`electrical-openstax-ohm`](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) (§9.4), [`electrical-mit-6002-course`](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) (nonlinear elements in syllabus) |
| E005000-03 | Series topology means common branch current and additive resistances | [`electrical-openstax-seriesparallel`](https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel) (§10.2) |
| E005000-04 | Parallel topology means common voltage and summed currents | [`electrical-openstax-seriesparallel`](https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel) (§10.2) |
| E005000-05 | Kirchhoff junction law follows charge conservation in circuit approximation | [`electrical-openstax-kirchhoff`](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules) (§10.3), [`electrical-mit-6002-lecture2`](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/c7c33e6a7c168cda50ff54f99c45e041_6_0022007L02.pdf) |
| E005000-06 | Loop equations express voltage changes in standard lumped model | [`electrical-openstax-kirchhoff`](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules) (§10.3), [`electrical-mit-6002-lecture2`](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/c7c33e6a7c168cda50ff54f99c45e041_6_0022007L02.pdf) |
| E005000-07 | Physical changing magnetic flux limits naive field interpretation of KVL | [`electrical-openstax-inductors`](https://openstax.org/books/university-physics-volume-2/pages/14-2-self-inductance-and-inductors) (§14.2); verify more explicitly with Maxwell–Faraday before publication |
| E005000-08 | \(I^2R\) can concentrate heating at a resistive joint | [`electrical-openstax-power`](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (§9.5); independent connector failure-mode corroboration not yet completed |
| E005000-09 | An open branch can have no steady current while terminals remain energized | [`electrical-openstax-seriesparallel`](https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel) (§10.2, topology only), [`electrical-osha333`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) (occupational safe-work boundary) — not field-validated |
| E005000-10 | Numeric circuit examples do not certify installation safety | [`electrical-osha304`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) (occupational protection context), [`electrical-iec60364`](https://webstore.iec.ch/en/publication/63699) (installation scope abstract only) |

### Reference and attribution notes

- Gustav Kirchhoff is the historical namesake of the two rules; the source checked here is OpenStax §10.3, **not** an examination of Kirchhoff's original publication. The derivation and practice problems above are original pedagogical exposition.
- MIT 6.002 materials are attributed to Anant Agarwal and Jeffrey H. Lang and the MIT OCW course team; their teaching of circuit abstraction corroborates the OpenStax textbook independently.
- **Review outstanding:** qualified electrical review of interpretations that could be mistaken for field practice; current adopted wiring code, product ratings, and live-work procedures are intentionally not specified.
