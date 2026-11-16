# 009000 — Threat Models and Secure Remote Access

**Track:** Networking, Controls, and Automation. **Background:** IP networks, PoE, local automation, monitoring, and backups. **Purpose:** choose remote-access designs by the assets they expose, the failures they tolerate, and the evidence available when something goes wrong.

<!-- BEGIN SPOKEN LECTURE -->

# Letting one person in without letting everyone in

A homeowner wants to view a camera at home while traveling. The camera already works perfectly on the local network. A quick internet search suggests forwarding a router port to the camera's web interface. That might make remote viewing possible, but it changes who can reach the camera. A private local service becomes a service exposed to anyone who can send traffic to that public address.

Remote access is not only a connectivity feature. It is the intentional crossing of a trust boundary. To design it, we need a threat model: what are we protecting, who or what might attempt to reach it, how could access fail, and what disruption would matter? A camera recording family activity, an automation controller operating a garage door, and a read-only weather sensor differ in consequence, even if they all use the same home router.

## Start with the asset and an attacker capability

Suppose the important assets are camera images, local device passwords, and the ability to command actuators. The threats might include an internet scanner finding an exposed service, an attacker guessing or stealing credentials, a vendor account compromise, or a lost phone that already has access. We do not need to imagine an omnipotent attacker to identify meaningful defenses. It is enough to ask what each route can do if a single control fails.

Direct port forwarding creates an internet-reachable endpoint. An attacker may not know your name or address; automated scanning can discover open services. A strong password alone does not solve vulnerabilities in the service implementation, and an encrypted connection does not solve stolen administrator credentials. Conversely, eliminating all remote access may be incompatible with the actual use case. Design is a trade among reachability, security, reliability, and recovery.

## Prefer a narrow authenticated doorway

A virtual private network, or VPN, can create an encrypted path that lets an authorized remote device reach selected services without publishing each service independently. Peer-to-peer overlay networks and managed remote-access services are variations on this architecture, with different trust dependencies. Some products offer a reverse connection through a vendor-operated relay rather than requiring inbound router ports. That can simplify NAT traversal, but places part of the availability and security model in the vendor's infrastructure.

Do not treat a VPN as magic protection. If an unauthorized person gains access to the VPN account or an already-trusted endpoint, they may reach internal services according to the permissions granted. Good design uses strong authentication, preferably phishing-resistant multi-factor authentication where supported, limited privileges, current software, and device-specific access boundaries. A VPN capable of reaching an entire household network may grant far more capability than a remote user needs to see one camera stream.

Network segmentation can reduce that blast radius. A camera subnet, a trusted workstation subnet, and a controller network can have different access rules. Segmentation is useful only if the router or firewall actually enforces the boundaries; assigning different labels to Wi-Fi networks without effective isolation may accomplish little. The required traffic should be documented: who can initiate connections, on which ports or protocols, and for what purpose.

## Reliability is a security design constraint

Now imagine the vendor remote-access service disappears. Does the camera still record locally? Can the homeowner reach the controller through an independent, maintained path? Does a door sensor still trigger the intended local automation when the internet connection drops? These questions connect security to system architecture. A dependency on a cloud account may be acceptable for notification delivery but undesirable for a critical local control function.

The best design may separate these functions. Local cameras record to local storage; local automation performs its actions on the home network; remote clients use a deliberately maintained access gateway. That arrangement introduces its own maintenance duties: credential rotation, update schedules, backup configuration, and a method of restoring access after a router replacement. Avoiding one vendor dependency is not the same as eliminating all dependencies.

## Test the boundary with failure scenarios

An effective review asks what happens if the travel phone is lost. Can its credentials or device authorization be revoked without reconfiguring every home device? What happens if a camera has an outdated firmware flaw? Can it reach a desktop computer on another subnet? What happens if a router update resets firewall policy? Is configuration backed up and is the restore procedure tested?

Also ask what evidence exists when something changes. Connection logs, authentication failures, software version inventories, and alerts from the access gateway help distinguish legitimate remote sessions from unwanted activity. Logging alone cannot prevent a compromise, and collecting logs without a retrieval plan is often ineffective. Security information has to reach someone who can act on it.

A common shortcut is to open whatever ports make an application work and promise to secure them later. A more disciplined sequence is to make the asset list, define the required remote action, choose the smallest exposure, authenticate it, test it from outside the home, and record how to reverse the configuration. Any remote administration path should have an intentional shutdown mechanism.

## A worked design comparison

Consider three choices for a home camera. The first forwards the camera's web port directly to the internet. This has a simple topology but exposes the camera software and its credentials. The second uses a maintained VPN gateway with strong account authentication and access rules limiting the remote client to camera services. The third uses a camera vendor's relay and mobile app. The latter two may avoid exposing the camera's own port, but each creates a different trust and availability dependency. Which is best depends on the equipment, update path, remote user's devices, and tolerance for vendor outages.

A threat model turns this comparison into a repeatable decision. It does not demand perfect security. It requires that the access path be chosen consciously rather than arising accidentally from a convenience setting. The central question is not 'Can I connect from outside?' It is 'Who can connect, to what, under which conditions, and how will I know or stop them if something goes wrong?'

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Example architecture

```
Remote phone --authenticated tunnel--> Remote-access gateway --firewall--> Camera subnet
                                                          \--deny--> Workstation subnet
Local automation controller -------------------- local network -----> Actuators
```

This is a conceptual design, not a deployable configuration. Authentication, endpoint patching, per-device policy, and recovery are additional components.

### Threat-model worksheet

| Field | Question |
|---|---|
| Asset | What information or physical action is at stake? |
| Exposure | What internet-accessible endpoint or identity provider is involved? |
| Authentication | What credentials, MFA, and device authorization exist? |
| Authorization | Which services and actions may the remote client access? |
| Dependency | What fails if internet, vendor, gateway, or phone is unavailable? |
| Recovery | How is access revoked and how is gateway configuration restored? |
| Audit | Which logs or events would expose unwanted access? |

### Scope

No single remote-access product is declared secure by category. Review the exact network, router firmware, vendor trust model, credential storage, and update policy. CISA guidance for remote-access software and NSA home-network recommendations provide authoritative defensive principles, not an endorsement of a particular VPN or camera platform.

## Selected reading and evidence records (non-spoken)

- `cisco-secure-remote-access` — [Cisco, What Is Secure Remote Access?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-secure-remote-access.html). Endpoint updates, access policy, MFA and VPN limitations; vendor-authored source
- `nist-router-security` — [Michael Fagan et al., Recommended Cybersecurity Requirements for Consumer-Grade Router Products, NIST IR 8425A (2024)](https://csrc.nist.gov/pubs/ir/8425/a/final). Router integrity, availability, and security as system dependencies
- `nist-smart-home-auditing` — [Suryadipta Mazumdar, Daniel Bostos, and Anoop Singhal, Security Auditing of Internet of Things Devices in a Smart Home (NIST, 2021)](https://www.nist.gov/publications/security-auditing-internet-things-devices-smart-home). Device audit challenges, readings, logs, configurations, and actionable policies
