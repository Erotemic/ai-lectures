# 036000 - Motors: Why Starting Is Different from Running

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** nameplates, speed-torque graphs, supply-impedance models, starter and protective-device functional drawings.

<!-- BEGIN SPOKEN LECTURE -->

# Motors: Why Starting Is Different from Running

A pump starts, and the lights in a nearby room dip briefly. The pump then runs smoothly for several minutes, with no visible effect on the lighting. Why does a machine demand so much from its electrical supply for the first few moments, then settle into ordinary operation?

An electric motor is not simply a resistance with a wattage printed on it. It converts electromagnetic energy into mechanical motion. While the shaft accelerates, currents, magnetic fields and mechanical load interact. When the machine is stationary, a motor can draw substantially more current than it draws once it is moving near its operating speed. The exact behavior depends on the motor design and the mechanism it drives.

Understanding that difference is the key to reading motor nameplates, interpreting startup voltage dips, choosing control strategies and understanding why a motor circuit usually needs several distinct protective functions.

## Mechanical work has its own vocabulary

Mechanical power is torque multiplied by angular speed. Torque describes the turning effort at a shaft; angular speed describes how quickly the shaft rotates. A motor supplying high torque at low speed can deliver different mechanical power from the same motor running quickly with little torque. The motor's electrical input supplies the mechanical output plus losses, which appear mainly as heat and, to a lesser extent, sound and other effects.

A motor's efficiency therefore concerns a ratio: mechanical output power divided by electrical input real power at a specified operating point. It is not the same as power factor. Power factor compares real electrical power to apparent electrical power and describes the relationship between supply voltage and current, including reactive and distorted components. An induction motor can be mechanically efficient while still imposing a significant reactive current demand on the supply.

This distinction helps interpret a common nameplate trap. A rating in horsepower or kilowatts often describes *shaft output*, not the watts drawn from the outlet or feeder. A one-horsepower shaft rating is approximately seven hundred forty-six watts of mechanical power. If the motor were eighty percent efficient at a particular operating point, it would require about nine hundred thirty-three watts of electrical real input. To estimate alternating-current supply current, one must also know voltage, phase arrangement and power factor. Even then, the calculation is only an operating-point estimate; the exact nameplate and manufacturer data govern the actual machine.

## The rotating field and the meaning of slip

In a three-phase induction motor, the stator windings produce a rotating magnetic field. That field induces currents in the rotor conductors. Interaction of the currents and field produces torque. For induction to continue, the rotor normally turns at a speed slightly different from the rotating field. The difference is called *slip*.

The field's synchronous speed is determined by supply frequency and the number of magnetic poles. For an idealized four-pole machine on sixty hertz, the synchronous speed is eighteen hundred revolutions per minute. An induction motor under load may run somewhat below that value, such as seventeen hundred fifty revolutions per minute, because it needs slip to produce torque. That is a constructed illustration, not a promised nameplate speed for every motor of that type.

At a standstill, slip is greatest. The electromagnetic situation is different from normal running, and across-the-line starting can draw several times rated full-load current. Schneider Electric's published motor-starter guide describes roughly six to seven times full-load current as a common order of magnitude for certain direct-on-line induction motors. It is not a universal multiplier. Motor design, supply conditions and the driven machine change the actual curve.

A single-phase induction motor has a different starting problem: one simple sinusoidal winding alone does not create the same freely rotating field as a balanced three-phase supply. Practical designs use arrangements such as auxiliary windings, capacitors or other starting mechanisms to establish starting torque. Compressors, fans and pumps may use very different constructions. Some modern appliances instead use electronically commutated or permanent-magnet motors with an integrated drive. Their startup characteristics cannot be inferred from the traditional across-the-line model.

## Why the lights can dip

The supply is not an ideal zero-impedance voltage source. A transformer, feeder, connections and other parts of the route have impedance. If motor current increases sharply during startup, the same impedance produces a larger voltage drop. For a deliberately simplified resistance-only model, imagine a source path with point one ohm of effective resistance. A current increase of forty amperes produces about four volts of additional drop. Real AC systems have reactive components and changing current waveforms, so a four-volt result from this model is a teaching illustration rather than a prediction at a particular panel.

A voltage dip may be most visible in lighting because some lamps react to relatively small supply variations. A brief dip synchronized with a compressor starting is evidence about the timing of a load event. It is not, by itself, a diagnosis of an undersized utility service or a defective motor. One would want to know the starting current, duration, equipment ratings, supply impedance, other simultaneous loads and whether the observed behavior has changed over time.

There are two separate questions: how much current flows as the motor starts, and how long the motor remains in that high-current state. Starting a lightly loaded fan may be different from starting a pump against a particular hydraulic condition or a compressor against a pressure difference. Acceleration depends on the motor's available torque minus the torque required by the load. If that difference is small, acceleration can take longer and thermal stress can increase, even if the peak current is not the largest in a comparison.

## Protection is a collection of different jobs

Motor circuits need protection from short circuits and ground faults. They also need consideration of overheating from sustained overload or failure to start. A motor controller decides when the machine should run, stop or change speed. A disconnecting means provides an intended separation of the motor and control equipment from its supply. These functions may be combined in particular products, but the design questions are distinct.

A conventional branch overcurrent device is not automatically a complete motor-overload protection system. A motor may draw excessive current for a period shorter or lower than the region in which a branch breaker would operate suitably. Conversely, an ordinary starting surge may be acceptable for the motor, even though it looks much larger than the running current. Protection therefore considers both the winding's thermal capability and the motor's legitimate starting characteristic.

The U.S. OSHA workplace text explicitly distinguishes overload and failure-to-start protection from short-circuit and ground-fault protection for motor circuits. That is a useful engineering separation regardless of the exact country's rules. It does not imply a single universal setting for a motor overload device. The protection needs the actual motor, load, operating duty and manufacturer information.

Thermal overload systems may estimate or measure motor heating and stop the machine when operating conditions threaten its windings. Other controls monitor phase loss, excessive temperature, speed or other conditions. Some mechanical systems need special treatment because a sudden stop can introduce an even greater hazard. Protection design is a system decision, not a contest to make a breaker trip on the smallest possible current.

## Three ways to start a motor

An across-the-line starter applies the supply directly to a motor designed for that use. It is simple, but its starting current and mechanical acceleration can stress the supply and the driven equipment.

A reduced-voltage soft starter controls the applied voltage during acceleration to change the starting current and torque profile. Reducing voltage can also reduce available motor torque, so a soft starter is not a promise that every motor will start every mechanical load. The equipment must reach running speed under the actual load conditions.

A variable-frequency drive is a different tool. A common drive rectifies incoming power, uses a DC link and synthesizes a controlled output waveform. By varying frequency and voltage, it can manage motor speed and torque over a range of operating conditions. For fans and pumps, operating at a lower speed can sometimes reduce energy consumption dramatically; the benefit depends on the mechanical system and control objective. Drive harmonics, cable effects, motor cooling at low speed and electromagnetic compatibility may introduce additional engineering questions.

A modern inverter-driven compressor illustrates why older rules of thumb cannot be applied indiscriminately. Its current profile and mechanical behavior can be quite different from an old contactor-started unit. A nameplate or data sheet should tell you what the manufacturer actually designed, not merely whether the word *compressor* appears on the casing.

## Read a nameplate as a compact description of the machine

When reviewing a motor, begin with rated voltage, frequency, number of phases, output power, full-load current and speed. Next look for duty, insulation or temperature information, enclosure or environmental rating, efficiency, power factor where given, and the control or protection requirements. Labels such as service factor or locked-rotor code belong to particular rating systems and need the applicable definition. They should not be treated as free permission to run any load above a nameplate value.

Suppose a hypothetical three-phase motor produces three kilowatts of shaft power. At eighty-eight percent efficiency it consumes about three point four one kilowatts of electrical real power. With a power factor of zero point eight four, its apparent power would be about four point zero six kilovolt-amperes. On a balanced four-hundred-volt three-phase line-to-line supply, the ideal current calculation gives about five point eight six amperes. That is a useful consistency check. It does not predict locked-rotor current, heating during startup, or the appropriate protective settings.

## Diagnose the machine, not just the breaker

Imagine a compressor that starts reliably in mild weather but occasionally stops during a demanding operating period. There are multiple plausible stories. It may face a different pressure load. A supply connection may have changed. The motor may overheat. A starting component may be deteriorating. A control may be responding to a sensor. A protective device may be operating exactly as intended—or reacting to an incompatible starting profile.

A diagnostic plan separates these hypotheses by the evidence they predict: event timing, ambient conditions, nameplate data, controller fault history, other load behavior and appropriately obtained electrical and mechanical measurements. Replacing a breaker with a larger one because the machine stops is not a diagnosis. It changes a protective assumption without explaining the failure.

The motor is a particularly instructive electrical load because it forces us to link electricity to mechanics and time. The current during acceleration, the torque required by the load, the power factor during running, the heat accumulated in windings and the response of protection all matter. Once those are treated as separate but interacting variables, a flickering light or a difficult start becomes an engineering question that can be investigated rather than guessed at.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Synchronous speed and slip

For a motor with `p` poles supplied at frequency `f` in hertz, the ideal rotating-field speed is `n_s = 120f/p` rpm. For `f = 60 Hz`, `p = 4`, `n_s = 1800 rpm`. At a hypothetical loaded speed `n = 1750 rpm`, the slip fraction is `(n_s - n)/n_s ≈ 0.0278`, or about 2.78%.

These formulas describe a conventional induction-motor concept, not an inverter-driven motor's fixed operating speed.

### Three-phase shaft-power thought experiment

`P_out = 3000 W`, `η = 0.88`, `PF = 0.84`, balanced `V_LL = 400 V`.

- `P_in = P_out/η = 3409.09 W`
- `S = P_in/PF = 4058.44 VA`
- `I_line = P_in/(√3 × V_LL × PF) ≈ 5.86 A`

No motor has been selected by this model; a real nameplate and rated conditions are needed.

### Conceptual protection functions

| Function | What it addresses | What it does not alone establish |
|---|---|---|
| Branch fault interruption | Short-circuit and ground-fault interruption within device rating | Accurate motor-winding thermal protection |
| Motor overload protection | Excess current/heat over a time-dependent duty | Short-circuit interrupting capacity of supply device |
| Contactor/controller | Intended start/stop and, possibly, direction | Safe isolation unless rated for that purpose |
| Disconnect | Intended supply isolation for motor/controller | Thermal overload control |
| Drive/soft starter | Start or speed behavior | Automatically correct protective device or installation ratings |

### Exercises (desk)

1. From a hypothetical motor nameplate, distinguish shaft output, real input, apparent input, power factor, speed and locked-rotor information. List which quantities are missing before judging starting behavior.
2. Plot a qualitative motor torque-versus-speed curve and a load torque-versus-speed curve. Identify where the shaft accelerates and where a stable operating point might occur.
3. Given a motor startup light dip and an event history, develop three competing hypotheses and the observations that would distinguish them. Do not change a protective-device rating as an experiment.

### Limits and counterexamples

- Six or seven times full-load current is a characteristic of some across-the-line induction motors, not all motors or all controllers.
- Slip and synchronous speed describe specific motor topologies; electronic drives can change applied frequency.
- Motor rated mechanical output is not equal to electrical input watts or volt-amperes.
- Lower startup current does not guarantee sufficient acceleration torque.
- Branch fault protection, motor overload protection, controller and isolator are not synonyms.
- OSHA motor requirements apply to the U.S. workplace scope; actual products and regional codes differ.

## Claim-level source map

| Claim ID | Consequential statement | Source and location | Boundaries |
|---|---|---|---|
| E036000-01 | Direct-on-line induction motors can exhibit high starting current compared with full-load running | [electrical-se-motor-starters](https://www.electrical-installation.org/enwiki/Motor_starter_configurations) (DOL starting, 6–7x example); [electrical-se-asynchronous-motors](https://www.electrical-installation.org/enwiki/Asynchronous_motors) (starting constraints) | Both are same-publisher engineering material, not independent empirical confirmation for a specific motor |
| E036000-02 | Starting current interacting with source impedance can produce voltage drop | [electrical-se-asynchronous-motors](https://www.electrical-installation.org/enwiki/Asynchronous_motors) (startup voltage drop); [electrical-openstax-ohm](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) (§9.4 voltage/resistance/current) | Simple 0.1 Ω example ignores reactance and dynamic source behavior |
| E036000-03 | Motor overload/failure-to-start protection and fault protection are distinct requirements | [electrical-osha305](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.305) (§1910.305(j)(4)(vii), primary U.S. workplace regulation); [electrical-se-asynchronous-motors](https://www.electrical-installation.org/enwiki/Asynchronous_motors) (motor starter protection context) | No model-specific settings, breaker choice or jurisdictional installation advice inferred |
| E036000-04 | Motor disconnect and controller serve different roles | [electrical-osha305](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.305) (§1910.305(j)(4)(ii)–(vi), disconnect requirements); [electrical-se-motor-starters](https://www.electrical-installation.org/enwiki/Motor_starter_configurations) (controller strategies) | Workplace normative scope and exact product ratings require review |
| E036000-05 | Soft starting and variable frequency drives alter acceleration/current/control behavior | [electrical-se-motor-starters](https://www.electrical-installation.org/enwiki/Motor_starter_configurations) (DOL, soft starter and VFD descriptions); [electrical-doe-motor-guide](https://www.energy.gov/sites/default/files/2014/04/f15/mc-0382.pdf) (motor selection and starting context, independent DOE guide) | Exact savings, harmonics or motor compatibility need model-specific study |
| E036000-06 | Motor output power, efficiency and power factor must be distinguished | [electrical-openstax-acpower](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (§15.4 real/apparent power); [electrical-doe-motor-guide](https://www.energy.gov/sites/default/files/2014/04/f15/mc-0382.pdf) (mechanical output and energy-efficient motors) | Sample numbers hypothetical, not nameplate ratings |
| E036000-07 | Motor nameplate/rated operating point cannot independently predict startup behavior | [electrical-doe-motor-guide](https://www.energy.gov/sites/default/files/2014/04/f15/mc-0382.pdf) (nameplate information and inrush); [electrical-se-motor-starters](https://www.electrical-installation.org/enwiki/Motor_starter_configurations) (starting modes) | Motor type, load and source conditions are required |
| E036000-08 | Motor slip and rotating field yield a relationship between frequency, pole count and synchronous speed | [electrical-iowa-motor-speed](https://iastate.pressbooks.pub/electriccircuits/chapter/motor-characteristics/) (Applied Industrial Electricity, motor characteristics, rotating-field speed); [electrical-doe-motor-theory](https://www.energy.gov/documents/doe-hdbk-1011-92vol4) (DOE electrical-science motor theory, synchronous speed/slip) | Ideal field speed is not measured rotor speed; nameplate speed and motor type must be considered |
