# 003000 — Switches, Routers, IP, DHCP, and DNS

**Track:** Networking, Controls, and Automation. **Background:** Copper pairs, Ethernet termination, and link tests. **Purpose:** explain the layers that must cooperate before a device can use a service.

<!-- BEGIN SPOKEN LECTURE -->

# The Camera Has Power. Why Is It Offline?

A security camera is plugged into a power-over-Ethernet switch. Its LEDs light up. The switch reports a link. Yet the camera application cannot reach it. Is the cable bad? Is the internet down? Has the camera failed? Those guesses confuse several separate systems that share one cable. Power delivery, Ethernet link, local network forwarding, IP configuration, name resolution, and access to an application can all succeed or fail independently.

The fastest path to understanding is to follow a packet through a small home network. Picture a camera plugged into an Ethernet switch. The switch connects to a router. A laptop also uses that local network. The router connects to an internet service provider. The words 'network' and 'internet' do not name the same boundary in this drawing.

## What a switch learns

An Ethernet device has a link-layer address, often called a MAC address. When a switch receives an Ethernet frame, it can learn which port the frame's source address came from. Over time, it builds a forwarding table linking destination MAC addresses to ports. A frame for a known destination can be forwarded toward that port, rather than sent out every eligible port. For an unknown destination or certain broadcast traffic, flooding may be required within the relevant switching domain.

A switch normally does not need to understand the application's meaning to forward an ordinary Ethernet frame. It is not reading a camera image to decide where it belongs. It is using link-layer addressing and its forwarding state. This also explains why a device can have a valid physical Ethernet link but still lack the IP configuration needed to communicate with a particular computer.

The switch may also supply PoE. The power negotiation and electrical delivery belong to another functional part of the link. Sufficient power for a status LED is not proof that a camera has adequate power under all operating conditions, nor that IP communications have been established. Keep the observations separate.

## IP addresses describe logical reachability

On top of the link, devices communicate using Internet Protocol, or IP. An IP address identifies an interface within an addressing scheme. A subnet prefix tells a device which destinations are considered directly reachable on a particular local network. If the destination is outside that local network, the device typically sends the packet toward a router, often called its default gateway.

The router's job is to forward packets between IP networks according to a routing table and associated policies. A switch may move frames between local ports without changing the IP network. A router crosses network boundaries. Consumer boxes often combine a router, a switch, an access point, and a firewall in one enclosure; the fact that they share a case does not erase their separate functions.

Suppose a laptop has address one nine two dot one six eight dot one dot twenty, and the camera has one nine two dot one six eight dot one dot forty, with the same appropriate local prefix. They may be able to communicate directly through the switch even when the external internet connection is unavailable. But if one device is on a different network, the route and firewall policy become important. A local camera does not inherently need a cloud service simply because it uses IP.

## Who hands out the address?

Most home devices are configured automatically using DHCP, the Dynamic Host Configuration Protocol. The device seeks a server willing to allocate an address and deliver other configuration information, commonly including a subnet mask, default gateway, and DNS server addresses. A DHCP lease is not a permanent claim on one address. Leases can expire and renew; devices may receive different addresses later.

A camera whose DHCP request fails may have no usable address for the expected network. A camera given a duplicate static address can create a different problem. A laptop on one wireless guest network may be intentionally isolated from a camera on another network. These failures feel similar from the application: the device appears offline. Their causes are not similar.

When DHCP works, it proves only part of the configuration. A wrong gateway or DNS setting can still prevent specific communications. That is why the phrase 'it got an IP address' should be considered a diagnostic milestone, not the end of diagnosis.

## Names add yet another step

People prefer names to numerical addresses. DNS, the Domain Name System, associates names with various records, including network addresses. A browser or application may first resolve a name, then establish a connection to the resulting address. Failure of DNS can make an otherwise reachable service appear offline when accessed by name.

This gives a powerful test distinction. If you can communicate with a local device by a known correct address but not by its hostname, name resolution or name-based discovery deserves attention. If neither works, check link, addressing, routing, policy, and service status before blaming DNS. DNS does not carry all application traffic; it helps locate destinations.

## Diagnose from the bottom upward

Start with what is definitely observed. Does the switch show a physical link? Is the required PoE class or budget available, if applicable? Is the camera assigned an IP address? What network and subnet is it on? Does the laptop have a route to it? Do the network rules allow traffic? Does the camera actually offer the expected local protocol or management page? Is the application trying an old address or a cloud-only endpoint?

A network diagnostic can be represented as a sequence of increasingly specific tests. Link state asks about the physical path. DHCP status asks about configuration. A ping, where supported and permitted, can provide limited evidence about network reachability but does not prove an application service is healthy. A connection test to the actual service port asks a different question. Name resolution is tested separately.

Return to the powered camera. The new question is not 'Why is my Ethernet broken?' but 'Which layer's promise has not been fulfilled?' That makes the failure smaller. Network engineering is often the discipline of refusing to diagnose a system as one indistinguishable black box.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Example map

`camera --(Ethernet/PoE)--> switch --(Ethernet)--> router --(WAN)--> provider`; laptop also connects to switch or a bridged Wi-Fi network. A managed switch with VLANs can separate even physically adjacent ports into distinct networks.

### Diagnostic matrix

| Verified observation | What it establishes | What it does not establish |
|---|---|---|
| Camera powers up | Some electrical power is available | Full PoE budget; correct IP route |
| Switch reports link | Link is negotiated | Application reachability |
| DHCP lease exists | Address was allocated | DNS, route, or service working |
| Local IP test responds | Some IP path functions | Hostname resolution or target application health |
| Hostname resolves | DNS supplied an answer | Connectivity to resolved endpoint |

### Standards provenance

Richard Droms's RFC 2131 defines DHCPv4 behavior. Jon Postel edited RFC 791 for IPv4; Mockapetris's RFC 1034/1035 introduced the domain-name architecture. These are protocol references, not product-specific setup instructions. Local firewalls, VLAN controls, PoE power budgets, or device security require model-specific examination.

## Selected reading and claim sources (non-spoken)

- `rfc2131` — [Ralph Droms, RFC 2131: Dynamic Host Configuration Protocol, IETF (1997)](https://www.rfc-editor.org/info/rfc2131/). DHCP address allocation and configuration.
- `rfc1034` — [Paul Mockapetris, RFC 1034: Domain Names — Concepts and Facilities, IETF (1987)](https://www.rfc-editor.org/info/rfc1034/). Domain names and DNS resolution architecture.
- `rfc791` — [Jon Postel, RFC 791: Internet Protocol, IETF (1981)](https://www.rfc-editor.org/info/rfc791/). IPv4 addressing and IP layer; updated by later RFCs.
- `cisco-switch` — [Cisco, What Is an Ethernet Switch?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-an-ethernet-switch.html). Switch forwarding using Ethernet MAC addresses.
- `cisco-poe` — [Cisco, What Is Power over Ethernet?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-power-over-ethernet.html). PoE standards family and source/device power relationships.
