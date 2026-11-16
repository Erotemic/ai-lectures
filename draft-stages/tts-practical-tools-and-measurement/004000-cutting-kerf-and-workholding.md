# 004000 — Cutting, Kerf, and Workholding

**Track:** Tools, Measurement, and Workmanship. **Background:** Accurate reference faces, layout, and measurement uncertainty. **Purpose:** teach a cut as a controlled geometry-and-force problem rather than simply a line to follow.

<!-- BEGIN SPOKEN LECTURE -->

# The Cut Has a Width, and the Material Has a Mind of Its Own

Suppose you have a board exactly one meter long and want two pieces each half a meter long. Mark the midpoint, put the saw blade directly on the line, and cut. The two pieces cannot both be exactly half a meter. The blade turns some wood into sawdust. That missing band is the *kerf*, and it matters whenever the finished dimensions must add up accurately.

A cut has at least three geometries: the intended finished edge, the material removed by the tool, and the direction in which the tool actually moves. A pencil line is not infinitely thin. A saw blade may wander, deflect, or tilt. A workpiece may move under load. The better approach begins by identifying which side of the line belongs to the finished piece. Place the kerf on the waste side, and keep the measured dimension in the material you intend to retain.

## Marking is not the same as locating

A tape measure gives a number; a square transfers a reference; a knife or pencil marks a location. But the tool that makes the cut needs its own reference. You can guide a hand saw from a marked line, run a circular saw against a straightedge, or use a miter saw fence and stop. These strategies produce different kinds of error. Following a drawn line depends on eyesight and hand control. Running against a reliable mechanical guide reduces some of that variation, but introduces the need to position the guide correctly relative to the blade.

Suppose the saw's cut removes three millimeters. If you cut a long board into several precisely measured pieces and place each new mark from the previous cut, errors and kerf losses accumulate. A cut list and a fixed origin reduce this uncertainty. In repetitive work, a physical stop can make part lengths consistent, provided the stop does not trap the offcut against a moving blade or create another mechanical hazard. Precision is not a property of the tape alone. It is a property of the entire referencing process.

## The blade works against the material

Different cuts ask the tool to break material in different directions. Wood has grain: ripping parallel to fibers is not the same as crosscutting across them. Metal, plastic, and composite materials have their own chip formation, heat, and edge behaviors. A saw with the wrong tooth geometry can tear fibers, generate excess heat, or demand excessive feed force. A dull edge may create more friction and unpredictable forces even if it still seems capable of separating the material.

Think about what happens at the cutting edge. The tool applies force over a small region, deforming and fracturing or shearing the material. That produces a reaction force against the tool. With a hand saw, your arm stabilizes the response. With a powered circular saw, blade speed, tooth contact, and the way the workpiece closes around the blade can create binding or kickback. The operator's job is not just to guide the blade; it is to arrange the support so the material does not close onto it.

## Holding the work is part of the operation

Imagine cutting a board resting across two sawhorses with a gap in the middle. As you finish the cut, the board's own weight may cause the opening to close or the offcut to pivot. A cut supported in the wrong places can pinch the blade. For a different cut, a poorly supported offcut may tear fibers from the finished edge as it falls. You need to predict which piece stays stable, where the waste moves, and whether the tool's path remains clear.

Clamps, vises, bench hooks, fences, sacrificial backing, and supports are ways of constraining degrees of freedom. A clamp doesn't automatically make an operation sound. It must resist the actual forces without obstructing the tool, guard, or escape path for the waste. A long piece may require support at both its free ends. Thin material may need a backing board to prevent chatter or breakout. A part that is secure under downward force may still twist when a blade enters from the side.

Workholding is also a way to protect your hands from becoming the only fixture. If your grip must be close to the cutting path to keep the piece still, redesign the setup. A machine's guarding, riving knife, and anti-kickback provisions are not optional performance accessories; they are part of the intended operating system. The manufacturer's tool-specific method matters because a table saw, miter saw, jigsaw, and portable circular saw handle the interaction of blade and work in different ways.

## A good cut can still be the wrong cut

Accuracy is more than a clean edge. If a frame requires two rails to be the same length, equal lengths may matter more than either rail matching a rounded nominal number. If an opening must receive a fitted part, clearance, out-of-square conditions, and thermal or moisture movement may matter more than a perfectly straight isolated cut.

Before cutting, ask: Which face is the reference? Which portion is the keeper? Where does the kerf go? What holds both the keeper and waste as the cut separates them? What tolerances actually affect assembly? And how will I check the piece after cutting? Those questions sound deliberate because they are. But once practiced, they become faster than trying to rescue an inaccurately cut part.

An accurate cut is a controlled transformation of a known piece of stock into a known shape, with a predictable loss of material. The saw performs the removal. Layout and workholding make that removal repeatable.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Kerf accounting

If a stock piece is \(L\) long and each full-width separation removes kerf \(k\), the sum of the kept segment lengths plus discarded segment lengths is \(L - nk\) after \(n\) cuts through the stock, neglecting trimming and measurement errors. Example: a 1000 mm piece cut once with a 3 mm kerf cannot produce two 500 mm finished pieces; at most their lengths sum to 997 mm. Nominal blade thickness and effective kerf can differ because of tooth set, runout, and deflection; test with scrap when tolerances matter.

### Precut worksheet

| Question | Record |
|---|---|
| Finished reference faces and dimensions | |
| Retained side and waste side | |
| Expected kerf and cut angle | |
| Workpiece support and allowed waste motion | |
| Guide or fence location | |
| Postcut measurement and tolerance | |

**Equipment-specific guardrails:** Follow the tool manufacturer's guard, blade, fence, riving-knife, clamp, feed and support instructions. Do not improvise a configuration that traps stock between fence and blade or defeats guards. Tool choice and procedures for metals, plastics, ceramics, and composite dust require separate assessment.

## Selected reading and claim sources (non-spoken)

- `osha-table-saws` — [OSHA, Machine Guarding eTool: Table Saws](https://www.osha.gov/etools/machine-guarding/saws/table). Saw binding, kickback, guides, stock support and guarding.
- `osha-hand-power-tools` — [OSHA, Hand and Power Tools (OSHA 3080)](https://www.osha.gov/sites/default/files/publications/OSHA3080.pdf). Tool guarding, securing work with clamps and correct tool operation.
