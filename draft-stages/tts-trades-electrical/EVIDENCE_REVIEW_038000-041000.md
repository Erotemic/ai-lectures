# Evidence review — electrical lectures 038000–041000

**Reviewed:** 2026-11-15. **Scope:** authorial source review of four educational manuscripts, their technical companions and structured claim maps. This document records the limits of the review; it is not a certification of an installation, product, code interpretation or field procedure. The spoken lectures emphasize engineering reasoning. Application-specific qualifications are collected here and in the source maps.

## Claim and source handling

The four manuscript tables contain **36 traceable consequential claims** (9 + 8 + 9 + 10). Each is mirrored in `metadata/<lecture>.json` and linked to the source IDs in `metadata/sources.json`. An organization publishing a general explanation is not automatically independent of another page issued by the same organization. Bibliography entries report actual review scope, including publicly visible publisher abstracts and pre-release catalog status. None of the inaccessible full normative IEC/NEC clauses has been represented as verified.

### 038000 — HVAC, pumps, water heating and EV charging

- **Heat-pump operating modes:** *You Installed an Air Source Heat Pump. Now What?* is a **Consortium for Energy Efficiency (CEE)** guide hosted by DOE Building Science Education, not a DOE-authored empirical study. Its FAQ and defrost passages support the existence of defrost and possible auxiliary heat; they do **not** establish that all heat pumps have resistance backup or that compressors and backup stages always operate together. DOE's general heat-pump description gives a second explanation of heat transfer but not independent testing of any manufacturer's controls.
- **Pumps:** *Variable Speed Pumping: A Guide to Successful Applications* is a documented **Hydraulic Institute + Europump + DOE Industrial Technologies Program** collaboration. Its executive summary covers system curves, static versus friction head, and affinity laws; the cover and relevant text were inspected. The cube-of-speed illustration presupposes appropriate centrifugal-system conditions and may be misleading for high static head or changing efficiency. It is not a sizing method for a particular well or hydronic pump.
- **Water heating:** DOE Building Science Education and DOE FEMP describe resistance-backup/hybrid modes; these share federal institutional context and are not independent corroboration of a specific model's wiring. The water-flow calculation is physically grounded by OpenStax specific heat; exact heater input depends on losses, water properties, and controls.
- **EVSE:** AFDC pages provide general Level 1/Level 2 and charging-configuration context. These are informational pages, not model-specific approval documents, and can contain time-sensitive market statements. The lecture avoids relying on obsolete connector market-share claims and separates wall AC input from battery energy received.

### 039000 — load inventories and service capacity

- **Statistical context:** the U.S. EIA's 2020 RECS results and Energy Explained show national and regional annual electricity use. Those are *not* load-flow measurements for one house, maximum service current, NEC demand factors or permission to use a historic meter peak in lieu of a code calculation.
- **Capacities:** the illustrative `240 V × 200 A = 48 kVA` is dimensional arithmetic at a nominal balanced single-phase rating only. It is **not** calculated permissible load, physical spare capacity, a continuous load allowance, or a conclusion about line-to-neutral unbalance. Actual service, feeder, disconnect and utility constraints require source documents and a code-compliant design evaluation.
- **Nameplate terminology:** appliance watts, motor shaft output, minimum circuit ampacity, maximum overcurrent protection, ratings and measured operating current are separate facts. A hypothetical inventory lists unknowns explicitly instead of inferring them. A manufacturer's actual rating instructions are needed before any real sizing conclusion.
- **Regional topology:** earlier 023000 references (Schneider LV distribution guide and independent AC physics) support split-phase versus three-phase relationships. The basic OpenStax AC power chapter does not alone verify nominal national voltages.

### 040000 — circuit architecture and fault behavior

- **Normal versus protective paths:** U.S. OSHA 1910.304 provisions and Schneider Electric's earthing-schemes diagrams are stronger for grounding/neutral distinctions than a draft NFPA rule. If the NEC Code-Making Panel working document is shown, it is labeled **unpublished development material**, not adopted 2026 NEC text. Different TN/TT/IT systems have different fault-clearing strategies.
- **Fault limits and coordination:** OSHA 1910.303(b)(4),(5) provides actual public U.S. *workplace* regulatory text on interrupting ratings and coordination; Schneider's published selection/coordination chapters provide engineering explanation. They do not approve a given breaker pairing, actual time-current setting or fault-current study.
- **Conductor heat and voltage:** the 16 A, 0.50-ohm round-trip conductor example yields 8 V drop, 128 W total conductor dissipation and about 3.33% of nominal 240 V. This is a lumped resistance model, not an installation voltage-drop rule. The watts are distributed along the path; a concentrated high-resistance connection must be analyzed separately.
- **Managed loads:** the behavior of an energy-management or demand-limiting product upon communication or sensor failure is a *design question*, not proven by generic EVSE documentation. Before treating any scheme as a protective constraint, inspect actual product listing, permitted wiring, fail-state documentation and locally applicable rules.

### 041000 — edition-aware regulatory and product reading

- **NFPA attribution and edition:** NFPA develops/publishes NFPA 70 through its code-making process. NFPA's 2025 explanatory article is the directly verified authority for **2026 NEC Article 120** reorganizing major service/feeder/branch load calculations from prior placements. It is not a substitute for the complete published 2026 tables. Local adoption and amendments must be checked independently; NFPA's collection of jurisdictional changes is descriptive, not an exhaustive adoption database.
- **IEC attribution and access:** IEC **Technical Committee 64** is credited for IEC 60364. The IEC publisher confirms IEC 60364-1:2025's sixth edition and restructuring, and IEC 60364-6:2016's verification scope. A separate catalog page identifies **IEC 60364-6:2026 PRV** as a *pre-release version*. None of these public abstracts verifies hidden clause-by-clause requirements or national legal adoption. Recheck the PRV publication status when updating.
- **OSHA authority:** 29 CFR 1910.303(b)(2) directly addresses installation and use of listed/labeled equipment in its workplace scope. OSHA's 2003 interpretation and current NRTL FAQ explain listing/certification scope; this is neither a blanket private-residence obligation nor independent product certification. NRTL recognition is not tied to one company alone; laboratories are recognized for specific scopes.
- **Hierarchy of documents:** a binding local code, official amendment, product-specific approved installation document, committee proposal, code commentary and a vendor FAQ can all be useful, but do different work. The lecture uses a hypothetical EVSE design to demonstrate the questions to ask, not to assert uninspected branch ratings or mandatory device arrangements.

## Open verification register

| Area | Missing evidence and practical next review | What must not be inferred |
|---|---|---|
| HVAC, pumps and water heating | Selected model's current and mode diagrams, inrush/control records, supply arrangement, thermal performance and protection requirements | That generic mode descriptions determine maximum simultaneous current or peak demand |
| EV charging | Current EVSE and vehicle documentation, certification, actual dynamic management support and fail-state behavior | That every cloud/smart charging function is an approved demand-limiting system |
| Load inventory and demand | Verified as-built one-line, phase mapping, nameplates, actual service/feeder ratings, quality-controlled records, supply provider conditions | That an annual utility bill, empty panel spaces or a single historical peak proves spare service capacity |
| Full normative content | Adopted electrical-code edition with amendments, current full standards, approved product documents and local official interpretation where necessary | That NFPA explanatory articles or IEC abstract pages establish specific binding clauses |
| Design and protection | Fault-current study for actual system, device series or coordination data, installation thermal environment, earthing arrangement and access | That a schematic or simple Ohm-law calculation is a certified system design |

## Independent arithmetic check

1. Water mass flow approximately `6 L/min = 0.1 kg/s`; with `c=4.19 kJ/(kg K)` and `DeltaT=25 K`: useful thermal power `0.1 × 4.19 × 25 = 10.475 kW`.
2. AC EV example: `240 V × 24 A = 5760 VA`. At `PF=0.99`: `P=5702.4 W`; four-hour source energy `22.8096 kWh`. A unity-power-factor approximation gives `23.04 kWh` before charging losses.
3. Rotodynamic affinity illustration at 80% speed: flow ratio `0.8`; head ratio `0.8^2 = 0.64`; power ratio `0.8^3 = 0.512`, under stated assumptions.
4. Load inventory scenarios: `3 + 5 = 8 kW`; `3 + 5.7 + 4 = 12.7 kW`. These are contemporaneous *illustrative real-power* sums, not code service-load computations or conductor phase-current calculations.
5. Hypothetical balanced 240 V service labeled 200 A: `S = 240 × 200 = 48,000 VA`. A nameplate multiplication does not establish continuous loading, permissible demand or actual spare capacity.
6. Simplified path: `16 A × 0.5 ohm = 8 V`; `8/240 = 0.03333...`; `16^2 × 0.5 = 128 W`.

## Editorial publication boundary

All four spoken works are standalone, with calculations and detailed source limitations in separate companions. The review checked content provenance and arithmetic but **did not** include independent qualified electrical design, inspection, manufacturer certification, fire-code, or local legal review. No live measurements or installation operations are required for any exercise. No shared code, TTS generation, runtime pack or repository-wide tests are part of this batch.
