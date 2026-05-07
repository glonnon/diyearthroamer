# Cabover Platform — Parametric Module Spec

The bed support structure forward of the main shell, sitting over
the F550 crew cab roof. Supports the **Olympic queen** mattress
(66" × 80", ADR-0011) transverse across the cabover. Includes the
gasketed cab pass-through, headboard with USB-C/PD + reading lights
+ small storage shelves, side cubbies, and an upholstered ceiling
panel.

## Envelope

| Param | Value (mm) | Value (in) | Note |
|---|---|---|---|
| Cabover platform length (X, vehicle longitudinal) | 1,960 | 77 | mattress depth + 1" headboard margin |
| Cabover floor width (Z, transverse) | 2,235 | 88 | shell interior width |
| Mattress envelope (W × L) | 1,676 × 2,032 | 66 × 80 | Olympic queen, transverse |
| Sleep clearance (mattress to ceiling) | 510 | 20 | 30" cabover − 8" mattress − 2" base |
| Pass-through opening | 600 × 600 | 24 × 24 | gasketed insulated door at cabover front bulkhead |
| Bed lower edge above main floor | 990 | 39 | mounted step + grab handle |
| Step height (2-step) | 200, 200 | 8, 8 | retractable or molded steps |

## Cab pass-through detail

- **Location:** front bulkhead of cabover, centered in width.
- **Construction:** composite plug door (similar to entry door but
  smaller), Sika-bonded into cabover front face; 4-side compression
  gasket.
- **Latch:** twist-cam from inside cab; secondary detent lock for
  travel.
- **Insulation:** 50 mm closed-cell foam core + thermal break around
  perimeter to limit condensation.
- **Power crossing:** Cat6 + 12V + 24V wiring crosses through a
  gasketed grommet adjacent to the door (not through the door).
- **CO/smoke detector:** placed in cabover; one shared with main cab
  is acceptable per RVIA.

## Construction

- **Platform structure:** 6061 aluminum 2"×2"×1/8" tube ladder
  spanning the cabover floor width; bonded + bolted to shell
  composite inserts at front, side, and rear.
- **Floor deck:** 18 mm Baltic birch ply over the aluminum ladder,
  bonded with Sika 252.
- **Ventilation:** mattress base is slatted ply or coir mat for
  airflow under the mattress (condensation control on cold cabover
  floor).
- **Side cubbies:** ~250 mm deep cubbies along port and curb sides
  for books, water bottles, charging gear; LED accent.
- **Headboard:** padded fabric over 9 mm ply; includes:
  - 2× USB-C PD 45W
  - 2× LED reading lights (dimmable, gooseneck)
  - Master switch panel (lights + fan + thermostat shortcut)
  - Phone holder + small shelf
- **Egress window:** required by RVIA — opening dual-pane acrylic
  on one side wall, sized ≥ 22" × 19" clear (FMVSS / RVIA spec).
- **Trim:** upholstered fabric ceiling panel; carpeted side walls
  for sound damping.

## Hardware

| Item | Spec |
|---|---|
| Bed slats / coir mat | ventilated under mattress |
| Reading lights | Lumitec or Imtra dimmable gooseneck |
| Egress window | Tern / Seitz dual-pane, opening + screen |
| Pass-through door | composite plug, gasket + twist-cam |
| Step + grab handle | retractable step + 12" stainless grab |
| Mattress | Olympic queen 66"×80", custom latex/hybrid 8" |

## Power & data rough-ins

| Service | Where |
|---|---|
| 24V LED ceiling | dimmable warm/cool |
| 24V LED accent (cubbies) | toe-kick / side cubbies |
| 24V reading lights | both sides of headboard |
| 120V GFCI | one each side of bed |
| USB-C PD 45W | both sides of headboard |
| Cat6 to TV | curb-side (TV swivel mount) |
| Speaker wires | 2× ceiling speakers |
| HVAC vent | hydronic fan-coil + MaxxAir intake |

## Weight estimate

| Component | Mass (lb) |
|---|---|
| Aluminum ladder + ply deck | 90 |
| Mattress (Olympic queen, 8" latex) | 80 |
| Headboard + electronics + finish | 35 |
| Side cubbies + trim + carpet | 25 |
| Pass-through door + gasket | 12 |
| **Cabover total** | **~242** |

(`weight/master.csv` has 90 + 80 + 60 = 230 lb across three rows; 
update with cubbies/trim row at next pass.)

## CAD files (planned)

```
cad/70-interior-cabinetry/cabover/
  SPECS.md
  build-cabover.FCMacro
  cabover-master.FCStd
```
