# Galley — Parametric Module Spec

Aisle galley along the curb (right) side of the 21' shell. Hybrid
construction (REQUIREMENTS.md §19): 6061 aluminum 1.5"×1.5"×1/8"
angle skeleton + Baltic birch ply panels and faces.

## Overall envelope

| Param | Value (mm) | Value (in) | Note |
|---|---|---|---|
| Galley run length | 2,200 | 86.6 | along curb side |
| Counter depth | 610 | 24 | standard |
| Counter height (top of finished surface) | 914 | 36 | ergonomic for cooking standing |
| Toe kick height | 100 | 4 | recessed 75 mm (3") |
| Upper cabinet bottom (above counter) | 460 | 18 | clearance to small appliances |
| Upper cabinet height | 460 | 18 | |
| Upper cabinet depth | 305 | 12 | |
| Backsplash height | 150 | 6 | |

## Module breakdown (curb side, front-to-rear)

| # | Module | Width (mm) | Width (in) | Notes |
|---|---|---|---|---|
| 1 | Pantry tower | 460 | 18 | full-height, pull-out wire bins, near galley front |
| 2 | Drawer tower (cookware) | 610 | 24 | 4-drawer Movento, soft-close, travel-rated locks |
| 3 | Cooktop module | 610 | 24 | induction 2-burner; range hood above |
| 4 | Sink module | 610 | 24 | undermount stainless 16"×18"; cover board |
| 5 | Fridge cabinet | 610 | 24 | drawer fridge (Vitrifrigo DP150i) or cabinet fridge |
| **Sum** | | **2,900** | **114** | over budget — see resolution |

### Resolution

114" exceeds the 86.6" budget. Reduce as follows:

| # | Module | Final width (mm) | Final width (in) | Note |
|---|---|---|---|---|
| 1 | Pantry tower | 380 | 15 | narrower; tall + deep + lazy-Susan style |
| 2 | Drawer tower (cookware) | 460 | 18 | three deep drawers |
| 3 | Cooktop | 510 | 20 | 2-burner induction (Empava 20") |
| 4 | Sink module | 460 | 18 | single bowl 14"×16"; cover board |
| 5 | Fridge cabinet | 460 | 18 | tall narrow drawer fridge OR move fridge across aisle |
| **Sum** | | **2,270** | **89** | within tolerance |

If fridge moves to **port side** (across the aisle, in a built-in
between dinette and bath), galley simplifies further:

| # | Module | Final width (mm) | Final width (in) |
|---|---|---|---|
| 1 | Pantry tower | 460 | 18 |
| 2 | Drawer tower | 610 | 24 |
| 3 | Cooktop | 610 | 24 |
| 4 | Sink module | 510 | 20 |
| **Sum** | | **2,190** | **86** | fits the 86.6" run |

**Recommended:** fridge across the aisle (Vitrifrigo DP150i drawer
fridge, 21" wide, integrated under counter on the port side near the
dinette). Galley curb side is sink + cooktop + drawer tower + pantry.

## Frame skeleton (per module box)

Aluminum 1.5"×1.5"×1/8" angle "ladders":

```
     Top rail (front)
       +----------+
      /|         /|
     / |        / |
    +----------+  |
    |  +-------|--+   ← captures plywood back panel
    | /        | /
    |/         |/
    +----------+
     Bottom rail (front)
```

- 4 vertical posts at corners
- 2 top rails (front/back)
- 2 bottom rails (front/back) — bottom rail sits on the toe-kick
  riser
- Cross members as needed for drawer slide rails

Plywood panels (18 mm Baltic birch):

- Side panels (left/right) captured between vertical angle posts
- Back panel
- Bottom panel (inside the frame, drawer support)
- Drawer faces and tops

## Hardware

| Item | Spec |
|---|---|
| Drawer slides | Blum Movento full-extension, soft-close + travel latch |
| Hinges | Blum Clip-Top blumotion + secondary catch |
| Latches (travel doors) | Southco compression |
| Faucet | marine pull-down + dedicated filtered tap |
| Sink | undermount stainless 14"×16" single bowl |
| Cooktop | Empava 20" 2-burner induction (120V/220V) |
| Range hood | recirculating + ducted option, dimmable LED |

## Travel locks

Every drawer and door has a positive lock for travel:

- Drawers: Movento + secondary push-latch (Tip-On Blumotion blocks
  open when not pressed)
- Doors: Southco compression on travel; Blum hinge for daily use
- Pantry pullout: positive detent at fully-closed; secondary cabin
  latch when underway

## Counter

Solid surface (Corian, ~12 lb/ft²) or compact laminate (Fenix NTM,
~10 lb/ft²). Avoid stone (≥18 lb/ft² + brittle).

Sink + cooktop cutouts on a single piece, sealed underneath with
silicone bead at the wall and bonded to backsplash.

## Lighting

- Under-cabinet LED strip, 24V, 2700K + 4000K dual, dimmable
- Range hood LED
- Toe-kick accent strip (low setting, night use)

## Power & water rough-ins

| Where | Service |
|---|---|
| Sink module | hot + cold + filtered cold (3 lines), 2" drain to grey |
| Cooktop | 120V/220V dedicated, EGC |
| Range hood | 24V (dimmable) + duct to roof or wall |
| Fridge (port side) | 24V dedicated breaker |
| Counter outlets | 2× 120V GFCI (per panel-schedule-ac) |
| USB-C PD | 2× under upper cabinet at 45W |

## Module CAD files (planned)

```
cad/70-interior-cabinetry/galley/
  build-galley.FCMacro       parametric generator (this batch)
  galley-master.FCStd        assembly snapshot (after first run in FreeCAD)
  modules/
    pantry-tower.FCStd
    drawer-tower.FCStd
    cooktop-module.FCStd
    sink-module.FCStd
  drawings/                  PDF + DXF + G-code per part (TBD)
```

## Weight estimate

| Module | Mass (lb) |
|---|---|
| Pantry tower (frame + ply + slides) | 65 |
| Drawer tower | 75 |
| Cooktop module | 50 + 12 cooktop |
| Sink module | 45 + 18 sink + 8 faucet |
| Counter (solid surface, 7' × 24") | 105 |
| **Galley total (less appliances)** | **~330** |
| With cooktop + sink + faucet + range hood | ~390 |

Captured in `weight/master.csv` (galley row).
