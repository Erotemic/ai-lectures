# 019000 — Reliable Automations as State Machines, Not Chains of Notifications

<!-- BEGIN SPOKEN LECTURE -->

A motion sensor reports movement. An automation turns on a light. Five seconds later a second motion report arrives, and the automation turns the light off because one delayed timer has expired. Nothing is electrically broken. The problem is in the logic: events, states and time were treated as interchangeable.

Many everyday automations are described as rules: when this happens, do that. Rules are useful, but as a system grows, the missing questions become important. What if the event arrives twice? What if it arrives late? What if the network goes away halfway through? What does the actuator do after a reboot? A reliable design answers those questions explicitly.

## An event is not a state

An event says that something happened at a particular moment: motion was detected, a door contact changed, a command was acknowledged. A state describes what we currently believe to be true: occupied, unoccupied, light commanded on, or motor stopped. A retained 'motion detected' message is not evidence of continuous presence. A command acknowledgement is not necessarily evidence that a mechanical actuator reached its target.

Consider a hallway light. There are at least three conceptual states: off, on with recent activity, and on while a manual override is active. When new motion arrives, the activity deadline should extend. A single old timer should not undo a more recent extension. One implementation uses a monotonically increasing deadline; another schedules a timer with a generation number so stale callbacks are ignored. Both make the state transition explicit.

The controls must also define what counts as evidence of absence. A motion sensor can fail to report a motionless person. For a short utility hallway, that may be acceptable with a generous dwell interval. In a room where someone sits quietly, a more robust occupancy model may combine sources or use a different sensor. The desired experience dictates the evidence standard, not the other way around.

## Commands can be duplicated; state transitions must cope

Network messages are not guaranteed to arrive once and only once in every real deployment. Retries are useful precisely because messages or acknowledgements can be lost. But retries can duplicate commands. Turning on a lamp twice is often harmless; sending a one-step-open command to a motor twice may not be. Good design favors idempotent commands—commands that reach the same desired state even if applied more than once—when possible.

Compare 'toggle the lamp' with 'set lamp to on.' If a controller retries a toggle after losing its acknowledgement, the lamp may end up off. A retried explicit 'on' command has a much clearer meaning. Still, stateful physical devices may need command identifiers, observed position and interlocks. A smart lock, gate or powered door has safety requirements beyond a light switch; a status message cannot replace sensing and safety-rated controls.

Message ordering is another trap. An old 'off' command may arrive after a newer 'on.' Using an event timestamp alone is insufficient if clocks are wrong or unsynchronized. The controller may instead maintain a sequence number, generation number or desired-state version. The device and controller need a documented rule for rejecting obsolete actions. That rule is part of the protocol, not a mysterious filter added after a failure.

## Make failures visible and bounded

A robust controller can be modeled with states such as idle, command pending, confirmed, timeout and fault. If the controller sends 'turn on' and receives no confirmation, it should not silently assume success. It can retry a bounded number of times, report a fault, and follow a defined fallback policy. Infinite fast retries can overload a recovering network and mask the real problem.

The difference between a safety policy and a convenience policy matters. For a night light, failure to turn on may be a minor inconvenience and a fallback can be simple. For a sump alarm or a door actuator, the behavior after loss of power or communication needs explicit engineering and perhaps independent hardware protection. Software automation is not a substitute for safety-critical physical design.

Now add a router outage. Local sensors and switches may still be reachable on a functioning local link, but cloud notifications disappear. A system that relies on an external identity provider even to issue local commands might stop responding altogether. Test the real dependency graph. Disconnect the internet while keeping the local network up; then test a router reboot, device reboot, and a cold power restoration separately. They exercise different failure paths.

## Model time as data

Automation bugs frequently appear at boundaries: a motion event at the exact moment a timeout fires, daylight-saving changes, delayed messages, or device clocks starting at the wrong date. Use monotonic time for elapsed intervals where the runtime supports it. Wall-clock time is needed for schedules such as 'at sunset,' but it should not be mistaken for a reliable elapsed-time counter. A recorded event needs both interpretation and enough context to diagnose clock quality.

For a presence-controlled light, the algorithm might be: on each valid presence report, record the present monotonic time plus the desired dwell duration. Periodically, if no override is active and the current monotonic time exceeds the latest stored deadline, request off. Notice the word 'latest.' An older timeout does not win simply because it was scheduled first.

## Test traces, not just the happy path

Write a small table of synthetic events before deploying. Motion at zero seconds. Motion again at nine seconds. A timer from the first motion at ten. A device acknowledgement delayed to twelve. Router loss at fifteen. Controller restart at twenty. For each event, define the expected state and output. If the answer depends on an unspoken assumption, the design is incomplete.

Logs should show event origin, receipt time, desired state version, command ID, device acknowledgement and observed state when available. They should not indiscriminately expose private occupancy schedules or secrets. A trace lets you answer whether an unwanted off transition was caused by a stale timer, a contradictory sensor report, a manual override or an actuator problem.

The larger lesson is that local-first automation is not merely automation without the cloud. Reliability emerges when the controller has a coherent state model, bounded timeouts, safe transitions and evidence that the physical world reached the requested condition. Once those are explicit, a complex automation becomes something you can reason about rather than a sequence of surprising callbacks.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**State machine exercise.** Draw `OFF`, `ON_OCCUPIED`, `ON_MANUAL_OVERRIDE` and `FAULT`. Label transitions triggered by presence, timeout, override, missing confirmation and restart. Specify what is persisted, reconstructed or invalidated on boot.

**Failure matrix.** Duplicate event, stale event, out-of-order event, dropped command, missing acknowledgement, sensor disconnect, local router restart, external internet failure, device reboot, and clock correction. Define expected output and observable log evidence for each.

**Boundaries.** Use direct desired-state commands where supported; idempotence needs protocol-level semantics, not just an optimistic client. Physical safety interlocks and code requirements cannot be implemented as best-effort cloud rules. Protect credentials and minimize behavioral logging.

**References.** IETF RFC 9110 on idempotent request semantics; NIST SP 800-34 on contingency planning; NIST SP 800-92 on event logging; Omron control hysteresis technical reference.
