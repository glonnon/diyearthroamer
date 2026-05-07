# DIY Earthroamer / HILT-Class Build

A custom 4-season expedition vehicle built on a Ford F550 crew-cab
flatbed with a 21' Global Trekker composite shell. Source of truth for
specs, CAD, electrical, plumbing, HVAC, BOM, and build log.

- **How to build & display the models:** [`HOWTO.md`](HOWTO.md) — start here if you've just cloned the repo.
- **Requirements:** [`REQUIREMENTS.md`](REQUIREMENTS.md) — what we're building.
- **Decisions log (ADRs):** [`decisions/`](decisions/) — why each choice was made.
- **CAD:** [`cad/`](cad/) — FreeCAD macros + STEP exports per subsystem.
- **Electrical:** [`electrical/`](electrical/) — KiCad schematics, load study, wire list.
- **Plumbing:** [`plumbing/`](plumbing/) — P&ID, fixture/tank schedules.
- **HVAC:** [`hvac/`](hvac/) — heat-load calc, hydronic loop diagram.
- **Diagrams:** [`diagrams/`](diagrams/) — Mermaid one-line, P&ID, hydronic, schematic hierarchy.
- **BOM:** [`bom/master.csv`](bom/master.csv) + [`bom/cost-summary.md`](bom/cost-summary.md).
- **Weight & CG:** [`weight/master.csv`](weight/master.csv) + [`weight/axle-analysis.md`](weight/axle-analysis.md).
- **Build plan:** [`build-log/phase-plan.md`](build-log/phase-plan.md) — 12-phase project plan.
- **Vendor docs:** [`vendor-docs/`](vendor-docs/) (datasheets, install manuals) + [`suppliers.md`](vendor-docs/suppliers.md).

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

**Source-only repo** — every derived artifact (CAD models, diagrams,
schematic PDFs, master document) is regenerated from text sources via
the top-level [`Makefile`](Makefile). No Git LFS.

After cloning:

```sh
bash scripts/install/install-ubuntu.sh        # or install-windows.ps1
make all
```

See [`HOWTO.md`](HOWTO.md) for the full workflow.

## Conventions

- Every released CAD part ships native + STEP AP242 + PDF drawing
  + DXF (if 2D-cut) or G-code + setup PDF (if CNC) — see §24.5.
- Every component lands in `bom/master.csv` (cost) and
  `weight/master.csv` (mass + station-X for CG).
- Every locked architectural decision has an ADR in `decisions/`.
- Branch `main` is releasable; design work on `design/<area>` branches.
