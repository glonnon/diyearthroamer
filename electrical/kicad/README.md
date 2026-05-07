# KiCad Project — `diy-earthroamer`

The electrical schematic project. Open `diy-earthroamer.kicad_pro` in
**KiCad 8.0+**.

## Layout

```
electrical/kicad/
  diy-earthroamer.kicad_pro     project (JSON, text)
  diy-earthroamer.kicad_sch     root schematic (s-expr)
  sheets-plan.md                hierarchical sheet plan + conventions
  sheets/                       hierarchical sub-sheets (added as drawn)
  lib/                          project symbol library (added as needed)
  exports/                      generated PDFs / BOM / netlist (gitignored)
```

## Quickstart (first time)

1. Install KiCad 8.0 or later.
2. `git lfs pull` to pull any binary footprints (none yet).
3. Open `diy-earthroamer.kicad_pro` from the KiCad project chooser.
4. Open the Schematic Editor; you'll see the empty root sheet with
   the title block populated.
5. Read `sheets-plan.md` for the hierarchical sheet plan and ABYC
   conventions.
6. Start with `48V_Bus` — it pulls in the battery bank, MultiPlus,
   MPPT, mini-split, and alternator path.

## Working conventions

- Schematic text format committed as-is (don't binary-mangle).
- Run `Inspect → Electrical Rules Checker` before each commit;
  resolve or document exclusions in `electrical/erc-exclusions.md`.
- Bump `rev` in the title block on each release tag.
- Export PDFs to `exports/` and commit only via Git LFS.

## Why a skeleton, not a full schematic

KiCad schematics are best drawn interactively in the editor (component
placement, net routing, hierarchical pin layout). The skeleton here
gives:

- A valid project file you can open immediately.
- The hierarchical plan (`sheets-plan.md`) so the structure is locked
  before drawing.
- The conventions (designators, net naming, ABYC colors) so multiple
  contributors stay aligned.

The actual schematic content is built in KiCad as the design firms up.
