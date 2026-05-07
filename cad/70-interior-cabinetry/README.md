# 70-interior-cabinetry — Hybrid Aluminum + Plywood

All cabinetry uses the hybrid construction defined in REQUIREMENTS.md
§19: 6061 aluminum or 8020 extrusion skeleton + Baltic birch plywood
panels and faces.

## Modules planned

- `galley/` — base cabinets, drawer towers, pantry, sink module,
  cooktop module, range hood, fridge cabinet
- `dinette/` — bench bases, table, storage, seat-belt anchor frames
- `bath/` — vanity, shower pan surround, towel rack mount, medicine
  cabinet
- `bed/` — cabover platform, headboard, side wardrobes, under-bed
  drawers (rear access)
- `wardrobe/` — full-height hanging + drawers
- `service-bay/` — pump/manifold/filter rack
- `battery-bay/` — Epoch module rack with vent + fire-rated liner

## CNC outputs per part

- Native FreeCAD `.FCStd`
- Flat pattern `.dxf` for the plywood (nested in sheets)
- G-code `.nc` for the chosen router (Onefinity / ShopBot / Avid)
- Setup PDF (origin, tool list, run time)
- Aluminum sheet parts: `.dxf` for waterjet/laser bureau

## Hardware spec (uniform across modules)

- Drawer slides: Blum Movento or Accuride 3832 (locking, travel-rated)
- Hinges: Blum Clip-Top + secondary catch
- Latches: Southco compression on travel doors
- Fasteners: stainless; aluminum-to-aluminum with rivet-nuts
- Edge banding: PVC or solid hardwood
- Finish: low-VOC waterborne poly (interior), HPL or Fenix (faces)
