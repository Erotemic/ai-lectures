# 008000 — Backups, Updates, and Configuration Recovery

**Track:** Networking, Controls, and Automation. **Background:** IP networks, PoE, sensors, local-first design, and fault isolation. **Purpose:** design a recovery process for infrastructure that otherwise quietly accumulates fragile state.

<!-- BEGIN SPOKEN LECTURE -->

# Can you rebuild your network without remembering it?

A home network appears to be a collection of boxes: a router, a switch, wireless access points, and perhaps cameras or automation devices. In practice it is also a collection of decisions. Which address belongs to a printer? Which device can reach the internet? Which sensor controls a light when the internet is absent? Which firmware version is installed? Those decisions are configuration, and configuration is a form of data that must be managed deliberately.

Consider a failed router. The replacement may establish internet access within minutes. Yet a local automation still cannot reach a camera, an address reservation has disappeared, and a remote-access rule no longer works. The hardware has been replaced, but the behavior of the system has not been recovered. That is the distinction between replacing a component and restoring a service.

## Inventory the network as relationships

A useful inventory records each important device, its role, physical connections, power source, management address, firmware or software version, and how to regain administrative access. For an Ethernet or Power-over-Ethernet network, note which switch port serves which device and what must remain powered during an outage. Record network segments, static assignments, DHCP reservations, local DNS names, and important firewall policy. Sensitive credentials belong in a protected password manager, not in a public inventory file.

Topology is as important as a device list. A drawing showing router, switch, access points, control host, and cameras can reveal a single point of failure. If every automation depends on one machine for its logic, back up that machine's data and configuration. If a device needs an outside account merely to be reactivated after a reset, record that dependency; pretending it is local-first will not remove it.

## Backups are only potential recoveries

A configuration export is useful only if it is current, restorable, and available after the machine that produced it fails. Some devices include hidden machine identifiers, secrets, or firmware-dependent settings in their backups. A backup from an old version may not import into new hardware. A backup that depends on a storage service hosted on the dead network may be unreachable during the outage.

Separate categories of state. Router and firewall rules are configuration. Home automation device registries and event histories may have different backup needs. Firmware images and installation documentation are not the same as current settings. Encryption keys and recovery tokens may be essential to reconnect systems after reinstall. The objective is to preserve what cannot simply be downloaded again and to document how components fit together.

Have more than one recovery path for vital information. A protected offline copy may remain accessible when cloud accounts, networked storage, or the internet are unavailable. Test restoring to spare equipment or a nonproduction environment where possible. A filename ending in 'backup' is evidence of a file, not evidence that recovery will work.

## Updates change both risk and behavior

Firmware updates can repair security vulnerabilities, bugs, and compatibility problems. Leaving internet-connected equipment permanently unpatched creates a growing maintenance risk, especially when vendor support ends. But an update can also change a device's interface, configuration semantics, or expected integrations. A sensible update process therefore includes reading release notes, backing up relevant state, choosing an appropriate maintenance window, and checking that critical functions still work afterward.

For a system controlling doors, lights, pumps, or alarms, identify what will happen if a service disappears during an update. Does the physical device remain safe? Is there a manual control? Will a sensor's previous state be retained incorrectly? Those questions connect network maintenance with controls engineering. Reliable automation specifies behavior under failure, not only under successful connectivity.

An update strategy can be staged. Test one device from a group before upgrading all similar devices, when that is feasible. Confirm that configuration exports still work. Record the firmware version and date, so a later fault can be correlated with a change. Avoid relying on memory to reconstruct what happened months afterward.

## A recovery drill

Imagine internet service fails while an automatically controlled light is needed. If the controller and switch still have local power, does the rule operate? If an access point fails, can a wired computer reach the controller? If the automation host is lost, can its configuration be restored without an active vendor cloud account? If the router is replaced, does local addressing return to a known state? Each question isolates a dependency.

A good drill begins with one service and follows its entire chain: sensor, network, controller, actuator, power, and user interface. Record the minimal steps to restore it, along with which steps require credentials or outside services. Do not run destructive resets just to prove that the plan is bold; a controlled spare or test environment can demonstrate much of the process.

We often measure a network by how fast it is when everything works. A more durable criterion is how predictably its behavior can be restored after failure. Inventory, backups, updates, and recovery exercises turn a collection of devices into maintainable infrastructure.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Recovery worksheet

| Component | Replaceable software? | Unique state | Backup method | Restore test | Failure behavior |
|---|---|---|---|---|---|
| Router | Firmware and package files | VLAN, firewall, DHCP, VPN keys | Encrypted export + policy document | Spare/test device | Local LAN may persist or fail |
| Automation controller | Installation packages | Devices, scenes, rules, credentials | Versioned encrypted backup | Restore to test environment | Define actuator fallback |
| PoE switch | Firmware | VLAN, power priorities, port labels | Settings export + port map | Config compare | Critical device power affected |

### Audit exercise

Choose one local service; draw power, network, DNS, authentication, control, and cloud dependencies. Mark which must survive a router reboot, ISP outage, or loss of the automation host. Write a recovery runbook with **observed** rather than merely assumed behavior.

**Security boundary:** Store secrets out of the content repository. Check the security and firmware-support policies of the exact vendor; staged testing does not justify leaving known critical vulnerabilities exposed indefinitely.

## Selected reading and evidence records (non-spoken)

- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies.
- `nist-smart-home-auditing` — [Suryadipta Mazumdar, Daniel Bostos, and Anoop Singhal, Security Auditing of Internet of Things Devices in a Smart Home (NIST, 2021)](https://www.nist.gov/publications/security-auditing-internet-things-devices-smart-home). Device audit challenges, readings, logs, configurations, and actionable policies.
