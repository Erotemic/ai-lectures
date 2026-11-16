# 013000 — Building a Maintenance and Warranty Handover Archive

<!-- BEGIN SPOKEN LECTURE -->

A new heat pump has been installed. Its owner has a polished invoice and a photograph of the outdoor unit. Three years later, a component fails. The service technician asks for the indoor unit's exact model, the original refrigerant line configuration, and the startup measurements. None is in the invoice. The owner remembers that an installer took photographs, but those photographs stayed on an employee's phone. The project may have been physically complete; its information handover was not.

Construction creates a physical asset and a record of how that asset was built. When walls are closed or equipment is replaced, important facts become hard to observe directly. A useful handover archive preserves those facts so someone can inspect, maintain, repair, or make a warranty claim years later. It is not just a folder of receipts. It is a map connecting equipment, locations, documents, responsibilities, and dates.

## Begin with an asset index

Imagine a house with a furnace, water heater, sump pump, several exhaust fans, a roof replacement, and a new electrical panel. Start with an index that names each item by function and location. For equipment, record manufacturer, exact model, serial number where appropriate, installation date, and service contact. For construction assemblies, record the project scope, contractor, affected location, and the important products used. Avoid relying on a general phrase such as “new roof,” which does not reveal underlayment, flashing, or ventilation changes.

An index should lead to the evidence without forcing someone to search dozens of ambiguous filenames. A file called `basement-sump-commissioning-2026-11.pdf` is more useful than `scan27.pdf`. Make the relationship explicit: which equipment and which job does this file describe? A maintenance record becomes usable when the next person can locate it under the problem they are trying to solve.

## Preserve things that become concealed

Photographs taken before walls, floors, or ceilings are closed can record pipe routes, cable paths, air sealing, structural repairs, and flashing details. A photograph needs context: location, orientation, scale, date, and ideally a reference to a plan. One close-up of an anonymous blue pipe is less useful than an image showing the pipe's position relative to an identifiable wall and the corresponding drawing.

Plans and as-built notes should distinguish original design from actual installation. A line on a drawing may represent intent, not the route the crew ultimately followed. Change orders, field observations, and final accepted details help reconcile that difference. Do not treat every contractor sketch as a survey-quality record, but do preserve what the sketch was meant to communicate.

Equipment startup and commissioning records are particularly valuable because they provide a performance baseline. A future technician can compare a later airflow measurement, pump pressure, or electrical reading with the values recorded when equipment was installed. A brochure listing nominal capacity is not a substitute for measurements taken in the actual building.

## Warranties have multiple conditions

A manufacturer may warrant a product for certain failures; an installer may warrant workmanship for a different period and under different conditions. Coverage can depend on registration deadlines, approved installation procedures, proof of purchase, maintenance, or authorized service. Never assume “ten-year warranty” means all labor, travel, and associated damage are covered for ten years. Read the actual language and keep the applicable version of the warranty and its registration confirmation.

Store proof of purchase, installer invoices, permit or inspection records where applicable, and documents establishing the specific equipment or material installed. If a dispute later arises, a clear record of dates, promises, changes, and acceptance can be more important than a stack of advertising brochures. Statutory rights and lien or warranty rules vary by location; a personal archive does not override a contract or law.

## Design the archive to survive the people who made it

A contractor's cloud portal can disappear, and a homeowner can change email accounts. Keep a durable local export of essential documents in common readable formats, with a backup independent of the main device. Preserve original copies where signatures or authenticity matter. Maintain one index describing the contents, and avoid turning it into a complex software system that nobody will update.

Sensitive documents need an access plan. A full alarm wiring diagram, camera passwords, and personal financial information should not be distributed indiscriminately to every future service provider. Store credentials separately in an appropriate secret manager, not in an unencrypted handover packet. A technician often needs a device model and network requirements, not access to every account in the house.

A useful archive can be transferred when the property is sold or responsibility changes. Separate owner-personal information from transferable system records. Verify that linked documents are present rather than only referencing a dead website or contractor drive. Keep printed emergency shutoff and critical equipment identifiers accessible even when the internet or electricity is out.

## Turn handover into a future maintenance plan

The archive should not stop at installation. Include manufacturer maintenance instructions, inspection intervals where applicable, consumables, replacement part numbers, and a log of service dates and findings. For a roof, that may include flashing locations and warranty details. For a pump, it may include the installed check valve, alarms, and tested operating points. For a cabinet or deck, it may include finish products and fastening details. Keep maintenance recommendations distinct from binding manufacturer obligations.

At project closeout, inspect the archive as if you were a future technician with no personal knowledge of the job. Can you identify the equipment? Find the right shutoff? Reconstruct the concealed work? Know what was actually tested? Understand the applicable warranty? If not, the handover is not finished.

A well-organized archive is a form of preventive maintenance. It reduces repeat investigation, avoids destructive guessing, and makes responsible ownership easier. The best time to record a fact is while the wall is open and the people who know the answer are still on the job.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Suggested folder schema

`assets/index.csv` with stable IDs; `projects/YYYY-MM-scope/` with contract, scope, change orders, permits, inspection outcomes, concealed-work photos and as-built notes; `equipment/asset-id/` with product data, commissioning baseline, warranty, service log; `emergency/` for shutoffs and contacts (without passwords). Keep sensitive materials in a separately permissioned location.

### Acceptance checklist

For each asset, check: unique location; model and serial; install date; contractor contact; manual/version; warranty terms and registration; commissioning readings; as-built or photographs; inspections; maintenance schedule; backup copy. Record missing documents explicitly rather than inventing entries.

**Editorial boundary:** Warranty enforcement, retention periods, mechanic's liens, data privacy, and property-transfer disclosure rules vary by jurisdiction and contract. An archive improves evidence quality; it does not itself confer warranty rights.

## Selected reading and evidence records (non-spoken)

- `aia-lima-submittals` — [Gustavo A. Lima, AIA, According to Hoyle: The Submittal Process (American Institute of Architects Community, 2025)](https://communityhub.aia.org/blogs/gustavo-a-lima-aia/2025/09/26/according-to-hoyle-the-submittal-process). AIA A201 distinction between submittals and contract documents; contract dependent.
- `ftc-improvement` — [Federal Trade Commission, How To Avoid a Home Improvement Scam](https://consumer.ftc.gov/articles/how-avoid-home-improvement-scam). Written estimates, contracts, licenses and payment caution.
- `aba-contract` — [American Bar Association, The Law & Your Home: What Should a Contract Include?](https://www.americanbar.org/groups/public_education/resources/law_issues_for_consumers/law-and-your-home/contract-include/). Scope, materials, change orders, responsibility and payment terms.
- `far-52-246-12-inspection` — [U.S. Federal Acquisition Regulation, FAR 52.246-12 Inspection of Construction](https://www.acquisition.gov/far/52.246-12). An example of contract-specified inspection and records; not universally binding for residential jobs.
