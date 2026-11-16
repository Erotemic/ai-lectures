# 007000 — Monitoring, Security, and Fault Isolation

**Track:** Networking, Controls, and Automation. **Background:** Ethernet, IP, DNS, DHCP, PoE, sensors, and local-first dependencies. **Purpose:** build observable, supportable networks without confusing connectivity with application health.

<!-- BEGIN SPOKEN LECTURE -->

# A green light does not prove the system works

A camera has a link light. The switch reports that it is supplying power. The router is online. Yet the recording application shows no video. These observations are not contradictory. Each confirms only a limited part of a chain. The link light reports a local electrical or optical link, not an end-to-end service. A PoE display may report power, but not a healthy video stream. The router's internet status says little about a local recording server.

Troubleshooting becomes much easier when we stop using the word 'network' for every layer of the system. A useful home or small-site network has physical links and power; local addressing and routing; name and time services; authentication and application protocols; and finally the function a person actually wants. Each layer offers observations, and each can fail while adjacent layers remain healthy.

## Draw what depends on what

Take an Ethernet camera connected to a PoE switch, a recorder on the same local network, a router with an internet connection, and a phone app. The camera may be powered by the switch. The recorder may retrieve video over the local network. The phone may use a remote service to learn where the recorder is. All three features can have different failure dependencies. If internet access disappears, local recording might continue while remote notifications fail. If the switch loses power, neither local nor remote video works. If a vendor account expires, local recording may or may not survive, depending on the software design.

Map separate arrows for power, data, discovery, authentication, and time synchronization. A block diagram with these distinctions is more useful than a rectangle labeled 'Wi-Fi.' It allows you to ask which failure disconnects which function. It also reveals single points of failure: a lone power supply, one switch, or one remote identity service supporting many seemingly independent devices.

## Observe the right indicator

Begin with the physical layer. Is power present? Does the link negotiate at the expected speed? Does a cable tester or switch port show excessive errors or repeated link flaps? A cable that passes a casual continuity test may still have poor pair termination or marginal performance at high speed. For PoE, power negotiation and shared switch power budget may matter separately from data link status.

At the network layer, determine the actual address, subnet, gateway, and whether the device is reachable from a suitable diagnostic host. A failed ping is ambiguous if the device blocks ICMP responses. A successful ping proves limited IP reachability, not that an application process is accepting sessions. A local name that resolves incorrectly can make an otherwise healthy device appear absent. A DHCP lease problem can affect one device while static-address devices continue operating.

At the application layer, ask whether the expected protocol responds and whether the endpoint performs useful work. A camera can answer an HTTP request but have a failed image sensor or an empty video stream. A sensor may publish readings that never change; the application is online but its data is stale. Define freshness and plausible value ranges explicitly where the function needs them.

## Logs require clocks

An event log is much more useful when devices agree on time. Without synchronization, a camera's reboot at 14:03 may appear to occur before a switch port drops at 14:01, even when the real order is reversed. Record the timestamp source, time zone, and any observed drift. A home automation controller should distinguish event time from the time it received the event when delayed messages are possible.

Useful records include link changes, device restarts, DHCP renewals, authentication failures, firmware changes, PoE power budget warnings, and application errors. Record enough context to correlate events without indiscriminately storing private content. Monitoring itself has costs: storage, false alarms, battery consumption, and security exposure. Choose the signals that meaningfully differentiate faults.

A simple baseline is powerful. Photograph or export the network diagram, label ports, list device addresses and firmware, and record expected power demand and normal traffic where available. Then when a camera disconnects every afternoon, compare the event against temperature, switch logs, PoE consumption, and controller restarts. The question becomes testable rather than anecdotal.

## Security is part of maintainability

An unmanaged network of default-password devices is hard to trust and hard to repair. Device inventory, unique credentials, firmware update support, least-privilege access, and deliberate separation between trusted workstations and less-trusted devices improve resilience. Isolation should follow an actual threat model; separating a camera VLAN is not useful if firewall rules accidentally prevent essential recorder traffic or permit unrestricted management from everywhere.

Remote access adds further dependencies and risks. A convenient application that opens an unauthenticated service to the public internet is not equivalent to a securely managed access path. Likewise, local operation does not guarantee privacy if devices continue uploading telemetry in the background. Verify both functional availability and communication behavior through documented device settings and network observation.

A complete system also has a recovery plan. Could you replace the router without losing all device configuration? Do you have a copy of controller automations and the mapping between sensors and actuators? What happens when a certificate expires or a firmware update changes a protocol? Recovery documentation is a form of reliability engineering.

## Work from the outside inward

Suppose a camera is reported offline. First record whether the camera is powered, whether the switch port links, whether its address is present, whether local traffic reaches it, and whether the recorder receives a stream. Compare its behavior with another camera on the same switch. If swapping a known-good patch cord changes the failure, the cable path becomes a candidate; if several devices fail simultaneously, investigate common infrastructure first. Change one variable at a time and write down the result.

The best monitoring strategy observes the chain from physical power to useful function. A green status badge is only one piece of evidence. The goal is a network whose behavior can be explained, whose faults can be located, and whose essential features can recover predictably.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Layered observation checklist

| Layer | Examples | Negative result does not establish |
|---|---|---|
| Power / link | Switch power budget, link speed, port errors | The endpoint application state |
| Addressing | Actual IP, lease, gateway, DNS lookup | Authorization and service health |
| Transport / app | Port availability, session, protocol response | Sensor correctness or fresh data |
| Function | Current image, relay movement, stored recording | Reliability after restart or outage |

### Investigation exercise

Two cameras on one PoE switch fail simultaneously while a third on another switch continues. List at least four common causes to test before replacing both cameras: shared switch supply, power budget, upstream network path, recorder, and name/authentication service.

**Review boundary:** Observability must respect privacy and authorized access. Do not expose device services publicly or disable security protections merely to simplify diagnosis.

## Selected reading and evidence records (non-spoken)

- `nist-smart-home-auditing` — [Suryadipta Mazumdar, Daniel Bostos, and Anoop Singhal, Security Auditing of Internet of Things Devices in a Smart Home (NIST, 2021)](https://www.nist.gov/publications/security-auditing-internet-things-devices-smart-home). Device audit challenges, readings, logs, configurations, and actionable policies.
- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies.
- `rfc791` — [Jon Postel, RFC 791: Internet Protocol, IETF (1981)](https://www.rfc-editor.org/info/rfc791/). IPv4 addressing and IP layer; updated by later RFCs.
