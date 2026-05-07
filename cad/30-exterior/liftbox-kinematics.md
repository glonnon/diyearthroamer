# Bike Lift-Box Kinematics & Drive (closes O5)

## Geometry

Box (per REQUIREMENTS.md §20):

- Interior clear: 75" L × 50" W × 36" H (1,905 × 1,270 × 914 mm)
- Construction: 1.5" sq aluminum tube + 0.090" 5052 sheet
- Estimated empty box mass: 200 lb (90 kg)
- Load: 3 bikes @ 35 lb each + accessories ≈ 130 lb (60 kg)
- **Design lift mass: 350 lb (160 kg)** with 25% safety factor → 437 lb

Travel:

- Stowed (travel) position: bottom of box at ≥ 18" road clearance
  (457 mm above ground). Top of box at ~54" + 18" = 72" off ground
  → tucks into the tail-taper envelope with departure-angle margin.
- Loaded position: bottom of box at ground level for walk-on
  loading, no ramp needed.
- **Total travel: 18" (457 mm) vertical.**

## Mechanism options

### Option A — Parallelogram + dual linear actuators

Two parallel four-bar linkages, one each side, driven by paired
electric linear actuators (synchronized via simultaneous-drive control
or mechanical tie bar).

```
        ┌─────box────┐
       /             /
      / arm         / arm
     /             /
    pivot ─────  pivot       ← chassis carrier
     \             \
      ↘ actuator   ↘
```

- Lift force per side at worst case (low position, max moment arm):
  ~F = (W/2) × (Larm / Lstroke) ≈ 350/2 × 1.4 ≈ 245 lbf per actuator
  for typical 4-bar geometry.
- **Margin: spec dual 1,500-lb-class actuators** (Progressive Auto
  PA-04, Firgelli Optimus, or Linak LA36) → 6× margin.

### Option B — 12V/24V hydraulic micro-pack + single/dual cylinders

Power pack drives one or two single-acting cylinders.

- Higher force capability (5,000+ lb easily).
- Quieter and smoother under load.
- Adds: pump, reservoir, valves, hoses, fluid filter, drip tray.

### Option C — Scissor lift

Mechanical advantage varies through stroke; force peaks at low
position. Either electric or hydraulic drive.

- Compact stowed envelope.
- Higher fab complexity; pivots in dirt = wear.

## Comparison

| Criterion | A: Dual actuators | B: Hydraulic | C: Scissor |
|---|---|---|---|
| Cost (parts) | $$ | $$$ | $$ |
| Fab complexity | Medium | High | High |
| Maintenance | Simple (no fluid) | Fluid changes, leaks | Pivots, grease |
| Failure modes | Actuator dies → manual crank | Hose burst, pump fail | Multiple pivots fail |
| Noise | Low (modern marine actuators) | Lowest | Medium |
| Off-road robustness | High (sealed marine) | Medium (hose chafe) | Medium |
| Weight | Lowest | Highest (fluid + pump) | Medium |
| Power draw | 5–10 A @ 24V momentary | 30–60 A @ 24V momentary | Either |
| Manual override | Crank end of actuator (Linak/PA option) | Hand pump | Hand crank |

## Decision

**Option A — dual electric linear actuators** (Linak LA36 or
Progressive Auto PA-04, IP67 marine, 1,500 lbf class, 18" stroke,
synchronous controller).

Rationale:

- Off-road robustness without fluid in the system.
- Lower maintenance burden over the life of the vehicle.
- Modern marine actuators are quiet enough.
- Simpler manual override (mechanical crank on most LA36/PA-04
  variants).
- Power draw fits within the 24V sub-bus without burdening the bank.

## Safety + interlocks

- Mechanical travel locks at both ends of stroke (do not rely on
  actuators alone).
- Limit switches (top/bottom).
- Pinch sensors on the upper edges.
- Vehicle-in-park interlock (CAN signal or door-cluster relay).
- Rear-light repeaters on the box; lights on whenever box is below
  stowed position.
- Manual crank tool stowed inside the box.

## Departure-angle envelope

With box stowed at 18" clearance and the tail taper of the shell
(`SPECS.md`), departure angle in CAD will be verified ≥ 28°. The lift
arms tuck under the shell taper rather than below it.

## Files

- This decision is captured in **ADR-0012**.
- Mechanism CAD lives in `cad/30-exterior/liftbox/` (TBD):
  `liftbox-frame.FCStd`, `liftbox-arms.FCStd`, `liftbox-carrier.FCStd`.
- Force/stroke calc spreadsheet: `cad/30-exterior/liftbox-forces.csv`
  (TBD once final geometry locked).
