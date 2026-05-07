# 48V_Bus Sheet — Drawing Plan

The KiCad file `48v-bus.kicad_sch` is a valid empty sheet with title
block. Open it in KiCad 8 and draw the schematic per this plan. Each
component listed here has a symbol in the project library
(`lib/diy-earthroamer.kicad_sym`) — use **Place → Symbol** and search
the symbol name.

## Components to place

| Ref | Symbol (project lib) | Qty | Notes |
|---|---|---|---|
| BT1..BT4 | `Epoch_48V_100Ah` | 4 | wired in parallel |
| F1 | `Class_T_Fuse_250A` | 1 | between battery + bus and busbar |
| BUS1 | `BlueSea_BusBar_250A_5pos` | 1 | + bus distribution |
| BUS_GND | `BlueSea_BusBar_250A_5pos` | 1 | DC ground bus (single-point ground here) |
| U1 | `Victron_MultiPlus_II_48_5000` | 1 | inverter/charger |
| U2 | `Victron_MPPT_250_100` | 1 | solar charger |
| U3 | `Victron_Orion_XS_48_24` | 1 | feeds 24V sub-bus |
| U4 | `Mabru_SCS_12000` | 1 | mini-split |
| U5 | `Victron_SmartShunt_500A` | 1 | in DC negative path |
| U6 | `Victron_Cerbo_GX` | 1 | system monitor (powered from 12V_Legacy) |
| CB1 | `DC_Breaker` | 1 | 200A — Multiplus DC in |
| CB2 | `DC_Breaker` | 1 | 100A — MPPT |
| CB3 | `DC_Breaker` | 1 | 50A — Orion XS |
| CB4 | `DC_Breaker` | 1 | 30A — Mabru |

## Wiring (net names)

Use these net labels (matches `electrical/wire-list.csv` and
`electrical/oneline.md`):

- `+48V_BAT` — battery + bus (between BT array and Class T)
- `+48V` — main 48V positive bus (after Class T)
- `GND_DC` — single DC negative bus
- `+24V_BUS` — 24V sub-bus output of Orion XS (export as hierarchical pin)
- `PV_HV+`, `PV_HV-` — high-voltage solar input from `Solar` sheet
- `AC_OUT_L`, `AC_OUT_N`, `AC_OUT_PE` — AC output to `AC_Distribution`
- `AC_IN_L`, `AC_IN_N`, `AC_IN_PE` — AC input from shore (from `AC_Distribution`)
- `VE_BUS_A`, `VE_BUS_B` — VE.Bus to Cerbo GX
- `VE_DIRECT_MPPT` — VE.Direct from MPPT to Cerbo
- `VE_DIRECT_SHUNT` — VE.Direct from SmartShunt to Cerbo
- `CAN_BMS_H`, `CAN_BMS_L` — Epoch BMS CAN to Cerbo

## Hierarchical pins (export to root)

Add these on the sheet boundary (Place → Hierarchical Label, or sheet
pins on the parent):

- **OUT** to `Solar`: `PV_HV+`, `PV_HV-`
- **OUT** to `24V_SubBus`: `+24V_BUS`, `GND_DC`
- **OUT** to `AC_Distribution`: `AC_OUT_L`, `AC_OUT_N`, `AC_OUT_PE`
- **IN**  from `AC_Distribution`: `AC_IN_L`, `AC_IN_N`, `AC_IN_PE`
- **OUT** to `Comms_AV` / `12V_Legacy`: `+12V_FROM_CERBO_AUX` (small)

## Step-by-step (in KiCad)

1. **Open** `electrical/kicad/diy-earthroamer.kicad_pro`. Confirm the
   project symbol library `diy-earthroamer` shows in
   **Preferences → Manage Symbol Libraries → Project Specific**.
2. **Open** the `48V_Bus` sheet by double-clicking it from the root.
3. **Place** the 4× Epoch modules along the left margin in a column.
   Wire all `+48V` pins together to a single net `+48V_BAT`. Wire all
   `GND` pins together. Wire all CAN_H/CAN_L together (twist pair).
4. **Place** `Class_T_Fuse_250A` immediately to the right of the
   battery + bus, in series with `+48V_BAT`. Output net = `+48V`.
5. **Place** `Victron_SmartShunt_500A` in series with `GND_DC`
   between battery negative and the GND busbar.
6. **Place** `BlueSea_BusBar_250A_5pos` for `+48V` distribution.
   Connect 4 outputs through breakers (200A → MultiPlus DC+,
   100A → MPPT BAT+, 50A → Orion XS IN+, 30A → Mabru DC+).
7. **Place** the second busbar for `GND_DC` distribution (each
   downstream device's negative returns here).
8. **Place** `Victron_MultiPlus_II_48_5000` to the right of the bus.
   Wire DC+/DC- through CB1. Add hierarchical labels for AC IN and
   AC OUT.
9. **Place** `Victron_MPPT_250_100`. Add hierarchical labels
   `PV_HV+` / `PV_HV-` for the PV input. Wire BAT+/BAT- to bus
   through CB2.
10. **Place** `Victron_Orion_XS_48_24`. Wire IN+/IN- to bus through
    CB3. Add hierarchical labels for OUT+/OUT- as `+24V_BUS` and
    `GND_DC`.
11. **Place** `Mabru_SCS_12000`. Wire DC+/DC- through CB4.
12. **Place** `Victron_Cerbo_GX`. Wire VE.Bus to MultiPlus.
    VE.Direct1 → MPPT, VE.Direct2 → SmartShunt. CAN_BMS to the Epoch
    bank's CAN bus.
13. **Annotate** (Tools → Annotate Schematic).
14. **ERC** (Inspect → Electrical Rules Checker). Resolve or
    document exclusions.
15. **Plot PDF** (File → Plot → Plot All Pages) to
    `electrical/kicad/exports/48v-bus.pdf`.

## Acceptance criteria

- ERC clean (or exclusions documented in
  `electrical/kicad/erc-exclusions.md`).
- Hierarchical pins on root sheet match net labels here.
- Title block rev bumped on each release.
- PDF export committed for review (via Git LFS).
