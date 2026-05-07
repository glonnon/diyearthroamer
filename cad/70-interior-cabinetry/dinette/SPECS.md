# Dinette — Parametric Module Spec

Port-side dinette opposite the galley. Two DOT seats (forward-facing,
3-point belts anchored to shell hard points). Lagun-mounted table.
Storage under benches; integrated drawer fridge (Vitrifrigo DP150i)
at the front of the dinette run.

## Envelope

| Param | Value (mm) | Value (in) | Note |
|---|---|---|---|
| Dinette run length | 2,000 | 78.7 | along port wall |
| Bench depth | 460 | 18 | seat cushion stretches to 19 in |
| Bench seat height | 432 | 17 | finished, w/ 25 mm cushion |
| Backrest height (above seat) | 380 | 15 | shaped lumbar |
| Table top above floor | 720 | 28.3 | typical RV dinette dining height |
| Table size | 800 × 600 | 31.5 × 23.6 | rounded corners |
| Lagun mount post | 32 dia | 1.25 | swing + slide |

## Module breakdown (port side, front-to-rear)

| # | Module | Width (mm) | Notes |
|---|---|---|---|
| 1 | Fridge cabinet | 540 | Vitrifrigo DP150i drawer fridge (530 mm wide); ventilated, top + bottom airflow |
| 2 | Front bench | 730 | DOT seat 1, lift-top + drawer-front access |
| 3 | Center storage tower | 0 | (none — table sits between benches) |
| 4 | Rear bench | 730 | DOT seat 2, lift-top + drawer-front access |
| **Sum** | | **2,000** | |

## Construction

Hybrid aluminum + Baltic birch ply per REQUIREMENTS.md §19.

- **Aluminum frame:** 1.5"×1.5"×1/8" 6061 angle ladder per bench;
  cross members welded or rivnut + bolt for serviceability.
- **Plywood:** 18 mm Baltic birch sides + back; 12 mm seat decks;
  9 mm front faces with HPL/Fenix laminate.
- **DOT seat reinforcement:**
  - 4× M10 bolt-through points per seat back, into shell composite
    inserts pre-installed by Global Trekker; spec at 4,000 lbf each
    (FMVSS 207/210).
  - 3-point belt upper anchor at shell wall insert; lower anchors
    at frame ladder hard points.
- **Storage access:** lift-top panels on slides (gas struts) +
  optional drawer-front pull-out for shoes / small gear.

## Fridge cabinet detail

| Param | Value |
|---|---|
| Fridge | Vitrifrigo DP150i drawer (130 L total: 95 L fridge + 35 L freezer) |
| Voltage | 12 V or 24 V (24V preferred to match sub-bus) |
| Power | ~50 W avg, ~85 W peak |
| Vent | bottom intake + top exhaust, both ducted to outside via roof or wall vent |
| Slide-out service tray | yes, behind front face |
| Door swing | drawer (no swing); zero clearance into aisle |
| Lock | freezer-rated detent; secondary travel pin |

## Hardware

| Item | Spec |
|---|---|
| Lift-top hinges | Sugatsune piano + soft-close |
| Bench gas struts | 60–80 lbf, locking |
| Drawer slides (where used) | Accuride 3832 locking |
| Belt anchors | Schroth 3-point (FMVSS 209/210 stamped) |
| Table mount | Lagun Marine swivel-slide (post + jaw) |
| Cushion fabric | marine vinyl or Sunbrella; 50 mm foam, vacuum-bagged |

## Power & data rough-ins

| Where | Service |
|---|---|
| Each seating position | 1× USB-C PD 45W; 1× 120V GFCI |
| Behind table | Cat6 to TV; 12V outlet |
| Below fridge | dedicated 24V breaker |
| Over fridge top (under window) | LED reading strip, dimmable |

## Weight estimate

| Component | Mass (lb) |
|---|---|
| 2× DOT bench frames + seat decks | 75 |
| Cushions + fabric | 35 |
| Fridge cabinet (frame + ply + slides) | 45 |
| Vitrifrigo DP150i drawer fridge | 110 |
| Table + Lagun mount | 25 |
| Hardware + finish | 15 |
| **Dinette total** | **~305** |

`weight/master.csv` already has `Dinette benches + table + cushions`
at 200 lb (excluding fridge); fridge tracked separately at 110 lb.

## CAD files (planned)

```
cad/70-interior-cabinetry/dinette/
  SPECS.md                        this document
  build-dinette.FCMacro           parametric generator (next iteration)
  dinette-master.FCStd            assembly snapshot
  modules/
    fridge-cabinet.FCStd
    bench-front.FCStd
    bench-rear.FCStd
    table.FCStd
```
