# Install scripts

One-shot installers for the DIY Earthroamer toolchain (Stack A — see
`decisions/0008-cad-stack.md`).

## Ubuntu / Debian

```sh
bash scripts/install/install-ubuntu.sh
```

Tested on Ubuntu 22.04 and 24.04. Should work on Debian 12+. Uses
`apt-get` and the official FreeCAD + KiCad PPAs to ensure recent
versions.

Installs:

- Build essentials, git, curl
- Python 3 + pip + venv
- FreeCAD 1.x (via `freecad-maintainers/freecad-stable` PPA)
- KiCad 8 (via `kicad/kicad-8.0-releases` PPA)
- Blender, Inkscape
- Pandoc + wkhtmltopdf (for `make pdf`)
- Node.js LTS + `@mermaid-js/mermaid-cli` (for `make diagrams`)
- GNU Make (almost always pre-installed)

Re-running is safe (idempotent). If a PPA fails on your distro the
script falls back to the default repos and prints a warning.

## Windows 10 / 11

Run from an **elevated PowerShell**:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\install\install-windows.ps1
```

Uses `winget`. If `winget` is missing, install **App Installer** from
the Microsoft Store first.

Installs the same toolchain via winget IDs:

- `Git.Git`, `Python.Python.3.12`, `GnuWin32.Make`
- `FreeCAD.FreeCAD`, `KiCad.KiCad`
- `BlenderFoundation.Blender`, `Inkscape.Inkscape`
- `JohnMacFarlane.Pandoc`, `wkhtmltopdf.wkhtmltopdf`
- `OpenJS.NodeJS.LTS` + `@mermaid-js/mermaid-cli` via npm

Restart your terminal after install so `PATH` picks up the new tools.
Then verify with `make check-tools`.

## macOS (manual — no formal script yet)

```sh
brew install --cask freecad kicad blender inkscape
brew install git python3 pandoc make
brew install --cask wkhtmltopdf
npm install -g @mermaid-js/mermaid-cli
```

## After install

Verify all tools resolve:

```sh
make check-tools
```

Then, from the repo root:

```sh
make all       # everything
make doc       # MASTER.md
make pdf       # MASTER.pdf
make diagrams  # SVG renders
make weight    # axle / GVWR check
make cad       # FreeCAD models -> STEP
make kicad     # KiCad ERC + PDF plots
make clean     # remove derived artifacts
```

See `HOWTO.md` for the full workflow.
