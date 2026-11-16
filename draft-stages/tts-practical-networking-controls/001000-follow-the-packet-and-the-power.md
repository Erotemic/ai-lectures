# 001000 — Follow the Packet and the Power: A Physical Model of a Home Network

**Track:** Networking, Controls, and Automation. **Background:** Everyday computers; no networking experience required. **Purpose:** connect cabling, Ethernet, IP routing, PoE, and control-system reliability.

<!-- BEGIN SPOKEN LECTURE -->

# Follow the Packet and the Power

You add an outdoor camera to a home network. It works when connected by a short patch cable inside, but not at the end of the new cable outside. Is the network down? Is the router misconfigured? Is the camera defective? The observation tells us less than it seems because the camera needs several things at once: electrical power, a usable physical communications link, a way to exchange packets with the right devices, and any services its software requires.

A home network becomes much easier to maintain when we keep those layers separate. The cable is not the internet. A link light is not proof that an application can authenticate. A device can have a working local connection without access to a cloud server. A camera can have its data path in perfect condition and still restart because its power supply cannot meet demand.

## What the cable carries

In a typical copper Ethernet installation, a cable contains four twisted pairs of insulated conductors. The twisting helps control electromagnetic interference and signal coupling. Ethernet transceivers transmit and receive encoded electrical signals over suitable pairs according to a particular standard. The rated category of cable, actual cable construction, termination quality, link length, bend radius and environment all matter to signal performance.

A connector is not good merely because its eight contacts look straight. Pair assignment and pair integrity are important. The two wires of a differential signaling pair should remain paired as intended, with untwisting limited by the applicable cabling specification. A basic continuity tester may detect opens, shorts and gross wire-map faults; it cannot necessarily certify high-frequency performance, insertion loss, near-end crosstalk, or all intermittent mechanical faults.

Copper network cable running outdoors also raises environmental questions. Water ingress, ultraviolet exposure, physical damage, and differences in grounding potential can shorten equipment life or create hazards. Fiber-optic links can provide electrical isolation between buildings where designed appropriately, while copper links require suitable bonding, surge protection, and installation practice. There is no universally correct outdoor cable route independent of the site.

## A switch is not a router

Ethernet organizes communication into frames that contain source and destination media-access-control addresses, usually called MAC addresses. A switch learns which source addresses appear at which ports and uses that table to forward frames toward likely destinations. For unknown destinations, a switch may flood frames within the relevant layer-two domain according to its forwarding rules. Ordinary broadcast traffic is also distributed within that domain, subject to configured controls.

A router connects IP networks. It consults a routing table to decide how IP packets move toward other networks. In a typical home, the router also performs functions such as network-address translation, firewalling and possibly DHCP, but those are additional roles, not what makes a router a router. A Wi-Fi access point provides a radio connection into some network; it need not perform routing. Consumer boxes often combine all these functions, which makes their names seem interchangeable even though their jobs differ.

Consider two devices on the same local subnet, with no need to reach the internet. They may communicate through a switch even if the upstream internet connection fails, provided their application and address configuration support local operation. But if the devices require a remote login or relay, an apparently local product can stop functioning because its software is cloud-dependent. Local physical connectivity and local functional autonomy are different properties.

## IP addresses solve a different problem

An IP address identifies a network endpoint for Internet Protocol communication in a given configuration. DHCP can assign an address, subnet mask or prefix, default gateway, and DNS settings automatically. DNS translates human-friendly names into relevant records; it is not the same as routing. An application that connects by numeric IP address may behave differently from one that requires a name lookup. A device can have an address and still be unable to reach its intended server.

A layered diagnostic sequence avoids changing several settings at once. Is the device powered? Is there a valid Ethernet link? Does it have an expected IP address? Can it reach a same-network endpoint? Can it reach the gateway? Does name resolution work? Can the application establish the necessary transport connection? Are authentication and service dependencies satisfied? These are separate questions with increasingly broad scope.

## Power over Ethernet is a negotiated electrical service

Power over Ethernet, or PoE, provides direct-current power over compatible copper Ethernet cabling. A power sourcing device, such as a PoE switch or injector, recognizes a compatible powered device according to the applicable PoE standard and then delivers power within specified limits. This is different from simply connecting arbitrary voltage to spare cable conductors.

The switch has a total power budget in addition to port-specific limits. Suppose four cameras each require twelve watts at the device under some operating mode. Their aggregate device demand is forty-eight watts. That does not mean a switch labeled "forty-eight watt budget" is necessarily sufficient: allowable source power and cable losses, startup peaks, cold-weather heaters, infrared illumination and other operating modes may matter. Device specifications and the applicable IEEE type and class are the source of truth, not casual addition of package labels.

Voltage drop increases with current and conductor resistance. Long cables, smaller conductors, corrosion and poor connections can worsen delivered voltage and heating. A device that works in daytime but reboots when infrared lights come on may indicate insufficient delivered power, a failing cable or power interface, or a device fault. The timing of failure is evidence to collect.

## A sensor is not the same as an automation

Now connect a motion sensor to a light controller. The sensor generates an observation: motion was detected or not detected under its operating conditions. A controller interprets that observation according to a rule. An actuator changes the physical world by switching a lamp. Each stage can fail independently.

A motion detector does not directly measure human presence. It may miss someone sitting still or respond to unrelated movement. If a rule turns off lights thirty seconds after the last detected motion, it can work well for a hallway and poorly for a room where people read quietly. More robust systems can use longer timeouts, multiple sensors, explicit manual overrides, or actual presence sensors, while acknowledging uncertainty rather than claiming a perfect detector.

Control loops also need to be designed for failure. What happens if a network packet is delayed? What if the cloud is unreachable? Does a switch turn off after a power outage or restore its previous state? Can a person override automation locally? Does the sensor record enough evidence to distinguish silence from device failure? An elegant automation should remain understandable when a component stops working.

## Diagnose from the physical edge inward

Return to the camera. First check whether the failure occurs on the long run but not on a known-good short run with the same power source. Check port power budget, link negotiation, cable path and terminations, then IP addressing and application access. Preserve the original configuration while changing one variable at a time. If the failure follows the cable, investigate cable and environmental conditions. If it follows one switch port, investigate the port and its PoE capability. If local streaming works while a vendor app fails, investigate the remote service dependency.

Networking is not magic layered on top of a wall jack. It is a combination of controlled signals, electrical power, addressing, forwarding, protocols and software policy. Learning to trace each path separately is what turns a blinking red light from a mystery into a tractable engineering problem.

<!-- END SPOKEN LECTURE -->

## Technical companion

**Layered checklist:** device power → physical link → Ethernet forwarding domain → IP address and prefix → gateway and routing → name resolution → transport connection → application authentication and dependencies. Passing a lower layer does not prove all higher layers.

**PoE budget illustration:** Four devices drawing 12 W each need 48 W at their inputs at that operating point. Source budget must account for actual PSE ratings, PD class/negotiation, cable losses, operating modes, and concurrent peaks. Never infer compatibility from this illustrative arithmetic alone.

**Evidence map:** IEEE 802.3 is the standards family governing Ethernet and standard PoE variants. Cisco's explanatory material distinguishes switching from routing and summarizes PoE power classes; device-specific engineering must reference IEEE specifications and manufacturer documentation. Manufacturer explanations may simplify the standards, so numerical installation conclusions should not rely on them alone.

**Exercise:** Draw a camera, PoE switch, router, local recorder and optional cloud server. Trace a separate arrow for power and each possible data route. Circle any dependency that would make local operation fail during an internet outage.
