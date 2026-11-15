# 008000 — Useful Power and Distorted Current: Power Factor, Harmonics, and Power Quality

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Background:** AC, RMS, phase and impedance. **Practice boundary:** paper calculations and examination of published waveform recordings; power-quality measurement inside real installations is qualified-person work with an application-specific safety plan.

<!-- BEGIN SPOKEN LECTURE -->

# Useful Power and Distorted Current: Power Factor, Harmonics, and Power Quality

Two electrical devices can consume the same average number of watts and draw different currents from the same supply. That fact is surprising if your entire picture of electricity comes from a direct-current battery and a resistance. In that model, knowing the voltage and watts can be enough to calculate the current. But in alternating-current systems, especially when the waveform is distorted, there is more than one way for current to be large without a corresponding increase in average real power.

The language for understanding the difference includes real power, apparent power, reactive power, power factor, and harmonics. These terms are often used in equipment specifications, energy audits, inverter ratings, and discussions of electrical quality. They are also widely misinterpreted. Power factor is not simply 'the percent of electricity wasted,' and a harmonic is not a mysterious form of free energy. Both are descriptions of how electrical quantities vary in time and interact with the system.

## What the watts are measuring

Begin at a pair of terminals. At an instant, voltage multiplied by current gives the rate of energy transfer, with sign determined by your reference directions. A waveform can deliver energy to a device during part of a cycle and receive some of it back during another part. Real power, measured in watts, is the average of that instantaneous product over an appropriate interval.

If a heating element receives one thousand watts of real electrical power and converts almost all of it into heat, that tells us something direct about its electrical energy consumption and thermal output. One hour at one thousand watts corresponds to one kilowatt-hour of transferred energy, ignoring any changes over time. The same wattage, in another device, might be converted to motion, light, heat and losses in different proportions. Electrical real power and useful output efficiency are different concepts.

Now ask a separate question: what RMS current and voltage must the supplying network accommodate? The product of RMS voltage and RMS current is called apparent power, measured in volt-amperes. The units are dimensionally equal to watts but the physical interpretation is not the same. Apparent power describes the combined RMS voltage-current burden at the interface. It does not, by itself, say how much energy is converted to heat, motion or light per second.

The ratio of real power to apparent power, for nonzero apparent power, is the overall power factor. If real power is nine hundred watts and apparent power is twelve hundred volt-amperes, the magnitude of the power factor is zero point seven five. In a simple absorbing-load convention we report a positive factor less than or equal to one. Sign conventions for generating equipment and bidirectional power vary, so a complete analysis must specify them rather than silently reusing a load-only convention.

Why can't real power exceed the product of the RMS values? Mathematically, the magnitude of the average product of two waveforms is bounded by the product of their RMS magnitudes. This is a special case of a general inequality about averages. It is not a regulation or a claim about any particular piece of equipment. It is a property of the definitions.

## Displacement: when current arrives out of phase

Suppose the supply voltage is a perfect sine wave and the current is also a sine wave of the same frequency. If they rise and fall together, the phase difference is zero, and a purely resistive load absorbs average power equal to RMS voltage times RMS current. If the current lags the voltage because the load has an inductive component, or leads because it has a capacitive component, the average real power is reduced relative to the same RMS magnitudes.

Under these sinusoidal assumptions, real power is apparent power multiplied by the cosine of the phase difference. The phase-shift portion is often called displacement power factor. We can also introduce reactive power, measured in vars, a term reflecting the energy exchange associated with reactive elements. In the simplest single-frequency case, reactive power is proportional to the sine of the phase difference. Real and reactive power form the sides of a familiar triangle, with apparent power as its hypotenuse.

But that triangle is not a universal formula for every distorted circuit. When voltage and current have several harmonic components, a unique single phase angle is generally not enough to describe them, and reactive-power definitions need additional care. Engineering standards distinguish multiple power quantities precisely because naive extensions of the sinusoidal triangle can be misleading.

An ideal coil receiving steady sinusoidal current stores magnetic energy and returns it later, transferring no *net* real energy over the cycle. A real motor contains coils, moving parts, losses and control electronics, so it does consume real power. Calling the motor 'inductive' is useful shorthand, not a complete equivalent circuit.

## Distortion: when the current is not a sine wave

Consider a power supply that rectifies AC into DC and charges a storage capacitor. Depending on its design, it might draw current in pulses rather than in a smooth sine wave. Modern products use many different techniques; some are designed to shape their input current to approximate a sine wave. The point is that a voltage waveform can look fairly smooth while the current waveform does not.

A periodically repeating waveform can be represented as a combination of sinusoidal components at different frequencies. The component at the repetition frequency is the fundamental. Components at integer multiples are harmonics. On a sixty-hertz system, the third harmonic is at one hundred and eighty hertz, the fifth at three hundred hertz, and so on. On a fifty-hertz system, those numbers are different. The mathematical description is associated with the Fourier-analysis tradition, but we should not treat every modern instrument or power-quality convention as a direct claim of a single historical inventor.

A nonlinear load can have a current waveform with strong harmonic content even when its fundamental current is in phase with the voltage. In that case the **displacement** power factor can be close to one while the **overall** power factor is substantially less than one. The difference comes from the additional RMS current in harmonics, which contributes to apparent power without necessarily contributing matching real power when the voltage remains sinusoidal.

Here is a deliberately artificial example that makes the distinction precise. Imagine a perfect one-hundred-and-twenty-volt RMS sine-wave supply. A device draws a six-ampere RMS current at the fundamental frequency, exactly in phase with the supply, plus an eight-ampere RMS current at the third harmonic. The two current components are orthogonal when averaged over a whole number of fundamental cycles. Their squares add for RMS, so the total current is ten amperes RMS.

The third-harmonic current contributes zero average real power *in this ideal example* because the supply voltage has only the fundamental sine wave. The real power is one hundred and twenty volts times six amperes, or seven hundred and twenty watts. The apparent power is one hundred and twenty volts times ten amperes, or twelve hundred volt-amperes. The overall power factor is zero point six. Meanwhile the fundamental displacement factor is one. A single cosine-of-phase formula would miss the difference entirely.

If the voltage itself is distorted, harmonic voltage and matching harmonic current components can contribute to real power, and the analysis must account for them. Source impedance also matters: non-sinusoidal current can cause distortion at the device terminals. These are measurable, engineering questions, not just variations in vocabulary.

## Why harmonics matter physically

A conductor's resistive heating depends strongly on RMS current. Harmonic current therefore matters even if a simplified real-power calculation shows little additional load power. Transformers, motors, capacitors, wiring and measuring devices have frequency-dependent behavior. Some equipment responds to harmonic current with additional losses, vibration, heating, or altered readings. High-frequency current and source impedance can complicate electrical power measurement; published laboratory work on LED lighting has demonstrated this rather than merely assuming it.

In a suitable three-phase, four-wire arrangement, some harmonic currents—particularly certain triplen harmonics—can add in the neutral instead of cancelling like balanced fundamental currents. That is a conditional statement about phase relationships and the system connection, not a blanket rule that every neutral in every home has a harmonic overload. Professional design and measurement must account for the actual network and loads.

Another useful distinction is between harmonic distortion and a transient. Harmonics describe components of a repeated waveform. A switching surge or lightning-related disturbance may occur once or intermittently and may not be represented adequately by a small set of steady harmonic amplitudes. Different phenomena call for different measurements, protection measures and engineering analysis.

## Why 'fix the power factor' is not a household recipe

For some industrial systems with inductive loads, engineers may use capacitor banks or other equipment to reduce reactive current and improve the source-side power factor. Other installations use active filters or power-electronic correction. But indiscriminately adding capacitance can worsen a condition by creating resonance with the network inductance, raising stresses or interacting with existing harmonics. A fix for phase displacement is not necessarily a fix for nonlinear current.

There is also an economic distinction. Utilities may use billing structures that charge for demand, apparent power or poor power factor, especially for larger customers. A typical residential bill may not separately price those quantities. Improving power factor does not automatically make a particular appliance use fewer kilowatt-hours of real energy for the same task. System current and losses can change, and those changes require actual measurements and an applicable tariff analysis. Neither a lower wattage on a marketing sheet nor a higher advertised power factor is proof of a safe or more economical installation.

The safe lesson is diagnostic: understand the waveform, the source, the loads and the protection objective before selecting any corrective equipment. No one should install capacitor banks, filters or inverter modifications based on an introductory power triangle.

## Choosing the right question for a measurement

Suppose a homeowner reports flickering lights whenever a large appliance starts. Many physical explanations are possible: startup current, voltage drop, wiring impedance, controls, or an unrelated supply issue. The observation itself does not identify a fault, and it certainly does not authorize live panel probing. A qualified technician may use properly rated instruments and an assessment of work hazards to measure voltage over time, harmonics, or other power-quality parameters. But the instrument selection, connection points, test conditions, and safety procedures must fit that installation.

Before any measurement, there is a question of *what must be measured*. A basic RMS reading may answer whether voltage is near its nominal value while failing to reveal short transients or harmonic detail. An instrument with insufficient bandwidth may understate power for some distorted waveforms. A reading can be numerically precise while being a poor answer to the engineering question. This is why publications from metrology laboratories and instrument manufacturers discuss sampling, source impedance, spectral content and definitions—not just the displayed digits.

For a desk exercise, imagine receiving a report with three entries: RMS voltage, RMS current, and real power. Compute apparent power and overall power factor. Next ask whether that is enough information to say *why* the factor has its value. It is not. You would need waveform or fundamental-phase information to distinguish displacement from distortion. The difference between calculating a result and diagnosing its cause is one of the most important habits in technical work.

## Connecting the vocabulary to ordinary decisions

When comparing equipment, a watt is not a volt-ampere, and neither is a watt-hour. Voltage describes a potential difference; RMS current describes a time-averaged magnitude relevant to many thermal questions; real power describes the rate at which energy is transferred on average; power factor relates real to apparent power. Harmonics describe components of the waveform that may affect current, heat and measurements. An inverter's output rating, peak capability, distortion limits and protective behavior are distinct specifications.

Once you can say those words precisely, you can ask better questions of an electrician, engineer, equipment manufacturer or utility. You can read a nameplate and recognize what it does not tell you. You can recognize that a poor power factor might arise from phase displacement, distortion, or both. And you can avoid turning a convenient number into an unsafe modification.

Electricity is not only about how much charge flows and how much energy is delivered. It is also about *when* the current flows. The shape and timing of a waveform can determine whether a system behaves as intended. That is the insight power quality adds to basic circuit theory.

<!-- END SPOKEN LECTURE -->

## Technical companion — display only

### Definitions valid beyond sinusoidal operation

For periodic voltage and current over a common period \(T\) with a declared passive sign convention:

\[
P=\frac1T\int_0^T v(t)i(t)\,dt,\qquad
S=V_{\rm rms} I_{\rm rms},\qquad
\mathrm{PF}=P/S \quad(S>0).
\]

For an absorbing load, \(0\leq\mathrm{PF}\leq1\) under the usual sign convention; for bidirectional exchange a signed ratio may be negative. The bound \(|P|\leq S\) follows from Cauchy–Schwarz. In the **sinusoidal single-frequency case only**, \(P=S\cos\varphi\), \(Q=S\sin\varphi\), and \(S^2=P^2+Q^2\). Do **not** automatically apply the same \(Q\) triangle to arbitrary nonlinear waveforms.

For periodic signals, a harmonic of order \(n\) occurs at \(nf_1\). With sinusoidal voltage *only at the fundamental*, a harmonic current at an integer multiple of the fundamental is orthogonal to the voltage over a complete period. For the original illustrative waveform with fundamental current 6 A RMS (in phase) and third-harmonic current 8 A RMS:

\[
I_{\rm rms}=\sqrt{6^2+8^2}=10\,\mathrm{A},\quad
P=120\times6=720\,\mathrm{W},\quad S=120\times10=1200\,\mathrm{VA},\quad\mathrm{PF}=0.6.
\]

The displacement factor of the **fundamental** is one. The overall factor is 0.6. This exercise is not a physically complete source/load design.

### Practice questions — desk only

1. **Computation.** A report shows 230 V RMS, 4 A RMS and 690 W average real power. Compute \(S\) and PF. **Answer:** 920 VA and 0.75. **Not enough information** is supplied to identify displacement or harmonic distortion.
2. **Reasoning.** A source has perfectly sinusoidal voltage; the load current has an in-phase fundamental and third harmonic. Does the third harmonic add to RMS current? Does it add to the average real power under the assumed perfectly sinusoidal voltage? **Answer:** It increases total RMS current; its contribution to average real power is zero in this specifically idealized case.
3. **Critical distinction.** Does improving PF from 0.75 to 0.95 prove a motor uses fewer kilowatt-hours for the same work? **Answer:** No. Real energy and the load's output efficiency must be examined separately. Wiring losses may change, but amount and applicability depend on system details.

### Claim-level source map (educational editorial check, 2026-11-15)

| ID | Supported claim | Sources and limitations |
|---|---|---|
| E008000-01 | Real power is the time average of instantaneous VI | [`electrical-openstax-acpower`](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (§15.4), [`electrical-nist-harmonics-measurement`](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=913513) (§3, Eqs. 8–10) |
| E008000-02 | Apparent power is RMS voltage × RMS current; PF = P/S | [`electrical-nist-harmonics-measurement`](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=913513) (§3), [`electrical-fluke-power-factor`](https://www.fluke.com/en-us/learn/blog/power-quality/improve-power-factor) (definition); independent lines |
| E008000-03 | Phase cosine formula is specific to single-frequency sinusoidal conditions | [`electrical-openstax-acpower`](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (§15.4), [`electrical-nist-harmonics-measurement`](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=913513) (§3, multi-harmonic power) |
| E008000-04 | Pure reactive ideal elements exchange field energy over a sinusoidal cycle | [`electrical-openstax-acpower`](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (§15.4), [`electrical-openstax-inductor-energy`](https://openstax.org/books/university-physics-volume-2/pages/14-3-energy-in-a-magnetic-field) (§14.3) |
| E008000-05 | Nonlinear electronic loads can produce harmonic current | [`electrical-nist-harmonics-measurement`](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=913513) (abstract, §2, LED current), [`electrical-fluke-harmonics`](https://www.fluke.com/en-us/learn/blog/power-quality/installation-harmonics) (nonlinear-load examples) |
| E008000-06 | Harmonics occur at integer multiples of fundamental frequency | [`electrical-nist-harmonics-measurement`](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=913513) (§3, equations 1–2 and definitions) |
| E008000-07 | Overall PF can differ from fundamental displacement PF in distorted systems | [`electrical-nist-harmonics-measurement`](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=913513) (§3), [`electrical-fluke-power-factor`](https://www.fluke.com/en-us/learn/blog/power-quality/improve-power-factor) (motor versus harmonic roots) |
| E008000-08 | Harmonics can affect thermal loading and power metrology | [`electrical-nist-harmonics-measurement`](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=913513) (abstract, §2, measurements), [`electrical-fluke-harmonics`](https://www.fluke.com/en-us/learn/blog/power-quality/installation-harmonics) (risk context) |
| E008000-09 | Some three-phase four-wire systems can have neutral harmonic addition | [`electrical-fluke-harmonics`](https://www.fluke.com/en-us/learn/blog/power-quality/installation-harmonics) (installation-harmonics article); system-specific corroboration outstanding |
| E008000-10 | Power factor correction methods depend on cause; added capacitors may interact with harmonics | [`electrical-fluke-power-factor`](https://www.fluke.com/en-us/learn/blog/power-quality/improve-power-factor) (improve-power-factor, manufacturer explanation), [`electrical-openstax-rlc`](https://openstax.org/books/university-physics-volume-2/pages/15-3-rlc-series-circuits-with-ac) (§15.3, resonance principle) — not a device-design endorsement |
| E008000-11 | Billing implications vary by actual tariff | [`electrical-fluke-power-factor`](https://www.fluke.com/en-us/learn/blog/power-quality/improve-power-factor) (industry context only); no consumer tariff conclusion verified |
| E008000-12 | Instrument bandwidth and source impedance affect distorted-waveform power measurements | [`electrical-nist-harmonics-measurement`](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=913513) (abstract and discussion), [`electrical-fluke-harmonics`](https://www.fluke.com/en-us/learn/blog/power-quality/installation-harmonics) (different measurement capability) |
| E008000-13 | Symptoms alone cannot identify wiring fault or justify live measurements | [`electrical-fluke-pq-symptoms`](https://www.fluke.com/en-us/learn/blog/power-quality/quick-guide-power-quality-symptom) (multiple possible causes), [`electrical-osha333`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) (occupational work practices, not homeowner prescription) |

**Source scope and outstanding review:** The NIST-hosted publication is a coauthored paper by CSTB and NIST researchers, not a blanket endorsement by NIST or a wiring code. Fluke supplies useful power-quality context but is an instrument vendor and not independent from itself. An electrical engineer should review the harmonics/neutral passages, metrology implications, product constraints and jurisdiction-specific interpretations before publication as field guidance. No live measurements, corrections or installations are instructed.
