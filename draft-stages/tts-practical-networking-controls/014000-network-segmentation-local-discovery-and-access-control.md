# 014000 — Network Segmentation, Local Discovery, and Access Control

<!-- BEGIN SPOKEN LECTURE -->

A camera sends a notification to a phone. A thermostat communicates with a local controller. A laptop stores photographs and tax documents. All three devices may use the same Wi-Fi router, but they do not need the same permissions. A camera that needs to send a picture to a recorder should not automatically have access to a workstation's file shares. This is the central idea of network segmentation: organize communications according to legitimate purpose, rather than treating everything connected to one router as equally trusted.

Segmentation is more than giving networks different names. It depends on actual boundaries and the rules that control traffic across them. Understanding those rules requires a model of what happens when two devices try to communicate.

## The three layers of a local conversation

At the physical and link layers, an Ethernet switch forwards frames on the basis of hardware addresses within a local broadcast domain. Devices on the same virtual local area network, or VLAN, usually share that domain even if they are plugged into different ports. A managed switch can tag and separate traffic into several VLANs using its configuration. A port assigned to one access VLAN and a trunk carrying multiple tagged VLANs play different roles; an incorrect port configuration can merge or disconnect networks unexpectedly.

At the IP layer, devices have addresses and routes. A network prefix describes which destinations are considered local. To reach a different IP subnet, a device normally forwards traffic through a router. The router can apply firewall rules controlling which source may initiate a connection to which destination and port. A VLAN by itself is not a firewall. If a router freely routes between VLANs, separating their broadcasts has not necessarily limited access to sensitive services.

At the application layer, a service still needs a way to authenticate a user or device. Segmentation reduces the opportunities for communication, but does not replace credentials, software maintenance, encryption, and prudent service configuration. Conversely, a password-protected camera is not reason to expose all of its web services to every device on the network.

## Begin with a communication matrix

Imagine four groups: trusted computers, local automation, cameras, and visitors. A local recorder needs to receive streams from the cameras. A phone may need to reach the automation dashboard. Cameras may need a time source, but perhaps they do not need internet access. Guest devices should be able to browse the web without reaching the recorder or private computers.

Write the requirements as pairs of endpoints. Source: camera VLAN. Destination: recorder address. Purpose: video streaming. Source: automation controller. Destination: sensor VLAN. Purpose: local device protocol. Source: administrator laptop. Destination: network switch management address. Purpose: configuration. If a connection has no identified purpose, it is a candidate for being denied.

This is a more useful starting point than a rule that says 'IoT devices cannot talk to anything.' That broad rule may break the very local functions we want to preserve. The aim is limited necessary connectivity, not arbitrary isolation.

## Local discovery complicates neat diagrams

Many consumer devices discover peers using broadcast or multicast messages. Multicast DNS, often called mDNS, commonly operates within a local link, and other protocols use their own discovery mechanisms. A phone in one subnet may therefore fail to find a printer, speaker, or automation bridge in another even when a direct connection would be allowed by a firewall rule.

One response is to forward or reflect selected discovery traffic across an appropriate boundary. But a broad reflector can reintroduce visibility and unintended interactions. Another option is to configure the destination address directly, if the software supports it. A third is to place only the tightly related endpoints in the same segment. The right answer depends on what protocol the devices actually use. 'It does not appear in the app' can mean discovery failed, authentication failed, routing failed, or the application requires a cloud service. Those are different diagnoses.

Similarly, a device reaching a public website does not establish that it can reach a device on another local subnet. Some routers employ different rule paths for internet-bound traffic and inter-VLAN traffic. Draw the actual route before making conclusions about a ping or port test.

## Policies need direction and state

Firewalls commonly evaluate connection initiation and may track established connections. If a trusted workstation is allowed to initiate a connection to a camera, the camera's responses may be permitted as part of that stateful session. That does not imply the camera can initiate arbitrary new sessions toward the workstation. Many apparent contradictions in firewall behavior disappear when the direction of initiation is made explicit.

Rules should be narrow enough to express the application while remaining maintainable. Allowing every port from an entire camera subnet to the computer subnet makes troubleshooting easy today but creates a broad dependency that may be forgotten. Restricting traffic to a specific recorder and required service is a more understandable design. Give management traffic a separate path from ordinary device operation where practical.

Address assignments also matter. A rule targeting an IP address can silently point at a different device if addresses change. DHCP reservations, documented static addressing, and device identity management prevent this class of error. Do not make a network depend on remembering one device's temporary address.

## Test both what should work and what should fail

After applying segmentation, confirm the intended stream, dashboard, or printer connection. Then test a prohibited path, for example a guest device attempting to reach a private administrative interface. A configuration that appears tidy in a router screenshot but has never been tested is only a theory.

Document the topology, VLAN identifiers, subnets, DHCP scopes, DNS behavior, allowed inter-segment flows, and any discovery helpers. Also test what happens after a router restart, a lost internet connection, or a device receiving a new lease. Local-first automation should continue functioning locally if that is a design goal; segmentation should not inadvertently replace a cloud dependency with a fragile, undocumented routing dependency.

Network segmentation is a way to make trust explicit. It turns the home or workshop network from an undifferentiated collection of devices into an architecture where each connection has a reason, a path, and a test. The goal is not to make compromise impossible. It is to limit what a compromised or malfunctioning device can reach, while leaving the useful system understandable and repairable.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Example access matrix

| Source | Destination | Justified flow | Policy intention |
|---|---|---|---|
| Camera subnet | Recorder | Video + supported control | Allow specified services |
| Trusted administrator | Switch/router management | Authenticated management | Allow from admin segment |
| Guest subnet | Private devices | None | Deny initiation |
| Automation controller | Sensor subnet | Named local protocol | Allow only required traffic |
| IoT devices | Internet | Case-dependent | Deny unnecessary egress |

### Acceptance checks

Record VLAN tagging on switch ports, per-subnet DHCP, routing, firewall initiation direction, local DNS and discovery, service authentication, and reboot behavior. Confirm both permitted and denied flows after a change. Keep an offline configuration backup and recovery plan.

**Review boundary:** A VLAN is not by itself a security boundary without appropriate routed access control. Multicast reflection should be narrowly justified; it may cross an intentionally placed isolation boundary. Device protocol requirements may change with firmware or vendor service updates.

## Selected reading and evidence records (non-spoken)

- `cisco-switch` — [Cisco, What Is an Ethernet Switch?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-an-ethernet-switch.html). Switch forwarding using Ethernet MAC addresses.
- `cisa-segmentation-2022` — [U.S. Cybersecurity and Infrastructure Security Agency, Layering Network Security Through Segmentation (2022)](https://www.cisa.gov/sites/default/files/2023-01/layering-network-security-segmentation_infographic_508_0.pdf). Segmentation restricts communication paths and requires appropriate access control boundaries.
- `nist-sp1800-15-iot` — [U.S. National Institute of Standards and Technology NCCoE, NIST SP 1800-15: Securing Small-Business and Home Internet of Things Devices](https://www.nccoe.nist.gov/publication/1800-15/VolB/index.html). Restrict IoT traffic to device-appropriate purposes and apply updates and access controls.
- `rfc1034` — [Paul Mockapetris, RFC 1034: Domain Names — Concepts and Facilities, IETF (1987)](https://www.rfc-editor.org/info/rfc1034/). Domain names and DNS resolution architecture.
- `rfc791` — [Jon Postel, RFC 791: Internet Protocol, IETF (1981)](https://www.rfc-editor.org/info/rfc791/). IPv4 addressing and IP layer; updated by later RFCs.
- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies.
- `nist-sp80034r1-contingency` — [Marianne Swanson, Pauline Bowen, Amy Phillips, Dean Gallup, and David Lynes, NIST SP 800-34 Revision 1: Contingency Planning Guide for Federal Information Systems (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Dependency analysis, service recovery strategies and validating recovery plans; federal-system context.
