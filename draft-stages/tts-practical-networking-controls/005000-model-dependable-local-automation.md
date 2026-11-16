# Model dependable local automation

<!-- BEGIN SPOKEN LECTURE -->

# Model dependable local automation

## Sensors, Actuators, State, and Hysteresis

A motion sensor sees movement in a hallway and turns on a light. Thirty seconds later the light goes out while somebody is still standing there. The system did what it was programmed to do, but its program had an inadequate model of the room. A motion event is evidence that somebody moved recently. It is not a direct measurement of continued occupancy. A useful automation must represent the difference between what a sensor observes and what the controller needs to know.

The components of a basic control loop have clear roles. A sensor measures some aspect of the environment. A controller interprets that measurement, retains relevant state, and decides what to do. An actuator changes something in the world: a relay supplies power to a light, a motor opens a valve, or a damper shifts position. Feedback then tells the controller whether the measured condition has changed as expected.

A button-operated switch can be simple because a person supplies the missing judgment. An automatic system has to turn physical observations into decisions under noise, delay, and uncertainty. That is the hard part.

### Measurements are not facts about intent

A passive infrared sensor detects changes in infrared radiation patterns as objects move across its field of view. It may miss somebody sitting motionless. A magnetic contact sensor reports whether a door or window is in one of two positions; it does not say why. A temperature sensor measures temperature at its own location, which may differ from the temperature of the controlled space. A water-leak sensor detects conductivity at its probes; it does not measure every possible leak in the room.

Each sensor has a detection model. We can describe false positives, false negatives, latency, range, sampling frequency, and what environmental conditions affect it. Combining sensors can improve confidence, but only when their limitations are understood. Two motion detectors that share the same blind spot do not provide independent evidence. A door contact and motion sensor report different events; their sequence may be informative, but there are still multiple explanations for a given pattern.

### Control systems need state

Consider a light with three states: OFF, ON_WHILE_ACTIVE, and ON_WAITING. A motion event while OFF changes state to ON_WHILE_ACTIVE and turns on the lamp. If no motion is detected, the controller can move to ON_WAITING and start a dwell interval. New motion resets that interval. The lamp turns off only when the dwell expires and no stronger presence evidence remains. This logic is easier to reason about as a state machine than as a dozen independent triggers.

The waiting interval is not a proof that the room is empty. It is a design choice balancing inconvenience from premature darkness against energy use. A presence sensor capable of detecting smaller movements may justify a different interval. A manually pressed override should usually have an explicit rule rather than fighting the automatic controller every few seconds.

Retained state can be lost on reboot, and distributed events can arrive late or out of order. If a controller restarts, what should the light do? Should the last commanded setting be restored, the physical relay state be read, or the system enter a known safe state? Those choices depend on the device. A pump controller must treat uncertain state differently from a decorative light. Local control also means that loss of internet connectivity need not prevent a device from performing the core function, provided sensing, logic, and actuation are local.

### Why a thermostat needs two thresholds

Suppose heating switches on whenever measured temperature drops below twenty degrees and off whenever it rises above twenty. If the sensor noise is a few tenths of a degree, the measured value may bounce around the threshold. The relay can chatter, cycling rapidly even though the room has scarcely changed.

Hysteresis solves this by separating the switch-on and switch-off thresholds. For example, a heating controller might switch on below nineteen-point-five degrees and switch off above twenty-point-five. Between those values it retains its prior state. That creates a memory of which direction the system was moving. A cooling controller uses the complementary logic: switch on above an upper threshold and off below a lower one. Threshold choice reflects sensor quality, physical system response time, comfort requirements, and equipment constraints.

Hysteresis is not just for temperature. A sump pump uses different water levels to start and stop. A battery charger has upper and lower state thresholds. An alert that turns on at one humidity value and clears at a slightly different value avoids flooding the user with alternating notifications. The principle is broadly reusable: if measurements fluctuate near a decision boundary, use state and separated thresholds instead of a single exact comparison.

### Commanded does not mean accomplished

Imagine a valve actuator commanded to open. The controller sends the command, receives an acknowledgment over a network, and marks the valve open. But the motor may have stalled, the gear may have slipped, or the valve may be mechanically stuck. The network acknowledgment proves that a message was received, not that water now flows. A limit switch, position sensor, or flow measurement can provide independent evidence, each with its own failure modes.

This leads to an important automation design discipline: distinguish desired state, commanded state, reported device state, and observed physical effect. For a lamp, checking electrical power may be sufficient for many uses, but it does not prove the bulb emits light. For a heating system, thermostat readings lag the actual actuator response. Good control design includes timeouts, plausible operating ranges, and sensible behavior when evidence is missing.

### Design around a failure, not a dashboard

Take a simple basement water alarm. A wet probe sends an event to a controller, which notifies someone and perhaps shuts an appropriate valve. The design questions are not primarily about the color of a dashboard button. What if power is lost? What if the sensor cable is disconnected? Can the controller tell 'dry' from 'not reporting'? Does the valve close when communication fails? Could a false trigger cause another significant harm? Where is the manual override? When and how is the system tested?

An automation that is easy to explain in terms of states, inputs, outputs, and failure behavior is easier to maintain and troubleshoot. Devices are components; the real product is a dependable decision about the physical world.

## Reliable Automations as State Machines, Not Chains of Notifications

Return to the hallway light, this time with a failure in its timing logic. A motion report turns on the light. Five seconds later a second motion report arrives, yet an expired timer turns the light off. Nothing is electrically broken. The problem is in the logic: events, states and time were treated as interchangeable.

Many everyday automations are described as rules: when this happens, do that. Rules are useful, but as a system grows, the missing questions become important. What if the event arrives twice? What if it arrives late? What if the network goes away halfway through? What does the actuator do after a reboot? A reliable design answers those questions explicitly.

### An event is not a state

An event says that something happened at a particular moment: motion was detected, a door contact changed, a command was acknowledged. A state describes what we currently believe to be true: occupied, unoccupied, light commanded on, or motor stopped. A retained 'motion detected' message is not evidence of continuous presence. A command acknowledgement is not necessarily evidence that a mechanical actuator reached its target.

Consider a hallway light. There are at least three conceptual states: off, on with recent activity, and on while a manual override is active. When new motion arrives, the activity deadline should extend. A single old timer should not undo a more recent extension. One implementation uses a monotonically increasing deadline; another schedules a timer with a generation number so stale callbacks are ignored. Both make the state transition explicit.

The controls must also define what counts as evidence of absence. A motion sensor can fail to report a motionless person. For a short utility hallway, that may be acceptable with a generous dwell interval. In a room where someone sits quietly, a more robust occupancy model may combine sources or use a different sensor. The desired experience dictates the evidence standard, not the other way around.

### Commands can be duplicated; state transitions must cope

Network messages are not guaranteed to arrive once and only once in every real deployment. Retries are useful precisely because messages or acknowledgements can be lost. But retries can duplicate commands. Turning on a lamp twice is often harmless; sending a one-step-open command to a motor twice may not be. Good design favors idempotent commands—commands that reach the same desired state even if applied more than once—when possible.

Compare 'toggle the lamp' with 'set lamp to on.' If a controller retries a toggle after losing its acknowledgement, the lamp may end up off. A retried explicit 'on' command has a much clearer meaning. Still, stateful physical devices may need command identifiers, observed position and interlocks. A smart lock, gate or powered door has safety requirements beyond a light switch; a status message cannot replace sensing and safety-rated controls.

Message ordering is another trap. An old 'off' command may arrive after a newer 'on.' Using an event timestamp alone is insufficient if clocks are wrong or unsynchronized. The controller may instead maintain a sequence number, generation number or desired-state version. The device and controller need a documented rule for rejecting obsolete actions. That rule is part of the protocol, not a mysterious filter added after a failure.

### Make failures visible and bounded

A robust controller can be modeled with states such as idle, command pending, confirmed, timeout and fault. If the controller sends 'turn on' and receives no confirmation, it should not silently assume success. It can retry a bounded number of times, report a fault, and follow a defined fallback policy. Infinite fast retries can overload a recovering network and mask the real problem.

The difference between a safety policy and a convenience policy matters. For a night light, failure to turn on may be a minor inconvenience and a fallback can be simple. For a sump alarm or a door actuator, the behavior after loss of power or communication needs explicit engineering and perhaps independent hardware protection. Software automation is not a substitute for safety-critical physical design.

Now add a router outage. Local sensors and switches may still be reachable on a functioning local link, but cloud notifications disappear. A system that relies on an external identity provider even to issue local commands might stop responding altogether. Test the real dependency graph. Disconnect the internet while keeping the local network up; then test a router reboot, device reboot, and a cold power restoration separately. They exercise different failure paths.

### Model time as data

Automation bugs frequently appear at boundaries: a motion event at the exact moment a timeout fires, daylight-saving changes, delayed messages, or device clocks starting at the wrong date. Use monotonic time for elapsed intervals where the runtime supports it. Wall-clock time is needed for schedules such as 'at sunset,' but it should not be mistaken for a reliable elapsed-time counter. A recorded event needs both interpretation and enough context to diagnose clock quality.

For a presence-controlled light, the algorithm might be: on each valid presence report, record the present monotonic time plus the desired dwell duration. Periodically, if no override is active and the current monotonic time exceeds the latest stored deadline, request off. Notice the word 'latest.' An older timeout does not win simply because it was scheduled first.

### Test traces, not just the happy path

Write a small table of synthetic events before deploying. Motion at zero seconds. Motion again at nine seconds. A timer from the first motion at ten. A device acknowledgement delayed to twelve. Router loss at fifteen. Controller restart at twenty. For each event, define the expected state and output. If the answer depends on an unspoken assumption, the design is incomplete.

Logs should show event origin, receipt time, desired state version, command ID, device acknowledgement and observed state when available. They should not indiscriminately expose private occupancy schedules or secrets. A trace lets you answer whether an unwanted off transition was caused by a stale timer, a contradictory sensor report, a manual override or an actuator problem.

The larger lesson is that local-first automation is not merely automation without the cloud. Reliability emerges when the controller has a coherent state model, bounded timeouts, safe transitions and evidence that the physical world reached the requested condition. Once those are explicit, a complex automation becomes something you can reason about rather than a sequence of surprising callbacks.

## Control Interlocks, Debouncing, and Fail-Safe States

An explicit state model also makes it possible to ask which transitions must be blocked or made safe.

A garage door controller receives a command to close. A sensor reports that something is in the doorway. The software now faces a question far more important than whether the button was pressed correctly: which conditions must be true before motion is permitted, and what should happen if a condition becomes unknown?

This is the practical world of interlocks. An interlock prevents or modifies an action unless required conditions are satisfied. Not every interlock is a safety interlock, and software alone is not sufficient for every safety function. Still, the reasoning applies broadly: motor controls, pumps, lights, heating, doors, valves, and automated tools all need explicit relationships between commands, physical state, and failure conditions.

### Commands and permissions are different things

Imagine a pump that should run when a water-level sensor says the tank is low. A command requests pump operation. Permission asks whether the relevant conditions allow it. Is the outlet valve open? Is a dry-run sensor satisfied? Has an over-temperature alarm occurred? Is the emergency stop active? A robust design treats these as separate inputs to a defined state machine rather than mixing them in an improvised chain of if-statements.

Consider a simple state set: off, ready, running, inhibited, and fault. In the ready state, a valid demand may initiate running. In the inhibited state, demand exists but an unmet condition blocks motion. A fault state records a problem requiring particular recovery actions. Some faults may clear automatically after a condition resolves; others should latch until intentionally acknowledged. The choice depends on consequence, not programmer convenience. Automatically restarting a motor after power returns can be acceptable in one controlled system and dangerous in another.

### Debouncing means deciding what a sensor event represents

A mechanical switch can chatter electrically during physical contact transitions. A software listener may see several rapid edges even though the user pressed the button once. Software debouncing often requires an input to remain stable for a minimum interval before changing the interpreted state. But the appropriate interval depends on the process. Filtering a nuisance door contact for a fraction of a second is different from deliberately delaying recognition of an emergency-stop signal. Safety-critical sensors are designed and evaluated using their applicable requirements, not treated as ordinary noisy inputs.

A slow physical process can also create apparent noise. A water level oscillates around a threshold because of ripples or pump-induced turbulence. Hysteresis solves a different problem: use one threshold to start and another to stop. For example, start draining above a high level and stop below a lower level. The deadband prevents rapid on-off cycling. Debounce manages transient observations; hysteresis manages a range of state transitions. You may need both, but they are not synonyms.

### What should happen on loss of information?

A sensor is absent, a network link drops, or the controller loses its clock. A design that treats every missing value as false may inadvertently create a dangerous permission. A design that treats every missing value as true can be worse. Select explicit representations: known-safe, known-unsafe, unknown, stale, and perhaps uninitialized. The machine's response depends on the physical hazard. On some systems an uncertain state should stop motion; on others stopping suddenly could create additional risk. Fail-safe is an engineering conclusion about the process, not a single universal electrical level.

A common software mistake is to assume that a closed relay implies a running motor, or that issuing an off command proves a valve has closed. A command is intent; a feedback sensor is observation. Feedback can fail too, so compare expected and observed transitions within appropriate timing windows. If a valve is commanded shut but the limit switch never changes state, the controller should record that discrepancy rather than declaring successful closure.

### Local control versus remote convenience

A network dashboard is useful for displaying status, but a home's basic protective control need not depend on an internet service round trip. The local controller can enforce physical conditions while remote software requests actions or receives alerts. This separation helps when the network is unavailable. A notification that a pump has stopped is not itself a pump safety function; communications can fail independently of the mechanical system.

For a door, distinguish the local obstruction response from the mobile app. For a heating loop, distinguish freeze protection from a cloud schedule. For a water shutoff, distinguish the actual position of the valve from the last command shown in the app. Reliable automation names its dependencies, then chooses which functions are allowed to depend on each one.

### Build a state table before code

A useful design exercise is to draw a table with current state, demand, interlock inputs, next state, actuator command, and recorded event. Include startup, power loss, sensor failure, contradictory inputs, stale messages, and restoration. Then test the transitions with a simulator or disconnected actuator first, and verify the hardware response separately. The system should not surprise you when two events occur nearly together.

The deepest idea is that a controller is not merely a machine that follows commands. It is a machine that arbitrates commands against physical reality. A control system becomes dependable when it defines which evidence authorizes an action, how uncertainty is represented, and what state it must reach when things do not proceed as expected.

## Retries, Timekeeping, and Event Delivery in Automation

Timing, retries, and delivery guarantees determine how that model behaves when events do not arrive just once and in order.

A motion sensor detects someone at the back door. The automation sends a command to turn on a light. The network drops for two seconds, and the sender cannot tell whether the command arrived. Should it try again? For a light-on command, repeating the request is usually harmless. For a command to open a motorized gate, repeating it might be consequential unless the controller understands what state it is supposed to reach. The difficulty is not simply unreliable Wi-Fi. It is the question of what **a message means when delivery can fail**.

### Sent, received, applied, observed

There are at least four events in a successful automation. A sensor measures something. A controller receives the report. The controller asks an actuator to change. Finally, the physical device reaches—or fails to reach—the requested state. A notification saying 'command sent' confirms only the sender's action. A communication acknowledgment may confirm that a broker or receiver accepted a packet, not that the motor moved or the light actually lit. A closed-loop system needs state feedback when the physical result matters.

Consider a valve. 'Close valve' describes a desired target state. 'Toggle valve' describes an operation whose meaning depends on what happened before. If a retry reaches an actuator twice, two toggles may return the valve to its original state. Two commands to reach the closed state can be safe to repeat if the device interprets them idempotently and has appropriate mechanical protection. When possible, describe desired state rather than an ambiguous relative operation.

### The uncertainty after a lost acknowledgment

Suppose the controller sends a message, and the receiver performs the requested action, but the acknowledgment packet is lost. The sender sees the same timeout it would have seen if the message had never arrived. From the sender's point of view, these two situations are indistinguishable. It has three choices: assume completion, retry, or ask for independent state. Every choice has consequences.

At-most-once handling prefers avoiding duplicates but may lose actions. At-least-once handling retries until delivery is more likely, but the receiver may see duplicates. 'Exactly once' is difficult as an end-to-end physical promise because the communication protocol cannot by itself guarantee that a real actuator applied its side effect exactly one time. Messaging protocols may provide scoped exactly-once delivery semantics within their own session or broker rules; that is not a general transaction spanning a switch, a motor, power loss, and the outside world.

A common mitigation is an event or command identifier. The receiver stores recently processed identifiers, so an identical retry can be recognized. A command also carries its intended target state, an expiration condition where appropriate, and the identity of the sender. The receiver replies with a result tied to that identifier. For especially important actions, a separate sensor confirms the final physical state. This does not eliminate every failure—persistent storage can fail and devices can reboot—but it makes the uncertainty explicit and testable.

### Clock time is not elapsed time

Automation needs two notions of time. Wall-clock time answers 'was this message sent at 8:30 AM?' and can be synchronized to a time service. A monotonic time source answers 'has thirty seconds elapsed?' without being disrupted when the wall clock jumps during synchronization or daylight saving changes. If a timeout or debounce interval is computed from a wall clock, a clock correction can make an event seem to take negative time or much longer than it did.

Timestamps also need context. A sensor may buffer reports while offline and upload them later. The event's occurrence time and the server's receipt time are different. An event with an older occurrence timestamp may still be newly received and actionable; a delayed motion report may instead be stale and should not trigger a new action. Record both when the decision depends on freshness. Synchronization error matters if events from multiple devices are being compared closely; do not infer millisecond ordering from unsynchronized timestamps.

### Debouncing, cooldown, and state machines

Imagine a doorway motion sensor that generates many reports as a person moves. The automation should not restart every timer indefinitely without policy. A simple state machine might have states such as empty, recently active, and occupied. Motion updates a last-seen time; expiration after a chosen interval can transition toward empty. But sensor silence does not prove absence, especially if the sensor or network is offline. A good design distinguishes 'no observation' from 'observed no one'.

Hysteresis helps when a measured quantity fluctuates around a threshold. Instead of turning a fan on at one exact humidity reading and off at the same reading, use separate on and off thresholds. Debouncing helps with rapid repeated transitions; cooldown limits how often a command may be issued. Neither can rescue a dangerous design that treats missing communication as proof of a safe physical state. Safety-relevant controls need a defined local fail-safe behavior independent of cloud services and notification paths.

### Recovery is where correctness becomes visible

Picture a home sensor network after a brief power outage. The router restarts first, a broker restarts next, and battery sensors reconnect at different times. Some devices have retained their state, while others reset. A controller that issues commands before it has reconciled the actual state can turn an actuator the wrong way. A stronger startup routine first discovers device identity and health, reads known state, rejects stale messages, and then calculates what actions are required.

Test the failure modes deliberately on non-hazardous devices. Disconnect the network after a command but before its acknowledgment. Reboot the receiver during an update. Restart the server with an event queue waiting. Compare logs showing event time, receipt time, command ID, desired state, acknowledgment, and observed state. If the log cannot tell whether an action was applied, that is a design gap to address before adding more automation.

The goal is not perfect messaging. The goal is a system whose behavior remains understandable when messages are late, repeated, missing, or out of order. In a reliable automation, the controller does not confuse its intention with the physical world. It continually reconciles the two.

## Testing Offline Automation During Router and Cloud Outages

An outage is a useful test of whether the automation depends on the physical state or on an assumed chain of notifications.

A door sensor turns on a hall light every evening. The automation looks local because the sensor and the light are in the same house. Yet when the internet connection disappears, the light may stop responding. Or the automation may keep working until the router reboots. These failures tell you something about its hidden dependency graph. To make automation reliable, we need to distinguish radio connectivity, local network services, remote servers, the controller, power, and the controlled device itself.

### Map the real command path

Take one simple action: motion in the hallway should switch on a light. Draw every step that turns the motion into a command. A battery sensor may transmit Zigbee to a local coordinator. A controller reads the state, evaluates a rule, and commands a smart plug over Wi-Fi. The plug then closes a relay. The controller may run on a mini PC. The coordinator may attach by USB. The plug uses the router's wireless access point and a local IP address. A cloud account may be involved only for setup, or it may relay every command. The mobile notification may use another path entirely.

These architectures behave differently. If the internet service provider is unreachable but the router and controller remain up, some systems continue locally. If the router stops, a Zigbee sensor may still reach its coordinator, but the Wi-Fi plug may be unreachable. If the cloud is required for rule execution, the motion event may never become a local command. If the switch requires a cloud login only during initial pairing, the automation may work offline after onboarding but fail when a factory reset forces re-enrollment. 'Works locally' must identify precisely which operations and which operating state it describes.

Create a table of dependencies. Mark each one as required for normal execution, required only for configuration, required for remote access, or required for notifications. Then add a row for each outage. This transforms an ambiguous label like 'cloud free' into an explicit engineering statement.

### Reliability is more than a binary on/off

Suppose a light turns on after a sensor event, but the controller never receives confirmation. Should it retry? Maybe. Repeating an idempotent 'set light on' command normally leaves the light on. Repeating a 'toggle light state' command can turn the light off again. The distinction matters during network delay and recovery. An acknowledgement may mean the command reached the transport layer, not that the physical relay moved or the lamp actually lit.

An automation often needs three separate ideas: the intended state, the observed device state, and the age or quality of the observation. If a temperature sensor last reported an hour ago, displaying its value as current can cause a heater or fan rule to make poor decisions. Stale data should be represented as stale. A safety-critical actuator should have a local fail-safe behavior defined independently of a cloud alert.

Time also matters. If a timer schedules a light to turn off in ten minutes, what happens after a power outage in minute eight? Does it remember the deadline, restart the interval, or immediately run a missed action? A system that stores absolute wall-clock deadlines must handle a wrong clock before time synchronization returns. One that uses only volatile elapsed time must define what a reboot means. You cannot declare a rule reliable just because it works during steady-state network connectivity.

### Design controlled outage tests

Start with a noncritical automation—perhaps a test lamp—and a written expected result. First disconnect only the internet uplink, leaving local networking powered. Trigger the sensor, observe whether the lamp responds, and record the time and event-log entries. Confirm that remote notifications may fail independently of actuation. Restore service and check whether old events get replayed.

Next, separate other dependencies. Turn off the router or access point in a controlled way while keeping the local controller running if possible. Test the sensor path and actuator path. Restart only the controller, then only the actuator. In another test, interrupt power briefly to several components together. Observe startup order: the controller may initialize before DHCP or DNS is ready. A robust program should recover without requiring a person to manually restart a service after each transient network failure.

Keep the experiment small. Do not test failure behavior by disabling a smoke alarm, bypassing a door lock's mechanical fail-safe, or interrupting medical or other life-safety devices. Electrical mains should not be handled by improvising a live test. Choose safe surrogate loads and document what has actually been exercised. Reliability claims should not extend to systems and conditions you did not test.

For each test, capture four times: when the physical event occurred, when the controller recorded it, when a command was sent, and when the actuator changed state. If one timestamp is missing, note what was observable rather than inventing it. A local log can survive an internet outage; a dashboard that depends on remote authentication may not. Logging should remain proportionate to the diagnostic need and protect private event data.

### Recovery exposes hidden design decisions

After connectivity returns, does the system reconcile its state or blindly replay queued actions? Consider an automation that opens a garage door on an event received late. Blind replay would be unacceptable. The event needs an expiry policy and perhaps confirmation of the current physical state. An automation that turns a lamp off after a timeout has a different risk. Define these differences in advance.

Document a recovery procedure: how to verify the controller is running, which service checks establish local connectivity, where logs can be inspected, how device credentials are restored, and what to do if configuration backups are needed. Keep trusted copies of configuration in an appropriate location and verify the recovery rather than assuming a backup file is sufficient. A common failure is having a perfect backup that cannot be used while the identity or password service is offline.

A reliable home-automation system makes its dependencies explicit and exposes enough evidence to explain what happened when something fails. Offline resilience is not a property conferred by one brand or protocol. It is a tested behavior of the complete sensor-to-actuator path and its recovery rules.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Sensors, Actuators, State, and Hysteresis

**Track:** Networking, Sensors, and Local Automation. **Background:** electrical power, network communication, and device reliability. **Purpose:** model automation as a feedback system rather than a collection of on/off gadgets.

#### Technical companion (non-spoken)

##### Example state machine

| Current state | Event | Next state | Output |
|---|---|---|---|
| OFF | motion | ON_ACTIVE | light on |
| ON_ACTIVE | inactivity begins | ON_WAITING | light on; start dwell timer |
| ON_WAITING | motion | ON_ACTIVE | light on; cancel dwell |
| ON_WAITING | dwell elapsed | OFF | light off |

A real system requires explicit clock semantics, startup/restart behavior, idempotent commands, manual override, sensor-unavailable state, and documented priority among rules. Consider a monotonic clock for local dwell timing where available, rather than assuming wall-clock time cannot jump.

##### Hysteresis example

Heating: turn on at `T < 19.5 C`, turn off at `T > 20.5 C`, otherwise retain prior state. The gap is illustrative; actual equipment control must follow manufacturer limits, minimum run/off times and sensor accuracy requirements. Distinguish threshold hysteresis from time-based debounce and minimum-run timers.

#### Selected reading and claim sources (non-spoken)

- `omron-control-hysteresis` — [OMRON Industrial Automation, Temperature Controllers FAQ: What Is Hysteresis?](https://www.ia.omron.com/support/faq/answer/53/faq00549/). On/off threshold hysteresis and prevention of rapid relay cycling.

### Reliable Automations as State Machines, Not Chains of Notifications

### 019000 — Reliable Automations as State Machines, Not Chains of Notifications

#### Technical companion (non-spoken)

**State machine exercise.** Draw `OFF`, `ON_OCCUPIED`, `ON_MANUAL_OVERRIDE` and `FAULT`. Label transitions triggered by presence, timeout, override, missing confirmation and restart. Specify what is persisted, reconstructed or invalidated on boot.

**Failure matrix.** Duplicate event, stale event, out-of-order event, dropped command, missing acknowledgement, sensor disconnect, local router restart, external internet failure, device reboot, and clock correction. Define expected output and observable log evidence for each.

**Boundaries.** Use direct desired-state commands where supported; idempotence needs protocol-level semantics, not just an optimistic client. Physical safety interlocks and code requirements cannot be implemented as best-effort cloud rules. Protect credentials and minimize behavioral logging.

**References.** IETF RFC 9110 on idempotent request semantics; NIST SP 800-34 on contingency planning; NIST SP 800-92 on event logging; Omron control hysteresis technical reference.

### Control Interlocks, Debouncing, and Fail-Safe States

### 012000 — Control Interlocks, Debouncing, and Fail-Safe States

#### Technical companion (non-spoken)

##### Example non-safety-critical tank-level controller

| Current state | Demand | High-level switch | Low-level switch | Next state |
|---|---|---|---|---|
| Off | Auto | High | Not low | Running (drain) |
| Running | Auto | Not high | Still above low | Running |
| Running | Auto | Not high | Low reached | Off |
| Any | Any | Contradictory / unavailable | Contradictory / unavailable | Fault or defined inhibited state |

This is illustrative logic, **not** a safety-certified pump control or flood-protection design. Real equipment may have additional faults, manual override, hardware interlocks, latching, and safe-state analysis.

##### Design review questions

Define what each input means electrically and physically, acceptable latency, stale data handling, boot state, restoration policy, actuation feedback, and time synchronization. Distinguish signal filtering from the required speed of protective response.

**Editorial boundary:** Functional safety requires hazard analysis, relevant standards and independent hardware design where appropriate. General-purpose home automation and a software debounce routine must not be described as certified personnel protection.

#### Selected reading and evidence records (non-spoken)

- `osha-machine-guarding` — [U.S. Occupational Safety and Health Administration, Machine Guarding: Additional Safety Considerations](https://www.osha.gov/etools/machine-guarding/introduction/safety-considerations). Safeguards, machine protection, and separating personnel safety from convenience control.
- `omron-control-hysteresis` — [OMRON Industrial Automation, Temperature Controllers FAQ: What Is Hysteresis?](https://www.ia.omron.com/support/faq/answer/53/faq00549/). On/off threshold hysteresis and prevention of rapid relay cycling.
- `nist-ir8350-iot-onboarding` — [Susan Symington, Blaine Mulugeta, William Polk, Murugiah Souppaya and Jeffrey Marron, NIST IR 8350, Foundational Concepts in Trusted IoT Device Network-Layer Onboarding (2025)](https://csrc.nist.gov/pubs/ir/8350/final). Onboarding functional roles, trust, lifecycle management and credentials.
- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies.

### Retries, Timekeeping, and Event Delivery in Automation

### 015000 — Retries, Timekeeping, and Event Delivery in Automation

#### Technical companion (non-spoken)

##### Example event record

```json
{
  "event_id": "sensor-A/boot-52/seq-104",
  "source": "hall-motion",
  "event_time_utc": "2026-11-15T20:01:04Z",
  "received_time_utc": "2026-11-15T20:01:08Z",
  "observed_state": "motion_detected",
  "source_status": "healthy"
}
```

Keep unique command IDs and desired state separately from reports of physical state. `event_time` may be wrong if the source clock is not synchronized; the receiver timestamp is not an occurrence timestamp.

##### Failure-injection exercise

For a harmless test light, exercise (1) duplicate reports, (2) lost acknowledgment, (3) sensor offline, (4) delayed buffered event, (5) server restart, and (6) wall-clock adjustment. Record what the controller *knows* and what it merely *assumes* in each condition.

**Review boundary:** Safety-related motor, door, lock, heating, and valve control require device-specific interlocks and local independent protections; an HTTP/MQTT delivery guarantee is not proof of a safe physical action.

#### Selected reading and source locators (non-spoken)

- `ietf-rfc9110-idempotency` — [Roy T. Fielding et al., RFC 9110: HTTP Semantics, Section 9.2.2 (IETF, 2022)](https://www.rfc-editor.org/rfc/rfc9110.html). Idempotent request semantics and when a client may safely retry after a lost response.
- `ietf-rfc5905-ntp` — [David L. Mills, Jim Martin, Jack Burbank and William Kasch, RFC 5905: Network Time Protocol Version 4 (IETF, 2010)](https://www.rfc-editor.org/info/rfc5905/). Time synchronization, offsets, delays and network clock discipline.
- `nist-sp80092-logs` — [Karen Kent (also published as Karen Scarfone) and Murugiah Souppaya, NIST SP 800-92: Guide to Computer Security Log Management (2006)](https://csrc.nist.gov/pubs/sp/800/92/final). Log collection, retention, analysis, and operational processes.
- `omron-control-hysteresis` — [OMRON Industrial Automation, Temperature Controllers FAQ: What Is Hysteresis?](https://www.ia.omron.com/support/faq/answer/53/faq00549/). On/off threshold hysteresis and prevention of rapid relay cycling.

### Testing Offline Automation During Router and Cloud Outages

### 018000 — Testing Offline Automation During Router and Cloud Outages

#### Technical companion (non-spoken)

**Failure matrix.** Rows: internet uplink, router, Wi-Fi AP, controller, Zigbee coordinator, actuator, power, DNS/DHCP, time sync, authentication service. Columns: sensor-to-relay action, schedules, configuration, notifications, restore behavior. Specify expected result before testing.

**Temporal test.** Log event occurrence, controller ingest, command request, actuator acknowledgement and physical state; mark unknown observations as unknown. Test repeated/late commands on a noncritical actuator. 'Set state' and 'toggle' have different retry behavior.

**Recovery record.** Firmware versions, backup date, credentials custody, network layout, local API dependence, access paths during outage, intended fail-safe actuator state, and confirmed restore procedure.

**Limits.** Do not interrupt alarms, locks, medical devices, mains protection or essential loads for classroom exercises. System-level reliability must be verified against actual hardware and software versions; generic protocol capabilities do not guarantee a particular vendor's offline operation.

#### Selected reading and source locators (non-spoken)

- `nist-sp80034r1-contingency` — [Marianne Swanson, Pauline Bowen, Amy Phillips, Dean Gallup, and David Lynes, NIST SP 800-34 Revision 1: Contingency Planning Guide for Federal Information Systems (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Dependency analysis, service recovery strategies and validating recovery plans; federal-system context.
- `nist-sp1800-15-iot` — [U.S. National Institute of Standards and Technology NCCoE, NIST SP 1800-15: Securing Small-Business and Home Internet of Things Devices](https://www.nccoe.nist.gov/publication/1800-15/VolB/index.html). Restrict IoT traffic to device-appropriate purposes and apply updates and access controls.
- `ietf-rfc9110-idempotency` — [Roy T. Fielding et al., RFC 9110: HTTP Semantics, Section 9.2.2 (IETF, 2022)](https://www.rfc-editor.org/rfc/rfc9110.html). Idempotent request semantics and when a client may safely retry after a lost response.
- `ietf-rfc5905-ntp` — [David L. Mills, Jim Martin, Jack Burbank and William Kasch, RFC 5905: Network Time Protocol Version 4 (IETF, 2010)](https://www.rfc-editor.org/info/rfc5905/). Time synchronization, offsets, delays and network clock discipline.
