# 001000 — Electricity Is a System: Voltage, Current, Power, and the Closed Path

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Background:** arithmetic. **Purpose:** create a physically useful mental model before teaching hardware or regional code.

<!-- BEGIN SPOKEN LECTURE -->

# Electricity Is a System

Look around a room. A lamp is on, a refrigerator makes a quiet sound, a phone is charging, and somewhere behind the walls there may be copper conductors connected to a much larger system. It is tempting to call all of that electricity as if electricity were a substance that appears wherever an appliance is plugged in. But the explanation that lets us reason safely about repairs begins with a more careful picture.

An electrical system has a source, a way for charges to move, and things that exchange energy with that movement. An individual wire, or a single battery terminal, tells us much less than the entire path. The same conductor can be harmless in one circuit arrangement and dangerous in another. The important questions are what is connected, what potential differences exist, how much current could flow, where energy is delivered, and what will happen when something fails.

We'll start with those questions, because they apply to a home circuit, a car, a small electronic device, or a solar-and-battery system even though the construction rules for those systems can differ.

## A source does not merely send electricity away

Consider a small battery and a lamp designed for that battery. A battery has two terminals. Inside, chemical processes maintain a difference in electrical potential. When a conductive path connects one terminal through the lamp to the other terminal, current can flow. The lamp converts electrical energy into light and heat. That conversion changes the battery's chemical state, and eventually it cannot maintain the same output.

The return path matters. Connect one wire from a battery to one terminal of a lamp and leave the other side disconnected, and you do not ordinarily get a lamp that continues operating. The loop is open. Electricity is not normally being consumed at the lamp and then replaced with fresh electricity. Charge is moving through the circuit, while energy is transferred from the source to the lamp.

This distinction is easy to overlook because language encourages us to say an appliance 'uses electricity.' It is more precise to say it uses *electrical energy*. In ordinary metal wires, charges are already present. The source establishes an electric field throughout the connected circuit, and energy is transferred by that field and by the resulting current. The charges themselves need not travel from a power station all the way to your lamp before the lamp turns on.

A useful analogy is a closed mechanical drive belt. A motor moves the belt; a machine attached elsewhere can receive power; the belt does not disappear inside the machine. The analogy breaks down in important ways, especially for alternating current and electromagnetic fields, but it protects us from the mistaken picture of electricity being spent like liquid poured from a bottle.

## Voltage is a difference, not a quantity sitting in one wire

Voltage expresses a difference in electric potential between two points. You can ask for the voltage between two battery terminals, or between a wire and a reference conductor. To say simply 'this wire has 120 volts' leaves the reference implicit. A safer mental habit is to ask, *120 volts relative to what?*

A source maintains an electrical potential difference, as a pump can maintain a pressure difference. The pump analogy helps with one idea: a difference can drive a flow. But electrons are not water, and a conductor can participate in high-frequency behavior where circuit geometry and electromagnetic fields matter. We use analogies as temporary tools, not as substitute laws.

Current measures the rate at which charge crosses a boundary. Its unit is the ampere. One ampere is one coulomb of charge per second. Conventional current direction is defined as the direction positive charge would move. In metals the mobile electrons drift in the opposite direction. Engineers still use conventional current because it makes circuit equations consistent.

If you have a battery attached to an appropriate resistive load, increasing the voltage across that load usually increases its current. For an ideal resistor at a fixed temperature, the relationship is Ohm's law, named for the nineteenth-century physicist Georg Simon Ohm: voltage equals current times resistance. A resistance of ten ohms with a voltage of five volts across it carries half an ampere in this simple model. Real components may have resistance that changes with temperature, and many electronic loads are not well described by a fixed resistance.

That last qualification matters. An LED is not just a little resistor. A motor changes its electrical behavior as it starts and spins. A computer power supply may draw more or less current to maintain a required output power. If you treat every appliance as a fixed resistor, you will make incorrect predictions.

## Power is the rate of energy transfer

Electrical power is energy per unit time. In a basic direct-current example, power in watts equals voltage in volts times current in amperes. A twelve-volt source delivering two amperes to a load supplies twenty-four watts at that instant. If the load consumes that amount for one hour, it receives twenty-four watt-hours of energy, ignoring changes in operation and losses.

The distinction between power and energy becomes especially important in a home. Power answers how hard a device demands the system to work *now*. Energy answers how much it consumes over a period. A heater rated at two thousand watts may need that level of power when its heating element is energized. Operating for half an hour at that power requires one kilowatt-hour of energy. If a thermostat switches it on and off, the actual energy over a day depends on duty cycle, not simply the rating multiplied by twenty-four hours.

A second example makes the limitations clearer. Take a hypothetical cooking appliance rated at two thousand watts. At a nominal supply of 120 volts, dividing power by voltage gives about sixteen point seven amperes for an ideal power-factor-one load at its rated operating point. At 240 volts the same ideal power would correspond to about eight point three amperes. That is not a wiring recommendation. Nameplate ratings, waveform, power factor, starting behavior, circuit rules, connectors, and the actual supply all matter. A quick calculation tells us the scale of a load; it cannot choose a breaker or cable for us.

This is a recurring pattern in electrical work: the physical equation is necessary, but the practical design also depends on operating conditions and fault behavior.

## The path is part of the design

Suppose you connect a source and a load with very long, thin wires. The wires have some resistance. As current flows, the wires heat and there is a voltage drop across them. In the simplest resistive model, heating power in a wire equals the square of the current times the wire's resistance. Doubling current at the same resistance creates four times the heating. That is one reason a connection that works briefly at light load may fail under heavier demand.

Connections deserve special attention. Every terminal has geometry and material surfaces. A poorly made connection can have higher resistance than intended. Current passing through that small resistance produces heat concentrated in a small volume. Heat can degrade surrounding materials, increase oxidation, or loosen a connection further. A safe electrical design is not only a drawing with correct symbols. It is a physical arrangement made of conductors, insulation, connectors, supports, protective devices, and enclosures whose condition matters throughout the installation's life.

The source can also deliver far more current during a fault than during normal operation. A battery capable of running a tiny light may still release substantial energy into an accidental short circuit. A household supply can supply a fault current very different from its ordinary load current. That is why we cannot choose protection just by asking how much an appliance uses when it works correctly.

## Alternating current changes direction but not the need for a circuit

Most modern homes are supplied with alternating current. Rather than a steady polarity at every instant, voltage and current vary with time. In ordinary utility systems, they repeat in a pattern characterized by frequency. Sixty cycles per second is common in North America; fifty is common in many other regions. These are practices, not universal properties of electricity.

When we hear that a socket supplies 120 volts or 230 volts alternating current, that generally refers to a *root-mean-square* value, abbreviated RMS, not the instantaneous peak. For a pure sinusoidal voltage, the peak magnitude is about one point four one four times the RMS value. RMS is chosen because it relates naturally to heating in a resistor. Real waveforms and electronic loads complicate matters, and the current may not rise and fall in step with the voltage. For that reason a simple multiplication of RMS voltage and RMS current gives apparent power, while actual average power also depends on waveform and phase relationship.

We will study those distinctions in their own right. For now, remember that alternating current does not eliminate the need to think about source, load, and the entire return path. It does mean that you cannot simply carry every rule learned from a battery over to a building supply unchanged.

## Efficiency is about where energy goes

Any conversion can have losses. A battery stores chemical energy. An inverter converts direct-current electrical energy into alternating-current electrical energy. A motor converts some input electrical energy into motion, with losses as heat and sound. A resistive heater converts nearly all of the electrical energy entering its element into heat where that element is located, although that does not make every heating system equally economical or appropriate.

Imagine a solar array feeding a battery and an inverter that powers a cooking appliance. Each stage has a voltage and current range, a maximum power, an efficiency curve, and constraints on its safe operation. Two kilowatt-hours required by the appliance do not mean exactly two kilowatt-hours drawn from the battery, because conversion and storage have losses. Nor does a solar panel labeled 'four hundred watts' provide four hundred watts at every hour of the day. The panel rating is measured under specified test conditions. Designing a practical system means respecting energy over time *and* instantaneous power, voltage, and current throughout the path.

Notice what we have not done. We have not inferred that a handful of compatible-looking connectors makes a complete electrical system. Interconnection, protective devices, control of sources, and manufacturer specifications remain indispensable. A model that predicts energy successfully can still be unsafe if it has no adequate way to interrupt a fault or keep an unintended conductor from becoming energized.

## Three questions to carry into every electrical project

When someone describes a proposed installation, ask first: *Where does the energy come from and through which complete paths could current flow?* Include normal operating paths and accidental ones.

Second: *What is the range of normal and fault conditions?* A circuit has to handle starting, steady operation, changing loads, heat, damaged insulation, accidental contact, and possible failure of protective components. Ratings are meaningful only relative to those conditions.

Third: *What evidence would make the design trustworthy?* That might include calculations, component listings, an appropriate wiring method, a competent inspection, or a test performed safely by someone trained to perform it. The evidence should address both the intended performance and the consequences of failure.

A final caution: understanding a formula is not the same as being equipped to work on the wiring behind a wall. Electrical energy can injure without warning. We will separate exercises that can be done on paper or with purpose-built, current-limited educational equipment from field tasks that require trained judgment, isolation, verification, and applicable authorization.

Electricity becomes much less mysterious when we stop thinking of it as something a device consumes and begin thinking in systems. A lamp, a house, a battery, and a solar inverter differ enormously in scale and construction. But source, circuit, energy transfer, and failure paths give us a common language for understanding all four.

<!-- END SPOKEN LECTURE -->

## Technical companion — display only

### Minimal model

- Current: \(I=dq/dt\) (one ampere is one coulomb per second).
- Electrical potential difference: \(V_{ab}=\phi(a)-\phi(b)\), with a stated reference.
- Lumped resistor, fixed conditions: \(V=IR\).
- Instantaneous electrical power at a port: \(p(t)=v(t)i(t)\). For steady DC, \(P=VI\).
- Energy: \(E=\int p(t)\,dt\), with \(1\ \mathrm{kWh}=3.6\ \mathrm{MJ}\).
- Resistive conductor heating: \(P_{\mathrm{loss}}=I^2R\) (valid for a resistive model and RMS current in AC).
- Sinusoid: \(V_{\mathrm{peak}}=\sqrt2\,V_{\mathrm{rms}}\). For arbitrary AC, \(P_{\mathrm{avg}}=\langle vi\rangle\) and \(S=V_{\mathrm{rms}}I_{\mathrm{rms}}\); average power is not necessarily \(S\).

### Worked example — energy versus power

An example load draws 2,000 W for 45 minutes: \(E=(2,000)(0.75)=1,500\ \mathrm{Wh}=1.5\ \mathrm{kWh}\). If a hypothetical conversion chain has 90% end-to-end efficiency at that operating condition, input energy is about \(1.5/0.9=1.67\ \mathrm{kWh}\). Not enough information exists to infer conductor size, protection, or connection method.

### Conceptual exercises (desk-only)

1. Two loads each use 100 W. One runs one hour, the other four hours. Compare their energies. **Answer:** 100 Wh versus 400 Wh.
2. A wire's resistance stays constant but its current doubles. How does resistive heating change? **Answer:** fourfold.
3. Why is an open switch not necessarily proof that an enclosure is safe to touch? **Answer:** it may not isolate all energized parts; other sources, capacitors, and misidentification remain possible.
4. Can a panel's nominal power rating specify its whole-day energy output? **Answer:** no; irradiance, temperature, shading, conversion and time determine production.

**Practice classification:** desk calculations and schematic simulation. No household wiring, opened covers, or live measurements.

### References

- IEC 60364-1 — safety goals for low-voltage installations (`electrical-iec60364`).
- U.S. Department of Energy — photovoltaic system design and energy conversion (`electrical-doe-solar-design`).
- OSHA — wiring/protection and the purpose of overcurrent protection (`electrical-osha-construction`).

### Claim-level source map (editorial review: 2026-11-15)

Each claim has a stable evidence ID in `metadata/001000.json`. The entries below identify the supporting source, a precise section when available, and its **role**. A publisher abstract supports only a standard's edition and scope, not the detailed requirements of its normative clauses. The reader-facing lecture is not an installation authorization.

| Evidence ID | Narrow claim | Evidence links, exact location, and role |
|---|---|---|
| E001000-01 | Idealized battery-and-lamp operation uses a closed circuit; voltage is a potential difference between two points | [Samuel J. Ling, William Moebs, Jeff Sanny; OpenStax (2016)](https://openstax.org/books/university-physics-volume-2/pages/10-1-electromotive-force) — §10.1: closed source-to-lamp-and-return circuit (main; `electrical-openstax-battery`); [Samuel J. Ling, William Moebs, Jeff Sanny; OpenStax (2016)](https://openstax.org/books/university-physics-volume-2/pages/9-1-electrical-current) — §9.1: definition of current (separate_support; `electrical-openstax-current`); [Samuel J. Ling, William Moebs, Jeff Sanny; OpenStax (2016)](https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference) — §7.2: potential difference (separate_support; `electrical-openstax-potential`) |
| E001000-02 | Ohm law applies to ohmic components, not to all appliances | [Samuel J. Ling, William Moebs, Jeff Sanny; OpenStax (2016)](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) — §9.4 (main; `electrical-openstax-ohm`) |
| E001000-03 | Power is energy-transfer rate; VI applies as stated for steady DC / instantaneous port values | [Samuel J. Ling, William Moebs, Jeff Sanny; OpenStax (2016)](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) — §9.5 (main; `electrical-openstax-power`) |
| E001000-04 | Joule heating scales as I squared times resistance | [Samuel J. Ling, William Moebs, Jeff Sanny; OpenStax (2016)](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) — §9.5 (main; `electrical-openstax-power`) |
| E001000-05 | Nominal AC voltage is generally RMS, not instantaneous peak | [Samuel J. Ling, William Moebs, Jeff Sanny; OpenStax (2016)](https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits) — §15.2 (main; `electrical-openstax-rms`) |
| E001000-06 | Actual AC real power need not equal Vrms times Irms | [Samuel J. Ling, William Moebs, Jeff Sanny; OpenStax (2016)](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) — §15.4, sinusoidal case (main; `electrical-openstax-acpower`) |
| E001000-07 | Electrical power and energy estimates do not establish conductor, overcurrent or equipment safety | [U.S. Department of Labor, OSHA](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) — §1910.304(f),(g); occupational example, not a homeowner design table (main; `electrical-osha304`) |
| E001000-08 | PV generation is a system requiring conversion and controls, not only modules | [U.S. Department of Energy](https://www.energy.gov/cmei/systems/solar-photovoltaic-system-design-basics) — PV system design basics (main; `electrical-doe-solar-design`) |

**Editorial limitation:** The citations identify evidence and its intended use. Not all consequential claims have two independent sources, and full locally adopted code clauses and equipment listing conditions have not been checked. A qualified safety/electrical review remains **pending**; the track is currently an educational draft, not a certified field manual.
