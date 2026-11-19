# 006000 — A Voltage That Keeps Changing: AC, Frequency, Phase, and RMS

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Background:** voltage, current and resistive circuit laws. **Practice boundary:** calculations, diagrams, recorded waveforms, or software simulation only; never use household sockets as teaching test points.

<!-- BEGIN SPOKEN LECTURE -->

# A Voltage That Keeps Changing: AC, Frequency, Phase, and RMS

A number printed on an appliance might say one hundred and twenty volts. If you imagine a steady electrical pressure of that size, you have a useful first approximation for some energy calculations. But if that appliance uses an ordinary alternating-current supply, the voltage is not sitting at one hundred and twenty volts. It changes with time. In a familiar North American example, it reaches positive and negative peaks of roughly one hundred and seventy volts, passing through zero repeatedly. And yet the supply is described as one hundred and twenty volts.

That is not a contradiction. It is a question about what the number means.

The moment a quantity varies, we need to decide whether we are describing it at an instant, its average over time, the size of its peaks, or its capacity to produce heat in a resistance. These are different measurements of the same waveform. Learning to tell them apart will make alternators, generators, inverters, motors, and electronic loads much easier to reason about.

## What alternates?

With a direct-current source, a simple textbook model keeps the polarity of its two terminals fixed, perhaps at a constant voltage. With an alternating-current source, the voltage between two named points changes periodically, and in many systems it reverses sign. If you choose a reference direction for current through a resistor, the current also reverses when the voltage does.

The word alternating is about the variation of electrical quantities. It does not mean that electricity sometimes works and sometimes stops working. An AC heating element can receive energy during the positive and negative halves of a cycle. When both voltage and current reverse in a resistor, their product remains positive. Energy continues to be converted to heat even though the algebraic direction of current changes.

The most familiar waveform is the sine wave: a smooth oscillation that repeats after a fixed interval. The time for one complete repetition is the period. Frequency is the number of periods per second, measured in hertz. A sixty-hertz waveform repeats sixty times each second; its period is about sixteen point seven milliseconds. A fifty-hertz waveform repeats fifty times per second; its period is twenty milliseconds.

These frequencies are examples of supply systems, not a worldwide promise. Regional nominal voltages and frequencies differ; certain equipment generates other frequencies, and electronic converters may deliberately synthesize their own waveforms. The actual supply and the equipment nameplate determine which values apply.

We can write a sine wave as a maximum amplitude multiplied by a sine function of time. You do not need to memorize the symbolic form to hear the structure. A peak sets the scale. The frequency tells you how fast the oscillation repeats. A phase angle tells you where the oscillation is in its cycle relative to a chosen reference.

## Phase is about comparing timing

Imagine two people running on identical circular tracks at identical speeds. If they start together and remain shoulder to shoulder, they are in phase. If one starts a quarter of a lap ahead, their positions have a quarter-cycle offset. The analogy does not mean that electricity is literally orbiting a circle. It gives us a way to compare periodic patterns.

When voltage and current through a pure, ideal resistor vary as matching sinusoids, their peaks and zero crossings line up. They are in phase. This relationship changes in circuits that store energy in electric or magnetic fields. In those circuits, the current may reach a peak before or after the voltage does. We call that a lead or a lag, but we must always say which quantity is leading which and specify the reference sign convention.

There is another complication: not all alternating currents have the shape of a sine wave. A current waveform can contain narrow pulses, flat sections, or other distortions while the supply voltage remains close to sinusoidal. Two waveforms may have the same fundamental frequency and still be poor candidates for describing with just one phase offset. That distinction becomes important for power factor and harmonics.

## Why the average can be zero while the heating is real

Over one complete cycle, a perfect sine wave has an average value of zero. Its positive half cancels its negative half when you use ordinary signed arithmetic. But that average is not a useful measure of how much the waveform heats a resistor. Both positive and negative current make the resistor warm, and resistive heating is proportional to current squared.

So we square the instantaneous quantity, average that square over time, and then take the square root. This produces the root-mean-square value, usually abbreviated RMS. RMS is not a mysterious alternate unit of voltage. It is an operation we apply to a time-varying signal. The answer for voltage is still measured in volts; for current it is still measured in amperes.

For a pure sine wave, RMS is the peak divided by the square root of two. A one-hundred-and-twenty-volt RMS sine wave therefore peaks near one hundred and seventy volts. A two-hundred-and-thirty-volt RMS sine wave peaks near three hundred and twenty-five volts. These are mathematical illustrations for ideal sinusoids, not proof of the actual peak of a particular supply at a particular instant. Real systems can have distortion, transients, and voltage variation.

You can reason in the other direction. If the RMS current in a resistive element is two amperes, it causes the same average resistive heating as two amperes of steady direct current through the same ideal resistance, over the averaging interval. That is why RMS appears in calculations about resistive losses and conductor heating. It does not mean the current remains at two amperes at every instant.

## From voltage and current to power

At any instant, the rate of electrical energy transfer at a pair of terminals is instantaneous voltage multiplied by instantaneous current, with a specified sign convention. The average real power is the time average of that product. For a pure resistor driven by a sine-wave voltage, current is in phase and the average power equals RMS voltage times RMS current.

Now suppose the voltage and current are both sinusoids of the same frequency, but the current is shifted in phase. Their average product includes a cosine of the phase difference. This is the origin of the familiar sinusoidal power-factor expression. Some of the energy transfer can reverse direction within each cycle because electric or magnetic fields store energy and later return it.

A warning about scope belongs here: the formula RMS voltage times RMS current times the cosine of one phase angle applies to a sinusoidal single-frequency model. It is not sufficient for arbitrary distorted current and voltage waveforms. General real power remains the average of instantaneous voltage times instantaneous current, and the overall power factor is the real power divided by the product of total RMS voltage and total RMS current when that denominator is nonzero. We will examine the difference rather than concealing it behind one tidy equation.

## The burden of a waveform on a source

Imagine a purely hypothetical alternating source rated at one hundred and twenty volts RMS supplying a ten-ohm ideal resistor. Ohm's law for that resistor predicts twelve amperes RMS. Its average heating power is one thousand four hundred and forty watts. Both voltage and current have alternating signs, yet the resistor receives positive energy on average. This is a desk calculation, not a safe circuit proposal. The available current, overcurrent protection, wiring method, enclosure, thermal conditions, and appliance rating have not been specified.

What if the source waveform is not sinusoidal? We can still calculate RMS by squaring and averaging the actual waveform. The factor of the square root of two is special to a pure sine wave. Applying that factor blindly to pulse-shaped or clipped waveforms produces wrong results. Likewise, meters differ in how they infer RMS, how broad their frequency response is, and what waveform shapes they can accurately measure. A meter's display is not independent evidence that an installation is safe.

This explains why knowing just a nominal voltage and frequency is not enough to select a component, a connector, or a protective device. Frequency affects the behavior of capacitors, inductors, transformers, and motors. Waveform shape affects heating and power measurement. Peak voltage affects insulation and semiconductor stress. Continuous and temporary ratings answer different questions.

## Where does this waveform come from?

A rotating generator offers one intuitive origin for a sinusoidal voltage. A changing magnetic flux linked with a conductor or coil produces an electromotive force. With suitable geometry and rotation, the result is approximately periodic and sinusoidal. This is part of the physics developed through Faraday's and Lenz's work on electromagnetic induction, now expressed in modern electromagnetic theory.

But not every AC source has moving parts. Inverters use switching electronics to synthesize alternating voltage from a direct-current source. Some create a carefully controlled waveform that is close to a sine wave after filtering; others have markedly different output characteristics. The words 'AC output' do not settle compatibility with a motor, a cooker, a charger, or another inverter. The waveform, rated output, neutral and bonding arrangements, protective behavior, and isolation requirements are all separate questions.

A numerical illustration makes the importance of time clear. At sixty hertz, one complete period is about sixteen point seven milliseconds. If an inverter controller changes its output within a small fraction of that period, the electrical system experiences a transient faster than the nominal cycle. A steady-state average cannot describe everything about such a moment. That does not make averaging useless. It tells us which question the average answers.

## An exercise in seeing rather than touching

Imagine two graphs on paper. The first is a sine wave that peaks at positive ten volts, passes through zero, falls to negative ten, and repeats. The second has the same frequency but is delayed by a quarter cycle. Identify the peak, the period, and the phase difference. Then calculate the RMS value of the first waveform if it is a pure sine. It is about seven point zero seven volts.

Now imagine a third waveform that spends most of the cycle at zero and briefly reaches a high positive current. Its ordinary average might be small, but its RMS can be considerably larger. You do not need to connect a meter to discover that. You can reason from the definition: squaring emphasizes the contributions from large current pulses before averaging.

This simple exercise is a doorway to later questions about rectifiers, switched power supplies, harmonics, and heating. It also offers a useful habit for every nameplate or specification sheet: ask whether the stated number is peak, RMS, average, nominal, continuous, or a transient rating. Those words are not decoration. They identify the physical claim being made.

There is a broader lesson here. Electrical systems can be governed by waveforms that change thousands of times while our senses report steady light, steady warmth, or a smoothly running motor. RMS and phase let us connect those fast variations to measurable behavior. They are tools for understanding the system, not a shortcut around knowing its protective design or local installation requirements.

<!-- END SPOKEN LECTURE -->

## Technical companion — display only

### Signal definitions (voltage and current measured between specified points)

For a periodic waveform of period \(T\):

\[
\overline v=\frac1T\int_0^T v(t)\,dt,\qquad V_{\rm rms}=\sqrt{\frac1T\int_0^T v(t)^2\,dt}.
\]

For a pure sinusoid \(v(t)=V_{\rm pk}\sin(2\pi f t + \alpha)\), \(V_{\rm rms}=V_{\rm pk}/\sqrt2\), \(T=1/f\). For a same-frequency sinusoidal current with phase \(\beta\):

\[
P=\frac1T\int_0^T v(t)i(t)\,dt=V_{\rm rms}I_{\rm rms}\cos(\alpha-\beta).
\]

The **integral definition**, not the cosine shortcut, applies to arbitrary periodic waveforms. A pure 120 V RMS sine has \(V_{\rm pk}\approx169.7\) V. A pure 230 V RMS sine has \(V_{\rm pk}\approx325.3\) V. A 60 Hz period is 16.667 ms; a 50 Hz period is 20 ms. Actual nominal systems and transients are outside this ideal calculation.

### Desk exercise with answer

A perfect 12 V peak, 50 Hz sinusoidal source drives an ideal 6 Ω resistor. Calculate the RMS voltage, RMS current, cycle period and mean power. **Answer:** \(V_{\rm rms}=12/\sqrt2\approx8.485\) V, \(I_{\rm rms}=\sqrt2\approx1.414\) A, \(T=0.020\) s, and \(P=12\) W. Do not construct the example; no source power rating, current limiting, or component thermal rating is specified.

### Crucial distinctions

| Quantity | Question answered | Common confusion |
|---|---|---|
| Instantaneous voltage \(v(t)\) | What is the voltage at this moment? | Confused with nominal voltage |
| Peak magnitude | What is the largest magnitude in the chosen interval? | Assuming always \(\sqrt2\) times RMS |
| RMS | What squared-average magnitude corresponds to resistive heating? | Assuming it is average signed voltage |
| Phase difference | How are two same-frequency periodic signals aligned? | Treating distorted waveforms as one shifted sine |
| Real power | What is the average signed electrical power transfer? | Identifying it with \(V_{rms}I_{rms}\) for all loads |

### Claim-level source map (educational editorial check, 2026-11-15)

| ID | Supported claim | Sources and limitations |
|---|---|---|
| E006000-01 | AC waveforms vary in time; frequency and phase are distinct parameters | [`electrical-openstax-ac-sources`](https://openstax.org/books/university-physics-volume-2/pages/15-1-ac-sources) (§15.1) |
| E006000-02 | AC current and voltage can reverse without cancelling resistive heating | [`electrical-openstax-acpower`](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (§15.4), [`electrical-openstax-power`](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (§9.5) |
| E006000-03 | Regional 50/60 Hz examples are not worldwide defaults | [`electrical-openstax-ac-sources`](https://openstax.org/books/university-physics-volume-2/pages/15-1-ac-sources) (§15.1, illustrative examples) |
| E006000-04 | RMS is the square root of a time mean of a squared waveform | [`electrical-openstax-ac-circuits`](https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits) (§15.2), [`electrical-openstax-acpower`](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (§15.4) |
| E006000-05 | Pure sine RMS is peak divided by square root of two | [`electrical-openstax-ac-circuits`](https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits) (§15.2), [`electrical-openstax-acpower`](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (§15.4) |
| E006000-06 | Phase difference of sinusoids yields cosine term in mean real power | [`electrical-openstax-acpower`](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (§15.4), [`electrical-mit-6002-course`](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) (energy and sinusoidal lectures outline) |
| E006000-07 | General real power is time-average of instantaneous VI | [`electrical-openstax-acpower`](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (§15.4); nonlinear waveform corroboration required, extended in lecture 008000 |
| E006000-08 | Inductors/capacitors shift sinusoidal current relative to voltage | [`electrical-openstax-ac-circuits`](https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits) (§15.2), [`electrical-openstax-rlc`](https://openstax.org/books/university-physics-volume-2/pages/15-3-rlc-series-circuits-with-ac) (§15.3) |
| E006000-09 | Non-sinusoidal waveforms need general RMS, not sine-only peak conversion | [`electrical-openstax-ac-circuits`](https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits) (§15.2: sine assumption explicitly), [`electrical-nist-harmonics-measurement`](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=913513) (§3: RMS and waveform measurement issues) |
| E006000-10 | Meters, inverters and installation hardware require separate specifications | [`electrical-nist-harmonics-measurement`](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=913513) (measurement bandwidth findings), [`electrical-osha304`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) (workplace installation scope only); no equipment-specific claim verified |

**Safety and professional-review boundary:** These are source-grounded waveform calculations. Never infer permission to measure an outlet, to probe a panel, or to connect an inverter from them. Specific device types, utility conditions, normative clauses and workplace procedures are not analyzed here. Independent qualified review remains pending.
