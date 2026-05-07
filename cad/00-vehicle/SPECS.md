# F550 Crew Cab Master Sketch — Dimensional Spec

All dimensions in **mm** unless otherwise noted. Origin = center of
**rear axle** at ground level. **+X forward, +Y up, +Z to driver
side (LH).** This is the master geometry every other CAD subsystem
references.

Numbers below are from Ford body-builder data, public Liquid Springs
install dimensions, and 41" tire specs. Replace with measured values
once the chassis is on hand.

## Wheelbase + axles

| Param | Value (mm) | Value (in) | Note |
|---|---|---|---|
| Wheelbase (baseline) | 4,470 | 176 | Common for 21' campers; alternates 169 / 192 |
| Front axle X | +4,470 | +176 | from rear-axle origin |
| Rear axle X | 0 | 0 | origin |
| Track width | 1,930 | 76 | 41" tires on stock-width axles |

## Tires (41" / 1041 mm OD)

| Param | Value (mm) | Note |
|---|---|---|
| Tire OD | 1,041 | 41" |
| Tire section | 343 | 13.5" wide |
| Loaded radius | 495 | with 5% deflection |
| Hub center Y | 495 | from ground |

## Frame

| Param | Value (mm) | Value (in) | Note |
|---|---|---|---|
| Frame top Y (above ground, unloaded) | 1,016 | 40 | with Liquid Springs ride |
| Frame outside-to-outside Z | 864 | 34 | typical F550 |
| Frame rail height | 254 | 10 | nominal |
| Frame end (rear) X | -1,524 | -60 | beyond rear axle, varies w/ WB option |

## Crew cab

| Param | Value (mm) | Value (in) | Note |
|---|---|---|---|
| Cab back-of-cab X | +3,200 | +126 | from rear axle (function of WB) |
| Cab front-of-cab X | +4,830 | +190 | |
| Cab roof Y (top) | 2,180 | 86 | exterior |
| Cab width Z | 2,030 | 80 | exterior |
| Crew cab interior length | 1,630 | 64 | back-of-cab to firewall |

## Liquid Springs CLASS

- Ride-height range: ±50 mm (±2") from neutral.
- Adds ~25 mm to nominal frame top vs OEM springs at neutral.

## Habitat shell (Globe Trekker 21' + tail taper)

| Param | Value (mm) | Value (in) | Note |
|---|---|---|---|
| Shell footprint length | 6,400 | 252 | 21' habitat |
| Tail taper additional | 600 | ~24 | departure-angle wedge |
| Total exterior length | 7,000 | ~276 | ~23' total |
| Shell width (exterior) | 2,438 | 96 | typical Globe Trekker |
| Shell width (interior) | 2,235 | 88 | composite skin allowance |
| Shell height (exterior, less cabover) | 2,135 | 84 | |
| Cabover nose extension over cab | 760 | 30 | |
| Cabover height interior | 760 | 30 | sleeping clearance, see `cad/20-shell/cabover-fit.md` |

## Stack-up (vertical, ground to top of shell)

```
Ground                                  Y = 0
Tire OD top                             Y = 1,041
Frame top (unloaded)                    Y = 1,016 (sits inside tire envelope)
+ Subframe height (Globe Trekker OEM)   ~+150
+ Shell floor structure                 ~+50
Shell interior floor                    Y ≈ 1,216
Shell interior ceiling (less cabover)   Y ≈ 3,351 (≈ 132" ≈ 11')
Shell exterior top                      Y ≈ 3,500
```

Walking-zone headroom target ≥ 1,930 mm (76"). Stack delivers ~2,135
mm (84") interior height — comfortable.

## Subframe interface

OEM Global Trekker subframe (ADR-0003) — pull vendor STEP for exact
mount-point pattern. Owner-side outriggers reference these mounts.

## Departure angle envelope

With ~610 mm (24") of taper at the tail and a ~1,524 mm (60") rear
overhang past the rear axle, departure angle (at unloaded ride height)
is approximately:

```
α = atan( (frame_top + subframe + shell_floor) / overhang )
  ≈ atan(1,216 / 1,524) ≈ 38.6°
```

After the lift-box (ADR-0006) is added, target stays ≥ 28°. Verify
in CAD against the box stowed envelope.
