# 003000 — Engines, Motors, Gearing, and Efficiency

**Track:** Automotive and Small-Engine Maintenance. **Background:** Tire forces and basic mechanical energy. **Purpose:** map energy from fuel or battery to the contact patch.

<!-- BEGIN SPOKEN LECTURE -->

# From Stored Energy to a Turning Wheel

A vehicle's accelerator pedal does not directly command the car to move. It requests something from a chain of energy conversions. In a gasoline car, fuel reacts with oxygen, hot gas pushes pistons, a crankshaft turns, a transmission modifies torque and speed, and the tires push backward on the road. In an electric car, stored electrical energy powers a motor, a gearbox often reduces rotational speed, and the tires provide the same kind of contact force.

Both vehicles obey the same mechanical principles. Their energy sources, conversion losses, control systems, and response to different operating conditions differ. Understanding those differences turns 'the engine feels weak' into questions that can be investigated.

## Torque is not power

Torque describes the turning effect of a force around an axis. A longer wrench produces more torque from the same perpendicular hand force because of its lever arm. A motor or engine delivers torque to a rotating shaft. Power is the rate of energy transfer. For a rotating shaft, power equals torque multiplied by angular speed.

Imagine a motor turning slowly with high torque. It may push hard but perform relatively little work per second if its rotational speed is very low. Another motor can deliver modest torque at much higher speed and transmit substantial power. This distinction explains why a specification that lists only torque, without the speed at which it is produced, tells an incomplete story.

A transmission trades rotational speed against torque. In an ideal lossless reduction, a shaft that turns one quarter as fast can deliver about four times the torque. It has not created energy. Real gears, bearings, seals, and oil consume some of the transmitted power. The gearbox lets a motor operate in a useful speed range while the wheels turn at the speeds appropriate to driving.

## The engine is a heat machine

A common four-stroke spark-ignition engine takes air and fuel into a cylinder, compresses the charge, releases chemical energy through combustion, lets expanding gas do work on a piston, and exhausts the products. The piston moves back and forth while the crankshaft delivers rotation. Some engines use other arrangements, but this is a useful reference model.

Not all of the fuel's chemical energy becomes useful shaft work. Energy leaves as exhaust heat, cooling-system heat, friction, pumping work, and other losses. The cooling system is not an unfortunate accessory bolted onto an otherwise perfect machine; it is necessary because the conversion creates substantial waste heat. An overheated engine can suffer damage even when it still appears to make power.

This also explains why operating conditions change efficiency. Throttle, speed, load, engine temperature, and gear choice affect combustion and losses. The engine may run inefficiently at idle because it consumes fuel while doing essentially no useful propulsive work. A hybrid can sometimes shut off its engine at stops or arrange operation nearer efficient regions, but its total performance also depends on electrical losses and battery management.

## An electric motor uses a different conversion

A traction motor uses electromagnetic forces to produce shaft torque. Power electronics control the currents supplied to it, while the battery stores chemical energy and supplies electrical power through the vehicle's electrical system. There is still heating: motor winding resistance, magnetic losses, inverter switching, mechanical friction, and battery losses matter. But the electric drive generally converts a larger fraction of delivered energy into shaft work than a combustion engine converts from fuel.

An electric drivetrain can often generate useful torque over a wide speed range and may need fewer transmission ratios. Yet wheel force still depends on final gear ratio, tire radius, vehicle traction, and motor control limits. The pedal requests torque subject to those limits. If the tires cannot grip the surface, adding wheel torque need not increase acceleration.

## Braking is an energy decision

Every moving vehicle stores kinetic energy. Slowing it requires removing some of that energy. Friction brakes turn much of it into heat. In a suitable electric or hybrid powertrain, the traction motor can operate as a generator, taking mechanical energy from the wheels and returning part of it to battery storage. This is regenerative braking.

Regeneration is not perfect recovery. Conversion and storage have losses, and battery state, temperature, motor capacity, and traction conditions can limit how much braking energy can be accepted. Friction brakes remain important. The efficiency benefit is especially visible in driving with repeated slowing and acceleration, because otherwise much of that kinetic energy would be discarded as heat at each stop.

## The road sets an additional bill

Even a perfect powertrain would have to overcome rolling resistance, aerodynamic drag, climbing hills, and accelerations. Tire deformation dissipates energy. Moving air out of the way takes more power as speed increases. Climbing stores gravitational potential energy, some of which can be recovered during descent only within the limits of the system.

Thus an efficiency comparison needs a clear boundary. Does the figure measure battery-to-wheels, grid-to-wheels, fuel-tank-to-wheels, or a complete driving cycle? Is recovered braking energy counted? Does it include cabin heating? A single percentage without conditions can mislead even when it comes from a legitimate test.

## Maintenance follows the energy path

If a vehicle becomes less efficient, investigate how the new energy losses could arise. Underinflated tires can increase rolling resistance. Dragging brakes convert motion into unwanted heat. A failing wheel bearing can waste energy and produce noise. A combustion engine with an ignition or fuel-control fault may not convert fuel efficiently. An electric vehicle with a battery or thermal-management issue may restrict performance.

A warning light or low economy figure is not a diagnosis by itself. Comparing symptoms to operating conditions, maintenance history, and appropriate diagnostic readings is more useful than replacing the component with the most dramatic name.

The route from fuel tank or battery to wheel is an energy accounting problem. Torque explains how components push; gearing explains how speed and torque are traded; efficiency tracks what survives each conversion. Once that map is clear, many vehicle complaints become questions about a particular link in the chain.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Equations and worked relation

`P = τω` where power is watts, torque `N·m`, and angular speed `rad/s`. For a hypothetical ideal reducer with ratio `4:1`, output speed is one-fourth input speed and output torque is four times input torque. Real output torque is lower by the mechanical efficiency factor at the stated operating point.

For translational kinetic energy: `E_k = (1/2)mv²`. Doubling speed multiplies kinetic energy by four for fixed mass. Regenerative braking cannot recover all of this stored energy due to losses and limits.

### Interpretation of published efficiencies

FuelEconomy.gov distinguishes energy conversion estimates for conventional and electric vehicles and warns implicitly through drive-cycle methods that energy-to-wheels percentages depend on test boundaries and driving conditions. Its energy-flow diagrams should not be quoted as one immutable efficiency figure for all vehicles.

### Review scope

Vehicle high-voltage systems, brake service, traction controls, and manufacturer procedures are model-specific; this lecture describes the physical energy path rather than repair operations or torque specifications.

## Selected reading and claim sources (non-spoken)

- `doe-ice` — [U.S. Department of Energy, Internal Combustion Engine Basics](https://www.energy.gov/cmei/vehicles/articles/internal-combustion-engine-basics). Four-stroke combustion engine energy flow.
- `fueleconomy-ev` — [U.S. Department of Energy/EPA FuelEconomy.gov, Where the Energy Goes: Electric Cars](https://www.fueleconomy.gov/feg/atv-ev.shtml). Drive-cycle efficiency, losses, regeneration and vehicle resistance.
- `openstax-energy` — [OpenStax College Physics 2e, Kinetic Energy and Work-Energy Theorem](https://openstax.org/books/college-physics-2e/pages/7-2-kinetic-energy-and-the-work-energy-theorem). Mechanical kinetic energy scaling with speed.
