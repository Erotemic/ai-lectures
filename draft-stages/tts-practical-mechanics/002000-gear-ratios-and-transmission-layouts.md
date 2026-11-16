# 002000 — Gear Ratios and Transmission Layouts

**Track:** Mechanical Systems and Repair. **Background:** Torque, force, motion and mechanical advantage. **Purpose:** teach gear ratios as conservation of motion and energy, then connect them to layout and failure modes.

<!-- BEGIN SPOKEN LECTURE -->

# The Gear That Turns Slowly Pushes Hard

Take two gearwheels. One has twelve teeth; the other has thirty-six. Mesh them so the teeth remain engaged. Turn the small gear one full revolution. The large gear turns only one third of a revolution. The motion looks like a trade: we surrender angular speed and gain turning force. That intuition is correct, within the limits imposed by losses. But it is useful to derive it rather than memorize a phrase.

A gear transfers tangential force at the point where its teeth meet. For two externally meshing gears, the tangential velocity at the pitch circles must match in magnitude when there is no slip at the idealized pitch contact. A larger pitch circle covers more distance per revolution, so it rotates more slowly for the same contact speed. If the tooth spacing, or module, is compatible, the ratio of pitch diameters equals the ratio of tooth counts.

## Count teeth, not wishful turns

Let the input gear have twelve teeth and the output gear thirty-six. The output speed is the input speed multiplied by twelve divided by thirty-six. Thus it rotates one third as fast. An external gear pair also reverses the direction of rotation. A small gear driving a large gear is a speed reduction; the reverse is a speed increase.

Now think about torque. Torque is a moment: force multiplied by the perpendicular lever arm. The same tangential tooth force acting at the larger gear's pitch radius produces greater output torque. For an ideal lossless mesh, output torque is three times input torque in our twelve-to-thirty-six example. The product of torque and angular speed is power, so tripling torque while dividing speed by three preserves transmitted power.

An actual mechanism has friction, deformation, lubricant churning, bearing losses and sometimes backlash or sliding contact. Output power is less than input power. If efficiency is ninety percent in this example, ideal three-times torque gain becomes approximately two point seven times at the same speed reduction. Efficiency depends on operating conditions and configuration; ninety percent is an illustrative assumption, not a universal gear rating.

## Compound stages make ratios multiply

Put a twelve-to-thirty-six stage on a shaft that also carries a second small gear. That second gear drives another large gear of the same ratio. There are now two three-to-one reductions, for nine to one overall. An input shaft spinning nine turns drives the final shaft through one turn. If all stages were lossless, final torque could be nine times input torque. With ninety percent efficiency in each stage, overall efficiency is eighty-one percent, not ninety percent. Energy losses compound along with the ratio.

This is why multi-stage transmissions can create high torque reduction in a compact volume, but adding gears is not free. Every stage adds components, alignment requirements, noise sources and possible failures. A design should choose gear sizes and stages by needed speed, torque, packaging, strength and duty cycle.

## An idler changes direction, not the simple overall ratio

Insert a third, intermediate gear between two external gears. It is called an idler when its main purpose is to transfer motion or adjust direction/spacing without creating an additional net speed ratio. The idler's tooth count cancels from the overall ideal ratio between the first and last gears, though it affects layout and tooth contact. Each external mesh reverses direction, so adding an idler changes the final rotation direction compared with a direct mesh.

Do not generalize this cancellation to arbitrary gearboxes. When gears share compound shafts or use internal teeth, the connection topology changes the equations. Planetary gearsets have sun, planet and ring gears; the relationship between their speeds depends on which member is held, driven or used as output. Counting two visible gears without understanding the carrier can produce the wrong answer.

## Gear shape matters as much as ratio

Spur gears have teeth parallel to their shafts. Helical gears have angled teeth and can engage progressively, often changing noise and load distribution, but they create axial forces that bearings must handle. Bevel gears transmit rotation between intersecting axes. Worm gearing may provide large reductions in compact geometry, but it introduces substantial sliding contact and efficiency consequences. The best selection depends on geometry and service conditions.

Backlash is the clearance between mating teeth needed for manufacturing tolerances, lubrication and thermal effects. Too little may bind under operating temperature or deflection; too much can cause lost motion, impacts and positioning error. Wear changes tooth shape, and misalignment moves load toward tooth edges. A gear that looks intact can still function poorly if shafts, housings and bearings no longer hold the correct geometry.

## Read a failure by the way power flows

Suppose a small electric motor drives a heavy load through a gearbox. The output stalls. Does that mean the motor is weak? Perhaps. But the gear train may be binding because of damaged bearings, inappropriate preload, contamination, distorted housing or excessive load. Current draw, motor temperature, output motion, noise and mechanical play help separate cases. A gearbox can also develop noise from pitted teeth or lubrication failure while still transmitting torque.

A diagnostic approach follows the power path. Where does torque enter? Which shafts must move together? Which gears rotate relative to each other? Which parts support the tooth forces? If you disconnect a load, does the upstream system behave differently? These are reasoning questions; procedures for physically testing energized or moving machinery need equipment-specific controls.

## Gearboxes teach a broader engineering habit

A transmission does not create power. It trades angular speed for torque and sometimes reverses or redirects rotation. Its ratios are defined by tooth counts and topology; its losses and failures depend on contact mechanics, lubrication and structure. Once you think in terms of power paths, the same framework applies to bicycle drivetrains, winches, clocks, automotive transmissions, robot joints and industrial reducers.

Next time you see a machine that moves something heavy and slowly, ask how fast the driving motor turns and how many stages of ratio sit between the motor and the load. The machine will begin to reveal its logic, one shaft at a time.

<!-- END SPOKEN LECTURE -->

## Technical companion: ratio and power accounting

For ideal external gears with teeth `z1` (driving) and `z2` (driven): `ω2/ω1 = -z1/z2`, `|τ2/τ1| = z2/z1` for zero losses; `P = τ ω`. With efficiency `η`, output torque magnitude is `η*(z2/z1)*input torque` under suitable steady operation. For compound stages, multiply speed ratios and efficiencies separately. Illustration: two 3:1 stages each at 90% efficiency yield 9:1 reduction and 81% net efficiency.

**Cautions of scope:** An idler cancels from an uncomplicated simple external gear train's overall magnitude ratio, not from every multi-shaft or planetary configuration. Real teeth transmit nontrivial radial/axial forces; shaft and bearing design is not determined by tooth count alone.

**Reading:** OpenStax mechanics chapters on rotational motion, work and simple machines provide the underlying moment and power framework. Gear type and rating details depend on manufacturer data and technical gear standards; this introduction is conceptual, not a design standard.

**Exercise:** Draw a three-gear simple train with 12, 18 and 36 teeth. Find the last shaft's speed ratio and direction. Then replace the middle gear with a compound shaft containing a second gear, and explain why the calculation must change.

## Selected reading and evidence (non-spoken)

- `mit-gear-ratios` — [Martin Culpepper, MIT OpenCourseWare 2.72 Elements of Mechanical Design, Lecture 12: Transmission Ratios for Serial Gears](https://ocw.mit.edu/courses/2-72-elements-of-mechanical-design-spring-2009/83d81a6f63d1c6f0fb775c08b207bc51_MIT2_72s09_lec12.pdf). Tooth-count and series gearing ratio derivations.
- `mit-gear-trains` — [MIT OpenCourseWare 2.00AJ, Gears and Linkages (2009)](https://ocw.mit.edu/courses/2-00aj-exploring-sea-space-earth-fundamentals-of-engineering-design-spring-2009/e8c25391a19f4a1ef3c427017307f509_MIT2_00AJs09_lec07.pdf). Gear trains, ideal power, efficiency and torque.
- `openstax-machines` — [OpenStax College Physics 2e, Simple Machines](https://openstax.org/books/college-physics-2e/pages/9-5-simple-machines). Mechanical advantage and energy conservation.
