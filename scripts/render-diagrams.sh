#!/usr/bin/env bash
# render-diagrams.sh — render every diagrams/*.mmd to .svg via Mermaid CLI.
#
# Tries mmdc on PATH first; falls back to Docker (minlag/mermaid-cli)
# if mmdc is not installed.
#
# Usage:
#     ./scripts/render-diagrams.sh
#
# Install the Mermaid CLI:
#     npm install -g @mermaid-js/mermaid-cli
# Or use Docker (auto-detected):
#     docker pull minlag/mermaid-cli

set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
SRC_DIR="$REPO/diagrams"

if [[ ! -d "$SRC_DIR" ]]; then
  echo "No diagrams/ directory at $SRC_DIR" >&2
  exit 1
fi

# Pick a renderer
if command -v mmdc >/dev/null 2>&1; then
  RUN="mmdc"
elif command -v docker >/dev/null 2>&1; then
  RUN="docker run --rm -u $(id -u):$(id -g) -v $REPO:/data minlag/mermaid-cli mmdc"
else
  echo "Neither 'mmdc' nor 'docker' found on PATH." >&2
  echo "Install one of:" >&2
  echo "  npm install -g @mermaid-js/mermaid-cli" >&2
  echo "  docker pull minlag/mermaid-cli" >&2
  exit 2
fi

echo "Renderer: $RUN"
echo

count=0
for src in "$SRC_DIR"/*.mmd; do
  [[ -e "$src" ]] || continue
  name="$(basename "$src" .mmd)"
  out="$SRC_DIR/$name.svg"
  echo "  $name.mmd -> $name.svg"
  if [[ "$RUN" == "mmdc" ]]; then
    "$RUN" -i "$src" -o "$out" -b transparent
  else
    # Docker: paths are /data/<rel>
    rel_in="diagrams/$(basename "$src")"
    rel_out="diagrams/$(basename "$out")"
    $RUN -i "/data/$rel_in" -o "/data/$rel_out" -b transparent
  fi
  count=$((count+1))
done

echo
echo "Rendered $count diagram(s) to $SRC_DIR/*.svg"
