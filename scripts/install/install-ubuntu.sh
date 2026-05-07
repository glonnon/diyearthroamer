#!/usr/bin/env bash
# install-ubuntu.sh — install the full DIY Earthroamer toolchain on
# Ubuntu (22.04+) or any Debian-derived distro.
#
# Tested on Ubuntu 22.04, 24.04. Should work on Debian 12+.
#
# Idempotent: re-running is safe; only missing packages get installed.
#
# Usage:
#     bash scripts/install/install-ubuntu.sh
#
# What it installs:
#   - Build essentials, git, git-lfs (just disabled, not used)
#   - Python 3 + pip (for helper scripts)
#   - FreeCAD 1.x (CAD)
#   - KiCad 8+ (electrical schematics)
#   - Blender (renders / walkthroughs)
#   - Inkscape (DXF/SVG cleanup)
#   - Pandoc + wkhtmltopdf (PDF render of MASTER.md)
#   - Node.js + Mermaid CLI (SVG render of diagrams)

set -euo pipefail

if ! command -v apt-get >/dev/null 2>&1; then
    echo "This script requires apt-get (Ubuntu/Debian)." >&2
    exit 1
fi

if [[ $EUID -ne 0 ]]; then
    SUDO="sudo"
else
    SUDO=""
fi

echo "=== DIY Earthroamer toolchain — Ubuntu installer ==="
echo

echo "[1/7] Updating apt index..."
$SUDO apt-get update -qq

echo "[2/7] Installing core dev tools..."
$SUDO apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    ca-certificates \
    python3 \
    python3-pip \
    python3-venv \
    make

echo "[3/7] Installing FreeCAD..."
# Ubuntu 24.04 ships FreeCAD 0.21; we want 1.x. Use the official PPA.
if ! command -v freecad >/dev/null 2>&1; then
    $SUDO add-apt-repository -y ppa:freecad-maintainers/freecad-stable || true
    $SUDO apt-get update -qq
    $SUDO apt-get install -y freecad freecad-python3 || \
        echo "PPA install failed; falling back to default repo (may be older)."
    $SUDO apt-get install -y freecad
fi

echo "[4/7] Installing KiCad 8..."
if ! command -v kicad >/dev/null 2>&1; then
    $SUDO add-apt-repository -y ppa:kicad/kicad-8.0-releases || true
    $SUDO apt-get update -qq
    $SUDO apt-get install -y kicad
fi

echo "[5/7] Installing Blender + Inkscape..."
$SUDO apt-get install -y blender inkscape

echo "[6/7] Installing Pandoc + wkhtmltopdf for PDF rendering..."
$SUDO apt-get install -y pandoc wkhtmltopdf

echo "[7/7] Installing Node.js + Mermaid CLI for diagram SVG..."
if ! command -v node >/dev/null 2>&1; then
    curl -fsSL https://deb.nodesource.com/setup_lts.x | $SUDO bash -
    $SUDO apt-get install -y nodejs
fi
if ! command -v mmdc >/dev/null 2>&1; then
    $SUDO npm install -g @mermaid-js/mermaid-cli
fi

echo
echo "=== Done. Verifying tooling: ==="
make check-tools 2>/dev/null || (cd "$(dirname "$0")/../.." && make check-tools)
echo
echo "Next: 'make doc' or 'make all' from the repo root."
