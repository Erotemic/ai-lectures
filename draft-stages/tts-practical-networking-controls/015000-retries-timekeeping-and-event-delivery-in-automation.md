# 015000 — Retries, Timekeeping, and Event Delivery in Automation

<!-- BEGIN SPOKEN LECTURE -->

A motion sensor detects someone at the back door. The automation sends a command to turn on a light. The network drops for two seconds, and the sender cannot tell whether the command arrived. Should it try again? For a light-on command, repeating the request is usually harmless. For a command to open a motorized gate, repeating it might be consequential unless the controller understands what state it is supposed to reach. The difficulty is not simply unreliable Wi-Fi. It is the question of what **a message means when delivery can fail**.

## Sent, received, applied, observed

There are at least four events in a successful automation. A sensor measures something. A controller receives the report. The controller asks an actuator to change. Finally, the physical device reaches—or fails to reach—the requested state. A notification saying 'command sent' confirms only the sender's action. A communication acknowledgment may confirm that a broker or receiver accepted a packet, not that the motor moved or the light actually lit. A closed-loop system needs state feedback when the physical result matters.

Consider a valve. 'Close valve' describes a desired target state. 'Toggle valve' describes an operation whose meaning depends on what happened before. If a retry reaches an actuator twice, two toggles may return the valve to its original state. Two commands to reach the closed state can be safe to repeat if the device interprets them idempotently and has appropriate mechanical protection. When possible, describe desired state rather than an ambiguous relative operation.

## The uncertainty after a lost acknowledgment

Suppose the controller sends a message, and the receiver performs the requested action, but the acknowledgment packet is lost. The sender sees the same timeout it would have seen if the message had never arrived. From the sender's point of view, these two situations are indistinguishable. It has three choices: assume completion, retry, or ask for independent state. Every choice has consequences.

At-most-once handling prefers avoiding duplicates but may lose actions. At-least-once handling retries until delivery is more likely, but the receiver may see duplicates. 'Exactly once' is difficult as an end-to-end physical promise because the communication protocol cannot by itself guarantee that a real actuator applied its side effect exactly one time. Messaging protocols may provide scoped exactly-once delivery semantics within their own session or broker rules; that is not a general transaction spanning a switch, a motor, power loss, and the outside world.

A common mitigation is an event or command identifier. The receiver stores recently processed identifiers, so an identical retry can be recognized. A command also carries its intended target state, an expiration condition where appropriate, and the identity of the sender. The receiver replies with a result tied to that identifier. For especially important actions, a separate sensor confirms the final physical state. This does not eliminate every failure—persistent storage can fail and devices can reboot—but it makes the uncertainty explicit and testable.

## Clock time is not elapsed time

Automation needs two notions of time. Wall-clock time answers 'was this message sent at 8:30 AM?' and can be synchronized to a time service. A monotonic time source answers 'has thirty seconds elapsed?' without being disrupted when the wall clock jumps during synchronization or daylight saving changes. If a timeout or debounce interval is computed from a wall clock, a clock correction can make an event seem to take negative time or much longer than it did.

Timestamps also need context. A sensor may buffer reports while offline and upload them later. The event's occurrence time and the server's receipt time are different. An event with an older occurrence timestamp may still be newly received and actionable; a delayed motion report may instead be stale and should not trigger a new action. Record both when the decision depends on freshness. Synchronization error matters if events from multiple devices are being compared closely; do not infer millisecond ordering from unsynchronized timestamps.

## Debouncing, cooldown, and state machines

Imagine a doorway motion sensor that generates many reports as a person moves. The automation should not restart every timer indefinitely without policy. A simple state machine might have states such as empty, recently active, and occupied. Motion updates a last-seen time; expiration after a chosen interval can transition toward empty. But sensor silence does not prove absence, especially if the sensor or network is offline. A good design distinguishes 'no observation' from 'observed no one'.

Hysteresis helps when a measured quantity fluctuates around a threshold. Instead of turning a fan on at one exact humidity reading and off at the same reading, use separate on and off thresholds. Debouncing helps with rapid repeated transitions; cooldown limits how often a command may be issued. Neither can rescue a dangerous design that treats missing communication as proof of a safe physical state. Safety-relevant controls need a defined local fail-safe behavior independent of cloud services and notification paths.

## Recovery is where correctness becomes visible

Picture a home sensor network after a brief power outage. The router restarts first, a broker restarts next, and battery sensors reconnect at different times. Some devices have retained their state, while others reset. A controller that issues commands before it has reconciled the actual state can turn an actuator the wrong way. A stronger startup routine first discovers device identity and health, reads known state, rejects stale messages, and then calculates what actions are required.

Test the failure modes deliberately on non-hazardous devices. Disconnect the network after a command but before its acknowledgment. Reboot the receiver during an update. Restart the server with an event queue waiting. Compare logs showing event time, receipt time, command ID, desired state, acknowledgment, and observed state. If the log cannot tell whether an action was applied, that is a design gap to address before adding more automation.

The goal is not perfect messaging. The goal is a system whose behavior remains understandable when messages are late, repeated, missing, or out of order. In a reliable automation, the controller does not confuse its intention with the physical world. It continually reconciles the two.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Example event record

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

### Failure-injection exercise

For a harmless test light, exercise (1) duplicate reports, (2) lost acknowledgment, (3) sensor offline, (4) delayed buffered event, (5) server restart, and (6) wall-clock adjustment. Record what the controller *knows* and what it merely *assumes* in each condition.

**Review boundary:** Safety-related motor, door, lock, heating, and valve control require device-specific interlocks and local independent protections; an HTTP/MQTT delivery guarantee is not proof of a safe physical action.

## Selected reading and source locators (non-spoken)

- `ietf-rfc9110-idempotency` — [Roy T. Fielding et al., RFC 9110: HTTP Semantics, Section 9.2.2 (IETF, 2022)](https://www.rfc-editor.org/rfc/rfc9110.html). Idempotent request semantics and when a client may safely retry after a lost response.
- `ietf-rfc5905-ntp` — [David L. Mills, Jim Martin, Jack Burbank and William Kasch, RFC 5905: Network Time Protocol Version 4 (IETF, 2010)](https://www.rfc-editor.org/info/rfc5905/). Time synchronization, offsets, delays and network clock discipline.
- `nist-sp80092-logs` — [Karen Kent (also published as Karen Scarfone) and Murugiah Souppaya, NIST SP 800-92: Guide to Computer Security Log Management (2006)](https://csrc.nist.gov/pubs/sp/800/92/final). Log collection, retention, analysis, and operational processes.
- `omron-control-hysteresis` — [OMRON Industrial Automation, Temperature Controllers FAQ: What Is Hysteresis?](https://www.ia.omron.com/support/faq/answer/53/faq00549/). On/off threshold hysteresis and prevention of rapid relay cycling.
