# 007000 — Where Electrical Energy Waits: Capacitors, Inductors, Impedance, and Transients

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Background:** simple AC waveforms and circuit laws. **Practice boundary:** calculations and simulations only. The existence of residual charge or inductive kickback is a reason not to open or modify electrical equipment without qualified procedures, not an invitation to discharge capacitors or disconnect inductive loads.

<!-- BEGIN SPOKEN LECTURE -->

# Where Electrical Energy Waits: Capacitors, Inductors, Impedance, and Transients

Imagine opening a switch on a circuit that contains only an ideal source and a resistor. In the simplest model the current stops immediately. Now imagine that the circuit also contains a coil or a capacitor. The situation changes. The coil can have energy stored in its magnetic field. The capacitor can have energy stored in its electric field. Changing the circuit does not erase that energy. It has to go somewhere.

This is why a power supply can remain hazardous after its input is disconnected, why switching a motor or a relay can produce a sharp transient, and why the response of a circuit depends on frequency even when the resistive part has not changed.

Our goal is not to learn a few rules for choosing capacitors or coils. It is to understand what those parts *do*, the time scales on which they do it, and the difference between a useful mathematical model and a verified protective design.

## A resistor transfers energy; a capacitor stores it

An ideal resistor is described by a voltage proportional to current, at a given resistance. Its absorbed electrical energy becomes heat. A capacitor behaves differently. It can accumulate equal and opposite charges on two conductive regions separated by an insulating medium. The stored electrical energy is associated with the electric field. The amount of charge for a given voltage is described by capacitance, measured in farads.

A simple model says that the capacitor's current depends on how quickly its voltage changes. A constant voltage across an ideal capacitor does not sustain an ongoing DC conduction current through its dielectric once the transient is over. But a changing voltage produces charging and discharging current at its terminals. That is why a capacitor can participate in an alternating-current circuit without being equivalent to a piece of conductive wire between its terminals.

A crucial distinction: an ideal capacitor being an open circuit for *steady DC* does not mean that a charged capacitor is safe to touch. Its terminals may hold substantial voltage, and the stored energy can be released through an unintended path. In real circuits there are leakage paths, dielectric properties, internal resistances, and protective circuits; none of those should be assumed to discharge it at a known rate without design evidence and verification. Never attempt to discharge an unknown capacitor as an educational exercise.

The energy stored by an ideal capacitor is proportional to its capacitance and to the square of its voltage. Doubling its voltage, with capacitance held constant, increases stored energy by a factor of four. This is one reason voltage ratings, insulation and discharge procedures cannot be inferred from the component's capacitance alone.

## The RC time constant

Put an ideal resistor and capacitor in a simple model with a DC source. When the source applies a step in voltage, the capacitor does not jump instantly to its final voltage. It charges over time. In the simplest series resistor-capacitor model, the product of resistance and capacitance sets a time scale. Engineers call that product the RC time constant.

Take a hypothetical resistor of ten thousand ohms and a capacitor of one hundred microfarads. Multiply them and you obtain one second. In the ideal step-response calculation, after one time constant the capacitor voltage has moved about sixty-three percent of the way toward its final value. After three time constants it has moved about ninety-five percent of the way. The progression is exponential, meaning each equal interval removes the same fraction of the remaining difference, not the same number of volts.

If the model describes discharging through a known resistance, after three time constants about five percent of the initial voltage remains. Five percent is not automatically harmless, and this calculation assumes the proposed discharge path, component values, and initial conditions are correct. It is not a field verification method. A real capacitor may have a very different discharge path—or none of the path the solver imagined.

This mathematical shape shows up everywhere: in sensing circuits, delays, filters, control systems and measurements. It also tells us why a circuit that appears steady after a few seconds may have behaved very differently just after a switch changed state.

## Inductors store energy in magnetic fields

Now consider a coil. A current produces a magnetic field. When that current changes, the changing magnetic flux induces an electromotive force that opposes the change. The phenomenon is described by Faraday's law and the opposition by Lenz's law. A simplified circuit model uses inductance, measured in henries, to relate the voltage across an ideal inductor to how fast its current changes.

Notice the complementarity. A capacitor resists an instantaneous change of its terminal voltage in the ordinary finite-current model. An inductor resists an instantaneous change of its current in the ordinary finite-voltage model. Neither one is magically rigid. Give an element enough voltage, current, or time, and real components can exceed limits, change properties, or fail.

The energy stored in an ideal inductor's magnetic field is proportional to its inductance and the square of its current. If the current is doubled, the ideal stored energy becomes four times as large. The energy is not a free extra source. It came from the circuit while the field was established, and it must be transferred back or dissipated as the current changes.

A changing magnetic field can drive a significant transient voltage across a switch or semiconductor when the current path is interrupted. That is one reason practical circuits use appropriately designed suppression, insulation and switching devices. But the correct method depends on the device, voltage, fault conditions and product design. The lecture does not teach someone to attach an improvised diode, capacitor or resistor to an unknown household device.

## The RL time constant

The simplest resistor-inductor circuit has another exponential time scale. This time it is inductance divided by resistance. A hypothetical inductor of two-tenths of a henry and a resistor of ten ohms give a time constant of two hundredths of a second, or twenty milliseconds. In the ideal step-response model, the current approaches its final value exponentially, reaching roughly sixty-three percent of the change after one time constant.

This is close to the period of some mains-frequency waveforms, so it should not be surprising that coils and alternating current interact strongly. Real motors and transformers are far more complex than a fixed inductor. Their effective inductance may vary with current, core saturation, temperature, and mechanical state. Inrush currents, switching stresses and magnetic fields make full design a different task from solving the simple RL equation.

## Why frequency changes the picture

If you apply a sinusoidal voltage to an ideal resistor, current and voltage rise and fall together. An ideal capacitor instead has current that leads voltage by a quarter cycle. An ideal inductor has current that lags voltage by a quarter cycle. That statement refers to the usual passive-sign convention and to steady sinusoidal operation of the ideal elements. It is not a complete account of what a real motor or electronic supply draws.

For sinusoidal steady-state analysis, engineers introduce impedance. Resistance is the real, dissipative part. Reactance describes the phase-related response associated with ideal energy storage. A capacitor's reactance magnitude becomes *smaller* as frequency rises. An inductor's reactance magnitude becomes *larger* as frequency rises. This gives a way of reasoning about why a component that is nearly irrelevant at one frequency can dominate at another.

Do not confuse a reactance, expressed in ohms, with resistance that dissipates the same amount of heat. An ideal inductor or capacitor can have a substantial voltage across it and current through it while absorbing zero *average* real power over a complete steady sinusoidal cycle. Energy goes into its field and comes back later. Real components contain resistance and other losses, so their actual behavior is not lossless.

At sixty hertz, consider an ideal one-tenth-henry inductor. Its reactance magnitude is about thirty-seven point seven ohms. A one-hundred-microfarad ideal capacitor has a reactance magnitude of about twenty-six point five ohms at the same frequency. Those are calculations for isolated ideal elements, not a recipe for assembling them on a power line. Choosing physical parts requires voltage ratings, ripple-current ratings, failure modes, component tolerances and circuit-specific design.

## Resonance and the possibility of large internal quantities

Now combine inductance and capacitance. Each stores energy in a different field. Under some conditions energy can oscillate between them. An ideal inductance-capacitance system has a natural oscillation frequency set by the two values. Add a resistor and the oscillation is damped. Drive the system from an alternating source and, under appropriate conditions, the response can be amplified near resonance.

A subtle point follows. The voltage across an individual component inside an AC network need not be smaller than the source voltage. In a resonant series circuit, substantial inductor and capacitor voltages can oppose each other in phase while adding to a modest net source voltage. That is no violation of Kirchhoff's loop rule. It is a warning about reasoning from only the supply rating when judging internal stress.

Actual resonant behavior depends on losses and coupling, and modern electronic equipment may introduce several frequencies at once. The simple sinusoidal impedance model is a tool, not a guarantee. Engineers use it to select questions for deeper analysis: Will current rise? Could component voltage become excessive? Could switching excite an unexpected resonance? Which part needs thermal and electrical protection?

## Why disconnection is not enough

The safety consequence is now clearer. A conductor may be disconnected from one power source and still be connected to another. A capacitor may retain field energy after the source is gone. An inductor or a moving machine may transfer energy back into a circuit. Solar equipment, batteries, motor drives and inverters may have multiple supplies and storage elements.

Workplace electrical rules such as OSHA's control of hazardous electrical energy and verification provisions describe safeguards for their legal scope. They are not a universal step-by-step method for private homeowners. A person untrained in the specific equipment should not assume that opening one switch, waiting a guessed time, or taking one voltage reading has proved an assembly safe. Product documentation and qualified verification procedures exist because the energy paths are not always visible from the front panel.

This is the most useful principle to carry from the lesson: **voltage and current are states, not just labels on components, and stored energy survives changes in configuration**. The rate of change can determine what the device does, not just the final steady state.

For practice, draw two graphs, entirely on paper. One begins at zero and approaches twelve volts exponentially with a one-second time constant. The other begins at twelve volts and decays toward zero. Mark the first, third and fifth time constants. Then explain, in words, why the fact that a mathematical curve comes close to zero cannot be substituted for a verified absence of hazardous voltage.

When we move to power quality and practical energy systems, this way of thinking will be essential. It helps us connect fast transients, steady waveforms, stored energy, protective behavior and the limits of everyday intuition.

<!-- END SPOKEN LECTURE -->

## Technical companion — display only

### Element laws and stored energy

Under the passive-sign convention for ideal lumped elements:

\[
v_R=Ri,\quad i_C=C\frac{dv_C}{dt},\quad v_L=L\frac{di_L}{dt},\quad E_C=\tfrac12 CV^2,\quad E_L=\tfrac12 LI^2.
\]

The DC-step RC charge response under an ideal source is \(v_C(t)=V(1-e^{-t/RC})\); an ideal isolated discharge through **the modeled resistor** follows \(v_C(t)=V_0 e^{-t/RC}\). An analogous RL step has \(i_L(t)=(V/R)(1-e^{-tR/L})\) for the ideal series circuit. Neither equation is a field procedure or a safe-discharge prediction for unknown equipment.

| Illustrative model | Time/frequency quantity | Interpretation |
|---|---|---|
| 10 kΩ, 100 µF RC | \(\tau=RC=1\,\mathrm{s}\) | After 3 s, ideal discharge retains \(e^{-3}\approx 0.0498\) of initial voltage |
| 0.2 H, 10 Ω RL | \(\tau=L/R=0.020\,\mathrm{s}\) | A current step evolves on ~20 ms scale |
| 0.1 H ideal inductor at 60 Hz | \(X_L=2\pi fL\approx37.7\,\Omega\) | Reactance, not energy-dissipating resistance |
| 100 µF ideal capacitor at 60 Hz | \(X_C=1/(2\pi fC)\approx26.5\,\Omega\) | Reactance, not a continuous DC conduction path |

### Sinusoidal impedance and resonance

\[
Z_R=R,\qquad Z_L=j\omega L,\qquad Z_C=\frac{1}{j\omega C},\qquad \omega=2\pi f.
\]

A simple ideal series RLC combination has \(Z=R+j(\omega L-1/(\omega C))\). If losses are ignored, the characteristic LC angular frequency satisfies \(\omega_0=1/\sqrt{LC}\). This relation **does not** establish a safe voltage or peak current in an actual device; resonance and component failures depend on damping, source impedance and ratings.

### Desk exercise with answer

An ideal 10 kΩ resistor and 100 µF capacitor are modeled in a step response. What fraction of the initial voltage remains after 1 s and 5 s of *ideal modeled discharge*? **Answer:** \(e^{-1}\approx36.8\%\) and \(e^{-5}\approx0.674\%\). **Safety finding:** neither percentage is a verified voltage, a safe touch limit, or an appropriate waiting period for equipment. Do not use this exercise on a real capacitor.

### Claim-level source map (educational editorial check, 2026-11-15)

| ID | Supported claim | Sources and limitations |
|---|---|---|
| E007000-01 | Capacitor stores energy in electric field, which can remain after disconnection | [`electrical-openstax-cap-energy`](https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor) (§8.3), [`electrical-openstax-rc`](https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits) (§10.5) |
| E007000-02 | Ideal \(i=C\,dv/dt\) and \(E=\tfrac12CV^2\) | [`electrical-openstax-cap-energy`](https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor) (§8.3), [`electrical-openstax-rc`](https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits) (§10.5); ideal constant-C assumption |
| E007000-03 | RC response is exponential with time constant RC | [`electrical-openstax-rc`](https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits) (§10.5) |
| E007000-04 | Inductance is an induced-emf response to changing magnetic flux/current | [`electrical-openstax-inductors`](https://openstax.org/books/university-physics-volume-2/pages/14-2-self-inductance-and-inductors) (§14.2), [`electrical-mit-6002-course`](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) (energy storage lectures) |
| E007000-05 | Inductor stores magnetic field energy \(\frac12 LI^2\) | [`electrical-openstax-inductor-energy`](https://openstax.org/books/university-physics-volume-2/pages/14-3-energy-in-a-magnetic-field) (§14.3) |
| E007000-06 | RL response is exponential with time constant L/R | [`electrical-openstax-rl`](https://openstax.org/books/university-physics-volume-2/pages/14-4-rl-circuits) (§14.4) |
| E007000-07 | Capacitive reactance falls and inductive reactance rises with frequency | [`electrical-openstax-ac-circuits`](https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits) (§15.2), [`electrical-openstax-rlc`](https://openstax.org/books/university-physics-volume-2/pages/15-3-rlc-series-circuits-with-ac) (§15.3) |
| E007000-08 | Ideal L and C shift phase and return average stored energy over a sinusoidal cycle | [`electrical-openstax-ac-circuits`](https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits) (§15.2), [`electrical-openstax-acpower`](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (§15.4) |
| E007000-09 | RLC resonance can amplify internal voltages/current | [`electrical-openstax-rlc`](https://openstax.org/books/university-physics-volume-2/pages/15-3-rlc-series-circuits-with-ac) (§15.3); engineering stress/insulation implications require device-specific verification |
| E007000-10 | Disconnecting input does not by itself establish safety | [`electrical-openstax-cap-energy`](https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor) (§8.3); [`electrical-osha333`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) (§1910.333(b), occupational work practice, not homeowner permissions) |
| E007000-11 | Protective switching for inductive energy requires engineered design | [`electrical-openstax-inductors`](https://openstax.org/books/university-physics-volume-2/pages/14-2-self-inductance-and-inductors) (§14.2, induced EMF); design details unresolved, qualified review pending |

### Outstanding review and scope limits

This manuscript does **not** give a discharge, measuring, isolation, motor-switching, suppression or inverter wiring procedure. No quantitative safe-touch, waiting-time or protection claim is made. Verify product-specific stored-energy warnings and locally applicable legal requirements before any work. A qualified electrician/engineer review remains pending; the content is a source-audited educational draft only.
