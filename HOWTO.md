# How to Build and Display the Models

End-to-end guide for someone with a fresh machine: install the
toolchain in one command, clone the repo, and rebuild every derived
artifact (CAD models, diagrams, schematic PDFs, master document) from
source.

> **This repo is source-only.** Every binary or rendered output is
> reproducible from the committed source files (`.FCMacro`, `.mmd`,
> `.kicad_sch`, `.csv`, `.md`) via the [`Makefile`](Makefile).
> Git LFS is not used.

## 0. Install the toolchain (one command)

### Ubuntu / Debian

```sh
bash scripts/install/install-ubuntu.sh
```

Idempotent. Installs FreeCAD 1.x, KiCad 8, Blender, Inkscape,
Pandoc + wkhtmltopdf, Node.js + Mermaid CLI, and Python 3 via apt
plus official PPAs.

### Windows 10 / 11 (elevated PowerShell)

```powershell
powershell -ExecutionPolicy Bypass -File scripts\install\install-windows.ps1
```

Uses winget. Installs the same toolchain. Restart your terminal so
PATH picks up new tools.

### macOS

```sh
brew install --cask freecad kicad blender inkscape wkhtmltopdf
brew install git python3 pandoc make
npm install -g @mermaid-js/mermaid-cli
```

### Verify

```sh
make check-tools
```

## 1. Clone the repo

```sh
git clone <repo-url>
cd diyearthroamer
```

No `git lfs` step — there are no LFS-tracked files. Everything is
source.

## 2. Rebuild everything (one command)

```sh
make all
```

That target chains:

| Target | What it builds |
|---|---|
| `make doc` | `MASTER.md` from every README + ADR + CSV + macro |
| `make pdf` | `MASTER.pdf` (via pandoc + wkhtmltopdf) |
| `make html` | `MASTER.html` |
| `make diagrams` | `diagrams/*.svg` from each `.mmd` |
| `make weight` | `weight/axle-report.csv` + axle/GVWR check |
| `make cad` | `build/cad/*.step` from every `.FCMacro` (FreeCAD headless) |
| `make kicad` | `electrical/kicad/exports/*.pdf` + ERC + BOM |

Run any target individually for faster iteration:

```sh
make diagrams        # just the SVG renders
make weight          # just the axle / GVWR check
make cad             # just the CAD STEP exports
make clean           # remove every derived artifact
```

## 3. Display the models

### FreeCAD (interactive)

The `make cad` target runs FreeCAD headless to produce STEP files in
`build/cad/`. To work *interactively* with a model:

1. Open FreeCAD.
2. **Macro → Macros…** → set the user-macros location to the repo's
   `cad/` directory.
3. Pick the macro you want (e.g. `cad/00-vehicle/build-master.FCMacro`)
   → **Execute**.
4. The model appears in the 3D view at the vehicle origin (rear axle
   center, ground).

| Macro | Builds |
|---|---|
| `cad/00-vehicle/build-master.FCMacro` | F550 chassis + cab + shell + subframe |
| `cad/00-vehicle/build-vehicle.FCMacro` | **Orchestrator** — runs all sub-macros + merges into `vehicle_full` |
| `cad/50-plumbing/build-tanks.FCMacro` | Fresh A/B + grey + black + pump bay |
| `cad/30-exterior/liftbox/build-liftbox.FCMacro` | Bike lift-box + arms + actuators |
| `cad/70-interior-cabinetry/galley/build-galley.FCMacro` | Galley modules |
| `cad/70-interior-cabinetry/dinette/build-dinette.FCMacro` | Dinette + fridge cabinet |
| `cad/70-interior-cabinetry/bath/build-bath.FCMacro` | Bath module |
| `cad/70-interior-cabinetry/wardrobe/build-wardrobe.FCMacro` | Wardrobe |
| `cad/70-interior-cabinetry/cabover/build-cabover.FCMacro` | Cabover platform + bed + headboard |

### Tweaking parameters

Each macro starts with a `PARAMS = { ... }` dict. Edit values, re-run
the macro — model rebuilds.

### Display tips in FreeCAD

- **Toggle transparency** on the shell: select `shell_main`, set
  Transparency = 70 — see the interior through it.
- **Use Section** (Part workbench → Cross-Sections) to slice at the
  floor plane (Y=1216 mm) or the centerline (Z=0).
- **Measure** (Std → Tools → Measure distance) for aisle width,
  cabover sleep clearance, etc.
- **Toggle parts** on/off with space-bar in the model tree.

### Blender (livability fly-through)

```sh
make cad                                         # produces build/cad/*.step
```

In Blender:

1. **File → Import → STEP** (install the
   "STEP/IGES Import" addon if needed) — pick
   `build/cad/f550-master.step` and any sub-models.
2. Walk the camera with **Shift + ` (backtick)** for fly-mode (WASD,
   mouse to look).
3. For a saved walkthrough animation: add a Camera, keyframe a path,
   **Render → Render Animation**.

### Diagrams (browser / docs)

`make diagrams` writes `diagrams/<name>.svg`. Open in any browser,
Inkscape, or drop into other Markdown.

The `.mmd` source files also render automatically in any
GitHub-flavored Markdown viewer (no rendering needed).

### KiCad

```sh
kicad electrical/kicad/diy-earthroamer.kicad_pro
```

The project's symbol library (`lib/diy-earthroamer.kicad_sym`,
12 custom symbols: Epoch 48V, Victron MultiPlus / MPPT / Cerbo /
SmartShunt / Orion XS, Mabru, Webasto, SmartPlug, Linak, SeeLevel,
Class T fuse, Blue Sea busbar) is auto-registered via the project's
`sym-lib-table`.

For batch ERC + PDF plot:

```sh
make kicad     # writes electrical/kicad/exports/diy-earthroamer.pdf
```

### Master document

```sh
make doc       # MASTER.md  (~280 KB, 7,000+ lines, 1,000+ tables)
make pdf       # MASTER.pdf (single printable spec)
make html      # MASTER.html
```

Outputs land at the repo root, all gitignored — regenerate any time.

### Weight + axle model

```sh
make weight                                              # default scenarios
python3 scripts/weight-cg.py --tire-load 6779 --gvwr 22000   # what-if
```

Edit `weight/master.csv` rows (mass + station-X), re-run.

## 4. Reproducible end-to-end check

After install, this should succeed without errors on a clean clone:

```sh
git clone <repo-url> && cd diyearthroamer
bash scripts/install/install-ubuntu.sh        # or install-windows.ps1
make all
```

You'll have: `MASTER.md` + `MASTER.pdf` + `MASTER.html` at the root,
SVGs in `diagrams/`, STEP files in `build/cad/`, KiCad PDFs in
`electrical/kicad/exports/`, and `weight/axle-report.csv`.

## 5. Source-only convention

| Committed | Derived (gitignored) |
|---|---|
| `*.md` | `MASTER.md`, `MASTER.pdf`, `MASTER.html` |
| `*.csv` (BOM, weight, panel/wire schedules, heat-load) | `weight/axle-report*.csv` |
| `*.FCMacro` (parametric Python for FreeCAD) | `*.FCStd`, `*.step`, `*.stp`, `*.glb`, `*.stl`, `*.dxf` |
| `*.mmd` (Mermaid source) | `diagrams/*.svg`, `diagrams/*.png` |
| `*.kicad_pro`, `*.kicad_sch`, `*.kicad_sym`, `sym-lib-table` | `electrical/kicad/exports/*` |
| `*.py` (helper scripts) | `__pycache__/` |
| `*.sh`, `Makefile`, `*.ps1` | `build/`, `out/`, `tmp/` |

If you find yourself wanting to commit a binary, ask: **"Can I derive
this from a source file?"** If yes, write a Makefile target instead.

## 6. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `make cad` fails: "FreeCAD CLI not found" | FreeCADCmd not on PATH | run install script; on macOS `/Applications/FreeCAD.app/Contents/MacOS/FreeCADCmd` |
| `make kicad` fails: "kicad-cli not found" | KiCad < 8 | install KiCad 8+ via the install script |
| `make pdf` fails | No PDF engine | install wkhtmltopdf or texlive |
| `make diagrams` fails | mmdc + docker both missing | run install script |
| FreeCAD macro errors `App not defined` | Run from outside FreeCAD | open FreeCAD first, use Macro → Execute |
| Macro produces no shapes (empty doc) | Wrong `REPO_CAD_BASE` in orchestrator | edit path at top of `cad/00-vehicle/build-vehicle.FCMacro` |
| KiCad symbol library missing | Project's `sym-lib-table` not loaded | open via the project file (`.kicad_pro`) not the schematic |
| `weight-cg.py` float error | Edited `weight/master.csv` with non-numeric mass | open CSV, fix the offending row |
| FreeCAD: parts at strange Z | Mixed mm/inch in PARAMS | all units mm; multiply inch values by 25.4 |
| Windows: `make` not found | `GnuWin32.Make` not on PATH | restart terminal after install |

## 7. Where to look for what

| Question | File |
|---|---|
| What's the build supposed to be? | `REQUIREMENTS.md` |
| Why was X chosen? | `decisions/<NNNN>-<slug>.md` |
| What does X cost? | `bom/master.csv`, `bom/cost-summary.md` |
| When does X happen? | `build-log/phase-plan.md` |
| Who supplies X? | `vendor-docs/suppliers.md` |
| Does it fit? | `weight/master.csv` + `make weight` + `weight/axle-analysis.md` |
| How much heat? | `hvac/heat-load.md`, `hvac/heat-load.csv` |
| What's the wiring? | `electrical/oneline.md`, `electrical/wire-list.csv`, KiCad project |
| What does the plumbing look like? | `plumbing/pid.md`, `plumbing/tank-layout.md` |
| What goes where in CAD? | `cad/README.md` + per-subsystem `SPECS.md` |
| How to integrate everything? | `cad/00-vehicle/full-vehicle-assembly.md` |
| How do I rebuild X? | `Makefile` |
