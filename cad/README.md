# CAD

FreeCAD 1.x is the primary tool (ADR-0008). All released parts must
also export STEP AP242 (and DXF/G-code where applicable) per
REQUIREMENTS.md §24.

## Subsystem layout

| Dir | Scope |
|---|---|
| `00-vehicle/` | F550 chassis model (vendor STEP if available, otherwise scanned/measured master sketch) |
| `10-subframe/` | Global Trekker subframe + owner-side outriggers and brackets |
| `20-shell/` | 21' Global Trekker shell with all penetrations marked |
| `30-exterior/` | Bumpers, racks, boxes, awning, ladder, lift-box carrier, spare tire |
| `40-electrical/` | Battery bay, panels, conduit/chase routing |
| `50-plumbing/` | Tanks, pump bay, manifold, fixture rough-ins |
| `60-hvac/` | Hydronic + mini-split + ducting + radiant floor zones |
| `70-interior-cabinetry/` | Galley, dinette, bath, bed, wardrobe (hybrid al + ply) |
| `80-finish/` | Flooring, wall panels, ceiling |
| `90-bom/` | Per-subsystem BOM CSVs feeding `/bom/master.csv` |

## Conventions

- **One FreeCAD doc per part** for parts; **one FreeCAD doc per
  assembly** for sub-assemblies; top-level vehicle assembly references
  STEP exports of subassemblies (link-type, not nested native).
- **Origin convention:** vehicle origin is at the **center of the rear
  axle** at ground level. +X forward, +Y up, +Z to driver side (LH).
  Document on every assembly.
- **Units:** millimeters. Drawings dual-dimension mm/inches.
- **Naming:** `<subsystem>__<part>__rev<NN>.FCStd` (double underscore
  separators, lowercase, no spaces).
- **Export pair:** every commit of a native file commits the matching
  `.step` export and (if drawing released) `.pdf` and `.dxf`.

## Weight & CG entry

Every released part adds a row to `/weight/master.csv` with `mass_lb`
and `station_x_in` (longitudinal distance from rear axle, +X forward).

## Livability deliverables (per REQUIREMENTS.md §4)

- 5th–95th percentile manikins placed in galley, dinette, bath, bed,
  cabover.
- Headroom heatmap in walking zones.
- Reach studies at upper cabinets.
- Door/drawer swing animations.
- Blender walkthrough (.blend + .glb) for review before fabrication.
