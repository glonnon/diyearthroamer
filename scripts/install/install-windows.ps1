# install-windows.ps1 — install the full DIY Earthroamer toolchain on
# Windows 10/11 using winget.
#
# Run from an elevated PowerShell:
#     powershell -ExecutionPolicy Bypass -File scripts\install\install-windows.ps1
#
# Idempotent: winget skips packages already installed.
#
# What it installs:
#   - Git, Python 3.12 (for helper scripts)
#   - FreeCAD 1.x
#   - KiCad 8+
#   - Blender, Inkscape
#   - Pandoc + wkhtmltopdf (PDF render)
#   - Node.js LTS + Mermaid CLI (SVG render)
#   - GNU Make for Windows (for the Makefile)

$ErrorActionPreference = "Stop"

function Install-Pkg($id, $label) {
    Write-Host ""
    Write-Host "==> $label ($id)" -ForegroundColor Cyan
    winget install --id $id --silent --accept-source-agreements --accept-package-agreements
    if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne -1978335189) {
        # -1978335189 == APPINSTALLER_CLI_ERROR_UPDATE_NOT_APPLICABLE
        # which means already installed, latest version.
        Write-Warning "winget exited $LASTEXITCODE for $id; continuing"
    }
}

Write-Host "=== DIY Earthroamer toolchain - Windows installer ===" -ForegroundColor Green
Write-Host ""

if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    Write-Error "winget is required but not found. Install App Installer from the Microsoft Store first."
    exit 1
}

# Core dev tools
Install-Pkg "Git.Git"                  "Git for Windows"
Install-Pkg "Python.Python.3.12"       "Python 3.12"
Install-Pkg "GnuWin32.Make"            "GNU Make"

# CAD / electrical / 3D
Install-Pkg "FreeCAD.FreeCAD"          "FreeCAD 1.x"
Install-Pkg "KiCad.KiCad"              "KiCad 8.0"
Install-Pkg "BlenderFoundation.Blender" "Blender 4.x"
Install-Pkg "Inkscape.Inkscape"        "Inkscape"

# Doc rendering
Install-Pkg "JohnMacFarlane.Pandoc"    "Pandoc"

# wkhtmltopdf is no longer maintained but still useful for pandoc PDFs.
# An alternative is MiKTeX for full LaTeX rendering.
Install-Pkg "wkhtmltopdf.wkhtmltopdf"  "wkhtmltopdf"

# Node + Mermaid CLI
Install-Pkg "OpenJS.NodeJS.LTS"        "Node.js LTS"

Write-Host ""
Write-Host "==> Mermaid CLI (npm)" -ForegroundColor Cyan
# Refresh PATH so npm is reachable in this session.
$env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + `
            [Environment]::GetEnvironmentVariable("Path", "User")
npm install -g `@mermaid-js/mermaid-cli

Write-Host ""
Write-Host "=== Done. ===" -ForegroundColor Green
Write-Host ""
Write-Host "Restart your terminal so PATH updates pick up. Then verify:"
Write-Host "    make check-tools"
Write-Host ""
Write-Host "Tip: from PowerShell or Git Bash, use 'make doc' / 'make all' / etc."
