# Secure and commission devices repeatably

<!-- BEGIN SPOKEN LECTURE -->

# Secure and commission devices repeatably

## Threat Models and Secure Remote Access

A homeowner wants to view a camera at home while traveling. The camera already works perfectly on the local network. A quick internet search suggests forwarding a router port to the camera's web interface. That might make remote viewing possible, but it changes who can reach the camera. A private local service becomes a service exposed to anyone who can send traffic to that public address.

Remote access is not only a connectivity feature. It is the intentional crossing of a trust boundary. To design it, we need a threat model: what are we protecting, who or what might attempt to reach it, how could access fail, and what disruption would matter? A camera recording family activity, an automation controller operating a garage door, and a read-only weather sensor differ in consequence, even if they all use the same home router.

### Start with the asset and an attacker capability

Suppose the important assets are camera images, local device passwords, and the ability to command actuators. The threats might include an internet scanner finding an exposed service, an attacker guessing or stealing credentials, a vendor account compromise, or a lost phone that already has access. We do not need to imagine an omnipotent attacker to identify meaningful defenses. It is enough to ask what each route can do if a single control fails.

Direct port forwarding creates an internet-reachable endpoint. An attacker may not know your name or address; automated scanning can discover open services. A strong password alone does not solve vulnerabilities in the service implementation, and an encrypted connection does not solve stolen administrator credentials. Conversely, eliminating all remote access may be incompatible with the actual use case. Design is a trade among reachability, security, reliability, and recovery.

### Prefer a narrow authenticated doorway

A virtual private network, or VPN, can create an encrypted path that lets an authorized remote device reach selected services without publishing each service independently. Peer-to-peer overlay networks and managed remote-access services are variations on this architecture, with different trust dependencies. Some products offer a reverse connection through a vendor-operated relay rather than requiring inbound router ports. That can simplify NAT traversal, but places part of the availability and security model in the vendor's infrastructure.

Do not treat a VPN as magic protection. If an unauthorized person gains access to the VPN account or an already-trusted endpoint, they may reach internal services according to the permissions granted. Good design uses strong authentication, preferably phishing-resistant multi-factor authentication where supported, limited privileges, current software, and device-specific access boundaries. A VPN capable of reaching an entire household network may grant far more capability than a remote user needs to see one camera stream.

Network segmentation can reduce that blast radius. A camera subnet, a trusted workstation subnet, and a controller network can have different access rules. Segmentation is useful only if the router or firewall actually enforces the boundaries; assigning different labels to Wi-Fi networks without effective isolation may accomplish little. The required traffic should be documented: who can initiate connections, on which ports or protocols, and for what purpose.

### Reliability is a security design constraint

Now imagine the vendor remote-access service disappears. Does the camera still record locally? Can the homeowner reach the controller through an independent, maintained path? Does a door sensor still trigger the intended local automation when the internet connection drops? These questions connect security to system architecture. A dependency on a cloud account may be acceptable for notification delivery but undesirable for a critical local control function.

The best design may separate these functions. Local cameras record to local storage; local automation performs its actions on the home network; remote clients use a deliberately maintained access gateway. That arrangement introduces its own maintenance duties: credential rotation, update schedules, backup configuration, and a method of restoring access after a router replacement. Avoiding one vendor dependency is not the same as eliminating all dependencies.

### Test the boundary with failure scenarios

An effective review asks what happens if the travel phone is lost. Can its credentials or device authorization be revoked without reconfiguring every home device? What happens if a camera has an outdated firmware flaw? Can it reach a desktop computer on another subnet? What happens if a router update resets firewall policy? Is configuration backed up and is the restore procedure tested?

Also ask what evidence exists when something changes. Connection logs, authentication failures, software version inventories, and alerts from the access gateway help distinguish legitimate remote sessions from unwanted activity. Logging alone cannot prevent a compromise, and collecting logs without a retrieval plan is often ineffective. Security information has to reach someone who can act on it.

A common shortcut is to open whatever ports make an application work and promise to secure them later. A more disciplined sequence is to make the asset list, define the required remote action, choose the smallest exposure, authenticate it, test it from outside the home, and record how to reverse the configuration. Any remote administration path should have an intentional shutdown mechanism.

### A worked design comparison

Consider three choices for a home camera. The first forwards the camera's web port directly to the internet. This has a simple topology but exposes the camera software and its credentials. The second uses a maintained VPN gateway with strong account authentication and access rules limiting the remote client to camera services. The third uses a camera vendor's relay and mobile app. The latter two may avoid exposing the camera's own port, but each creates a different trust and availability dependency. Which is best depends on the equipment, update path, remote user's devices, and tolerance for vendor outages.

A threat model turns this comparison into a repeatable decision. It does not demand perfect security. It requires that the access path be chosen consciously rather than arising accidentally from a convenience setting. The central question is not 'Can I connect from outside?' It is 'Who can connect, to what, under which conditions, and how will I know or stop them if something goes wrong?'

## Device Identity, Credentials, and Secure Provisioning

A threat model becomes an access decision only when devices and credentials can be identified.

A home automation device arrives in a box. You connect it to power, scan a code, and the application announces that it is online. But what has happened to the device's identity? Who decided that it belongs on your network, what credentials were installed, and what happens when it is sold, reset, or abandoned by its manufacturer? Those are practical questions for any household or workshop using networked sensors and actuators.

The first distinction is between recognizing a device and authorizing what it can do. A network address tells other machines where to send traffic; it does not prove that the machine is trustworthy. A MAC address is useful for local delivery and inventory, but it can be copied or changed. A hostname identifies a service for convenience. Neither is a sufficiently strong identity credential on its own. Authentication asks for evidence that a claimed identity is legitimate; authorization decides which actions that authenticated party may perform.

### What provisioning actually supplies

Provisioning is the process of giving a device the configuration needed for participation: local network access, credentials, time and name information, service endpoints, and sometimes permissions. In a Wi-Fi device, that may include network credentials or a secure onboarding mechanism. For an Ethernet sensor, network access may appear automatic, but the application may still need enrollment keys or certificates. Some systems use shared passwords; others use unique secrets, cryptographic key pairs, or certificates chained to a trusted issuer.

A shared password grants the same secret to multiple devices. If one device leaks that secret, the consequences can extend to the others. A per-device credential can restrict the damage and support revocation of one compromised unit without replacing every device's credentials. The feasibility depends on hardware, firmware, onboarding protocol, and administration, not just an app setting labeled secure.

The National Institute of Standards and Technology's work on trusted network-layer onboarding treats this as an entire lifecycle problem. Before network credentials are entrusted to a device, the network may need evidence of its identity or security posture. The device, meanwhile, should avoid silently joining an unauthorized network. There are different ways to achieve these objectives, but the goal is to establish trust rather than assume that mere physical proximity proves ownership.

### Bootstrap credentials are not operational credentials

Manufacturers often need an initial way to enroll a device before it possesses your site's credentials. A printed setup code, temporary pairing mode, factory certificate, or physical button can be part of that bootstrapping step. Each has different attack surfaces. A code photographed and posted publicly can lose its intended secrecy. A pairing mode that remains open indefinitely may expose unintended connections. A certificate without a trustworthy validation process is little better than an unexplained identifier.

In a well-designed workflow, initial enrollment establishes the authority to issue the operational credentials. The setup channel can then be closed or restricted. You should understand what a factory reset changes: does it erase local Wi-Fi credentials, cloud registration, cryptographic keys, device-generated data, and user permissions? Products vary. Resetting an app's state is not necessarily equivalent to removing its authority from the network.

### Separate device, service, and human access

A security camera needs to send video to an authorized recorder. It may not need to reach arbitrary Internet servers, printers, and laptops. A temperature sensor may need to publish readings to a local broker but never administer that broker. A person managing the system needs a distinct identity from the sensor that reports temperatures. These are separate principals with separate privileges.

Network segmentation and firewall rules can limit which destinations a device can contact. Application-level authorization can limit which topics it can publish or control commands it can issue. Segmentation is not encryption, and encryption alone does not tell a service which device is allowed to unlock a door. Good designs combine appropriate identity, confidentiality, integrity, and permission boundaries without depending on one mechanism to do every job.

### Provision for the day the vendor disappears

Device security includes continuing operation and removal. If a camera requires a vendor relay for routine local viewing, a future cloud shutdown can disable functionality that looked local. If the vendor stops publishing fixes, an Internet-facing device may accumulate vulnerability risk. Look for documented local protocols, exportable configurations, maintainable firmware, replacement options, and a clear procedure to revoke a lost or sold device's access.

Keep an asset record containing model, serial or local identifier, firmware version, network location, administrator and service roles, update method, and the date credentials last changed. Do not put secrets in an ordinary inventory spreadsheet. Record *where* credentials are secured and how access will be recovered if the usual administrator becomes unavailable. Backup plans must preserve confidentiality as well as convenience.

### A commissioning and retirement exercise

Take a hypothetical PoE camera. At first connection, it receives an address through DHCP. That is network configuration, not proof of ownership. An administrator then enrolls it using an authenticated management process, changes or establishes unique credentials, sets a time source, limits service exposure, and verifies video reaches the local recorder without unnecessary external dependencies. The camera's firmware and configuration are documented.

Now suppose the camera must be replaced. What happens to its old credentials, its local recording permissions, its fixed address reservation, and its private key? What happens to stored video or configuration on the removed unit? A good retirement plan revokes access and wipes or controls residual data before disposal or transfer. Hardware that no longer operates is not automatically a device that can no longer authenticate.

Secure provisioning is a form of systems engineering. Every device enters a network through a boundary, acquires authority, performs a limited role, and eventually leaves. If you can explain who vouches for its identity, what permissions it holds, how its software is maintained, and how to revoke it, you are no longer relying on the reassuring phrase "connected successfully." You understand the actual trust relationships.

## Network Segmentation, Local Discovery, and Access Control

A camera sends a notification to a phone. A thermostat communicates with a local controller. A laptop stores photographs and tax documents. All three devices may use the same Wi-Fi router, but they do not need the same permissions. A camera that needs to send a picture to a recorder should not automatically have access to a workstation's file shares. This is the central idea of network segmentation: organize communications according to legitimate purpose, rather than treating everything connected to one router as equally trusted.

Segmentation is more than giving networks different names. It depends on actual boundaries and the rules that control traffic across them. Understanding those rules requires a model of what happens when two devices try to communicate.

### The three layers of a local conversation

At the physical and link layers, an Ethernet switch forwards frames on the basis of hardware addresses within a local broadcast domain. Devices on the same virtual local area network, or VLAN, usually share that domain even if they are plugged into different ports. A managed switch can tag and separate traffic into several VLANs using its configuration. A port assigned to one access VLAN and a trunk carrying multiple tagged VLANs play different roles; an incorrect port configuration can merge or disconnect networks unexpectedly.

At the IP layer, devices have addresses and routes. A network prefix describes which destinations are considered local. To reach a different IP subnet, a device normally forwards traffic through a router. The router can apply firewall rules controlling which source may initiate a connection to which destination and port. A VLAN by itself is not a firewall. If a router freely routes between VLANs, separating their broadcasts has not necessarily limited access to sensitive services.

At the application layer, a service still needs a way to authenticate a user or device. Segmentation reduces the opportunities for communication, but does not replace credentials, software maintenance, encryption, and prudent service configuration. Conversely, a password-protected camera is not reason to expose all of its web services to every device on the network.

### Begin with a communication matrix

Imagine four groups: trusted computers, local automation, cameras, and visitors. A local recorder needs to receive streams from the cameras. A phone may need to reach the automation dashboard. Cameras may need a time source, but perhaps they do not need internet access. Guest devices should be able to browse the web without reaching the recorder or private computers.

Write the requirements as pairs of endpoints. Source: camera VLAN. Destination: recorder address. Purpose: video streaming. Source: automation controller. Destination: sensor VLAN. Purpose: local device protocol. Source: administrator laptop. Destination: network switch management address. Purpose: configuration. If a connection has no identified purpose, it is a candidate for being denied.

This is a more useful starting point than a rule that says 'IoT devices cannot talk to anything.' That broad rule may break the very local functions we want to preserve. The aim is limited necessary connectivity, not arbitrary isolation.

### Local discovery complicates neat diagrams

Many consumer devices discover peers using broadcast or multicast messages. Multicast DNS, often called mDNS, commonly operates within a local link, and other protocols use their own discovery mechanisms. A phone in one subnet may therefore fail to find a printer, speaker, or automation bridge in another even when a direct connection would be allowed by a firewall rule.

One response is to forward or reflect selected discovery traffic across an appropriate boundary. But a broad reflector can reintroduce visibility and unintended interactions. Another option is to configure the destination address directly, if the software supports it. A third is to place only the tightly related endpoints in the same segment. The right answer depends on what protocol the devices actually use. 'It does not appear in the app' can mean discovery failed, authentication failed, routing failed, or the application requires a cloud service. Those are different diagnoses.

Similarly, a device reaching a public website does not establish that it can reach a device on another local subnet. Some routers employ different rule paths for internet-bound traffic and inter-VLAN traffic. Draw the actual route before making conclusions about a ping or port test.

### Policies need direction and state

Firewalls commonly evaluate connection initiation and may track established connections. If a trusted workstation is allowed to initiate a connection to a camera, the camera's responses may be permitted as part of that stateful session. That does not imply the camera can initiate arbitrary new sessions toward the workstation. Many apparent contradictions in firewall behavior disappear when the direction of initiation is made explicit.

Rules should be narrow enough to express the application while remaining maintainable. Allowing every port from an entire camera subnet to the computer subnet makes troubleshooting easy today but creates a broad dependency that may be forgotten. Restricting traffic to a specific recorder and required service is a more understandable design. Give management traffic a separate path from ordinary device operation where practical.

Address assignments also matter. A rule targeting an IP address can silently point at a different device if addresses change. DHCP reservations, documented static addressing, and device identity management prevent this class of error. Do not make a network depend on remembering one device's temporary address.

### Test both what should work and what should fail

After applying segmentation, confirm the intended stream, dashboard, or printer connection. Then test a prohibited path, for example a guest device attempting to reach a private administrative interface. A configuration that appears tidy in a router screenshot but has never been tested is only a theory.

Document the topology, VLAN identifiers, subnets, DHCP scopes, DNS behavior, allowed inter-segment flows, and any discovery helpers. Also test what happens after a router restart, a lost internet connection, or a device receiving a new lease. Local-first automation should continue functioning locally if that is a design goal; segmentation should not inadvertently replace a cloud dependency with a fragile, undocumented routing dependency.

Network segmentation is a way to make trust explicit. It turns the home or workshop network from an undifferentiated collection of devices into an architecture where each connection has a reason, a path, and a test. The goal is not to make compromise impossible. It is to limit what a compromised or malfunctioning device can reach, while leaving the useful system understandable and repairable.

## Configuration as Code and Repeatable Device Commissioning

Those access decisions also have to survive commissioning and replacement, rather than exist only in the installer’s memory.

An automated door works perfectly until its controller is replaced. The replacement has the same model number, the same wiring and even the same name in the application, yet a sensor event now triggers the wrong action. The difference may be buried in a default setting, a changed firmware version, a retained cloud association or an undocumented automation rule.

In a small automation installation, manual configuration can feel convenient. But as the system grows, the problem changes. You must be able to state what the system is supposed to do, reproduce that state on new equipment and detect when the installed state differs from the intended one. This is the purpose of configuration as code, understood broadly: treating configuration as a reviewable, versioned description rather than as a collection of clicks whose history has been forgotten.

### Identity is not configuration

Start by separating physical identity, network identity and functional identity. A controller has a serial number or hardware identifier. It may receive a different IP address after reboot. It can also have a logical name such as 'garage-light-relay.' Replacing hardware while preserving the logical purpose requires a mapping between these identities. A fixed IP address by itself does not guarantee the replacement behaves correctly.

Then separate desired state from observed state. The desired state says a relay starts off after power restoration, accepts commands only from specified local services and turns on for a defined period after a sensor transition. The observed state might include its actual firmware, enabled services, current network address, relay state and most recent successful command. Configuration management is the process of comparing and reconciling them.

A useful configuration record may include device type, firmware and protocol versions, logical role, safe initial outputs, network placement, sensor-to-actuator mappings, thresholds, timeouts, permissions, and dependency on any remote service. Secrets need special handling: a plain-text configuration in version control should not casually include device passwords, tokens or private keys. Instead record how credentials are provisioned and rotated, while keeping the secret material in an appropriate protected store.

### A change should be repeatable and reviewable

Imagine three humidity controllers installed in different rooms. Each has an 'on above threshold' and 'off below threshold' setting to prevent rapid toggling. One was configured manually with a different threshold. Months later, an operator sees a fan running more often and suspects defective equipment. A versioned configuration lets you distinguish a changed policy from a changed sensor or a mechanical problem.

The principle of idempotence is useful here. An operation is idempotent when repeating it does not continue changing the desired result. 'Set the output to off' is often easier to retry safely than 'toggle the output.' Similarly, 'ensure this named automation exists with these parameters' is safer to reconcile than 'create another automation every time the setup runs.' Actual devices may not support a clean desired-state interface, so a commissioning script must sometimes read before writing and verify afterward.

### Commissioning is more than deployment

A new device should be identified, placed in the intended network segment, authenticated, loaded with approved configuration, and tested against expected inputs and outputs. Record the result. Try a cold boot. Try a network outage. Check whether the physical output returns to the intended safe state and whether stale retained messages create an unwanted action after reconnection.

For instance, a presence-triggered light may reasonably turn on again after an outage, while a garage door motor should not replay a stale 'open' instruction when a message broker reconnects. That difference belongs in the system's state-machine design, not in a one-size-fits-all retry mechanism. A controller that reports successful configuration application but has the relay wired to another circuit has not passed functional commissioning.

Versioning alone is not enough. The deployed environment also includes device firmware, radio quality, sensor calibration, network services, power supplies and physical wiring. A faithful backup of a dashboard may omit a critical setting stored in an end device. Test restoration on a spare unit or in a controlled maintenance window, recording what could not be reproduced automatically.

### How to design the handover

Suppose you are giving the system to someone else. Could that person answer which device controls the basement fan, what its expected startup behavior is, which service sends commands, which credentials it requires and how to verify that it has recovered after a power cut? If the answer requires the original installer to remember every step, the installation is not yet reproducible.

A small but effective handover might consist of a device inventory, exported configuration files, a readable diagram of command flows, a credential-management plan, tested restoration steps and a list of acceptance checks. You can keep these in ordinary text files when the system supports it. Stable naming matters more than elaborate infrastructure.

The goal is not to impose software-development ceremony on every light switch. It is to make replacement and recovery predictable. A practical automation system should be understandable from its saved intent and observable behavior, even after the person who installed it has forgotten the details.

## Device Certificates, Authentication, and Recovery in Local Networks

A home automation dashboard shows that all cameras have gone offline, yet their Ethernet links are up and a local ping still works. Yesterday the devices were trusted; today the controller rejects their connections. No hardware was replaced. The cause may be something invisible on a network diagram: a certificate expired, a device clock changed, or the controller lost the authority needed to recognize a device's identity.

Security credentials are not just a login screen. They are pieces of state with owners, lifetimes, renewal rules and recovery paths. If we want a local-first automation system to survive a cloud outage, we must design its identity and trust system to survive one too.

### Identity, authentication and authorization are separate

Identity answers which device or service we believe we are communicating with. Authentication supplies evidence supporting that claim. Authorization decides what the authenticated party is allowed to do. These are different questions. A camera might prove that it possesses the private key corresponding to a particular certificate, but that does not mean the camera should be permitted to unlock a door or change a thermostat.

In certificate-based authentication, a device may hold a private key and a certificate binding its public key to an identity under a trusted issuer. During a secure connection, the peer checks the certificate chain, validity period, name constraints and other policy; cryptographic handshake operations demonstrate possession of the appropriate private key. A certificate is not a secret password. Its associated private key is what must remain protected.

The certificate also has a time interval when it is considered valid. If the controller's clock is wrong, a perfectly legitimate certificate may appear to be from the future or already expired. An offline system with no working time source can therefore lose access to local devices despite having working power and network cables. This is why time synchronization belongs in an availability design as well as in a security design.

### The trust-anchor problem

Imagine a device whose certificate was issued by a private local certificate authority. The controller must recognize that authority as trusted. If the authority's certificate is replaced without updating clients, all the device certificates issued under it may become untrusted. If a certificate expires, replacing it with a fresh one is not enough when the corresponding device identity, key ownership or trust chain has not been updated correctly.

Now consider a private key leak. An attacker who obtains a usable key could impersonate a device if other authentication constraints do not stop them. Recovery must include invalidating or revoking the old credential and provisioning a new one. Deleting a suspicious certificate file while leaving a compromised copy of the key active somewhere else does not solve the problem.

Certificate systems need inventory: which device holds which credential, who issued it, what name it asserts, what service relies on it, when it expires and how it is replaced. The same inventory must track a trust anchor carefully, because losing it or rotating it incorrectly may affect every device in the household. The inventory should not casually contain exportable copies of all private keys.

### Offline availability is an architectural decision

A system described as local may still contact a cloud identity provider at enrollment, refresh a token remotely or validate a certificate through a network service outside the house. It can work fine with the Internet connected and fail weeks later when a token expires. Test the full lifecycle, not just the ability to switch a light once while the router's Internet cable is unplugged.

There are tradeoffs in revocation. An online revocation check can give a client fresher information, but can also create a dependency on another server. A system that ignores revocation completely may continue trusting a lost credential. Some deployments use short-lived credentials with automated renewal; others distribute revocation information locally. Whatever the approach, its failure behavior must be explicit. Does it fail closed for dangerous actuators? Does it preserve local monitoring? Can a new controller be enrolled without the manufacturer's cloud service?

Enrollment itself is a critical boundary. A factory-new device needs a way to establish a relationship with the local controller. That might involve a physically confirmed code, a provisioned certificate, a QR-based secret or a trusted onboarding channel. If anyone connected to Wi-Fi can claim to be a new lock or controller, strong encryption after enrollment does not repair the original trust failure.

### Designing an incident recovery drill

Suppose a controller is replaced after a disk failure. The device network still works, but the new controller has no credential database. Can it restore its own keys and certificate configuration from a protected backup? Can it re-establish trust without resetting every sensor? Does that backup create an unacceptable risk if stolen? Are the device credentials bound to hardware and deliberately non-exportable, requiring an enrollment procedure instead of copying keys?

A disciplined test uses a spare or noncritical device first. Record the current trust chain, expiration dates and backup process. Simulate an expired device certificate in a controlled environment, rotate a test certificate and confirm the controller recognizes the new identity while refusing the invalid old one. Verify that routine operation remains possible without an external authentication service, if offline continuity is a design requirement.

For high-consequence automation, define the safety state separately. A camera that cannot authenticate might stop transmitting, but a door lock or water shutoff needs an explicitly designed behavior under loss of communications. 'Fail secure,' 'fail safe,' and 'remain available' can demand different actions depending on the device and context. Security architecture cannot be chosen without understanding the physical system it controls.

The practical takeaway is that certificates are living configuration, not decorations added after installation. Their creation, inventory, renewal, loss and replacement are part of operating the network. A genuinely reliable local system must know who its devices are and must still be able to answer that question after an outage, an expired credential or a controller replacement.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Threat Models and Secure Remote Access

**Track:** Networking, Controls, and Automation. **Background:** IP networks, PoE, local automation, monitoring, and backups. **Purpose:** choose remote-access designs by the assets they expose, the failures they tolerate, and the evidence available when something goes wrong.

#### Technical companion (non-spoken)

##### Example architecture

```
Remote phone --authenticated tunnel--> Remote-access gateway --firewall--> Camera subnet
                                                          \--deny--> Workstation subnet
Local automation controller -------------------- local network -----> Actuators
```

This is a conceptual design, not a deployable configuration. Authentication, endpoint patching, per-device policy, and recovery are additional components.

##### Threat-model worksheet

| Field | Question |
|---|---|
| Asset | What information or physical action is at stake? |
| Exposure | What internet-accessible endpoint or identity provider is involved? |
| Authentication | What credentials, MFA, and device authorization exist? |
| Authorization | Which services and actions may the remote client access? |
| Dependency | What fails if internet, vendor, gateway, or phone is unavailable? |
| Recovery | How is access revoked and how is gateway configuration restored? |
| Audit | Which logs or events would expose unwanted access? |

##### Scope

No single remote-access product is declared secure by category. Review the exact network, router firmware, vendor trust model, credential storage, and update policy. CISA guidance for remote-access software and NSA home-network recommendations provide authoritative defensive principles, not an endorsement of a particular VPN or camera platform.

#### Selected reading and evidence records (non-spoken)

- `cisco-secure-remote-access` — [Cisco, What Is Secure Remote Access?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-secure-remote-access.html). Endpoint updates, access policy, MFA and VPN limitations; vendor-authored source
- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies
- `nist-smart-home-auditing` — [Suryadipta Mazumdar, Daniel Bostos, and Anoop Singhal, Security Auditing of Internet of Things Devices in a Smart Home (NIST, 2021)](https://www.nist.gov/publications/security-auditing-internet-things-devices-smart-home). Device audit challenges, readings, logs, configurations, and actionable policies

### Device Identity, Credentials, and Secure Provisioning

### 011000 — Device Identity, Credentials, and Secure Provisioning

#### Technical companion (non-spoken)

##### Identity and authorization table

| Attribute | What it is | What it does not prove |
|---|---|---|
| IP address | Current network locator | Cryptographic device identity |
| MAC address | Link-layer identifier | That a claimant is genuine |
| Certificate/key pair | Potential authentication mechanism, with validation | That the holder should access every service |
| Application role | Permission to perform named actions | Trustworthiness of firmware |

##### Provisioning exercise

Write a commissioning checklist for a locally operated PoE camera: bootstrap, unique credentials, time sync, minimum network access, local storage, logging, firmware maintenance, backup recovery, revocation, disposal. For each step define what could go wrong and how one would verify success without leaking credentials.

##### Original references

NIST CSWP 42 (Fagan, Marron, Souppaya, Watrobski, Kent, Mulugeta, Symington; final 2025) and NIST IR 8350 (Symington et al.; final 2025) distinguish network-layer onboarding and lifecycle management. Product-specific support for certificates, Matter, Wi-Fi Easy Connect, or other mechanisms must be verified rather than assumed.

#### Selected reading and evidence records (non-spoken)

- `nist-cswp42-iot-onboarding` — [Michael Fagan, Jeffrey Marron, Murugiah Souppaya, Paul Watrobski, Karen Kent, Blaine Mulugeta and Susan Symington, NIST CSWP 42, Towards Automating IoT Security: Implementing Trusted Network-Layer Onboarding (2025)](https://csrc.nist.gov/pubs/cswp/42/towards-automating-iot-security-implementing-trust/final). Device/network trust and secure provisioning of local network credentials.
- `nist-ir8350-iot-onboarding` — [Susan Symington, Blaine Mulugeta, William Polk, Murugiah Souppaya and Jeffrey Marron, NIST IR 8350, Foundational Concepts in Trusted IoT Device Network-Layer Onboarding (2025)](https://csrc.nist.gov/pubs/ir/8350/final). Onboarding functional roles, trust, lifecycle management and credentials.
- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies.

### Network Segmentation, Local Discovery, and Access Control

### 014000 — Network Segmentation, Local Discovery, and Access Control

#### Technical companion (non-spoken)

##### Example access matrix

| Source | Destination | Justified flow | Policy intention |
|---|---|---|---|
| Camera subnet | Recorder | Video + supported control | Allow specified services |
| Trusted administrator | Switch/router management | Authenticated management | Allow from admin segment |
| Guest subnet | Private devices | None | Deny initiation |
| Automation controller | Sensor subnet | Named local protocol | Allow only required traffic |
| IoT devices | Internet | Case-dependent | Deny unnecessary egress |

##### Acceptance checks

Record VLAN tagging on switch ports, per-subnet DHCP, routing, firewall initiation direction, local DNS and discovery, service authentication, and reboot behavior. Confirm both permitted and denied flows after a change. Keep an offline configuration backup and recovery plan.

**Review boundary:** A VLAN is not by itself a security boundary without appropriate routed access control. Multicast reflection should be narrowly justified; it may cross an intentionally placed isolation boundary. Device protocol requirements may change with firmware or vendor service updates.

#### Selected reading and evidence records (non-spoken)

- `cisco-switch` — [Cisco, What Is an Ethernet Switch?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-an-ethernet-switch.html). Switch forwarding using Ethernet MAC addresses.
- `cisa-segmentation-2022` — [U.S. Cybersecurity and Infrastructure Security Agency, Layering Network Security Through Segmentation (2022)](https://www.cisa.gov/sites/default/files/2023-01/layering-network-security-segmentation_infographic_508_0.pdf). Segmentation restricts communication paths and requires appropriate access control boundaries.
- `nist-sp1800-15-iot` — [U.S. National Institute of Standards and Technology NCCoE, NIST SP 1800-15: Securing Small-Business and Home Internet of Things Devices](https://www.nccoe.nist.gov/publication/1800-15/VolB/index.html). Restrict IoT traffic to device-appropriate purposes and apply updates and access controls.
- `rfc1034` — [Paul Mockapetris, RFC 1034: Domain Names — Concepts and Facilities, IETF (1987)](https://www.rfc-editor.org/info/rfc1034/). Domain names and DNS resolution architecture.
- `rfc791` — [Jon Postel, RFC 791: Internet Protocol, IETF (1981)](https://www.rfc-editor.org/info/rfc791/). IPv4 addressing and IP layer; updated by later RFCs.
- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies.
- `nist-sp80034r1-contingency` — [Marianne Swanson, Pauline Bowen, Amy Phillips, Dean Gallup, and David Lynes, NIST SP 800-34 Revision 1: Contingency Planning Guide for Federal Information Systems (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Dependency analysis, service recovery strategies and validating recovery plans; federal-system context.

### Configuration as Code and Repeatable Device Commissioning

### 020000 — Configuration as Code and Repeatable Device Commissioning

#### Non-spoken technical companion

**Example desired-state declaration (illustrative, vendor-neutral):** device logical ID, hardware ID, approved firmware, network segment, safe startup output, sensors, threshold/hysteresis, maximum runtime, allowable command senders, dependencies and restoration test. Store no secret values in public configuration.

**Acceptance checks.** Fresh-device provisioning; idempotent reapplication; authentication and authorization; offline behavior; cold boot; retained-message handling; rollback; human/manual override. Reconciliation is not a substitute for functional output testing.

**Sources.** NIST IoT Device Cybersecurity Requirement Catalog—Device Configuration and NISTIR 8259A family; IETF HTTP semantics for idempotent methods as an analogy, not a universal guarantee for non-HTTP actuators. Device-specific protocols and firmware determine actual feasibility. Different services and hardware may not offer declarative configuration or reliable export.

### Device Certificates, Authentication, and Recovery in Local Networks

### 021000 — Device Certificates, Authentication, and Recovery in Local Networks

#### Non-spoken technical companion

**Credential register:** Device; role; key generation and storage location; subject identity; issuer and trust anchor; certificate fingerprint; validity start/end; renewal owner; revocation mechanism; provisioning/replacement method; local/offline dependencies; recovery test date. Do not put secrets or private keys in the ordinary register.

**Failure matrix:** Controller clock inaccurate; device certificate expired; issuer certificate untrusted; key compromised; controller disk loss; token renewal depends on cloud; local DNS fails; safety-critical actuation loses identity. Distinguish a TLS connection failure from authorization denial after successful authentication.

**Test boundary:** Carry out renewal and trust-anchor drills on test devices first; changes to real locks, alarms, life-safety equipment or water valves require a designed rollback. A certificate does not grant authorization by itself.

**Sources:** NIST SP 800-57 Part 1 Rev. 5, *Recommendation for Key Management* (certificate inventories, expiration and recovery); NIST IoT onboarding guidance; NIST digital identity and derived credential lifecycle materials (conceptual comparison, not blanket application of federal PIV rules to home devices).
