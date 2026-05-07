#!/usr/bin/env python3
"""
build-cad.py — drive FreeCAD in headless mode to run every parametric
macro and export STEP files.

Usage:
    scripts/build-cad.py                              # auto-detect FreeCADCmd
    scripts/build-cad.py --freecad /path/to/freecad   # override
    scripts/build-cad.py --out build/cad              # output directory

This is invoked by `make cad`. The FreeCAD CLI is launched once per
macro to keep environments clean. Each macro's output is written to a
named STEP file.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# (macro_path_relative_to_repo, output_step_basename)
MACROS = [
    ("cad/00-vehicle/build-master.FCMacro",                      "f550-master"),
    ("cad/50-plumbing/build-tanks.FCMacro",                      "tanks"),
    ("cad/30-exterior/liftbox/build-liftbox.FCMacro",            "liftbox"),
    ("cad/70-interior-cabinetry/galley/build-galley.FCMacro",    "galley"),
    ("cad/70-interior-cabinetry/dinette/build-dinette.FCMacro",  "dinette"),
    ("cad/70-interior-cabinetry/bath/build-bath.FCMacro",        "bath"),
    ("cad/70-interior-cabinetry/wardrobe/build-wardrobe.FCMacro", "wardrobe"),
    ("cad/70-interior-cabinetry/cabover/build-cabover.FCMacro",  "cabover"),
]

# Driver: runs the macro then exports every shape in the active doc.
DRIVER = '''
import sys
import FreeCAD as App
import Part

macro_path = sys.argv[-2]
out_step   = sys.argv[-1]

ns = {"__name__": "__main__", "__file__": macro_path}
with open(macro_path, "r", encoding="utf-8") as f:
    exec(compile(f.read(), macro_path, "exec"), ns)

doc = App.activeDocument()
if doc is None:
    print(f"ERROR: no active document after running {macro_path}",
          file=sys.stderr)
    sys.exit(2)

shapes = [o for o in doc.Objects
          if hasattr(o, "Shape") and o.Shape and not o.Shape.isNull()]
if not shapes:
    print(f"ERROR: no exportable shapes in document {doc.Name}",
          file=sys.stderr)
    sys.exit(3)

Part.export(shapes, out_step)
print(f"  wrote {out_step}  ({len(shapes)} shapes)")
'''


def find_freecad_cli() -> str | None:
    for name in ("FreeCADCmd", "freecadcmd", "freecad"):
        p = shutil.which(name)
        if p:
            return p
    return None


def run_one(freecad_bin: str, macro_path: Path, out_step: Path,
            driver_path: Path) -> int:
    print(f"  -> {macro_path.name}  ->  {out_step.name}")
    cmd = [freecad_bin, "-c", str(driver_path),
           str(macro_path), str(out_step)]
    try:
        return subprocess.call(cmd)
    except FileNotFoundError:
        print(f"FreeCAD CLI '{freecad_bin}' not found.", file=sys.stderr)
        return 127


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--freecad", default=None,
                    help="Path to FreeCAD CLI (auto-detect if omitted)")
    ap.add_argument("--out", default="build/cad",
                    help="Output directory for .step files")
    args = ap.parse_args()

    freecad = args.freecad or find_freecad_cli()
    if not freecad:
        print("FreeCAD CLI not found. Install with:\n"
              "  bash scripts/install/install-ubuntu.sh", file=sys.stderr)
        return 1

    out_dir = (REPO / args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False,
                                     encoding="utf-8") as tf:
        tf.write(DRIVER)
        driver = Path(tf.name)

    print(f"Using FreeCAD: {freecad}")
    print(f"Output dir   : {out_dir}\n")

    failures = 0
    for rel, name in MACROS:
        macro = REPO / rel
        if not macro.exists():
            print(f"  skip (missing): {rel}")
            continue
        out_step = out_dir / f"{name}.step"
        rc = run_one(freecad, macro, out_step, driver)
        if rc != 0:
            failures += 1

    driver.unlink(missing_ok=True)

    if failures:
        print(f"\n{failures} macro(s) failed.", file=sys.stderr)
        return 1
    print(f"\nAll CAD outputs in {out_dir.relative_to(REPO)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
