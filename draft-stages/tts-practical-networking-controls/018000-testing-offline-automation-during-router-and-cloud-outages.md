# 018000 — Testing Offline Automation During Router and Cloud Outages

<!-- BEGIN SPOKEN LECTURE -->

A door sensor turns on a hall light every evening. The automation looks local because the sensor and the light are in the same house. Yet when the internet connection disappears, the light may stop responding. Or the automation may keep working until the router reboots. These failures tell you something about its hidden dependency graph. To make automation reliable, we need to distinguish radio connectivity, local network services, remote servers, the controller, power, and the controlled device itself.

## Map the real command path

Take one simple action: motion in the hallway should switch on a light. Draw every step that turns the motion into a command. A battery sensor may transmit Zigbee to a local coordinator. A controller reads the state, evaluates a rule, and commands a smart plug over Wi-Fi. The plug then closes a relay. The controller may run on a mini PC. The coordinator may attach by USB. The plug uses the router's wireless access point and a local IP address. A cloud account may be involved only for setup, or it may relay every command. The mobile notification may use another path entirely.

These architectures behave differently. If the internet service provider is unreachable but the router and controller remain up, some systems continue locally. If the router stops, a Zigbee sensor may still reach its coordinator, but the Wi-Fi plug may be unreachable. If the cloud is required for rule execution, the motion event may never become a local command. If the switch requires a cloud login only during initial pairing, the automation may work offline after onboarding but fail when a factory reset forces re-enrollment. 'Works locally' must identify precisely which operations and which operating state it describes.

Create a table of dependencies. Mark each one as required for normal execution, required only for configuration, required for remote access, or required for notifications. Then add a row for each outage. This transforms an ambiguous label like 'cloud free' into an explicit engineering statement.

## Reliability is more than a binary on/off

Suppose a light turns on after a sensor event, but the controller never receives confirmation. Should it retry? Maybe. Repeating an idempotent 'set light on' command normally leaves the light on. Repeating a 'toggle light state' command can turn the light off again. The distinction matters during network delay and recovery. An acknowledgement may mean the command reached the transport layer, not that the physical relay moved or the lamp actually lit.

An automation often needs three separate ideas: the intended state, the observed device state, and the age or quality of the observation. If a temperature sensor last reported an hour ago, displaying its value as current can cause a heater or fan rule to make poor decisions. Stale data should be represented as stale. A safety-critical actuator should have a local fail-safe behavior defined independently of a cloud alert.

Time also matters. If a timer schedules a light to turn off in ten minutes, what happens after a power outage in minute eight? Does it remember the deadline, restart the interval, or immediately run a missed action? A system that stores absolute wall-clock deadlines must handle a wrong clock before time synchronization returns. One that uses only volatile elapsed time must define what a reboot means. You cannot declare a rule reliable just because it works during steady-state network connectivity.

## Design controlled outage tests

Start with a noncritical automation—perhaps a test lamp—and a written expected result. First disconnect only the internet uplink, leaving local networking powered. Trigger the sensor, observe whether the lamp responds, and record the time and event-log entries. Confirm that remote notifications may fail independently of actuation. Restore service and check whether old events get replayed.

Next, separate other dependencies. Turn off the router or access point in a controlled way while keeping the local controller running if possible. Test the sensor path and actuator path. Restart only the controller, then only the actuator. In another test, interrupt power briefly to several components together. Observe startup order: the controller may initialize before DHCP or DNS is ready. A robust program should recover without requiring a person to manually restart a service after each transient network failure.

Keep the experiment small. Do not test failure behavior by disabling a smoke alarm, bypassing a door lock's mechanical fail-safe, or interrupting medical or other life-safety devices. Electrical mains should not be handled by improvising a live test. Choose safe surrogate loads and document what has actually been exercised. Reliability claims should not extend to systems and conditions you did not test.

For each test, capture four times: when the physical event occurred, when the controller recorded it, when a command was sent, and when the actuator changed state. If one timestamp is missing, note what was observable rather than inventing it. A local log can survive an internet outage; a dashboard that depends on remote authentication may not. Logging should remain proportionate to the diagnostic need and protect private event data.

## Recovery exposes hidden design decisions

After connectivity returns, does the system reconcile its state or blindly replay queued actions? Consider an automation that opens a garage door on an event received late. Blind replay would be unacceptable. The event needs an expiry policy and perhaps confirmation of the current physical state. An automation that turns a lamp off after a timeout has a different risk. Define these differences in advance.

Document a recovery procedure: how to verify the controller is running, which service checks establish local connectivity, where logs can be inspected, how device credentials are restored, and what to do if configuration backups are needed. Keep trusted copies of configuration in an appropriate location and verify the recovery rather than assuming a backup file is sufficient. A common failure is having a perfect backup that cannot be used while the identity or password service is offline.

A reliable home-automation system makes its dependencies explicit and exposes enough evidence to explain what happened when something fails. Offline resilience is not a property conferred by one brand or protocol. It is a tested behavior of the complete sensor-to-actuator path and its recovery rules.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Failure matrix.** Rows: internet uplink, router, Wi-Fi AP, controller, Zigbee coordinator, actuator, power, DNS/DHCP, time sync, authentication service. Columns: sensor-to-relay action, schedules, configuration, notifications, restore behavior. Specify expected result before testing.

**Temporal test.** Log event occurrence, controller ingest, command request, actuator acknowledgement and physical state; mark unknown observations as unknown. Test repeated/late commands on a noncritical actuator. 'Set state' and 'toggle' have different retry behavior.

**Recovery record.** Firmware versions, backup date, credentials custody, network layout, local API dependence, access paths during outage, intended fail-safe actuator state, and confirmed restore procedure.

**Limits.** Do not interrupt alarms, locks, medical devices, mains protection or essential loads for classroom exercises. System-level reliability must be verified against actual hardware and software versions; generic protocol capabilities do not guarantee a particular vendor's offline operation.

## Selected reading and source locators (non-spoken)

- `nist-sp80034r1-contingency` — [Marianne Swanson, Pauline Bowen, Amy Phillips, Dean Gallup, and David Lynes, NIST SP 800-34 Revision 1: Contingency Planning Guide for Federal Information Systems (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Dependency analysis, service recovery strategies and validating recovery plans; federal-system context.
- `nist-sp1800-15-iot` — [U.S. National Institute of Standards and Technology NCCoE, NIST SP 1800-15: Securing Small-Business and Home Internet of Things Devices](https://www.nccoe.nist.gov/publication/1800-15/VolB/index.html). Restrict IoT traffic to device-appropriate purposes and apply updates and access controls.
- `ietf-rfc9110-idempotency` — [Roy T. Fielding et al., RFC 9110: HTTP Semantics, Section 9.2.2 (IETF, 2022)](https://www.rfc-editor.org/rfc/rfc9110.html). Idempotent request semantics and when a client may safely retry after a lost response.
- `ietf-rfc5905-ntp` — [David L. Mills, Jim Martin, Jack Burbank and William Kasch, RFC 5905: Network Time Protocol Version 4 (IETF, 2010)](https://www.rfc-editor.org/info/rfc5905/). Time synchronization, offsets, delays and network clock discipline.
