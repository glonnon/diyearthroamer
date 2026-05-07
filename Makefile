# DIY Earthroamer — top-level build entry point.
#
# This repo is source-only. Every derived artifact (FreeCAD .FCStd,
# STEP, glTF, DXF, G-code, MASTER.md/.pdf/.html, diagram SVGs, weight
# reports, KiCad PDF plots) is regenerated from the committed sources
# via the targets below.
#
# Usage:
#     make help         # list targets
#     make all          # everything (long; needs full toolchain)
#     make doc          # master Markdown
#     make pdf          # master PDF (needs pandoc)
#     make diagrams     # SVG from Mermaid
#     make weight       # weight + axle report
#     make cad          # all FreeCAD models -> STEP
#     make kicad        # KiCad ERC + PDF plots
#     make clean        # remove all derived
#
# Install the toolchain first:
#     scripts/install/install-ubuntu.sh        (or)
#     scripts/install/install-windows.ps1

REPO         := $(shell pwd)
BUILD_DIR    := $(REPO)/build
CAD_OUT      := $(BUILD_DIR)/cad
KICAD_OUT    := electrical/kicad/exports

PYTHON       ?= python3
FREECAD      ?= $(shell command -v FreeCADCmd 2>/dev/null || command -v freecadcmd 2>/dev/null || command -v freecad 2>/dev/null)
KICAD_CLI    ?= $(shell command -v kicad-cli 2>/dev/null)
PANDOC       ?= $(shell command -v pandoc 2>/dev/null)
MMDC         ?= $(shell command -v mmdc 2>/dev/null)

DIAGRAM_SRC  := $(wildcard diagrams/*.mmd)
DIAGRAM_SVG  := $(DIAGRAM_SRC:.mmd=.svg)

.PHONY: help all doc pdf html diagrams weight cad kicad clean check-tools

help:
	@echo "DIY Earthroamer — build targets"
	@echo ""
	@echo "  make doc         # MASTER.md from every source file"
	@echo "  make pdf         # MASTER.pdf via pandoc"
	@echo "  make html        # MASTER.html via pandoc"
	@echo "  make diagrams    # diagrams/*.svg from .mmd via mmdc"
	@echo "  make weight      # weight/axle-report.csv + stdout summary"
	@echo "  make cad         # build/cad/*.step from every FCMacro"
	@echo "  make kicad       # KiCad ERC + per-sheet PDF plots"
	@echo "  make all         # all of the above"
	@echo "  make clean       # remove every derived artifact"
	@echo "  make check-tools # report which tools are installed"

all: doc pdf diagrams weight cad kicad

# ---------------- Docs ---------------- #

doc:
	$(PYTHON) scripts/build-master-doc.py

pdf:
	@if [ -z "$(PANDOC)" ]; then \
		echo "pandoc not installed. Run scripts/install/install-ubuntu.sh first." >&2; \
		exit 1; \
	fi
	$(PYTHON) scripts/build-master-doc.py --pdf

html:
	@if [ -z "$(PANDOC)" ]; then \
		echo "pandoc not installed. Run scripts/install/install-ubuntu.sh first." >&2; \
		exit 1; \
	fi
	$(PYTHON) scripts/build-master-doc.py --html

# ---------------- Diagrams ---------------- #

diagrams: $(DIAGRAM_SVG)

diagrams/%.svg: diagrams/%.mmd
	@if [ -z "$(MMDC)" ] && ! command -v docker >/dev/null 2>&1; then \
		echo "Neither mmdc nor docker installed. Run scripts/install/install-ubuntu.sh first." >&2; \
		exit 1; \
	fi
	@./scripts/render-diagrams.sh

# ---------------- Weight model ---------------- #

weight:
	$(PYTHON) scripts/weight-cg.py --tire-load 6779 --csv weight/axle-report.csv

# ---------------- CAD (FreeCAD headless) ---------------- #

cad:
	@if [ -z "$(FREECAD)" ]; then \
		echo "FreeCAD CLI not installed. Run scripts/install/install-ubuntu.sh first." >&2; \
		exit 1; \
	fi
	@mkdir -p $(CAD_OUT)
	$(PYTHON) scripts/build-cad.py --freecad "$(FREECAD)" --out "$(CAD_OUT)"

# ---------------- KiCad (CLI) ---------------- #

kicad:
	@if [ -z "$(KICAD_CLI)" ]; then \
		echo "kicad-cli not installed. Run scripts/install/install-ubuntu.sh first." >&2; \
		exit 1; \
	fi
	@mkdir -p $(KICAD_OUT)
	./scripts/kicad-build.sh

# ---------------- Tooling check ---------------- #

check-tools:
	@echo "Checking required tooling..."
	@printf "  %-20s %s\n" "python3"      "$$(command -v $(PYTHON) || echo MISSING)"
	@printf "  %-20s %s\n" "FreeCAD CLI"  "$${FREECAD:-MISSING}"
	@printf "  %-20s %s\n" "kicad-cli"    "$${KICAD_CLI:-MISSING}"
	@printf "  %-20s %s\n" "pandoc"       "$${PANDOC:-MISSING}"
	@printf "  %-20s %s\n" "mmdc"         "$${MMDC:-MISSING}"
	@printf "  %-20s %s\n" "git"          "$$(command -v git || echo MISSING)"
	@printf "  %-20s %s\n" "git-lfs"      "(not used)"

# ---------------- Clean ---------------- #

clean:
	rm -rf $(BUILD_DIR)
	rm -f MASTER.md MASTER.pdf MASTER.html
	rm -f diagrams/*.svg diagrams/*.png
	rm -f weight/axle-report*.csv
	rm -rf $(KICAD_OUT)
	@echo "All derived artifacts removed."
