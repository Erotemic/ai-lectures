# 004000 — Bearings, Seals, and Alignment

**Track:** Mechanical Systems and Repair. **Background:** Gears, friction, lubrication, and heat. **Purpose:** see the bearing-and-shaft assembly as a controlled contact and contamination system.

<!-- BEGIN SPOKEN LECTURE -->

# Why a Perfectly Good Bearing Fails Early

A small electric motor drives a fan. After a few months, it becomes louder, runs hotter, and develops vibration. Someone replaces the bearing. For a few weeks the machine sounds better, then the noise returns. Perhaps the bearing was defective. But perhaps the bearing was carrying a load it was not meant to carry because the shaft was misaligned, the belt tension was wrong, a seal admitted contamination, or the installation damaged the bearing before it even began operating.

A bearing's fundamental task is to support relative motion while constraining unwanted motion. A plain bearing permits sliding with an appropriate lubrication regime. A rolling-element bearing places balls or rollers between raceways, converting much of that sliding contact into rolling contact. Neither type eliminates force or friction. The design chooses how those forces are carried, what motion is allowed, and what lubrication and cleanliness are needed.

## The load has a direction

Bearings are not interchangeable circles of metal. Some are mainly intended to support *radial* loads, perpendicular to a shaft's axis. Others handle substantial *axial* or thrust loads along the shaft. Many designs carry combinations, but capacity depends on geometry and application. Consider a fan shaft with a belt pulley. Belt tension creates a radial load. A propeller or screw mechanism may create thrust. A shaft mounted between bearings also changes length as it warms; if both bearings rigidly prevent that expansion, extra axial load can develop.

Engineers often distinguish a locating bearing, which establishes axial position, from a nonlocating bearing arrangement that permits appropriate axial movement. The details depend on shaft geometry, bearing type, and fit. The mental model is that supports must constrain *just enough* motion. Too little restraint permits wobble. Too much can preload parts that were expected to move slightly.

## Alignment makes loads predictable

Two coupled shafts may look almost coaxial but differ in offset or angle. When rotated, a misaligned coupling transmits cyclic forces into shafts, bearings, and seals. A pulley installed crooked can increase belt edge wear, belt vibration, and bearing load. A machine supported on an uneven base may have a soft foot: one mounting point does not sit firmly, so tightening fasteners distorts the housing and changes the geometry.

Now imagine installing a bearing by hammering on the outer ring when the desired interference fit is on the inner ring. The assembly force may travel through the rolling elements and raceways. It can damage precisely finished contact surfaces. Proper installation transmits force through the fitted ring using suitable fixtures and methods. Temperature-assisted fits, where appropriate, must respect manufacturer limits. A bearing is not simply a component to be shoved onto a shaft until it fits.

## Seals defend the contact zone

A bearing may fail because dirt, water, or metal particles enter its lubricant. Hard debris can create surface damage; water can degrade lubrication and promote corrosion. Seals are not cosmetic covers. A contact lip seal relies on the correct relationship between the sealing lip and its shaft surface. Misalignment, roughness, insufficient lubrication, or excessive speed can wear it. Noncontact labyrinth-style seals use a tortuous path and small clearances rather than continuous rubbing, with different benefits and limitations.

A leaking seal and a damaged bearing may be symptoms of the same upstream problem. If a shaft runs eccentric, the seal may lose contact on one side and rub too heavily on another. Changing only the seal leaves the cause untouched. Similarly, filling a contaminated housing with extra grease does not remove abrasive particles or correct an inappropriate seal design.

## Read the failure before discarding it

A worn bearing leaves clues. Repeated marks on a raceway, discoloration, corrosion, pitting, smearing, and lubricant condition can suggest different failure mechanisms. No one symptom is a perfect signature: overheating may follow overload, lubrication starvation, excessive preload, or other faults. Noise frequencies and vibration signatures can be diagnostic, but interpretation requires knowledge of rotating speed, bearing geometry, mounting, and measurement conditions.

A useful troubleshooting sequence compares *what changed* against *what remained constant*. Did vibration appear after a belt replacement? Did the motor get moved? Was a seal replaced with a different material? Did washdown spray increase? Does the housing temperature rise only under certain loads? These questions test hypotheses instead of turning bearing replacement into a recurring maintenance ritual.

## A repair is complete when the load path is restored

When a shaft rotates smoothly after assembly, the job is not necessarily finished. Verify that supporting elements are aligned, that axial expansion has a legitimate path where required, that lubricant and seals suit the application, and that the operating load is within the intended arrangement. The right checks may include runout, shaft alignment, belt tension, mounting flatness, endplay, vibration, and temperature trends. Which checks apply depends on the machine.

The bearing is often the first damaged component you can hear. It is not always the component that caused the damage. Understanding the complete rotating assembly turns a repeated parts replacement into an engineering diagnosis.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Diagnostic matrix

| Observation | Competing explanations to evaluate |
|---|---|
| Rising housing temperature | Load, preload, lubricant quantity/condition, contamination, alignment |
| Cyclic vibration after belt service | Tension, pulley runout, angular/parallel misalignment, foundation |
| Seal lip wear on one side | Shaft eccentricity, alignment, housing distortion, sealing-surface wear |
| Corrosion or debris in grease | Water ingress, cleaning process, damaged housing or seals |

A failure image or frequency signature alone does not establish causation. Save removed components and baseline operating measurements when possible.

### Terms and review

*Radial load* acts perpendicular to the shaft; *axial load* acts along it. *Endplay* is permitted axial movement, whereas *preload* is intended internal load applied to eliminate or control clearance. Fits and bearing life calculations are equipment-specific. Rotating machinery and stored tension can be hazardous; follow lockout and manufacturer disassembly procedures. SKF's failure taxonomy and application guides support the conceptual mechanisms, not a universal repair prescription.

## Selected reading and claim sources (non-spoken)

- `skf-bearing-guide` — [SKF, Bearing Damage and Failure Analysis: misalignment and seal inspection excerpts](https://cdn.skfmediahub.skf.com/api/public/0901d19680c41453/pdf_preview_medium/0901d19680c41453_pdf_preview_medium.pdf). Misalignment, lubrication, seal contact pattern, locating/non-locating bearings.
- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms.
