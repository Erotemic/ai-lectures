# 017000 — Home Network Access Inventory and Incident Recovery

<!-- BEGIN SPOKEN LECTURE -->

A home automation system stops responding after a router update. Some lights still work from their physical switches, two cameras are reachable locally, and an app says that everything is offline. Which part has failed? Before changing settings at random, it helps to know exactly what devices exist, what each one depends on, and who has the credentials needed to recover it.

## An inventory is a map of dependencies

A basic list of device names is a start, but a useful network inventory connects each device to its function, physical location, power supply, network path, administrator, and recovery method. A camera might require a PoE switch, Ethernet cable, IP address, local recorder, DNS service, and remote application. A smart thermostat might rely on Wi-Fi to report to an app while continuing local temperature control. A device can be unavailable to a cloud service without being nonfunctional locally.

Draw the system as a directed dependency graph. A battery-backed switch may keep cameras powered, but if the recorder or router is on an unprotected outlet, the monitoring service still fails. A Wi-Fi access point may be healthy while DHCP is unavailable, preventing newly connected devices from getting addresses. A local controller may reach devices by IP address but fail by hostname when DNS stops working. These are not arbitrary IT details; they determine what can survive a partial outage.

An inventory entry should include a stable identifier that is not only a current IP address. DHCP leases may change. Record a device's manufacturer and model, serial or local asset ID where appropriate, MAC address if useful, firmware version, connection type, assigned network, and whether the IP is reserved or dynamic. Credentials and recovery codes should be stored securely, not pasted into a plain-text repository or casually printed in the inventory. Store a pointer to a secure credential record instead.

## Classify the failure before trying to fix it

A useful first question is what still works. If a lamp responds to its wall switch but not to a phone, the lamp's electrical function may be intact while its remote-control path is unavailable. If a camera's PoE port has no power, the network configuration may be irrelevant until power is restored. If devices are reachable by numeric IP address but not by name, investigate DNS or discovery. If only remote access fails, examine internet connectivity, authentication, and remote-access service dependencies before resetting local equipment.

Testing should move from the simplest local layer upward. Is there power? Is the link established? Does the device have an expected address? Can the local gateway be reached? Does the application see the endpoint? Are authentication and certificates valid? Each test narrows the failure domain. Rebooting everything simultaneously may restore service, but it destroys the sequence of evidence and makes recurrence harder to diagnose.

Treat logs as a timeline. Router lease events, switch link changes, controller restart times, firmware installation, and application errors can be correlated. Time synchronization matters because a device clock that reset during an outage may produce misleading timestamps. A record saying 'offline at 13:42' is useful only if we know which clock produced it.

## A network incident includes security decisions

Suppose an unfamiliar device appears on the wireless network, or a camera begins making unexpected outbound connections. Do not assume a compromise from one ambiguous log entry. First confirm the asset and expected behavior. If compromise is plausible, preserve evidence, revoke or rotate exposed credentials, isolate affected devices, and restore from known-good configurations according to a plan. Changing passwords on a compromised controller without addressing its underlying access path may achieve little.

Segmentation can reduce the reach of an incident. Cameras, guest devices, and the computers used for administrative work often have different access needs. A device that only needs a local recorder should not automatically have unrestricted access to every home computer. But segmentation can also break multicast discovery, update paths, or management access. Document necessary traffic and test control functions before treating 'more VLANs' as a security achievement.

When restoring a factory-reset device, remember that identity changes are part of recovery. A new key, certificate, or token may be needed. Older saved configuration might refer to a device by an identity that no longer exists. Restoring a router backup is similarly incomplete unless it is compatible with the hardware and software version. The recovery procedure should explain what is restored automatically and what requires manual re-enrollment.

## Design a recovery drill before an actual outage

Pick one low-consequence device and rehearse what happens if it disappears. Can you identify the exact power source and switch port? Can you confirm a missing DHCP lease? Is the setup documentation current enough to rejoin the device? How will you know normal functionality has returned? A successful drill proves more than the presence of a backup file; it proves that a person can use the records to recover a specific capability.

Include failure of the administrator's own phone or laptop. If the only recovery credentials and setup instructions reside inside the cloud account that has failed, the plan is circular. Maintain secure offline access to essential information. For critical physical controls, decide what should happen when the controller is unavailable. Lighting and door access should have an intentional local fallback rather than assume the home network is always healthy.

After an incident, write a compact timeline: first symptom, tests, confirmed failures, actions, state after recovery, and unresolved causes. Avoid confusing restoration of service with proof that the root cause is known. A switch reboot can end an outage while concealing failing power or thermal conditions that will recur.

The aim is not to make the house look like a corporate data center. It is to know what exists, what depends on what, and how to restore each important function without guessing. A simple accurate inventory and a rehearsed recovery procedure are more valuable than sophisticated monitoring nobody understands.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Inventory columns:** stable asset name, purpose/criticality, room, power and UPS path, switch port/SSID/VLAN, hostname/IP allocation, gateway/recording dependencies, device/firmware version, configuration backup, secure credential pointer, recovery/test procedure, owner, last verified date.

**Decision tree:** power → physical link/Wi-Fi association → address/DHCP → gateway and local reachability → name resolution/discovery → authentication → application/cloud dependency. Change one variable at a time; preserve incident logs.

**Mini recovery drill:** disable one noncritical endpoint; identify it via switch/router status; recover its address and credentials; restore local function; verify the remote app separately; document exact steps and assumptions. Do not disrupt access control, medical or life-safety functions as a training exercise.

**Security:** No credentials, private keys, or tokens in shared lecture source. Treat device reset and certificate rotation as identity events. Backup testing must cover compatibility, not just ZIP integrity.

## Selected reading and source locators (non-spoken)

- `nist-sp80034r1-contingency` — [Marianne Swanson, Pauline Bowen, Amy Phillips, Dean Gallup, and David Lynes, NIST SP 800-34 Revision 1: Contingency Planning Guide for Federal Information Systems (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Dependency analysis, service recovery strategies and validating recovery plans; federal-system context.
- `nist-sp80092-logs` — [Karen Kent (also published as Karen Scarfone) and Murugiah Souppaya, NIST SP 800-92: Guide to Computer Security Log Management (2006)](https://csrc.nist.gov/pubs/sp/800/92/final). Log collection, retention, analysis, and operational processes.
- `nist-ir8350-iot-onboarding` — [Susan Symington, Blaine Mulugeta, William Polk, Murugiah Souppaya and Jeffrey Marron, NIST IR 8350, Foundational Concepts in Trusted IoT Device Network-Layer Onboarding (2025)](https://csrc.nist.gov/pubs/ir/8350/final). Onboarding functional roles, trust, lifecycle management and credentials.
- `cisa-segmentation-2022` — [U.S. Cybersecurity and Infrastructure Security Agency, Layering Network Security Through Segmentation (2022)](https://www.cisa.gov/sites/default/files/2023-01/layering-network-security-segmentation_infographic_508_0.pdf). Segmentation restricts communication paths and requires appropriate access control boundaries.
