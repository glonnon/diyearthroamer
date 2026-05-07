# Diagrams

Mermaid source diagrams. Two ways to view:

1. **Render in any GitHub-flavored Markdown viewer** — Mermaid blocks
   render natively. The same source is also embedded inline in
   `electrical/oneline.md`, `plumbing/pid.md`, etc.
2. **Render to SVG** with the Mermaid CLI (`mmdc`):

   ```sh
   ./scripts/render-diagrams.sh
   ```

   Produces an `.svg` next to each `.mmd`. Generated SVGs are
   gitignored — regenerate any time.

## Files

| Source | What it shows |
|---|---|
| [`electrical-oneline.mmd`](electrical-oneline.mmd) | 48V bus, batteries, MPPT, MultiPlus, AC, alternator, monitoring |
| [`plumbing-fresh.mmd`](plumbing-fresh.mmd) | Fresh-water supply: fill, tanks, pump, manifold, fixtures |
| [`plumbing-drains.mmd`](plumbing-drains.mmd) | Grey + black drains, vents, dump panel |
| [`hydronic-loop.mmd`](hydronic-loop.mmd) | Webasto loop — cabin, radiant, towel rack, tank bay, DHW, engine pre-heat |
| [`schematic-hierarchy.mmd`](schematic-hierarchy.mmd) | KiCad sub-sheet tree |

## Installing the Mermaid CLI

```sh
# Node-based (most reliable)
npm install -g @mermaid-js/mermaid-cli
mmdc --version

# Or use Docker (no node required)
docker pull minlag/mermaid-cli
```

The render script tries `mmdc` first, then falls back to a Docker
invocation if Docker is available.

## Editing

- Use any text editor.
- Live preview: VS Code `bierner.markdown-mermaid` extension; or
  `mermaid.live`.
- Keep diagrams **focused** — one subsystem per file. Compose larger
  views by referencing them in Markdown documents.

## Style guide (use the same palette across diagrams)

Every diagram must start with:

```
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#fff','primaryTextColor':'#000','primaryBorderColor':'#000','lineColor':'#1f2937','fontFamily':'Inter, system-ui, sans-serif','fontSize':'15px'}}}%%
```

This forces black text and a clean font regardless of viewer theme
(light vs dark mode).

Standard `classDef` palette — pick the one that matches the role:

| Role | Fill | Stroke | Width |
|---|---|---|---|
| **bus / busbar** | `#fed7aa` orange-200 | `#7c2d12` dark amber | 3px |
| **battery / power source** | `#bbf7d0` green-200 | `#14532d` dark green | 2–3px |
| **inverter / converter** | `#bfdbfe` blue-200 | `#1e3a8a` dark blue | 2px |
| **solar** | `#fde68a` yellow-200 | `#78350f` dark amber | 2px |
| **AC / shore** | `#fbcfe8` pink-200 | `#831843` dark pink | 2px |
| **load / consumer** | `#ddd6fe` purple-200 | `#4c1d95` dark purple | 2px |
| **passive / fuse / breaker** | `#e5e7eb` gray-200 | `#1f2937` dark gray | 2px |
| **cold water** | `#bfdbfe` blue-200 | `#1e3a8a` dark blue | 2px |
| **hot water** | `#fecaca` red-200 | `#991b1b` dark red | 2px |
| **tank** | `#bbf7d0` green-200 | `#14532d` dark green | 3px |
| **filter** | `#ddd6fe` purple-200 | `#4c1d95` dark purple | 2px |
| **heat / hydronic** | `#fed7aa` orange-200 | `#7c2d12` dark amber | 2–3px |
| **fixture** | `#f3f4f6` gray-100 | `#1f2937` dark gray | 2px |
| **drain output** | `#fde68a` yellow-200 | `#78350f` dark amber | 3px |

All `classDef` rules must include `color:#000` for explicit black
text. Strokes are 2px minimum, 3px for primary buses / tanks /
outputs.
