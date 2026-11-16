# 005000 — Sensors, Actuators, State, and Hysteresis

**Track:** Networking, Sensors, and Local Automation. **Background:** electrical power, network communication, and device reliability. **Purpose:** model automation as a feedback system rather than a collection of on/off gadgets.

<!-- BEGIN SPOKEN LECTURE -->

# A smart switch needs a theory of what is happening

A motion sensor sees movement in a hallway and turns on a light. Thirty seconds later the light goes out while somebody is still standing there. The system did what it was programmed to do, but its program had an inadequate model of the room. A motion event is evidence that somebody moved recently. It is not a direct measurement of continued occupancy. A useful automation must represent the difference between what a sensor observes and what the controller needs to know.

The components of a basic control loop have clear roles. A sensor measures some aspect of the environment. A controller interprets that measurement, retains relevant state, and decides what to do. An actuator changes something in the world: a relay supplies power to a light, a motor opens a valve, or a damper shifts position. Feedback then tells the controller whether the measured condition has changed as expected.

A button-operated switch can be simple because a person supplies the missing judgment. An automatic system has to turn physical observations into decisions under noise, delay, and uncertainty. That is the hard part.

## Measurements are not facts about intent

A passive infrared sensor detects changes in infrared radiation patterns as objects move across its field of view. It may miss somebody sitting motionless. A magnetic contact sensor reports whether a door or window is in one of two positions; it does not say why. A temperature sensor measures temperature at its own location, which may differ from the temperature of the controlled space. A water-leak sensor detects conductivity at its probes; it does not measure every possible leak in the room.

Each sensor has a detection model. We can describe false positives, false negatives, latency, range, sampling frequency, and what environmental conditions affect it. Combining sensors can improve confidence, but only when their limitations are understood. Two motion detectors that share the same blind spot do not provide independent evidence. A door contact and motion sensor report different events; their sequence may be informative, but there are still multiple explanations for a given pattern.

## Control systems need state

Consider a light with three states: OFF, ON_WHILE_ACTIVE, and ON_WAITING. A motion event while OFF changes state to ON_WHILE_ACTIVE and turns on the lamp. If no motion is detected, the controller can move to ON_WAITING and start a dwell interval. New motion resets that interval. The lamp turns off only when the dwell expires and no stronger presence evidence remains. This logic is easier to reason about as a state machine than as a dozen independent triggers.

The waiting interval is not a proof that the room is empty. It is a design choice balancing inconvenience from premature darkness against energy use. A presence sensor capable of detecting smaller movements may justify a different interval. A manually pressed override should usually have an explicit rule rather than fighting the automatic controller every few seconds.

Retained state can be lost on reboot, and distributed events can arrive late or out of order. If a controller restarts, what should the light do? Should the last commanded setting be restored, the physical relay state be read, or the system enter a known safe state? Those choices depend on the device. A pump controller must treat uncertain state differently from a decorative light. Local control also means that loss of internet connectivity need not prevent a device from performing the core function, provided sensing, logic, and actuation are local.

## Why a thermostat needs two thresholds

Suppose heating switches on whenever measured temperature drops below twenty degrees and off whenever it rises above twenty. If the sensor noise is a few tenths of a degree, the measured value may bounce around the threshold. The relay can chatter, cycling rapidly even though the room has scarcely changed.

Hysteresis solves this by separating the switch-on and switch-off thresholds. For example, a heating controller might switch on below nineteen-point-five degrees and switch off above twenty-point-five. Between those values it retains its prior state. That creates a memory of which direction the system was moving. A cooling controller uses the complementary logic: switch on above an upper threshold and off below a lower one. Threshold choice reflects sensor quality, physical system response time, comfort requirements, and equipment constraints.

Hysteresis is not just for temperature. A sump pump uses different water levels to start and stop. A battery charger has upper and lower state thresholds. An alert that turns on at one humidity value and clears at a slightly different value avoids flooding the user with alternating notifications. The principle is broadly reusable: if measurements fluctuate near a decision boundary, use state and separated thresholds instead of a single exact comparison.

## Commanded does not mean accomplished

Imagine a valve actuator commanded to open. The controller sends the command, receives an acknowledgment over a network, and marks the valve open. But the motor may have stalled, the gear may have slipped, or the valve may be mechanically stuck. The network acknowledgment proves that a message was received, not that water now flows. A limit switch, position sensor, or flow measurement can provide independent evidence, each with its own failure modes.

This leads to an important automation design discipline: distinguish desired state, commanded state, reported device state, and observed physical effect. For a lamp, checking electrical power may be sufficient for many uses, but it does not prove the bulb emits light. For a heating system, thermostat readings lag the actual actuator response. Good control design includes timeouts, plausible operating ranges, and sensible behavior when evidence is missing.

## Design around a failure, not a dashboard

Take a simple basement water alarm. A wet probe sends an event to a controller, which notifies someone and perhaps shuts an appropriate valve. The design questions are not primarily about the color of a dashboard button. What if power is lost? What if the sensor cable is disconnected? Can the controller tell 'dry' from 'not reporting'? Does the valve close when communication fails? Could a false trigger cause another significant harm? Where is the manual override? When and how is the system tested?

An automation that is easy to explain in terms of states, inputs, outputs, and failure behavior is easier to maintain and troubleshoot. Devices are components; the real product is a dependable decision about the physical world.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Example state machine

| Current state | Event | Next state | Output |
|---|---|---|---|
| OFF | motion | ON_ACTIVE | light on |
| ON_ACTIVE | inactivity begins | ON_WAITING | light on; start dwell timer |
| ON_WAITING | motion | ON_ACTIVE | light on; cancel dwell |
| ON_WAITING | dwell elapsed | OFF | light off |

A real system requires explicit clock semantics, startup/restart behavior, idempotent commands, manual override, sensor-unavailable state, and documented priority among rules. Consider a monotonic clock for local dwell timing where available, rather than assuming wall-clock time cannot jump.

### Hysteresis example

Heating: turn on at `T < 19.5 C`, turn off at `T > 20.5 C`, otherwise retain prior state. The gap is illustrative; actual equipment control must follow manufacturer limits, minimum run/off times and sensor accuracy requirements. Distinguish threshold hysteresis from time-based debounce and minimum-run timers.

## Selected reading and claim sources (non-spoken)

- `omron-control-hysteresis` — [OMRON Industrial Automation, Temperature Controllers FAQ: What Is Hysteresis?](https://www.ia.omron.com/support/faq/answer/53/faq00549/). On/off threshold hysteresis and prevention of rapid relay cycling.
