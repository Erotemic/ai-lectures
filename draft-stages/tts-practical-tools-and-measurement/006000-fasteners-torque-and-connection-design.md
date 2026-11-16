# 006000 — Fasteners, Torque, and Connection Design

**Track:** Tools and Measurement. **Background:** Layout, drilling, and cutting. **Purpose:** learn to reason about clamping force, joint geometry, and why fasteners fail.

<!-- BEGIN SPOKEN LECTURE -->

# The fastener is only part of the connection

Two boards are held together by a screw. From a distance, it looks as though the screw does all the work. In reality, the connection includes threads, wood fibers, head bearing, friction between the boards, distances to nearby edges, moisture conditions, and the direction of the applied force. Change any of these and the same screw may perform very differently.

That is the first principle of fastening: specify and inspect a connection, not merely a metal object. A screw advertised as strong is not automatically suitable for carrying a beam. A bolt tightened hard is not automatically secure against vibration. A nail that resists lateral movement well may be much weaker when the load tries to pull it straight out. Different fasteners create different mechanical systems.

## Pulling, sliding, and prying

Imagine two plates joined by a bolt. If a force tries to slide one plate sideways, the joint experiences shear. If it pulls the plates apart along the bolt's axis, the joint experiences tension. If the force acts away from the plane of contact, it can create a prying moment that increases tension in part of the joint. A successful design identifies which of these actions actually occurs.

In some bolted assemblies, deliberate preload clamps the surfaces together. Friction between the clamped surfaces can then resist a portion of the sliding force. But that model requires properly controlled preload and appropriate surface conditions. Other connections are designed to transmit force through direct bearing of the bolt or screw against the surrounding material. You cannot freely substitute one model for the other.

Wood behaves differently from steel. Screws can transmit axial load through thread engagement, but the surrounding wood can split or crush. Nails can deform and share lateral load across a pattern; their withdrawal behavior depends on many variables. A structural connector may call for a particular fastener diameter, length, head, coating, and installation pattern because its tested capacity depends on those details. Filling every visible hole with whichever screws are nearby is not equivalent to following its specified fastening schedule.

## Torque is not the same thing as tension

A wrench applies torque, a turning moment. Tightening a bolt converts some of that rotation into axial stretch of the fastener and compression of the joint. Yet much of the applied torque is spent overcoming friction in threads and under the head. Change lubrication, thread finish, surface coatings, or washer geometry and the same wrench reading can produce very different clamp loads.

For that reason, torque specifications belong to a particular fastener, joint, lubrication condition, and tightening sequence. A generic rule of thumb cannot replace manufacturer instructions for critical connections. Over-tightening can strip a wood screw, crush a soft gasket, crack brittle material, distort a bearing seat, or yield a bolt. Under-tightening can permit movement and progressive loosening. The right result is neither maximum torque nor a satisfying sensation in the hand; it is the intended joint condition.

Suppose a bolt must hold two sheets in position. Tightening until the sheets meet may be sufficient for one noncritical fixture. A high-preload structural joint or a gasketed flange has different requirements. On a gasket, the sequence of tightening may matter as much as the final torque: tightening one bolt fully before its neighbors can tilt the flange and compress the seal unevenly.

## Geometry controls the outcome

A pilot hole is not simply a convenience. In wood it changes how much of the driving force expands the surrounding fibers. In metal, a clearance hole permits a bolt shank to pass while the threads engage a nut or tapped feature. Countersinking creates a seat for a tapered head; counterboring creates a cylindrical recess. These are distinct geometries, and choosing the wrong one can concentrate force in a material that does not tolerate it.

Edge distance matters because loads must spread into the surrounding material. A fastener set too close to a board edge may split it. A masonry anchor placed near a corner may break out a wedge of substrate rather than fail in the steel. A sheet-metal screw in a thin sheet may strip before the screw itself reaches a significant stress. If you want higher capacity, adding a larger fastener in the same vulnerable location might make the failure worse.

Fastener length is also functional. A screw that barely enters the receiving board may not develop enough thread engagement. An excessively long screw can emerge into a hidden wire, pipe, or finished surface. In dissimilar materials, thermal movement and corrosion compatibility can influence long-term behavior. Coatings that resist one environment may be inappropriate in contact with certain treated woods or incompatible metals.

## Failure tells a story

A backed-out screw suggests repeated movement, insufficient locking, or insufficient engagement. A crushed surface suggests excessive contact pressure. A split board suggests inappropriate geometry, moisture movement, or force application. A fastener that has broken across its shank may have been overloaded in one event, or it may have accumulated fatigue damage from repeated cycles. A rusted fastener can lose cross-section even if the connection looks tight from the front.

When examining a failed joint, preserve the evidence before replacing hardware. Note the direction of load, the condition of the holes, whether parts moved, and whether surrounding material is cracked or distorted. Compare the original connection with a drawing or installation instruction if one exists. A repair that changes only the fastener but ignores the load path repeats the same experiment.

A good fastening decision begins with a statement of purpose: these parts must stay aligned, carry this kind of load, tolerate these movements, and remain inspectable. That description determines the fastener, hole, torque procedure, spacing, and test of success. The screw is visible. The load path is what makes the connection work.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Three load cases

- **Axial pull:** threads, embedment depth and substrate govern withdrawal or pullout.
- **Lateral shear:** bearing, shank bending, hole condition and group geometry govern response.
- **Moment/prying:** eccentric force causes different tension at different connection points; inspect edge distances and connector geometry.

### Worked qualitative example

A hinge has two screws close together near a soft wood edge. Increasing screw diameter alone may increase splitting risk. Compare the alternatives of a manufacturer-approved longer fastener into sound backing, a repaired substrate, and redistributing loads with a suitable plate.

**Review boundary:** Torque-preload relationships are friction-sensitive. Use engineered schedules and manufacturer instructions for structural, pressure, rotating or critical connections. Tool technique does not establish design capacity.

## Selected reading and evidence records (non-spoken)

- `rammer-fastenings` — [Douglas R. Rammer, Fastenings, Wood Handbook ch. 8, USDA Forest Service Forest Products Laboratory (2010)](https://research.fs.usda.gov/treesearch/37424). Fastener types, withdrawal versus lateral loading, splitting, connector assumptions.
- `openstax-torque` — [OpenStax College Physics 2e, The Second Condition for Equilibrium](https://openstax.org/books/college-physics-2e/pages/9-2-the-second-condition-for-equilibrium). Torque and perpendicular moment arm.
