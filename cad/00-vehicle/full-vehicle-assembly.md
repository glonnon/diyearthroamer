# Full Vehicle Assembly — Integration Procedure

How to combine every parametric sub-macro into a single
`full-vehicle-assembly.FCStd` for clearance / livability review.

## Sub-models that compose the vehicle

| Order | Sub-macro | Document | Anchors against |
|---|---|---|---|
| 1 | `cad/00-vehicle/build-master.FCMacro` | `f550_master` | (origin) |
| 2 | `cad/50-plumbing/build-tanks.FCMacro` | `tanks` | F550 frame top |
| 3 | `cad/30-exterior/liftbox/build-liftbox.FCMacro` | `liftbox` | rear bumper |
| 4 | `cad/70-interior-cabinetry/galley/build-galley.FCMacro` | `galley` | shell floor, curb |
| 5 | `cad/70-interior-cabinetry/dinette/build-dinette.FCMacro` | `dinette` | shell floor, port |
| 6 | `cad/70-interior-cabinetry/bath/build-bath.FCMacro` | `bath` | shell floor, aft port |
| 7 | `cad/70-interior-cabinetry/wardrobe/build-wardrobe.FCMacro` | `wardrobe` | shell floor, port |
| 8 | `cad/70-interior-cabinetry/cabover/build-cabover.FCMacro` | `cabover` | F550 cab roof |

## Quick path (orchestrator)

1. Open FreeCAD 1.x.
2. Macro → Macros → File → Add → select
   `cad/00-vehicle/build-vehicle.FCMacro`.
3. **Edit `REPO_CAD_BASE` in the macro** if your clone path is not
   `~/diyearthroamer/cad`.
4. Execute. The macro runs every sub-macro, then merges every shape
   into a new `vehicle_full` document. A bounding-box report prints
   to the console so you can eyeball placement.
5. **File → Save As** `cad/00-vehicle/full-vehicle-assembly.FCStd`.
6. **File → Export** `full-vehicle-assembly.step` (binary STEP AP242).

## Manual path (one sub-macro at a time)

If the orchestrator is unwanted (e.g., you want to tweak parameters
between sub-macros):

1. Run each sub-macro individually (Macro → Macros → run).
2. Save each as its named `*.FCStd` and export STEP.
3. New empty document → File → Import each `.step`.
4. Use Part → Compound to combine.

## Clearance / interference checks (after merge)

In the `vehicle_full` document:

- **Part → Boolean → Common (intersection)** between any two parts
  produces an empty solid if they don't overlap; non-empty solid =
  interference.
- **Part → Section** at known clearance planes (e.g., shell floor
  plane Y=1216, frame top Y=1016) shows whether anything pokes
  through.
- **Part → Measure** for headroom in walking zones (galley aisle,
  dinette knee, cabover sleep clearance).

Common spots where clearance is tight in this build:

| Spot | Required clearance | How to check |
|---|---|---|
| Cabover bed to ceiling | ≥ 510 mm (sleep) | Measure between mattress top and shell ceiling |
| Aisle between galley and dinette | ≥ 760 mm (30") | X-section through the middle of the cabinetry run |
| Lift box stowed vs shell tail taper | ≥ 50 mm air gap | Boolean Common between liftbox and shell taper |
| Tank bottom vs frame top | ≥ 25 mm | Boolean Common; tanks should sit above frame |
| Pass-through door vs cab roof | ≥ 50 mm air gap | Y-section through cabover front bulkhead |
| Mini-split condenser locker vs roof | ≥ 100 mm above shell | Section view |

## Livability review pass

Before fab:

1. Place a 5th-percentile and 95th-percentile manikin (FreeCAD
   FemMesh + skeleton, or a simple bounding cylinder) at the galley,
   dinette, bath, bed, and cabover.
2. Check head clearance at every standing zone.
3. Check reach to upper cabinets, cooktop, sink, fridge.
4. Check door swings and drawer pulls.
5. Export to glTF (`Tools → Add-on Manager` → install Mesh Designer
   → Export glTF) and open in Blender for a fly-through.

Acceptance criteria:

- [ ] No interference detected between any two parts.
- [ ] Walking zones ≥ 76" (1,930 mm) headroom.
- [ ] Cabover sleep clearance ≥ 20" (510 mm).
- [ ] Cabover egress window position confirmed (RVIA-spec).
- [ ] All cabinet doors clear adjacent surfaces by ≥ 25 mm.
- [ ] Service-bay access (battery, hydronic, pump) confirmed
      reachable without removing other components.

## Outputs to commit (via Git LFS)

After acceptance:

- `cad/00-vehicle/full-vehicle-assembly.FCStd`
- `cad/00-vehicle/full-vehicle-assembly.step`
- `cad/00-vehicle/full-vehicle-assembly.glb` (Blender export)
- `cad/00-vehicle/livability-report.md` — manikin study + headroom
  heatmap screenshots
