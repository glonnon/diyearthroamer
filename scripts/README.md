# scripts/

Helper scripts for working with the repo.

## `build-master-doc.py`

Bundle every Markdown + CSV in the repo into a single **`MASTER.md`**
at the repo root, with all CSVs rendered as Markdown tables and all
ADRs / READMEs / analyses inlined in a deterministic order.

### Usage

```sh
# Markdown only (always works, stdlib-only)
python3 scripts/build-master-doc.py

# Markdown + HTML (requires pandoc)
python3 scripts/build-master-doc.py --html

# Markdown + PDF (requires pandoc + a PDF engine)
python3 scripts/build-master-doc.py --pdf

# Custom output path
python3 scripts/build-master-doc.py --out out/build-spec.md
```

### Dependencies

- **Python 3.8+** (no third-party packages needed)
- For `--pdf` / `--html`: **pandoc** on PATH
  - Ubuntu/Debian: `sudo apt install pandoc`
  - macOS (Homebrew): `brew install pandoc`
  - Windows: `winget install pandoc`
- For prettier PDFs, install one of these (auto-detected):
  - `wkhtmltopdf` — fastest, simplest, good fidelity
  - `weasyprint` — modern HTML/CSS-driven
  - `xelatex` / `pdflatex` — professional typesetting

### What gets included

Walks the repo in a fixed order (per `SECTION_ORDER` in the script):

1. `README.md` — overview
2. `REQUIREMENTS.md` — full requirements
3. `decisions/` — every ADR
4. `cad/` — every README + analysis (`SPECS.md`, `cabover-fit.md`,
   `liftbox-kinematics.md`, etc.) and FreeCAD macros as code blocks
5. `electrical/` — README, one-line, panel schedules, wire list,
   load study, `voltage-drop.py` as a code block
6. `plumbing/` — README + future P&ID notes
7. `hvac/` — README, heat-load analysis, heat-load CSV
8. `bom/master.csv` — rendered as a table
9. `weight/master.csv` — rendered as a table
10. `build-log/`
11. `vendor-docs/`

CSVs are rendered as GitHub-flavored Markdown tables. Python and
`.FCMacro` files are embedded as code blocks. Binary CAD/mesh/render
files are skipped (they live in Git LFS and aren't useful in a printed
doc anyway).

### Output

`MASTER.md` is generated at the repo root by default. It is **not**
committed to git (added to `.gitignore`) — regenerate any time. Same
for `MASTER.pdf` / `MASTER.html`.

### Determinism

File order within each section is alphabetical so the output diff is
stable run-to-run. If you reorganize the repo, update `SECTION_ORDER`
in the script.
