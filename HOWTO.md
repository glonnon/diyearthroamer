# How to Build and Display the Models

End-to-end guide for someone with a fresh machine: install the tools,
clone the repo, run the parametric models, view them, and export for
review or fabrication.

## 0. Prerequisites — install once

Stack A (locked in ADR-0008) is fully open-source. You can install
everything below for free.

| Tool | Purpose | Install |
|---|---|---|
| **FreeCAD 1.x** | 3D CAD (parts, assemblies, sheet metal, CAM) | https://www.freecad.org/downloads.php |
| **KiCad 8+** | Electrical schematics + PCB | https://www.kicad.org/download/ |
| **Blender 4.x** | Renders, fly-through walkthroughs, VR | https://www.blender.org/download/ |
| **Inkscape** | DXF/SVG cleanup for laser/waterjet | https://inkscape.org/release/ |
| **Git + Git LFS** | Source control for binary CAD files | https://git-scm.com / `git lfs install` |
| **Python 3.8+** | Helper scripts (weight model, doc bundler) | usually pre-installed |
| **Pandoc** *(optional)* | Render `MASTER.md` to PDF / HTML | https://pandoc.org/installing.html |
| **Node + Mermaid CLI** *(optional)* | Render `.mmd` → `.svg` | `npm install -g @mermaid-js/mermaid-cli` |
| **Docker** *(optional)* | Mermaid CLI fallback | https://docs.docker.com/get-docker/ |

### Linux (Ubuntu / Debian)

```sh
sudo apt install freecad kicad blender inkscape git git-lfs python3 pandoc
git lfs install
```

### macOS (Homebrew)

```sh
brew install --cask freecad kicad blender inkscape
brew install git git-lfs python3 pandoc
git lfs install
```

### Windows

```powershell
winget install FreeCAD.FreeCAD KiCad.KiCad BlenderFoundation.Blender Inkscape.Inkscape Git.Git GitHub.GitLFS Python.Python.3.12 JohnMacFarlane.Pandoc
git lfs install
```

## 1. Clone the repo

```sh
git clone <repo-url>
cd diyearthroamer
git lfs pull
```

Git LFS pulls the binary CAD/render/drawing files. Without LFS you'll
get text pointers instead.

## 2. Run a single FreeCAD macro

Each subsystem has a parametric Python macro that builds simplified
solids. Pick any of:

| Macro | Builds |
|---|---|
| `cad/00-vehicle/build-master.FCMacro` | F550 chassis + cab + shell + subframe |
| `cad/50-plumbing/build-tanks.FCMacro` | Fresh A/B + grey + black + pump bay |
| `cad/30-exterior/liftbox/build-liftbox.FCMacro` | Bike lift-box + arms + actuators |
| `cad/70-interior-cabinetry/galley/build-galley.FCMacro` | Galley modules |
| `cad/70-interior-cabinetry/dinette/build-dinette.FCMacro` | Dinette + fridge cabinet |
| `cad/70-interior-cabinetry/bath/build-bath.FCMacro` | Bath module |
| `cad/70-interior-cabinetry/wardrobe/build-wardrobe.FCMacro` | Wardrobe |
| `cad/70-interior-cabinetry/cabover/build-cabover.FCMacro` | Cabover platform + bed + headboard |

### Steps in FreeCAD

1. Open FreeCAD.
2. **Macro → Macros…**
3. **User macros location** — click **…** and point at the repo's
   `cad/` directory (or wherever the `.FCMacro` file is). FreeCAD
   accepts any directory.
4. Pick the macro from the list, click **Execute**.
5. A new document opens in the 3D view with simplified solids in
   place against the vehicle origin (rear axle center, ground).
6. **View → Fit All** (`V, F`) to frame the model.
7. **View → Standard views** to switch between front / top / side /
   axonometric.

### Tweaking parameters

Every macro starts with a `PARAMS = { ... }` dict. Edit the values,
re-run the macro — the document is rebuilt with the new dimensions.

## 3. Build the full vehicle assembly

When you want to see everything together (and check for clearance /
interference issues):

1. Open `cad/00-vehicle/build-vehicle.FCMacro` in a text editor.
2. Edit `REPO_CAD_BASE` near the top to point at your local clone's
   `cad/` directory (default is `~/diyearthroamer/cad`).
3. In FreeCAD: **Macro → Macros → Execute** → select
   `build-vehicle.FCMacro`.
4. The orchestrator runs every sub-macro, then merges every shape
   into a single `vehicle_full` document. A bounding-box report
   prints to the **View → Panels → Report view**.
5. **File → Save As…** `cad/00-vehicle/full-vehicle-assembly.FCStd`.
6. Walk through `cad/00-vehicle/full-vehicle-assembly.md` for the
   clearance / interference check list.

### Display tips in FreeCAD

- **Toggle transparency** on the shell: select `shell_main`, set
  Transparency = 70 in the Property panel — you can see all the
  interior cabinetry through it.
- **Use the Section tool** (Part workbench → Cross-Sections) to slice
  at the floor plane (Y=1216 mm) or the centerline (Z=0) for a 2D
  cut view.
- **Measure** (Std → Tools → Measure distance) to verify aisle width,
  cabover sleep clearance, etc.
- **Turn parts on/off** by space-bar in the model tree.

## 4. Export for sharing or review

### STEP (universal CAD interchange)

In FreeCAD with any document open:

```
File → Export → choose `.step` → save as cad/.../<name>.step
```

STEP files open in Fusion 360, SolidWorks, Onshape, Blender,
KiCad's 3D viewer, etc.

### glTF for Blender / web

```
File → Export → choose `.glb` → save as cad/.../<name>.glb
```

### PDF drawings

In FreeCAD: switch to **TechDraw** workbench → **TechDraw → Insert
view → drawing template → place views → annotate → File → Export
PDF**.

## 5. Open in Blender for fly-through

1. Open Blender.
2. **File → Import → glTF 2.0** → pick the `.glb` you exported.
3. Press **Numpad 5** to switch to perspective.
4. **Numpad 1 / 3 / 7** for front / side / top views.
5. Walk the camera with **Shift + ` (backtick)** for fly-mode (WASD
   to move, mouse to look, shift to speed up).
6. For a saved walkthrough animation: Add a Camera, set keyframes
   along a path through the cabin, **Render → Render Animation**.

This is how the livability review pass works (REQUIREMENTS.md §4 /
`cad/00-vehicle/full-vehicle-assembly.md`).

## 6. Render Mermaid diagrams to SVG

The diagrams live as `.mmd` files in `diagrams/`. They render
automatically on GitHub. To produce SVG / PNG for printing or
embedding elsewhere:

```sh
./scripts/render-diagrams.sh
```

The script:
- Tries `mmdc` on PATH first.
- Falls back to `docker run minlag/mermaid-cli` if Docker is
  installed.
- Produces `diagrams/<name>.svg` next to each `.mmd` source.

Output SVGs are gitignored — regenerate any time. View them in any
browser, Inkscape, or drop them into Markdown / docs.

## 7. Render the full project document

`scripts/build-master-doc.py` walks the entire repo and produces a
single `MASTER.md` (every subsystem README + every ADR + every CSV
rendered as a table + every Python helper / FreeCAD macro embedded
as code). 7,000+ lines, 1,000+ tables.

```sh
# Markdown only (always works)
python3 scripts/build-master-doc.py

# Plus PDF (needs pandoc + a PDF engine)
python3 scripts/build-master-doc.py --pdf

# Plus HTML
python3 scripts/build-master-doc.py --html
```

Outputs at the repo root: `MASTER.md`, `MASTER.pdf`, `MASTER.html`
(all gitignored — regenerate any time).

## 8. Run the weight + axle model

```sh
# Default scenarios (DRY / CRUISE / WET) with Continental MPT 81
python3 scripts/weight-cg.py --tire-load 6779

# Save axle report CSV
python3 scripts/weight-cg.py --tire-load 6779 --csv weight/axle-report.csv

# What-if: GVWR upgrade to 22,000 lb
python3 scripts/weight-cg.py --tire-load 6779 --gvwr 22000
```

Edit `weight/master.csv` (mass and station-X per row) any time, then
re-run. Every component carries its own row, so the model rebuilds
itself.

## 9. Open the KiCad project

1. Launch **KiCad 8+**.
2. **File → Open Project…** → select
   `electrical/kicad/diy-earthroamer.kicad_pro`.
3. The project explorer shows the root schematic and 11 hierarchical
   sub-sheets (`48V_Bus`, `24V_SubBus`, `Solar`, `AC_Distribution`,
   etc.).
4. **Schematic Editor** → double-click any sheet box to enter the
   sub-sheet.
5. The project's symbol library (`lib/diy-earthroamer.kicad_sym`,
   12 custom symbols: Epoch 48V, Victron MultiPlus / MPPT / Cerbo /
   SmartShunt / Orion XS, Mabru, Webasto, SmartPlug, Linak, SeeLevel,
   Class T fuse, Blue Sea busbar) is auto-registered via
   `sym-lib-table`. **Place → Symbol** and search the project library.
6. Use `electrical/kicad/sheets/48v-bus-plan.md` as the drawing
   walkthrough for the first sheet.

After a sheet is drawn:

```
Inspect → Electrical Rules Checker        # ERC clean before commit
File → Plot → Plot All Pages              # PDF export to electrical/kicad/exports/
```

## 10. Run a clean reproducible check

To verify everything builds end-to-end (after you've installed
prerequisites):

```sh
# repo health
git status
git lfs pull

# weight model
python3 scripts/weight-cg.py --tire-load 6779

# project doc
python3 scripts/build-master-doc.py
ls -lh MASTER.md     # ~280 KB

# diagrams
./scripts/render-diagrams.sh   # if mmdc / docker installed
ls -lh diagrams/*.svg

# CAD: open FreeCAD, Macro -> build-master, then build-vehicle
# KiCad: open electrical/kicad/diy-earthroamer.kicad_pro
```

## 11. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| FreeCAD macro errors `App not defined` | Run from outside FreeCAD | Open FreeCAD first; use Macro → Execute |
| Macro produces no shapes | `REPO_CAD_BASE` mis-set in orchestrator | Edit path at top of `build-vehicle.FCMacro` |
| `git lfs pull` says `Smudge error` | LFS not installed | `git lfs install`, retry |
| KiCad symbol library missing | Project's `sym-lib-table` not loaded | Open via the project file, not just the schematic file |
| `mmdc: command not found` | Mermaid CLI not installed | `npm install -g @mermaid-js/mermaid-cli` or use Docker fallback |
| Pandoc PDF fails | No PDF engine on PATH | `apt install wkhtmltopdf` (or texlive); rerun with `--pdf` |
| Weight script error: float conversion | Edited `weight/master.csv` left a non-numeric mass | Open CSV, fix the offending row, save |
| FreeCAD: parts at strange Z coords | Mixed mm / inch in PARAMS dict | All units are mm; `25.4` multiplier on inch values in the macros |
| KiCad ERC fails on power flags | Missing PWR_FLAG on a power net | Add `Place → Power port → PWR_FLAG` near each net |

## 12. Where to look for what

| Question | File |
|---|---|
| What's the build supposed to be? | `REQUIREMENTS.md` |
| Why was X chosen? | `decisions/<NNNN>-<slug>.md` |
| What does X cost? | `bom/master.csv`, `bom/cost-summary.md` |
| When does X happen in the build? | `build-log/phase-plan.md` |
| Who supplies X? | `vendor-docs/suppliers.md` |
| Does it fit? | `weight/master.csv` + `scripts/weight-cg.py` + `weight/axle-analysis.md` |
| How much heat? | `hvac/heat-load.md`, `hvac/heat-load.csv` |
| What's the wiring? | `electrical/oneline.md` (ASCII + Mermaid), `electrical/wire-list.csv`, KiCad project |
| What does the plumbing look like? | `plumbing/pid.md`, `plumbing/tank-layout.md` |
| What goes where in CAD? | `cad/README.md` + per-subsystem `SPECS.md` |
| How to integrate everything? | `cad/00-vehicle/full-vehicle-assembly.md` |
