# Evidence review — electrical lectures 030000–033000

**Review date:** 2026-11-15. **Status:** source-audited educational manuscripts; not professionally field-reviewed or jurisdiction-approved. All new claim-level records live in `metadata/<id>.json` and resolve into `metadata/sources.json`; each manuscript also contains a readable evidence map. No fixed duration or source-count criteria apply.

## Key source distinctions

- **030000 — terminations:** B. N. J. Persson's 2022 paper, *On the Electric Contact Resistance*, is an open peer-reviewed theory source for constriction resistance and explicitly discusses the older Holm model. A separate 2022 AIP Advances contact model corroborates the microscopic rough-contact framing. OSHA 1910.303(c) provides direct U.S. covered-workplace requirements for terminal materials, multi-conductor identification, splices and suitable compounds. UL Solutions describes distinct UL 486 connector categories. IAEI's 2011 trade article is **historical, secondary, edition-specific** evidence for why present torque cannot reconstruct original torque; it is not a source for current numerical torque values. No actual connector/model torque, ferrule approval, crimp die, or compound prescription has been validated.
- **031000 — cable paths:** OSHA 1910.305 is directly available for physical support and damp/wet enclosure conditions in its occupational scope. UL's *The Code Authority Q&A: Fireblocking* distinguishes concealed-space fireblocking from a listed penetration firestop for rated assemblies; its firestop certification article explains why marks under different test systems are not interchangeable. IEC 60364-5-52:2009+A1:2024 is used only for publisher-verified scope, not unsupported claims about specific support spacing or local permissions. Firestop design **requires an individual tested listed system** whose wall construction, opening, penetrants and fill conditions actually match the design.
- **032000 — coordination:** Schneider Electric's *Coordination between circuit-breakers* and *Calculation of minimum levels of short-circuit current* provide public engineering descriptions of total versus partial selectivity and low-current clearing. They come from **one publisher**, so two guide chapters are not independent field validation. OSHA 1910.303(b)(4) directly covers interrupting ratings for covered workplaces; UL Solutions' SCCR discussion independently distinguishes assembly fault capability from a breaker rating. IEC 60947-2:2024 publisher abstract verifies edition and TC 121/SC 121A scope **only**, not values of Icu/Ics. No actual device pairing, source-mode study, breaker setting, or incident-energy calculation has been reviewed.
- **033000 — electrodes and fault returns:** Schneider's TT/TN/IT guide supplies the technical basis that TT earth loops can be too resistive to operate overcurrent devices, motivating RCD protection. OSHA 1910.305(a)(1)(i) states continuity/bonding requirements for metallic equipment serving as a grounding conductor in covered workplaces. The NFPA Code-Making Panel 5 October 2024 A2025 **working draft** provides a direct primary *process* record for the effective ground-fault current-path principle and a distinction from soil; its cover explicitly says **not final**. It does not prove the exact final 2026 NEC clause, article number, local adoption, or a site-specific design. The two 25-ohm electrodes example is a deliberately simplified thought experiment, not a valid electrode measurement or an accepted protective arrangement.

## Unresolved technical-review register

| Area | What remains unverified | Why it matters |
|---|---|---|
| Connections | Numeric torque, stripping length, conductor number/material/class, approved tools/dies and retorque procedures for any given equipment | Wrong assumptions can damage contacts or leave joints that heat in service |
| Environmental wiring | Actual fire-resistance assembly and firestop listing, local fireblocking/building code, wet-location classification, support/fitting ratings | Route and penetration detail may compromise building barriers or equipment protection |
| Fault protection | Prospective max/min short-circuit current at each device, TCC tolerances, manufacturer-selectivity and series-rating data, assembly SCCR | A nominal device rating alone neither verifies interruption nor selective clearing |
| Grounding/earthing | Actual TN/TT/IT architecture, source connection, bonding/continuity, electrode system, residual-current protection and local limits | A soil connection does not substitute for an effective fault loop; incorrect fault assumptions can defeat protection |
| Edition and jurisdiction | Full adopted 2026 NEC or other actual code edition, IEC national deviations, utility requirements and approved product instructions | Publisher abstracts or draft committee text do not establish enforceable current requirements |

## Calculation spot checks

- Termination model at 20 A: `20² × 0.002 = 0.8 W`, `20² × 0.02 = 8 W`, `20² × 0.1 = 40 W`.
- Fault-loop comparison at 120 V: `120/0.12 = 1000 A`; `120/1.2 = 100 A`. This is an ideal circuit model.
- Simplified thermal stress: `1000² × 0.01 = 10000 A²s` and `100² × 1 = 10000 A²s`; neither predicts incident energy by itself.
- Two-electrode thought experiment: `120/(25+25) = 2.4 A`. The figure is not a grounding design criterion.

## Review scope

Narration is focused on technical concepts and engineering reasoning. Detailed source limits live here, in companions and in the metadata rather than recurring generic spoken warnings. Field implementation, product approval and binding code interpretation require a separate qualified professional review for their specific scope. A successful inventory scan is structural verification only.
