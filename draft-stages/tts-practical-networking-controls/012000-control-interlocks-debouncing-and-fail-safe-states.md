# 012000 — Control Interlocks, Debouncing, and Fail-Safe States

<!-- BEGIN SPOKEN LECTURE -->

A garage door controller receives a command to close. A sensor reports that something is in the doorway. The software now faces a question far more important than whether the button was pressed correctly: which conditions must be true before motion is permitted, and what should happen if a condition becomes unknown?

This is the practical world of interlocks. An interlock prevents or modifies an action unless required conditions are satisfied. Not every interlock is a safety interlock, and software alone is not sufficient for every safety function. Still, the reasoning applies broadly: motor controls, pumps, lights, heating, doors, valves, and automated tools all need explicit relationships between commands, physical state, and failure conditions.

## Commands and permissions are different things

Imagine a pump that should run when a water-level sensor says the tank is low. A command requests pump operation. Permission asks whether the relevant conditions allow it. Is the outlet valve open? Is a dry-run sensor satisfied? Has an over-temperature alarm occurred? Is the emergency stop active? A robust design treats these as separate inputs to a defined state machine rather than mixing them in an improvised chain of if-statements.

Consider a simple state set: off, ready, running, inhibited, and fault. In the ready state, a valid demand may initiate running. In the inhibited state, demand exists but an unmet condition blocks motion. A fault state records a problem requiring particular recovery actions. Some faults may clear automatically after a condition resolves; others should latch until intentionally acknowledged. The choice depends on consequence, not programmer convenience. Automatically restarting a motor after power returns can be acceptable in one controlled system and dangerous in another.

## Debouncing means deciding what a sensor event represents

A mechanical switch can chatter electrically during physical contact transitions. A software listener may see several rapid edges even though the user pressed the button once. Software debouncing often requires an input to remain stable for a minimum interval before changing the interpreted state. But the appropriate interval depends on the process. Filtering a nuisance door contact for a fraction of a second is different from deliberately delaying recognition of an emergency-stop signal. Safety-critical sensors are designed and evaluated using their applicable requirements, not treated as ordinary noisy inputs.

A slow physical process can also create apparent noise. A water level oscillates around a threshold because of ripples or pump-induced turbulence. Hysteresis solves a different problem: use one threshold to start and another to stop. For example, start draining above a high level and stop below a lower level. The deadband prevents rapid on-off cycling. Debounce manages transient observations; hysteresis manages a range of state transitions. You may need both, but they are not synonyms.

## What should happen on loss of information?

A sensor is absent, a network link drops, or the controller loses its clock. A design that treats every missing value as false may inadvertently create a dangerous permission. A design that treats every missing value as true can be worse. Select explicit representations: known-safe, known-unsafe, unknown, stale, and perhaps uninitialized. The machine's response depends on the physical hazard. On some systems an uncertain state should stop motion; on others stopping suddenly could create additional risk. Fail-safe is an engineering conclusion about the process, not a single universal electrical level.

A common software mistake is to assume that a closed relay implies a running motor, or that issuing an off command proves a valve has closed. A command is intent; a feedback sensor is observation. Feedback can fail too, so compare expected and observed transitions within appropriate timing windows. If a valve is commanded shut but the limit switch never changes state, the controller should record that discrepancy rather than declaring successful closure.

## Local control versus remote convenience

A network dashboard is useful for displaying status, but a home's basic protective control need not depend on an internet service round trip. The local controller can enforce physical conditions while remote software requests actions or receives alerts. This separation helps when the network is unavailable. A notification that a pump has stopped is not itself a pump safety function; communications can fail independently of the mechanical system.

For a door, distinguish the local obstruction response from the mobile app. For a heating loop, distinguish freeze protection from a cloud schedule. For a water shutoff, distinguish the actual position of the valve from the last command shown in the app. Reliable automation names its dependencies, then chooses which functions are allowed to depend on each one.

## Build a state table before code

A useful design exercise is to draw a table with current state, demand, interlock inputs, next state, actuator command, and recorded event. Include startup, power loss, sensor failure, contradictory inputs, stale messages, and restoration. Then test the transitions with a simulator or disconnected actuator first, and verify the hardware response separately. The system should not surprise you when two events occur nearly together.

The deepest idea is that a controller is not merely a machine that follows commands. It is a machine that arbitrates commands against physical reality. A control system becomes dependable when it defines which evidence authorizes an action, how uncertainty is represented, and what state it must reach when things do not proceed as expected.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Example non-safety-critical tank-level controller

| Current state | Demand | High-level switch | Low-level switch | Next state |
|---|---|---|---|---|
| Off | Auto | High | Not low | Running (drain) |
| Running | Auto | Not high | Still above low | Running |
| Running | Auto | Not high | Low reached | Off |
| Any | Any | Contradictory / unavailable | Contradictory / unavailable | Fault or defined inhibited state |

This is illustrative logic, **not** a safety-certified pump control or flood-protection design. Real equipment may have additional faults, manual override, hardware interlocks, latching, and safe-state analysis.

### Design review questions

Define what each input means electrically and physically, acceptable latency, stale data handling, boot state, restoration policy, actuation feedback, and time synchronization. Distinguish signal filtering from the required speed of protective response.

**Editorial boundary:** Functional safety requires hazard analysis, relevant standards and independent hardware design where appropriate. General-purpose home automation and a software debounce routine must not be described as certified personnel protection.

## Selected reading and evidence records (non-spoken)

- `osha-machine-guarding` — [U.S. Occupational Safety and Health Administration, Machine Guarding: Additional Safety Considerations](https://www.osha.gov/etools/machine-guarding/introduction/safety-considerations). Safeguards, machine protection, and separating personnel safety from convenience control.
- `omron-control-hysteresis` — [OMRON Industrial Automation, Temperature Controllers FAQ: What Is Hysteresis?](https://www.ia.omron.com/support/faq/answer/53/faq00549/). On/off threshold hysteresis and prevention of rapid relay cycling.
- `nist-ir8350-iot-onboarding` — [Susan Symington, Blaine Mulugeta, William Polk, Murugiah Souppaya and Jeffrey Marron, NIST IR 8350, Foundational Concepts in Trusted IoT Device Network-Layer Onboarding (2025)](https://csrc.nist.gov/pubs/ir/8350/final). Onboarding functional roles, trust, lifecycle management and credentials.
- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies.
