# 010000 — Logs, Time Synchronization, and Reliable Alerts

<!-- BEGIN SPOKEN LECTURE -->

At three in the morning, a home automation controller reports that a basement water sensor was dry at three oh five, wet at three oh seven, and dry again at three oh four. The sequence is impossible if the timestamps all mean the same thing. Perhaps the sensor sent delayed messages, the controller's clock changed, the events came from separate devices, or the stored records were sorted by a time field with the wrong meaning. A log is useful only when we know what an event record actually represents.

## An event and an observation are not the same thing

A sensor may detect a change at one moment, transmit it later, and have it recorded still later. Imagine a wireless device that wakes, measures water, retries transmission twice, and finally reaches a hub. It might contain a device timestamp, a message sequence number, and a hub reception time. Those fields answer different questions. A device timestamp claims when measurement occurred according to that device's clock. Reception time says when the collector learned about it. The two may differ even when every component is working correctly.

A log entry should make those distinctions legible. It may need a device identity, event type, value and units, time source, quality or confidence flag, and the state that the automation entered. Without them, a line saying 'sensor changed' carries too little information to diagnose anything. For troubleshooting, a unique event identifier or increasing sequence number can also help detect duplicate delivery and missing messages.

## Clocks need a common language

Most computer systems represent civil time as an instant relative to a time standard, then display it in a chosen time zone. Coordinated Universal Time, or U T C, is a useful common frame for storing cross-device event timestamps. Local clock time can repeat during the autumn daylight-saving change or jump forward during the spring change. Two events both labeled one fifteen in the morning may be an hour apart, while a wall clock can skip a time that never occurred locally.

Network Time Protocol, originally developed by David Mills and other contributors and specified in I E T F standards, helps synchronize device clocks with reference time. Synchronization does not make every inexpensive sensor clock perfect. Devices drift, lose connectivity, reboot with an incorrect default, or step their clocks after receiving a time correction. A timestamp generated before synchronization should not be assumed reliable merely because later entries look good.

Wall-clock time is also different from elapsed time. A timer that controls a pump or checks whether a sensor has been silent for ten minutes should use an elapsed-time clock where possible, not subtract local displayed clock readings. When daylight saving starts or N T P makes an adjustment, elapsed time should continue to measure duration. This difference between a wall clock and a monotonic clock is foundational to reliable automation.

## Logs must preserve causality where possible

Suppose a heater controller receives a thermostat request, enables a relay, then detects that the expected temperature rise did not happen. A useful record includes the requested action, relay command, observed feedback, and final state. Logging only the command produces an optimistic story: 'heater on.' It does not show whether power reached the heater or heat was delivered. A careful automation distinguishes intent from observation.

Sequence numbers and correlation identifiers help connect a command to its acknowledgement or sensor reading. But distributed systems have no magic universally correct event ordering unless their design supplies one. Two devices may report different events with overlapping timestamp uncertainty. For diagnosis, it is better to state that the ordering cannot be established than to invent a precise chronology from clocks that were never synchronized.

Retries create another important trap. A sensor might resend a message after it hears no acknowledgement. The receiver may therefore see the same event twice. Counting every received message as a separate water alarm can exaggerate a problem. If commands are retried, repeating an action may be harmless for setting a light to an absolute state but dangerous for a toggle action that flips it on and off. Idempotent commands and event de-duplication are engineering tools for managing this.

## Alerts need a policy, not just a threshold

An alert is a decision that some observation deserves a human response. A bare threshold can become noisy. A humidity sensor reporting forty-nine point nine percent one moment and fifty point one the next might generate a stream of on-off notifications. Hysteresis separates the threshold for entering the alarm state from the threshold for leaving it. For example, an alert could begin after humidity remains above a chosen high level for a specified duration and clear only after it drops below a lower level. The thresholds are application choices, not universal humidity safety values.

Debouncing rejects brief transitions that are expected from mechanical contacts or noisy signals. Rate limiting prevents endless repeats of the same message. Escalation changes what happens when a severe condition persists or a first notification is not acknowledged. A critical flood alarm should not be suppressed forever by a rule intended to prevent nuisance notifications. Likewise, a missing sensor message can be an alertable event in its own right: silence may indicate lost battery, wireless failure, or controller outage.

The alert path can fail even when the sensor and local controller work. If a notification depends on cloud servers, internet access, push gateways, a phone battery, and user attention, then all of those are dependencies. A local siren or local shutoff mechanism can sometimes reduce dependence on remote delivery, but only if designed and tested appropriately. For any consequential control, identify what still works when the internet, the hub, or its clock is unavailable.

## Keep evidence without keeping everything forever

Logs consume storage and may reveal when people are home, which doors opened, or which rooms were occupied. A useful policy says what data to record, how long to retain it, how to protect it, and who can read it. Overwriting the only log during a fault destroys evidence. Keeping private sensor histories indefinitely without purpose creates another kind of risk. A rolling operational log, separate critical incident record, and deliberate retention period can be better than an unstructured archive.

A good test does not merely press the alarm's demonstration button. It induces safe representative sensor states, checks what was logged, verifies timestamps and delivery, disconnects a dependency if appropriate, and confirms what an operator actually sees. The alert is part of an observed chain, not just a configured rule.

When a time sequence looks impossible, do not first assume the physics is wrong. Ask which device measured, which device recorded, what each clock knew, and whether delivery was delayed or duplicated. Reliable monitoring is an exercise in preserving meaning across imperfect machines.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Event schema example

```json
{
  "event_id": "sensor-a-4172",
  "device_id": "sump-water-sensor-a",
  "sequence": 4172,
  "observed_state": "wet",
  "device_utc": "2026-11-15T08:07:11Z",
  "collector_utc": "2026-11-15T08:07:18Z",
  "clock_quality": "device-clock-unsynchronized",
  "collector_state": "alarm-pending"
}
```

- Distinguish UTC wall time from elapsed/monotonic time; record clock quality and timezone offset where useful.
- An alert pipeline includes sensor, transport, collector, rule, notification service, recipient, and acknowledgment. Test failure modes at each boundary.
- Use idempotent state-setting commands or event de-duplication for retries; a toggle can be unsafe on replay.
- Hysteresis, debounce windows, missing-heartbeat checks, and escalation thresholds are different mechanisms.

### Test exercise

Simulate a sensor sequence `dry, wet, wet, dry` with a repeated message ID, a delayed transport delivery, and a clock jump. Decide which fields preserve the event sequence and which cannot establish physical order.

### Review boundary

RFC 5905 specifies NTP version 4; deployment security and newer updates must be assessed separately. NIST log-management guidance addresses retention and operational processes but does not prescribe one universal household log format or retention period.

## Selected reading and evidence records (non-spoken)

- `ietf-rfc5905-ntp` — [David L. Mills, Jim Martin, Jack Burbank and William Kasch, RFC 5905: Network Time Protocol Version 4 (IETF, 2010)](https://www.rfc-editor.org/info/rfc5905/). Time synchronization, offsets, delays and network clock discipline
- `nist-sp80092-logs` — [Karen Kent (also published as Karen Scarfone) and Murugiah Souppaya, NIST SP 800-92: Guide to Computer Security Log Management (2006)](https://csrc.nist.gov/pubs/sp/800/92/final). Log collection, retention, analysis, and operational processes
- `omron-control-hysteresis` — [OMRON Industrial Automation, Temperature Controllers FAQ: What Is Hysteresis?](https://www.ia.omron.com/support/faq/answer/53/faq00549/). On/off threshold hysteresis and prevention of rapid relay cycling
