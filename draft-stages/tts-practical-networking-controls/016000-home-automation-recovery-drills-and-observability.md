# 016000 — Home Automation Recovery Drills and Observability

<!-- BEGIN SPOKEN LECTURE -->

A power outage ends. The lights return, the router boots, and the wall switch works. Yet the motion-triggered hallway light does not come on, and the door sensor appears 'online' even though its battery died two days ago. This is a familiar kind of system failure: all the pieces appear present, but the chain of events that was supposed to connect them is broken. Recovery testing and observability are ways to discover that break before an urgent situation depends on the automation.

## A service is a chain of dependencies

Imagine a local sensor that reports motion over a wireless network. An access point receives the event, a controller interprets it, a rule decides whether to turn on a lamp, and an actuator switches power. The dashboard shows the result. There may also be a router, address assignment, name resolution, time synchronization, and a database storing device state. A single user-facing action depends on several machines and several kinds of state.

Write the chain on paper. The physical sensor has a power source. The access point has its own supply and network uplink. The controller may run on a computer or appliance that takes longer to restart than the router. The output relay may restore its previous state, default off, or choose a configured state after power returns. These choices matter. A lighting relay that returns on may be mildly inconvenient; a heater, valve, or motor that returns on without confirming prerequisites can be dangerous.

Recovery behavior is not identical to startup behavior. If components boot in a different order, a device may fail to reconnect or may keep a stale address. A controller may initially have no valid time, making scheduled events ambiguous. A cloud service may be unreachable while local devices remain fully capable of operating. A robust local-first design should distinguish a connection needed for actuation from a connection used only for remote notification or management.

## Separate three kinds of evidence

An automation log often says 'command sent.' That does not mean the actuator received the command. An acknowledgment from a device does not prove the connected mechanism moved. A reported state may itself be stale. Useful observability records three levels: the intended command, the communication acknowledgment, and an independently observed physical result where the application warrants it. For a door, a contact sensor can provide evidence different from a motor's position estimate. For a lamp, power consumption or a light sensor could provide different evidence from a relay status bit.

Do not add sensors to every circuit merely to make graphs interesting. Add independent feedback where failure matters. If the consequence of a missed command is a dim hallway, a local state check may be sufficient. If the consequence is water continuing to run, the value of flow or leak feedback rises considerably. Define the failure consequence first, then decide what observation is justified.

Time is another source of confusion. A wall clock can jump after synchronization or change for daylight saving time. An elapsed timeout should usually be based on a monotonic interval, not subtraction between potentially corrected wall-clock timestamps. Event occurrence, receipt, decision, and actuation times may differ. If logs retain only one timestamp, a delayed event can look as though it happened in the wrong order. For recurring rules, store enough information to tell what was received, when, and which action resulted.

## Build a bounded recovery drill

A safe drill begins by choosing a low-consequence service: a test lamp or a sensor whose action is easy to observe. Write down its normal behavior and the expected behavior when network or controller connectivity disappears. Then deliberately interrupt one dependency at a time, using the device's documented controls and without defeating required safety systems. A brief access-point restart can test wireless reconnection. Restarting the controller can test whether it reestablishes subscriptions and recovers its last known configuration. An Internet disconnection can test whether local control survives without the cloud.

For each interruption, record three things: what happened during the outage, what happened when service returned, and what action a person needed to take. Some failures are acceptable: an optional notification may be delayed. Others indicate a design fault: a valve remains open indefinitely because the 'close' event was lost. A rule that depends on a one-time rising-edge event may miss that event while offline and never revisit the required desired state after reconnection.

This leads to an important distinction between **events** and **state**. 'Toggle the light' is an event whose safe retry behavior is ambiguous. If the acknowledgment disappears, retrying may turn the light back off. 'Set the light to on' is a desired-state operation and is usually easier to repeat. Retry design must still account for device behavior and whether an operation is truly idempotent. Some commands, such as dispensing fluid, are not inherently safe to retry.

## Recover configuration as well as runtime

A system can survive one reboot and still fail after hardware replacement. Maintain configuration backups, device inventories, software and firmware versions, network names, local addresses or reservations, credentials recovery arrangements, and a short runbook describing how to restore services. Protect backups because configuration may include secrets. A backup is not proven usable merely because a file exists; a controlled restore test to a spare or isolated test environment reveals missing dependencies.

During restoration, resist the urge to change multiple things simultaneously. If a sensor does not reconnect, first determine whether it has power, whether it joins the network, whether the controller can see it, and whether the automation rule is enabled. Each observation narrows the fault domain. Reinstalling everything may restore function while destroying evidence of the underlying reliability issue.

The aim is not a home that never fails. It is a home whose automated behavior remains predictable, whose failures are visible, and whose manual controls still work. Recoverability is a designed feature. The best test is not the dashboard's reassuring green indicator; it is a repeatable exercise showing what the physical system actually does before, during, and after a dependency fails.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Dependency chain example:** sensor battery → wireless radio → AP → controller subscription → automation state machine → actuator network → relay → physical feedback → log/alert. Mark which links require internet, DNS, DHCP, wall-clock time, and continuous power.

**Recovery checklist:** define normal state, failure state, allowable fallback, manual override, test scope, start time, observed command, acknowledgment, physical result, recovery time, and restoration steps. Perform nonhazardous tests only; do not simulate failures on life-safety systems.

**Time and retry semantics:** distinguish event-time and receipt-time, monotonic duration from corrected wall-clock time, idempotent `set X` from non-idempotent `toggle X` or `dispense Y`. Duplicate, delayed and lost events must be handled deliberately.

**Scope:** Backups and credentials may be sensitive; test in an isolated environment and follow vendor safety instructions for controlled equipment.

## Selected reading and source locators (non-spoken)

- `nist-sp80034r1-contingency` — [Marianne Swanson, Pauline Bowen, Amy Phillips, Dean Gallup, and David Lynes, NIST SP 800-34 Revision 1: Contingency Planning Guide for Federal Information Systems (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Dependency analysis, service recovery strategies and validating recovery plans; federal-system context.
- `nist-sp80092-logs` — [Karen Kent (also published as Karen Scarfone) and Murugiah Souppaya, NIST SP 800-92: Guide to Computer Security Log Management (2006)](https://csrc.nist.gov/pubs/sp/800/92/final). Log collection, retention, analysis, and operational processes.
- `ietf-rfc9110-idempotency` — [Roy T. Fielding et al., RFC 9110: HTTP Semantics, Section 9.2.2 (IETF, 2022)](https://www.rfc-editor.org/rfc/rfc9110.html). Idempotent request semantics and when a client may safely retry after a lost response.
- `nist-ir8350-iot-onboarding` — [Susan Symington, Blaine Mulugeta, William Polk, Murugiah Souppaya and Jeffrey Marron, NIST IR 8350, Foundational Concepts in Trusted IoT Device Network-Layer Onboarding (2025)](https://csrc.nist.gov/pubs/ir/8350/final). Onboarding functional roles, trust, lifecycle management and credentials.
