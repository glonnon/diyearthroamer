# DIY Earthroamer / HILT-Class Build

A custom 4-season expedition vehicle built on a Ford F550 crew-cab
flatbed with a 21' Global Trekker composite shell. Source of truth for
specs, CAD, electrical, plumbing, HVAC, BOM, and build log.

- **Requirements:** [`REQUIREMENTS.md`](REQUIREMENTS.md) — read first.
- **Decisions log (ADRs):** [`decisions/`](decisions/)
- **CAD:** [`cad/`](cad/) — FreeCAD natives + STEP exports per subsystem.
- **Electrical:** [`electrical/`](electrical/) — KiCad schematics, load study.
- **Plumbing:** [`plumbing/`](plumbing/) — P&ID, fixture/tank schedules.
- **HVAC:** [`hvac/`](hvac/) — heat-load calc, hydronic loop diagram, ducting.
- **BOM:** [`bom/master.csv`](bom/master.csv)
- **Weight & CG:** [`weight/master.csv`](weight/master.csv)
- **Build log:** [`build-log/`](build-log/)
- **Vendor docs:** [`vendor-docs/`](vendor-docs/) (datasheets, install manuals)

## Tooling (locked — Stack A, all OSS)

| Use | Tool |
|---|---|
| 3D CAD + assemblies + sheet metal | **FreeCAD 1.x** (Assembly4 / Ondsel-merged) |
| CAM / G-code | **FreeCAD Path** + **Kiri:Moto** |
| G-code simulation | **CAMotics** |
| Electrical schematics + PCB | **KiCad 8+** |
| Renders, walkthroughs, VR | **Blender 4.x** |
| 2D vector cleanup (DXF/SVG) | **Inkscape** |
| Plumbing P&ID, AC one-line, network | **draw.io** |
| BOM, weight model, load study | CSV (LibreOffice Calc / Sheets) |

See `REQUIREMENTS.md` §24 for the full file format contract and export
checklist.

## Working with this repo

This repo uses **Git LFS** for binary CAD/render/drawing artifacts.
After cloning:

```sh
git lfs install
git lfs pull
```

See `.gitattributes` for the tracked extensions.

## Conventions

- Every released CAD part ships native + STEP AP242 + PDF drawing
  + DXF (if 2D-cut) or G-code + setup PDF (if CNC) — see §24.5.
- Every component lands in `bom/master.csv` (cost) and
  `weight/master.csv` (mass + station-X for CG).
- Every locked architectural decision has an ADR in `decisions/`.
- Branch `main` is releasable; design work on `design/<area>` branches.
