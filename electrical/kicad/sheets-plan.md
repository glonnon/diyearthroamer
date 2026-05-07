# KiCad Hierarchical Sheet Plan

The root schematic (`diy-earthroamer.kicad_sch`) is the top of a
hierarchical design. Each subsystem is a separate sheet so the
schematic stays printable and reviewable.

## Planned sheets

| Sheet | File (planned) | Scope |
|---|---|---|
| `Root` | `diy-earthroamer.kicad_sch` | Top-level: shore + alternator + battery + bus, hierarchical pins out to sub-sheets |
| `48V_Bus` | `sheets/48v-bus.kicad_sch` | Battery bank, Class T main, busbar, MultiPlus, MPPT, mini-split, alternator path |
| `24V_SubBus` | `sheets/24v-subbus.kicad_sch` | Orion XS 48-24, ANL fuses, sub-bus distribution |
| `12V_Legacy` | `sheets/12v-legacy.kicad_sch` | 24-12V converter, legacy fuse block |
| `Solar` | `sheets/solar.kicad_sch` | 4× 320W panels, combiner, MPPT input, gland |
| `AC_Distribution` | `sheets/ac-distro.kicad_sch` | Shore inlet, EMS, isolator, MultiPlus AC, load center, branch breakers |
| `Lighting` | `sheets/lighting.kicad_sch` | Interior + exterior LED, switches, dimmers |
| `HVAC_Control` | `sheets/hvac-control.kicad_sch` | Mini-split control, hydronic blower, MaxxAir fans, thermostats |
| `Plumbing_Control` | `sheets/plumbing-control.kicad_sch` | Pump, tank senders (SeeLevel RV-C), heater pads |
| `LiftBox_Control` | `sheets/liftbox.kicad_sch` | Dual actuators, sync controller, limit switches, interlocks |
| `Comms_AV` | `sheets/comms-av.kicad_sch` | Starlink, router, TV, audio, USB-C PD distribution |

## Conventions

- **Net labels** use ABYC color codes mirrored in net colors (red =
  positive, yellow/black = ground/negative, etc.).
- **Power ports:** `+48V`, `+24V`, `+12V`, `GND` (DC negative bus),
  `AC_L`, `AC_N`, `EGC`.
- **Reference designators:**
  - `BAT*` battery modules
  - `F*` fuses (number per panel-schedule-dc.csv ordering)
  - `CB*` breakers
  - `SW*` switches/relays
  - `Q*` MOSFETs / solid-state relays
  - `K*` mechanical relays
  - `J*` connectors / inlets
  - `U*` controllers (Cerbo, MPPT, MultiPlus)
- **Title block:** date + rev bumped per release tag.

## Building a sheet (workflow in KiCad)

1. Open `diy-earthroamer.kicad_pro` in KiCad 8 (Schematic Editor).
2. `Place → Hierarchical Sheet`, name it (e.g., `48V_Bus`), filename
   `sheets/48v-bus.kicad_sch`.
3. Double-click into the new sheet, draw the schematic.
4. Add hierarchical pins to expose nets to the parent.
5. Sync to ERC (`Inspect → Electrical Rules Checker`).
6. Export PDF: `File → Plot → Plot All Pages` to `electrical/exports/`.

## Symbol libraries to add

KiCad's stock libs cover most things, but for marine/RV gear add a
project-local lib:

- `electrical/kicad/lib/dy-earthroamer.kicad_sym` — symbols for:
  - Epoch 48V module (with BMS comm pins)
  - Victron MultiPlus-II 48/5000 (DC in/out, AC in/out, VE.Bus)
  - Victron Cerbo GX (CAN, VE.Direct, VE.Bus, GX touch, NMEA 2000)
  - Victron SmartShunt (battery + load shunt)
  - Victron MPPT 250/100 (PV in, battery out, VE.Direct)
  - Victron Orion XS 48/24 (in/out + sense)
  - Mabru SCS 12000 (DC in, comm)
  - Webasto Dual Top Evo 8 (12/24V control, fuel, sensors)
  - SmartPlug 30A inlet
  - Progressive EMS-PT30X
  - Garnet SeeLevel RV-C
  - Linak LA36 actuator
  - Generic ABYC fuse holders / breakers / busbars

Build these incrementally as each sheet needs them. Commit the
`.kicad_sym` file as text (it's diff-friendly).

## Output products

For each release tag of the schematic:

- PDF of every sheet (`electrical/exports/<sheet>.pdf`)
- BOM CSV (`electrical/exports/bom.csv`) — auto-generated
- Net list (`electrical/exports/netlist.txt`) — for sanity checks
- Hierarchical block diagram (`electrical/exports/hierarchy.pdf`)

## Status

- Project file + empty root sheet committed (skeleton).
- Sub-sheets to be drawn in KiCad GUI; this directory will fill in
  as they're drafted.
