# 002000 — Copper Cable, Pairs, Termination, and Link Tests

**Track:** Networking, Controls, and Automation. **Background:** Ethernet frames, switches and PoE. **Purpose:** connect the physical cable to the logical network and distinguish connectivity checks from channel qualification.

<!-- BEGIN SPOKEN LECTURE -->

# A Cable Is Four Conversations, Not Eight Wires

Look at an Ethernet cable after its outer jacket has been stripped back. Inside are usually eight insulated copper conductors organized as four twisted pairs. It is tempting to think a wire is simply a wire, and that any path connecting the right pin at one end to the right pin at the other is enough. But high-speed Ethernet depends on the electrical relationship between conductors. The twist is not decoration. It is part of the communication system.

A typical twisted-pair link uses balanced signaling. The receiver is concerned with differences between the voltages on the conductors in a pair, not just one wire's voltage relative to the room. External interference that affects both conductors similarly can partly cancel at the receiver. Twisting helps distribute exposure to surrounding fields, and different pairs may have different twist rates to reduce coupling among them. The idea is not perfect immunity. It is signal integrity engineered into cable geometry.

## Four pairs and several Ethernet families

A gigabit copper Ethernet link based on 1000BASE-T uses all four pairs for signaling. Other Ethernet variants use the pairs differently, including older 100-megabit links that use two of them. This matters when diagnosing faults: a cable might appear to carry traffic at a lower negotiated speed while failing to support the intended higher speed. Link lights are therefore evidence of something, not proof of full cable quality.

Cable categories such as Category 5e, 6 and 6A specify transmission performance over a defined frequency range and under standardized test conditions. The category belongs to the installed channel or link and components' measured performance, not simply a marketing word printed on a jacket. The network may also be limited by the transceivers, switch ports, connected devices or negotiated operating mode.

## The termination preserves pairs

At the connector, conductors must reach specified contacts while maintaining the intended pairing. Wiring schemes commonly called T568A and T568B are both recognized pin assignments. Choosing one scheme consistently for a straight-through link avoids an accidental cross-connection. For ordinary modern Ethernet equipment, automatic pair-swap support can hide some differences in signal path, but it does not transform a poor termination into a qualified link.

A subtler failure is called a split pair. Suppose each pin has electrical continuity end to end, but wires belonging to different physical twisted pairs are combined into apparent signal pairs. A simple pin-to-pin continuity tester may report success. However, the physical pair geometry is broken, causing poor crosstalk performance. This is a compelling example of why testing must reflect the function of the system rather than only the most obvious property.

Terminations introduce other problems: excessive untwisting at a jack, inconsistent conductor seating, mixed connector types, poor strain relief, damage from crushing or sharp bends, and corrosion in wet environments. Shielded cable introduces additional grounding and bonding considerations. Many installations work reliably with unshielded twisted pair; adding shielding without a coherent design is not a universal upgrade.

## Length is electrical as well as geometric

A common structured-cabling channel model allows up to one hundred meters of channel, including patch cords, with a typical permanent-link limit of ninety meters under the applicable standard. That does not mean every “Ethernet cable” will support every speed for exactly that distance. Performance depends on cable category, connectors, topology, frequency and the relevant Ethernet physical-layer requirements.

Electric signals travel through cable at a substantial fraction of the speed of light, but slower than in vacuum. Test instruments can estimate cable length from signal propagation time, using a velocity factor appropriate to the cable. If a cable has a hidden splice or damage, a time-domain reflectometer may reveal impedance changes by measuring reflected pulses. Like sonar, it infers a location from the travel time of a disturbance.

## A hierarchy of tests

The simplest tester checks continuity and wiremap: is there an open, short, reversal or obvious crossed connection? A more capable verifier checks whether the cabling can carry a particular network service. A certifier evaluates the installed link against an appropriate cabling standard using specified electrical measurements and pass/fail limits.

Certified measurements can include insertion loss, which measures attenuation of signal along the link; near-end crosstalk, which measures unwanted coupling between pairs; return loss, which measures energy reflected by impedance mismatch; and delay skew, which compares travel times among pairs. Those terms sound abstract until you connect them to failure modes. A damaged cable may attenuate a signal. Poor terminations may cause reflections. Split pairs may increase crosstalk. Different propagation delays can complicate simultaneous use of all pairs.

A ping test lives at a very different layer. Successful pings show that packets traversed a route under the tested conditions. They do not prove that every pair meets category performance, that PoE voltage drop is acceptable at peak load, or that the link has margin against interference or future aging. Conversely, a physically certified link can still fail at the network layer because of addressing, switching, routing or software configuration.

## PoE adds a second kind of load

Power over Ethernet uses conductors in a communications cable to deliver electrical power as well as data. Standards specify power sourcing and powered-device behavior, classification and other protections. A nominal PoE switch budget must be compared with connected devices' needs and the actual standard the ports support. Cable conductor resistance matters because current creates voltage drop and heat; bundling and installation conditions can affect thermal behavior.

Consider a long run powering an outdoor camera. If the camera loses connectivity only when night illumination starts, the cause may not be weak wireless reception—there may be no wireless link at all. The camera could be demanding more electrical power, exposing a supply, cable or connector weakness. On the other hand, the same symptom could be firmware or device hardware. A diagnostic plan asks what changes at night and measures the relevant boundary rather than swapping equipment at random.

## Build a record before a problem arrives

Label both ends, map each run to a switch port and room, note approximate length and cable type, and retain test results. Record whether the run carries data only or PoE, and the expected powered device. Photographs and a simple port table can turn a future troubleshooting session from a maze into a sequence of hypotheses.

Copper Ethernet is a physical communications system. It has twisted pairs, impedance, reflections, interference, propagation time and power loss. Treat the cable as part of the network rather than as invisible string, and you can explain why a link that works today might have no margin tomorrow—and how to tell the difference.

<!-- END SPOKEN LECTURE -->

## Technical companion: layered tests

**Reference hierarchy:** A basic continuity/wiremap test checks conductor assignments; verification establishes support for an intended service; certification tests to the selected TIA/ISO cable standard. Certification commonly covers wiremap, length, insertion loss, NEXT, return loss and other specified quantities. Category claims require the correct standard edition and test configuration, not simply cable-jacket printing.

**Cable model:** Four twisted pairs; differential signaling; 1000BASE-T uses all four. The conventional structured-cabling maximum of 90 m permanent link plus channel cords up to a 100 m channel is a standards-based design model, not a universal maximum for all copper Ethernet variants.

**Evidence:** Fluke Networks certification descriptions and FOA's premises cabling testing reference describe wiremap, split pairs and certification. IEEE 802.3 defines Ethernet PHY and PoE variants; consult authoritative standard editions and device specifications for design and power limits.

**Exercise:** A camera links at 100 Mbps, drops at 1 Gbps, and passes an eight-pin continuity test. Propose a test sequence distinguishing pair damage, bad terminations, poor category performance and a bad switch port. Avoid inferring a diagnosis from a single indicator.

## Selected reading and evidence (non-spoken)

- `foa-copper-testing` — [Fiber Optic Association, Testing UTP Premises Cabling](https://www.foa.org/tech/ref/premises/test.html). Wiremap and split pairs, length and TDR.
- `fluke-certification` — [Fluke Networks, Network Engineer Tools and Troubleshooting Guide](https://www.flukenetworks.com/expertise/role/network-engineers). Certification vs verification and parameter suite.
- `ieee-poe` — [IEEE 802.3 Ethernet Standards Family](https://standards.ieee.org/standard/802_3-2022.html). Normative standard family; precise edition and amendment should be confirmed.
- `cisco-poe` — [Cisco, What Is Power over Ethernet?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-power-over-ethernet.html). PoE standards family and source/device power relationships.
