#!/usr/bin/env bash
# kicad-build.sh — run KiCad ERC and export PDFs for the project.
#
# Invoked by `make kicad`. Requires kicad-cli (KiCad 8+).
#
# Outputs:
#   electrical/kicad/exports/<sheet>.pdf
#   electrical/kicad/exports/erc-report.txt

set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
PROJ="$REPO/electrical/kicad/diy-earthroamer.kicad_pro"
SCH="$REPO/electrical/kicad/diy-earthroamer.kicad_sch"
OUT="$REPO/electrical/kicad/exports"

mkdir -p "$OUT"

if ! command -v kicad-cli >/dev/null 2>&1; then
  echo "kicad-cli not found. Install with scripts/install/install-ubuntu.sh" >&2
  exit 2
fi

if [[ ! -f "$PROJ" ]]; then
  echo "Project file missing: $PROJ" >&2
  exit 1
fi

echo "  ERC..."
kicad-cli sch erc \
  --output "$OUT/erc-report.txt" \
  --severity-all \
  --exit-code-violations \
  "$SCH" || {
  echo "  ERC reported violations (see $OUT/erc-report.txt)"
}

echo "  Plot all sheets to PDF..."
kicad-cli sch export pdf \
  --output "$OUT/diy-earthroamer.pdf" \
  --pages all \
  "$SCH"

echo "  Generate netlist..."
kicad-cli sch export netlist \
  --output "$OUT/netlist.net" \
  "$SCH"

echo "  BOM CSV..."
kicad-cli sch export bom \
  --output "$OUT/bom.csv" \
  --fields "Reference,Value,Footprint,Datasheet,Manufacturer" \
  --group-by "Value" \
  "$SCH" || true

echo
echo "KiCad outputs in: $OUT"
ls -1 "$OUT"
