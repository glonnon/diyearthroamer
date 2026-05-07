# Wardrobe — Parametric Module Spec

Full-height port-side wardrobe between dinette and bath. Hanging rod
+ drawers + utility space (dirty laundry, vacuum, comms equipment).

## Envelope

| Param | Value (mm) | Value (in) | Note |
|---|---|---|---|
| Wardrobe length (X) | 600 | 23.6 | port wall, single bay |
| Wardrobe depth (Z) | 530 | 21 | enough for hangers + jacket bulk |
| Floor-to-ceiling | 1,950 | 76.8 | full-height; door soft-close |
| Door clear opening | 540 × 1,830 | 21 × 72 | Blum hinge + secondary catch |

## Internal layout

```
+---------------------+  ceiling
|  +--- shelf --------|
|  +---  hanging ----+|   500 mm hanging zone, top
|  |   (rod 1)       ||
|  +-----------------+|
|                     |
|  +-----------------+|
|  |   hanging       ||   500 mm hanging zone, lower
|  |   (rod 2)       ||
|  +-----------------+|
|                     |
|  +---  drawer 1 ---+|   3-drawer stack
|  +---  drawer 2 ---+|
|  +---  drawer 3 ---+|
|                     |
+---------------------+  floor + 100 mm toe-kick
```

## Modules

| Module | Dim (mm) | Notes |
|---|---|---|
| Top hanging rod (jackets) | 540 W × 530 D × 500 H | chrome rod + hanger hooks |
| Lower hanging rod (shirts) | 540 × 530 × 500 | second rod below |
| Drawer stack (3 drawers) | 540 × 480 × 600 H total | 200 mm each, Movento slides |
| Top shelf | 540 × 510 × ply | seasonal storage |
| Toe-kick recess | 540 × 75 × 100 | flush with cabinetry |

## Construction

- **Aluminum frame:** 1.5"×1.5"×1/8" 6061 angle ladder, 4 verticals
  + 4 horizontals (top, mid, drawer-rail, bottom).
- **Plywood:** 18 mm Baltic birch back + sides; 12 mm shelves and
  drawer bottoms.
- **Door:** 18 mm ply core + HPL/Fenix face; Blum Clip-Top + Blumotion
  + Southco compression latch for travel.
- **Hanging rod:** 25 mm chrome marine rod, end caps + center support
  if rod span exceeds 500 mm.
- **Mounting:** through-bolts to shell composite inserts; floating
  attachment for thermal expansion.

## Hardware

| Item | Spec |
|---|---|
| Drawer slides | Blum Movento full-extension, soft-close + travel lock |
| Hinges | Blum Clip-Top blumotion |
| Latch (travel) | Southco compression |
| Hanger rod | 25 mm chrome marine, end caps |
| LED interior | 24V dimmable strip, motion-on |
| Hooks (door interior) | over-door coat hooks |

## Power & data

| Service | Where |
|---|---|
| 24V LED strip | top of wardrobe interior |
| 120V GFCI | inside wardrobe (laundry / vacuum) |
| USB-C PD 45W | shelf top (charge phone overnight) |

## Weight estimate

| Component | Mass (lb) |
|---|---|
| Frame (aluminum angle) | 25 |
| Plywood panels | 60 |
| Door + hardware | 35 |
| Drawer slides + boxes (3) | 45 |
| Rod + hooks + finish | 12 |
| **Wardrobe total** | **~177** |

(`weight/master.csv` line "Wardrobe + drawers + door area" = 250 lb;
the ~73 lb difference accounts for clothing + utility contents.)

## CAD files (planned)

```
cad/70-interior-cabinetry/wardrobe/
  SPECS.md
  build-wardrobe.FCMacro
  wardrobe-master.FCStd
```
