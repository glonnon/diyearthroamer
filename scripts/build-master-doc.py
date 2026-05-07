#!/usr/bin/env python3
"""
build-master-doc.py — Bundle every Markdown + CSV in the repo into a
single MASTER.md, with CSVs rendered as Markdown tables.

Usage:
    scripts/build-master-doc.py                # build MASTER.md
    scripts/build-master-doc.py --pdf          # also build MASTER.pdf via pandoc
    scripts/build-master-doc.py --html         # also build MASTER.html via pandoc
    scripts/build-master-doc.py --out OUT.md   # custom output path

The output is deterministic: directories and files are walked in a
fixed order so diffs are stable. Section numbering follows the
top-level directory order below.

PDF / HTML rendering requires `pandoc` on PATH. Install via your
package manager:
    Ubuntu/Debian:  sudo apt install pandoc
    macOS (brew):   brew install pandoc
    Windows:        winget install pandoc

For prettier PDFs install a TeX engine (e.g., wkhtmltopdf for the
quickest path: sudo apt install wkhtmltopdf, then pass --pdf-engine
in the script if needed).

No third-party Python packages required — stdlib only.
"""

from __future__ import annotations

import argparse
import csv
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

# Order in which top-level subsystems appear in the master document.
SECTION_ORDER = [
    ("README.md",                   "Overview"),
    ("REQUIREMENTS.md",             "Requirements"),
    ("decisions",                   "Decisions Log (ADRs)"),
    ("cad",                         "CAD Subsystems"),
    ("electrical",                  "Electrical"),
    ("plumbing",                    "Plumbing"),
    ("hvac",                        "HVAC"),
    ("bom",                         "Bill of Materials"),
    ("weight",                      "Weight & CG"),
    ("build-log",                   "Build Log"),
    ("vendor-docs",                 "Vendor Docs"),
]

# Files we never include (binary CAD, locks, build outputs).
SKIP_EXTENSIONS = {
    ".FCStd", ".FCStd1", ".FCBak",
    ".f3d", ".f3z",
    ".step", ".stp", ".iges", ".igs",
    ".stl", ".glb", ".gltf", ".obj", ".fbx", ".ply",
    ".dwg",
    ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".exr", ".psd",
    ".blend", ".blend1",
    ".kicad_pcb", ".kicad_sch", ".kicad_pro", ".kicad_prl",
    ".lib", ".mod", ".wrl",
    ".nc", ".gcode", ".tap",
    ".xlsx", ".ods", ".zip", ".7z",
    ".pdf",
}

SKIP_DIRS = {".git", ".github", "scripts", "out", "build", ".venv"}

REPO_ROOT = Path(__file__).resolve().parent.parent


# --------------------------------------------------------------------- #
# CSV → Markdown table
# --------------------------------------------------------------------- #

def csv_to_markdown(path: Path, max_rows: int | None = None) -> str:
    """Render a CSV file as a GitHub-flavored Markdown table."""
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    if not rows:
        return f"_({path.name} is empty)_\n"

    header = rows[0]
    body = rows[1:]
    if max_rows is not None:
        body = body[:max_rows]

    # Normalize row widths
    width = max(len(header), max(len(r) for r in body) if body else 0)
    header += [""] * (width - len(header))
    body = [r + [""] * (width - len(r)) for r in body]

    def esc(s: str) -> str:
        return (s or "").replace("|", "\\|").replace("\n", " ").strip()

    out: list[str] = []
    out.append("| " + " | ".join(esc(c) for c in header) + " |")
    out.append("|" + "|".join(["---"] * width) + "|")
    for r in body:
        out.append("| " + " | ".join(esc(c) for c in r) + " |")
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------- #
# File walking
# --------------------------------------------------------------------- #

@dataclass
class Doc:
    path: Path
    title: str
    body: str


def relpath(p: Path) -> str:
    return str(p.relative_to(REPO_ROOT))


def render_md(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return text.rstrip() + "\n"


def render_csv(path: Path) -> str:
    table = csv_to_markdown(path)
    return f"_Source: `{relpath(path)}`_\n\n{table}\n"


def render_python(path: Path) -> str:
    code = path.read_text(encoding="utf-8")
    return f"_Source: `{relpath(path)}`_\n\n```python\n{code.rstrip()}\n```\n"


def render_macro(path: Path) -> str:
    code = path.read_text(encoding="utf-8")
    return f"_Source: `{relpath(path)}` (FreeCAD macro)_\n\n```python\n{code.rstrip()}\n```\n"


def render_drawio(path: Path) -> str:
    return (
        f"_Source: `{relpath(path)}` — open in draw.io / diagrams.net._\n"
    )


def collect(path: Path) -> Iterable[Doc]:
    """Yield Doc entries for files under `path` in deterministic order."""
    if path.is_file():
        yield from _maybe_doc(path)
        return

    # Directory: recurse, sorted, skipping unwanted dirs.
    for entry in sorted(path.iterdir(), key=lambda p: p.name.lower()):
        if entry.is_dir():
            if entry.name in SKIP_DIRS:
                continue
            yield from collect(entry)
        else:
            yield from _maybe_doc(entry)


def _maybe_doc(path: Path) -> Iterable[Doc]:
    suffix = path.suffix.lower()
    name = path.name

    # Hidden / dotfiles
    if name.startswith("."):
        return

    if suffix in SKIP_EXTENSIONS:
        return

    rel = relpath(path)
    title = rel

    if suffix == ".md":
        yield Doc(path, title, render_md(path))
    elif suffix == ".csv":
        yield Doc(path, title, render_csv(path))
    elif suffix == ".py":
        yield Doc(path, title, render_python(path))
    elif suffix == ".fcmacro":
        yield Doc(path, title, render_macro(path))
    elif suffix == ".drawio":
        yield Doc(path, title, render_drawio(path))
    elif suffix in {".txt", ".rst"}:
        yield Doc(path, title, render_md(path))
    # else silently skip


# --------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------- #

def build_master(out_path: Path) -> Path:
    parts: list[str] = []
    parts.append("---")
    parts.append('title: "DIY Earthroamer / HILT Build — Master Document"')
    parts.append("subtitle: \"Auto-generated from the repo by "
                 "`scripts/build-master-doc.py`\"")
    parts.append("toc: true")
    parts.append("toc-depth: 3")
    parts.append("number-sections: true")
    parts.append("---")
    parts.append("")

    parts.append("> This document is generated. Edit the source files in "
                 "the repo, not this output.\n")

    for top, label in SECTION_ORDER:
        target = REPO_ROOT / top
        if not target.exists():
            continue

        parts.append(f"\n# {label}\n")
        parts.append(f"_Sourced from `{top}`._\n")

        docs = list(collect(target))
        if not docs:
            parts.append("_(no rendered files)_\n")
            continue

        # When the target is a directory, emit one sub-section per file.
        if target.is_dir():
            for d in docs:
                parts.append(f"\n## {d.title}\n")
                parts.append(d.body)
        else:
            # Single file (e.g., README.md, REQUIREMENTS.md): inline.
            parts.append(docs[0].body)

    out_path.write_text("\n".join(parts), encoding="utf-8")
    return out_path


def to_pdf(md_path: Path, pdf_path: Path) -> None:
    if shutil.which("pandoc") is None:
        print("pandoc not found on PATH. Install pandoc and rerun.",
              file=sys.stderr)
        print("  Ubuntu/Debian: sudo apt install pandoc", file=sys.stderr)
        print("  macOS (brew):  brew install pandoc", file=sys.stderr)
        print("  Windows:       winget install pandoc", file=sys.stderr)
        sys.exit(2)

    cmd = [
        "pandoc",
        str(md_path),
        "-o", str(pdf_path),
        "--from", "gfm+yaml_metadata_block",
        "--toc",
        "--standalone",
    ]
    # Try a couple of PDF engines in order; first one available wins.
    for engine in ("wkhtmltopdf", "weasyprint", "xelatex", "pdflatex"):
        if shutil.which(engine):
            cmd.extend(["--pdf-engine", engine])
            break
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)


def to_html(md_path: Path, html_path: Path) -> None:
    if shutil.which("pandoc") is None:
        print("pandoc not found on PATH.", file=sys.stderr)
        sys.exit(2)
    cmd = [
        "pandoc", str(md_path), "-o", str(html_path),
        "--from", "gfm+yaml_metadata_block",
        "--toc", "--standalone", "--self-contained",
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="MASTER.md",
                    help="Output Markdown path (default MASTER.md at repo root)")
    ap.add_argument("--pdf", action="store_true",
                    help="Also render MASTER.pdf via pandoc")
    ap.add_argument("--html", action="store_true",
                    help="Also render MASTER.html via pandoc")
    args = ap.parse_args()

    out_md = (REPO_ROOT / args.out).resolve()
    out_md.parent.mkdir(parents=True, exist_ok=True)

    md = build_master(out_md)
    print(f"Wrote {md.relative_to(REPO_ROOT)}  ({md.stat().st_size:,} bytes)")

    if args.html:
        out_html = out_md.with_suffix(".html")
        to_html(out_md, out_html)
        print(f"Wrote {out_html.relative_to(REPO_ROOT)}")

    if args.pdf:
        out_pdf = out_md.with_suffix(".pdf")
        to_pdf(out_md, out_pdf)
        print(f"Wrote {out_pdf.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
