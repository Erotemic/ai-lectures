# Evidence and editorial review: electrical materials 026000–029000

**State:** source-audited educational drafts; no qualified field or locally adopted code review. No prescribed duration or word-count target. Evidence is recorded in each `metadata/<lecture_id>.json` and the manuscript's non-spoken claim map.

## Manuscript-specific scope

- **026000 - Copper and aluminum.** OpenStax §9.3 supports uniform-conductor geometry and idealized 20°C metal resistivities. IEC 60228:2023 identifies the standardized conductor scope but not a full dimensional table. UL 486A-486B 2025 verifies connector families, not the suitability of any real terminal. CPSC's dated 1978 and 2003 reports concern historical U.S. aluminum branch-wire systems and must not be generalized into a ban on modern aluminum feeders. This lecture's examples distinguish wire resistance from localized contact heating, and resistor material from evaluated terminal systems.
- **027000 - Insulation, cable assemblies and raceways.** UL's publicly readable wire/cable guide distinguishes temperature and environment markings. OSHA §1910.305 supports *covered U.S. workplace* classifications, not general homeowner rights or all adopted NEC requirements. IEC 60228, 60364-5-52 and 60529 publisher summaries establish scope and responsible committees only. UL panelboard/enclosure accessory material supports the need for appropriate assembled-enclosure ratings. No direct IP-to-NEMA equivalence or unspecified conduit fill permission is claimed.
- **028000 - Ampacity and derating.** Schneider Electric's IEC-oriented public guide explains reference methods, ambient correction, grouping and soil effects; IEC 60287-1-1:2023 officially describes steady-state current-rating calculations. Numeric correction factors in our example are **hypothetical** and must not be treated as an actual conductor table. No terminal-temperature selection, fault withstand, or continuous-load allowance is inferred from a cable's 90°C insulation label.
- **029000 - Voltage drop and sizing.** OpenStax physics supplies the resistivity/Ohm law mathematics; Schneider Electric's public voltage-drop guide supplies the linear AC phasor approximations. The 30 m / 12 A example is a fixed-current mathematical comparison, not a cable selection. Resistance and drop at 70°C use a linear **teaching approximation**. An older NEC 210.19 informational note reproduced in a Schneider reference shows the familiar U.S. 3%/5% guidance; the edition and adoption have not been established for any current installation. IEC 60364-5-52's 2024 catalogue mentions Clause 525 but does not reveal an adopted full annex.

## Cross-checks and source independence

1. **Aluminum vs copper:** OpenStax's 20°C resistivity ratio directly yields the larger equal-resistance aluminum area; IEC 60228's separate standard scope confirms modern copper/aluminum conductor families, but not any particular product's reliability. The lecture limits its conclusion to material properties and explicitly requires alloy/connection context. CPSC evidence is kept in its historically investigated population.
2. **System insulation versus installed suitability:** UL product application information and U.S. OSHA wiring-method requirements agree that different cord, conductor and cable products have distinct uses. Their scopes differ; a U.S. workplace rule is not a residential permit.
3. **Heating and cable grouping:** The basic I²R equation, the published engineering installation-method guide, and the IEC 60287 official scope all support treating heat rejection as central to ampacity. They do not validate a universal multiplier or local cable size.
4. **Voltage drop:** Direct algebra matches the published R/X/phase-aware cable equations in their stated sinusoidal, balanced cases. Exact current, conductor temperature, loop topology and upstream supply voltage remain necessary.
5. **Authority:** IEC TC20 is attributed to IEC 60228/60287; IEC TC64 to IEC 60364-5-52; IEC TC70 to IEC 60529; UL/CSA/ANCE to the 2025 harmonized wire-connector standard. Textbook physics belongs to its textbook authors and editors; CPSC findings to the agency and underlying investigations, not to a manufacturer.

## Open issues requiring specific follow-up

- **Standards access:** full current IEC 60228, 60287, 60364-5-52, 60529 and adopted local NEC provisions were not read. Public abstracts cannot support normative conductor sizes, installation methods, connector torques, derating rows or enforceability.
- **Product checks:** exact cable marking, conductor alloy/stranding, termination listing, wet/UV suitability, manufacturer torque and tested tool/die systems are unverified for any real installation.
- **Independent professional review:** sustained connection heating, aluminum wiring hazard descriptions, current-carrying neutral rules, and region-specific ampacity/voltage-drop recommendations remain to be reviewed by an appropriately qualified engineer or electrician.
- **Model limits:** conductor resistance equations are homogeneous, steady-state approximations; constant-current voltage-drop comparisons are not predictions for regulated loads; lumped thermal capacitance is instructional synthesis. AC formulas presume stated phasor and balance assumptions. Cable-specific electromagnetic, thermal, and fault coordination computations remain unperformed.
- **Source independence:** multiple Schneider Electric guide pages are the same publisher, CPSC 1978 and CPSC 2003 are the same agency, and OpenStax chapters share a textbook. They should never be counted as separate independent corroboration merely because they are separate URLs.

## Editorial practice

Spoken narration teaches material behavior, equipment construction, and engineering tradeoffs directly; protective limitations appear where they change the mechanism, with further compliance detail in companions. No live-work procedures are part of these papers. This batch changes only `draft-stages/tts-trades-electrical/`; no server, TTS, UI, or other agents' content is touched.

**Summary:** four manuscripts, 48 claim-level records, 125 cumulative bibliography sources.
