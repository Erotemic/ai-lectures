# Observe failures and rehearse recovery

<!-- BEGIN SPOKEN LECTURE -->

# Observe failures and rehearse recovery

## Logs, Time Synchronization, and Reliable Alerts

At three in the morning, a home automation controller reports that a basement water sensor was dry at three oh five, wet at three oh seven, and dry again at three oh four. The sequence is impossible if the timestamps all mean the same thing. Perhaps the sensor sent delayed messages, the controller's clock changed, the events came from separate devices, or the stored records were sorted by a time field with the wrong meaning. A log is useful only when we know what an event record actually represents.

### An event and an observation are not the same thing

A sensor may detect a change at one moment, transmit it later, and have it recorded still later. Imagine a wireless device that wakes, measures water, retries transmission twice, and finally reaches a hub. It might contain a device timestamp, a message sequence number, and a hub reception time. Those fields answer different questions. A device timestamp claims when measurement occurred according to that device's clock. Reception time says when the collector learned about it. The two may differ even when every component is working correctly.

A log entry should make those distinctions legible. It may need a device identity, event type, value and units, time source, quality or confidence flag, and the state that the automation entered. Without them, a line saying 'sensor changed' carries too little information to diagnose anything. For troubleshooting, a unique event identifier or increasing sequence number can also help detect duplicate delivery and missing messages.

### Clocks need a common language

Most computer systems represent civil time as an instant relative to a time standard, then display it in a chosen time zone. Coordinated Universal Time, or U T C, is a useful common frame for storing cross-device event timestamps. Local clock time can repeat during the autumn daylight-saving change or jump forward during the spring change. Two events both labeled one fifteen in the morning may be an hour apart, while a wall clock can skip a time that never occurred locally.

Network Time Protocol, originally developed by David Mills and other contributors and specified in I E T F standards, helps synchronize device clocks with reference time. Synchronization does not make every inexpensive sensor clock perfect. Devices drift, lose connectivity, reboot with an incorrect default, or step their clocks after receiving a time correction. A timestamp generated before synchronization should not be assumed reliable merely because later entries look good.

Wall-clock time is also different from elapsed time. A timer that controls a pump or checks whether a sensor has been silent for ten minutes should use an elapsed-time clock where possible, not subtract local displayed clock readings. When daylight saving starts or N T P makes an adjustment, elapsed time should continue to measure duration. This difference between a wall clock and a monotonic clock is foundational to reliable automation.

### Logs must preserve causality where possible

Suppose a heater controller receives a thermostat request, enables a relay, then detects that the expected temperature rise did not happen. A useful record includes the requested action, relay command, observed feedback, and final state. Logging only the command produces an optimistic story: 'heater on.' It does not show whether power reached the heater or heat was delivered. A careful automation distinguishes intent from observation.

Sequence numbers and correlation identifiers help connect a command to its acknowledgement or sensor reading. But distributed systems have no magic universally correct event ordering unless their design supplies one. Two devices may report different events with overlapping timestamp uncertainty. For diagnosis, it is better to state that the ordering cannot be established than to invent a precise chronology from clocks that were never synchronized.

Retries create another important trap. A sensor might resend a message after it hears no acknowledgement. The receiver may therefore see the same event twice. Counting every received message as a separate water alarm can exaggerate a problem. If commands are retried, repeating an action may be harmless for setting a light to an absolute state but dangerous for a toggle action that flips it on and off. Idempotent commands and event de-duplication are engineering tools for managing this.

### Alerts need a policy, not just a threshold

An alert is a decision that some observation deserves a human response. A bare threshold can become noisy. A humidity sensor reporting forty-nine point nine percent one moment and fifty point one the next might generate a stream of on-off notifications. Hysteresis separates the threshold for entering the alarm state from the threshold for leaving it. For example, an alert could begin after humidity remains above a chosen high level for a specified duration and clear only after it drops below a lower level. The thresholds are application choices, not universal humidity safety values.

Debouncing rejects brief transitions that are expected from mechanical contacts or noisy signals. Rate limiting prevents endless repeats of the same message. Escalation changes what happens when a severe condition persists or a first notification is not acknowledged. A critical flood alarm should not be suppressed forever by a rule intended to prevent nuisance notifications. Likewise, a missing sensor message can be an alertable event in its own right: silence may indicate lost battery, wireless failure, or controller outage.

The alert path can fail even when the sensor and local controller work. If a notification depends on cloud servers, internet access, push gateways, a phone battery, and user attention, then all of those are dependencies. A local siren or local shutoff mechanism can sometimes reduce dependence on remote delivery, but only if designed and tested appropriately. For any consequential control, identify what still works when the internet, the hub, or its clock is unavailable.

### Keep evidence without keeping everything forever

Logs consume storage and may reveal when people are home, which doors opened, or which rooms were occupied. A useful policy says what data to record, how long to retain it, how to protect it, and who can read it. Overwriting the only log during a fault destroys evidence. Keeping private sensor histories indefinitely without purpose creates another kind of risk. A rolling operational log, separate critical incident record, and deliberate retention period can be better than an unstructured archive.

A good test does not merely press the alarm's demonstration button. It induces safe representative sensor states, checks what was logged, verifies timestamps and delivery, disconnects a dependency if appropriate, and confirms what an operator actually sees. The alert is part of an observed chain, not just a configured rule.

When a time sequence looks impossible, do not first assume the physics is wrong. Ask which device measured, which device recorded, what each clock knew, and whether delivery was delayed or duplicated. Reliable monitoring is an exercise in preserving meaning across imperfect machines.

## Power Failures, UPS Design, and Recovery Testing

A recovery record must account for power loss as well as network or software failure.

A home has a battery-backed router. The electricity fails, the router stays lit, and yet nothing works. The fiber terminal in the basement has lost power. Or the network switch still runs but a powered camera has shut down. Or the server recovered before its storage drive was ready and never resumed service. This is why backup power should be designed around a service path rather than around the one device whose status light is easiest to see.

A networked service is a chain of dependencies. A phone accessing a local camera may need the camera, its power source, a PoE switch, the local network, an address, and sometimes a name-resolution service. Remote access may also require an optical terminal or cable modem, the provider's functioning outside network, a gateway, and a reachable authentication service. Backing up one link protects only the parts of the chain downstream from it.

### Draw the dependency graph

Begin with a question specific enough to test. “Keep local cameras recording during a short outage” defines a different system from “keep internet access available.” For local recording, perhaps cameras, switch, network video recorder, and local storage all need power. For remote access, the modem or optical network terminal and any necessary external communications equipment join the critical set. Some communication services still fail when the utility and provider infrastructure are down, even if every device inside the house is protected.

Draw a line between each service and everything it needs. Label components with steady operating power, expected startup behavior, and whether they are essential. Include devices that provide time, DNS, DHCP, or authentication if the service relies on them. Ask what happens if a component is unavailable but its network link remains active. A system can have electrical power and still fail at software dependencies.

### Understand UPS capacity

An uninterruptible power supply has at least two distinct ratings: how much instantaneous power it can deliver, and how much usable stored energy it has. A UPS labeled in volt-amperes describes an apparent-power capability, not a promise of that many watts or hours. Its watt rating and the actual load's electrical behavior must both be respected. Runtime depends on battery capacity, age, discharge rate, conversion efficiency, and temperature.

For a rough calculation, suppose the essential equipment draws eighty watts continuously and you want forty-five minutes of operation. Ignoring losses, eighty watts times three quarters of an hour equals sixty watt-hours. The battery must supply more than that because conversion and battery losses exist, and some margin is needed. This rough energy calculation is a screening tool, not a manufacturer runtime specification. High inrush currents and power factors can determine whether the UPS supports the load even when the steady watts appear modest.

PoE complicates the accounting. The switch consumes power for its own electronics and delivers additional power to devices through cables. A camera advertised as drawing six watts on average may consume more with heaters, infrared illumination, or motors activated. The sum of the switch's port ratings is not necessarily the shared PoE budget, and the UPS sees the switch's input draw, including losses. Measure or conservatively estimate the full operating modes rather than multiplying one average number by the camera count.

### Design a recovery sequence

An outage ends in stages. Power may flicker several times. The UPS may shift to battery, shut down at low charge, and return when electricity reappears. Some switches power on immediately, while a recording server may require storage checks. A service that depends on DNS or authentication can come up before those dependencies are ready. Startup order is therefore a functional requirement, even for a modest home network.

A controlled shutdown can protect storage from an abrupt power loss. A UPS with compatible signaling may tell a computer to stop writes and shut down when remaining runtime falls below a threshold. It is also important that the computer can restart afterward, whether through firmware power settings, a management controller, or deliberate human action. Automated restart must be designed so it does not repeatedly power-cycle defective equipment or defeat protections.

Power cycling is not identical to resilience. An internet modem may require network synchronization after restart. A local automation controller may reboot, lose time, or restore a relay to an unsafe state. Decide the desired recovery behavior of each critical actuator, and treat personnel safety as a separate engineered function rather than as a convenience script in a home automation platform.

### Test the actual outage, not just the battery

A UPS self-test says something about the battery and circuitry under that test. It does not demonstrate that a local camera recording can survive a long outage, nor that all services recover when electricity returns. After documenting the current setup, conduct a controlled and appropriate outage simulation with the responsible equipment and its required shutdown procedures. Record which devices stayed powered, when recording stopped, whether time stamps remained coherent, and which services required manual intervention. Do not remove power abruptly from equipment that cannot be safely interrupted.

Repeat the test after major configuration or wiring changes. Battery capacity declines with age; local temperature and the manufacturer's replacement guidance matter. Keep the UPS itself accessible for inspection, and do not overload extension wiring or block ventilation.

The most useful distinction is between power availability, service availability, and safe recovery. A light on a router proves only that the router has power. A resilient network proves that the service the user actually needs remains available—or returns predictably—across the outage conditions it was designed to tolerate.

## Backups, Updates, and Configuration Recovery

A home network appears to be a collection of boxes: a router, a switch, wireless access points, and perhaps cameras or automation devices. In practice it is also a collection of decisions. Which address belongs to a printer? Which device can reach the internet? Which sensor controls a light when the internet is absent? Which firmware version is installed? Those decisions are configuration, and configuration is a form of data that must be managed deliberately.

Consider a failed router. The replacement may establish internet access within minutes. Yet a local automation still cannot reach a camera, an address reservation has disappeared, and a remote-access rule no longer works. The hardware has been replaced, but the behavior of the system has not been recovered. That is the distinction between replacing a component and restoring a service.

### Inventory the network as relationships

A useful inventory records each important device, its role, physical connections, power source, management address, firmware or software version, and how to regain administrative access. For an Ethernet or Power-over-Ethernet network, note which switch port serves which device and what must remain powered during an outage. Record network segments, static assignments, DHCP reservations, local DNS names, and important firewall policy. Sensitive credentials belong in a protected password manager, not in a public inventory file.

Topology is as important as a device list. A drawing showing router, switch, access points, control host, and cameras can reveal a single point of failure. If every automation depends on one machine for its logic, back up that machine's data and configuration. If a device needs an outside account merely to be reactivated after a reset, record that dependency; pretending it is local-first will not remove it.

### Backups are only potential recoveries

A configuration export is useful only if it is current, restorable, and available after the machine that produced it fails. Some devices include hidden machine identifiers, secrets, or firmware-dependent settings in their backups. A backup from an old version may not import into new hardware. A backup that depends on a storage service hosted on the dead network may be unreachable during the outage.

Separate categories of state. Router and firewall rules are configuration. Home automation device registries and event histories may have different backup needs. Firmware images and installation documentation are not the same as current settings. Encryption keys and recovery tokens may be essential to reconnect systems after reinstall. The objective is to preserve what cannot simply be downloaded again and to document how components fit together.

Have more than one recovery path for vital information. A protected offline copy may remain accessible when cloud accounts, networked storage, or the internet are unavailable. Test restoring to spare equipment or a nonproduction environment where possible. A filename ending in 'backup' is evidence of a file, not evidence that recovery will work.

### Updates change both risk and behavior

Firmware updates can repair security vulnerabilities, bugs, and compatibility problems. Leaving internet-connected equipment permanently unpatched creates a growing maintenance risk, especially when vendor support ends. But an update can also change a device's interface, configuration semantics, or expected integrations. A sensible update process therefore includes reading release notes, backing up relevant state, choosing an appropriate maintenance window, and checking that critical functions still work afterward.

For a system controlling doors, lights, pumps, or alarms, identify what will happen if a service disappears during an update. Does the physical device remain safe? Is there a manual control? Will a sensor's previous state be retained incorrectly? Those questions connect network maintenance with controls engineering. Reliable automation specifies behavior under failure, not only under successful connectivity.

An update strategy can be staged. Test one device from a group before upgrading all similar devices, when that is feasible. Confirm that configuration exports still work. Record the firmware version and date, so a later fault can be correlated with a change. Avoid relying on memory to reconstruct what happened months afterward.

### A recovery drill

Imagine internet service fails while an automatically controlled light is needed. If the controller and switch still have local power, does the rule operate? If an access point fails, can a wired computer reach the controller? If the automation host is lost, can its configuration be restored without an active vendor cloud account? If the router is replaced, does local addressing return to a known state? Each question isolates a dependency.

A good drill begins with one service and follows its entire chain: sensor, network, controller, actuator, power, and user interface. Record the minimal steps to restore it, along with which steps require credentials or outside services. Do not run destructive resets just to prove that the plan is bold; a controlled spare or test environment can demonstrate much of the process.

We often measure a network by how fast it is when everything works. A more durable criterion is how predictably its behavior can be restored after failure. Inventory, backups, updates, and recovery exercises turn a collection of devices into maintainable infrastructure.

## Home Automation Recovery Drills and Observability

The documented recovery path becomes more credible when it is rehearsed under a controlled failure.

A power outage ends. The lights return, the router boots, and the wall switch works. Yet the motion-triggered hallway light does not come on, and the door sensor appears 'online' even though its battery died two days ago. This is a familiar kind of system failure: all the pieces appear present, but the chain of events that was supposed to connect them is broken. Recovery testing and observability are ways to discover that break before an urgent situation depends on the automation.

### A service is a chain of dependencies

Imagine a local sensor that reports motion over a wireless network. An access point receives the event, a controller interprets it, a rule decides whether to turn on a lamp, and an actuator switches power. The dashboard shows the result. There may also be a router, address assignment, name resolution, time synchronization, and a database storing device state. A single user-facing action depends on several machines and several kinds of state.

Write the chain on paper. The physical sensor has a power source. The access point has its own supply and network uplink. The controller may run on a computer or appliance that takes longer to restart than the router. The output relay may restore its previous state, default off, or choose a configured state after power returns. These choices matter. A lighting relay that returns on may be mildly inconvenient; a heater, valve, or motor that returns on without confirming prerequisites can be dangerous.

Recovery behavior is not identical to startup behavior. If components boot in a different order, a device may fail to reconnect or may keep a stale address. A controller may initially have no valid time, making scheduled events ambiguous. A cloud service may be unreachable while local devices remain fully capable of operating. A robust local-first design should distinguish a connection needed for actuation from a connection used only for remote notification or management.

### Separate three kinds of evidence

An automation log often says 'command sent.' That does not mean the actuator received the command. An acknowledgment from a device does not prove the connected mechanism moved. A reported state may itself be stale. Useful observability records three levels: the intended command, the communication acknowledgment, and an independently observed physical result where the application warrants it. For a door, a contact sensor can provide evidence different from a motor's position estimate. For a lamp, power consumption or a light sensor could provide different evidence from a relay status bit.

Do not add sensors to every circuit merely to make graphs interesting. Add independent feedback where failure matters. If the consequence of a missed command is a dim hallway, a local state check may be sufficient. If the consequence is water continuing to run, the value of flow or leak feedback rises considerably. Define the failure consequence first, then decide what observation is justified.

Time is another source of confusion. A wall clock can jump after synchronization or change for daylight saving time. An elapsed timeout should usually be based on a monotonic interval, not subtraction between potentially corrected wall-clock timestamps. Event occurrence, receipt, decision, and actuation times may differ. If logs retain only one timestamp, a delayed event can look as though it happened in the wrong order. For recurring rules, store enough information to tell what was received, when, and which action resulted.

### Build a bounded recovery drill

A safe drill begins by choosing a low-consequence service: a test lamp or a sensor whose action is easy to observe. Write down its normal behavior and the expected behavior when network or controller connectivity disappears. Then deliberately interrupt one dependency at a time, using the device's documented controls and without defeating required safety systems. A brief access-point restart can test wireless reconnection. Restarting the controller can test whether it reestablishes subscriptions and recovers its last known configuration. An Internet disconnection can test whether local control survives without the cloud.

For each interruption, record three things: what happened during the outage, what happened when service returned, and what action a person needed to take. Some failures are acceptable: an optional notification may be delayed. Others indicate a design fault: a valve remains open indefinitely because the 'close' event was lost. A rule that depends on a one-time rising-edge event may miss that event while offline and never revisit the required desired state after reconnection.

This leads to an important distinction between **events** and **state**. 'Toggle the light' is an event whose safe retry behavior is ambiguous. If the acknowledgment disappears, retrying may turn the light back off. 'Set the light to on' is a desired-state operation and is usually easier to repeat. Retry design must still account for device behavior and whether an operation is truly idempotent. Some commands, such as dispensing fluid, are not inherently safe to retry.

### Recover configuration as well as runtime

A system can survive one reboot and still fail after hardware replacement. Maintain configuration backups, device inventories, software and firmware versions, network names, local addresses or reservations, credentials recovery arrangements, and a short runbook describing how to restore services. Protect backups because configuration may include secrets. A backup is not proven usable merely because a file exists; a controlled restore test to a spare or isolated test environment reveals missing dependencies.

During restoration, resist the urge to change multiple things simultaneously. If a sensor does not reconnect, first determine whether it has power, whether it joins the network, whether the controller can see it, and whether the automation rule is enabled. Each observation narrows the fault domain. Reinstalling everything may restore function while destroying evidence of the underlying reliability issue.

The aim is not a home that never fails. It is a home whose automated behavior remains predictable, whose failures are visible, and whose manual controls still work. Recoverability is a designed feature. The best test is not the dashboard's reassuring green indicator; it is a repeatable exercise showing what the physical system actually does before, during, and after a dependency fails.

## Home Network Access Inventory and Incident Recovery

A home automation system stops responding after a router update. Some lights still work from their physical switches, two cameras are reachable locally, and an app says that everything is offline. Which part has failed? Before changing settings at random, it helps to know exactly what devices exist, what each one depends on, and who has the credentials needed to recover it.

### An inventory is a map of dependencies

A basic list of device names is a start, but a useful network inventory connects each device to its function, physical location, power supply, network path, administrator, and recovery method. A camera might require a PoE switch, Ethernet cable, IP address, local recorder, DNS service, and remote application. A smart thermostat might rely on Wi-Fi to report to an app while continuing local temperature control. A device can be unavailable to a cloud service without being nonfunctional locally.

Draw the system as a directed dependency graph. A battery-backed switch may keep cameras powered, but if the recorder or router is on an unprotected outlet, the monitoring service still fails. A Wi-Fi access point may be healthy while DHCP is unavailable, preventing newly connected devices from getting addresses. A local controller may reach devices by IP address but fail by hostname when DNS stops working. These are not arbitrary IT details; they determine what can survive a partial outage.

An inventory entry should include a stable identifier that is not only a current IP address. DHCP leases may change. Record a device's manufacturer and model, serial or local asset ID where appropriate, MAC address if useful, firmware version, connection type, assigned network, and whether the IP is reserved or dynamic. Credentials and recovery codes should be stored securely, not pasted into a plain-text repository or casually printed in the inventory. Store a pointer to a secure credential record instead.

### Classify the failure before trying to fix it

A useful first question is what still works. If a lamp responds to its wall switch but not to a phone, the lamp's electrical function may be intact while its remote-control path is unavailable. If a camera's PoE port has no power, the network configuration may be irrelevant until power is restored. If devices are reachable by numeric IP address but not by name, investigate DNS or discovery. If only remote access fails, examine internet connectivity, authentication, and remote-access service dependencies before resetting local equipment.

Testing should move from the simplest local layer upward. Is there power? Is the link established? Does the device have an expected address? Can the local gateway be reached? Does the application see the endpoint? Are authentication and certificates valid? Each test narrows the failure domain. Rebooting everything simultaneously may restore service, but it destroys the sequence of evidence and makes recurrence harder to diagnose.

Treat logs as a timeline. Router lease events, switch link changes, controller restart times, firmware installation, and application errors can be correlated. Time synchronization matters because a device clock that reset during an outage may produce misleading timestamps. A record saying 'offline at 13:42' is useful only if we know which clock produced it.

### A network incident includes security decisions

Suppose an unfamiliar device appears on the wireless network, or a camera begins making unexpected outbound connections. Do not assume a compromise from one ambiguous log entry. First confirm the asset and expected behavior. If compromise is plausible, preserve evidence, revoke or rotate exposed credentials, isolate affected devices, and restore from known-good configurations according to a plan. Changing passwords on a compromised controller without addressing its underlying access path may achieve little.

Segmentation can reduce the reach of an incident. Cameras, guest devices, and the computers used for administrative work often have different access needs. A device that only needs a local recorder should not automatically have unrestricted access to every home computer. But segmentation can also break multicast discovery, update paths, or management access. Document necessary traffic and test control functions before treating 'more VLANs' as a security achievement.

When restoring a factory-reset device, remember that identity changes are part of recovery. A new key, certificate, or token may be needed. Older saved configuration might refer to a device by an identity that no longer exists. Restoring a router backup is similarly incomplete unless it is compatible with the hardware and software version. The recovery procedure should explain what is restored automatically and what requires manual re-enrollment.

### Design a recovery drill before an actual outage

Pick one low-consequence device and rehearse what happens if it disappears. Can you identify the exact power source and switch port? Can you confirm a missing DHCP lease? Is the setup documentation current enough to rejoin the device? How will you know normal functionality has returned? A successful drill proves more than the presence of a backup file; it proves that a person can use the records to recover a specific capability.

Include failure of the administrator's own phone or laptop. If the only recovery credentials and setup instructions reside inside the cloud account that has failed, the plan is circular. Maintain secure offline access to essential information. For critical physical controls, decide what should happen when the controller is unavailable. Lighting and door access should have an intentional local fallback rather than assume the home network is always healthy.

After an incident, write a compact timeline: first symptom, tests, confirmed failures, actions, state after recovery, and unresolved causes. Avoid confusing restoration of service with proof that the root cause is known. A switch reboot can end an outage while concealing failing power or thermal conditions that will recur.

The aim is not to make the house look like a corporate data center. It is to know what exists, what depends on what, and how to restore each important function without guessing. A simple accurate inventory and a rehearsed recovery procedure are more valuable than sophisticated monitoring nobody understands.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Logs, Time Synchronization, and Reliable Alerts

### 010000 — Logs, Time Synchronization, and Reliable Alerts

#### Technical companion (non-spoken)

##### Event schema example

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

##### Test exercise

Simulate a sensor sequence `dry, wet, wet, dry` with a repeated message ID, a delayed transport delivery, and a clock jump. Decide which fields preserve the event sequence and which cannot establish physical order.

##### Review boundary

RFC 5905 specifies NTP version 4; deployment security and newer updates must be assessed separately. NIST log-management guidance addresses retention and operational processes but does not prescribe one universal household log format or retention period.

#### Selected reading and evidence records (non-spoken)

- `ietf-rfc5905-ntp` — [David L. Mills, Jim Martin, Jack Burbank and William Kasch, RFC 5905: Network Time Protocol Version 4 (IETF, 2010)](https://www.rfc-editor.org/info/rfc5905/). Time synchronization, offsets, delays and network clock discipline
- `nist-sp80092-logs` — [Karen Kent (also published as Karen Scarfone) and Murugiah Souppaya, NIST SP 800-92: Guide to Computer Security Log Management (2006)](https://csrc.nist.gov/pubs/sp/800/92/final). Log collection, retention, analysis, and operational processes
- `omron-control-hysteresis` — [OMRON Industrial Automation, Temperature Controllers FAQ: What Is Hysteresis?](https://www.ia.omron.com/support/faq/answer/53/faq00549/). On/off threshold hysteresis and prevention of rapid relay cycling

### Power Failures, UPS Design, and Recovery Testing

### 013000 — Power Failures, UPS Design, and Recovery Testing

#### Technical companion (non-spoken)

##### Screening calculation

For an illustrative 80 W load over 0.75 h, `energy_at_load = 60 Wh`. Required battery energy is greater after efficiency losses, discharge constraints, aging reserve, and UPS electronics. Verify with the manufacturer's runtime curve for the **actual load and model**; VA capacity does not equal energy capacity.

##### Dependency and test record

List essential service; modem/ONT; gateway/router; switches and PoE loads; cameras; recorder/storage; DNS/DHCP/time/authentication dependencies; steady and peak power; UPS watt and VA limits; shutdown signal method; restart behavior; controlled test results. Record outage duration and any lost footage or missing events.

**Editorial boundary:** Mains wiring, battery handling, connected-load limits, and life-safety controls follow approved products and qualified practice. An indoor UPS does not guarantee that the external service provider's network remains operational.

#### Selected reading and evidence records (non-spoken)

- `nist-sp80034r1-contingency` — [Marianne Swanson, Pauline Bowen, Amy Phillips, Dean Gallup, and David Lynes, NIST SP 800-34 Revision 1: Contingency Planning Guide for Federal Information Systems (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Dependency analysis, service recovery strategies and validating recovery plans; federal-system context.
- `cisco-poe` — [Cisco, What Is Power over Ethernet?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-power-over-ethernet.html). PoE standards family and source/device power relationships.
- `nist-sp80092-logs` — [Karen Kent (also published as Karen Scarfone) and Murugiah Souppaya, NIST SP 800-92: Guide to Computer Security Log Management (2006)](https://csrc.nist.gov/pubs/sp/800/92/final). Log collection, retention, analysis, and operational processes.

### Backups, Updates, and Configuration Recovery

**Track:** Networking, Controls, and Automation. **Background:** IP networks, PoE, sensors, local-first design, and fault isolation. **Purpose:** design a recovery process for infrastructure that otherwise quietly accumulates fragile state.

#### Technical companion (non-spoken)

##### Recovery worksheet

| Component | Replaceable software? | Unique state | Backup method | Restore test | Failure behavior |
|---|---|---|---|---|---|
| Router | Firmware and package files | VLAN, firewall, DHCP, VPN keys | Encrypted export + policy document | Spare/test device | Local LAN may persist or fail |
| Automation controller | Installation packages | Devices, scenes, rules, credentials | Versioned encrypted backup | Restore to test environment | Define actuator fallback |
| PoE switch | Firmware | VLAN, power priorities, port labels | Settings export + port map | Config compare | Critical device power affected |

##### Audit exercise

Choose one local service; draw power, network, DNS, authentication, control, and cloud dependencies. Mark which must survive a router reboot, ISP outage, or loss of the automation host. Write a recovery runbook with **observed** rather than merely assumed behavior.

**Security boundary:** Store secrets out of the content repository. Check the security and firmware-support policies of the exact vendor; staged testing does not justify leaving known critical vulnerabilities exposed indefinitely.

#### Selected reading and evidence records (non-spoken)

- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies.
- `nist-smart-home-auditing` — [Suryadipta Mazumdar, Daniel Bostos, and Anoop Singhal, Security Auditing of Internet of Things Devices in a Smart Home (NIST, 2021)](https://www.nist.gov/publications/security-auditing-internet-things-devices-smart-home). Device audit challenges, readings, logs, configurations, and actionable policies.

### Home Automation Recovery Drills and Observability

### 016000 — Home Automation Recovery Drills and Observability

#### Technical companion (non-spoken)

**Dependency chain example:** sensor battery → wireless radio → AP → controller subscription → automation state machine → actuator network → relay → physical feedback → log/alert. Mark which links require internet, DNS, DHCP, wall-clock time, and continuous power.

**Recovery checklist:** define normal state, failure state, allowable fallback, manual override, test scope, start time, observed command, acknowledgment, physical result, recovery time, and restoration steps. Perform nonhazardous tests only; do not simulate failures on life-safety systems.

**Time and retry semantics:** distinguish event-time and receipt-time, monotonic duration from corrected wall-clock time, idempotent `set X` from non-idempotent `toggle X` or `dispense Y`. Duplicate, delayed and lost events must be handled deliberately.

**Scope:** Backups and credentials may be sensitive; test in an isolated environment and follow vendor safety instructions for controlled equipment.

#### Selected reading and source locators (non-spoken)

- `nist-sp80034r1-contingency` — [Marianne Swanson, Pauline Bowen, Amy Phillips, Dean Gallup, and David Lynes, NIST SP 800-34 Revision 1: Contingency Planning Guide for Federal Information Systems (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Dependency analysis, service recovery strategies and validating recovery plans; federal-system context.
- `nist-sp80092-logs` — [Karen Kent (also published as Karen Scarfone) and Murugiah Souppaya, NIST SP 800-92: Guide to Computer Security Log Management (2006)](https://csrc.nist.gov/pubs/sp/800/92/final). Log collection, retention, analysis, and operational processes.
- `ietf-rfc9110-idempotency` — [Roy T. Fielding et al., RFC 9110: HTTP Semantics, Section 9.2.2 (IETF, 2022)](https://www.rfc-editor.org/rfc/rfc9110.html). Idempotent request semantics and when a client may safely retry after a lost response.
- `nist-ir8350-iot-onboarding` — [Susan Symington, Blaine Mulugeta, William Polk, Murugiah Souppaya and Jeffrey Marron, NIST IR 8350, Foundational Concepts in Trusted IoT Device Network-Layer Onboarding (2025)](https://csrc.nist.gov/pubs/ir/8350/final). Onboarding functional roles, trust, lifecycle management and credentials.

### Home Network Access Inventory and Incident Recovery

### 017000 — Home Network Access Inventory and Incident Recovery

#### Technical companion (non-spoken)

**Inventory columns:** stable asset name, purpose/criticality, room, power and UPS path, switch port/SSID/VLAN, hostname/IP allocation, gateway/recording dependencies, device/firmware version, configuration backup, secure credential pointer, recovery/test procedure, owner, last verified date.

**Decision tree:** power → physical link/Wi-Fi association → address/DHCP → gateway and local reachability → name resolution/discovery → authentication → application/cloud dependency. Change one variable at a time; preserve incident logs.

**Mini recovery drill:** disable one noncritical endpoint; identify it via switch/router status; recover its address and credentials; restore local function; verify the remote app separately; document exact steps and assumptions. Do not disrupt access control, medical or life-safety functions as a training exercise.

**Security:** No credentials, private keys, or tokens in shared lecture source. Treat device reset and certificate rotation as identity events. Backup testing must cover compatibility, not just ZIP integrity.

#### Selected reading and source locators (non-spoken)

- `nist-sp80034r1-contingency` — [Marianne Swanson, Pauline Bowen, Amy Phillips, Dean Gallup, and David Lynes, NIST SP 800-34 Revision 1: Contingency Planning Guide for Federal Information Systems (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Dependency analysis, service recovery strategies and validating recovery plans; federal-system context.
- `nist-sp80092-logs` — [Karen Kent (also published as Karen Scarfone) and Murugiah Souppaya, NIST SP 800-92: Guide to Computer Security Log Management (2006)](https://csrc.nist.gov/pubs/sp/800/92/final). Log collection, retention, analysis, and operational processes.
- `nist-ir8350-iot-onboarding` — [Susan Symington, Blaine Mulugeta, William Polk, Murugiah Souppaya and Jeffrey Marron, NIST IR 8350, Foundational Concepts in Trusted IoT Device Network-Layer Onboarding (2025)](https://csrc.nist.gov/pubs/ir/8350/final). Onboarding functional roles, trust, lifecycle management and credentials.
- `cisa-segmentation-2022` — [U.S. Cybersecurity and Infrastructure Security Agency, Layering Network Security Through Segmentation (2022)](https://www.cisa.gov/sites/default/files/2023-01/layering-network-security-segmentation_infographic_508_0.pdf). Segmentation restricts communication paths and requires appropriate access control boundaries.
