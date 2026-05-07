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
