# ADR-0008: CAD Tooling — Stack A (FreeCAD + KiCad + Blender)

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** REQUIREMENTS.md §4, §24

## Context

Need a tooling stack that supports parametric 3D assemblies (livability
+ fitment), sheet-metal, CAM/G-code, electrical schematics, and
high-quality renders/walkthroughs — without making documents public,
without licensing risk, and without vendor lock-in over a multi-year
build.

## Options considered

1. **Stack A — FreeCAD + KiCad + Blender + Inkscape + draw.io
   (chosen).** Fully OSS, offline-capable, no IP exposure, free in
   perpetuity, all required exports possible.
2. **Stack B — Fusion 360 Personal + KiCad + Blender.** Powerful and
   ergonomic, but Autodesk hobby terms have changed before and may
   change again; commercial use needs paid license.
3. **Stack C — Onshape Free + Kiri:Moto + KiCad.** Free tier requires
   public documents — unacceptable IP exposure.
4. **Stack D — SolidWorks for Makers + KiCad.** $48/yr, non-commercial
   only, Windows-only.

## Decision

Stack A. All design work in FreeCAD; CAM via FreeCAD Path and
Kiri:Moto; G-code simulated in CAMotics before machining; KiCad for
electrical; Blender for renders and VR walkthroughs; Inkscape for
DXF/SVG cleanup; draw.io for P&ID and one-line diagrams; CSV for BOM
and weight model.

## Consequences

- File format contract (REQUIREMENTS.md §24.3) is the integration
  surface — STEP AP242 + DXF + glTF + PDF + G-code.
- FreeCAD assembly discipline matters (Assembly4 / mainline Assembly)
  to avoid solver pain on large assemblies; established in
  `cad/README.md`.
- Defection path: any individual subsystem can move to Fusion or
  SolidWorks via STEP without losing prior work.
- No subscription cost; ongoing learning cost on FreeCAD.

## Open questions

- Pin a FreeCAD release (1.0.x) for the project to avoid solver churn.
- Decide on Assembly4 vs mainline Assembly workflow.
