# Electrical

KiCad project (skeleton) lives in `electrical/kicad/` once initialized.
For now this directory holds the load study and the system one-line as
markdown until the schematics are drawn.

## Architecture (locked, ADR-0004)

- **48V DC primary bus** — Epoch LiFePO4 battery bank (~20 kWh usable).
- **24V DC sub-bus** via 48→24V converter (Victron Orion XS or
  equivalent), feeding the bulk of cabin loads.
- **12V DC** only for legacy accessories via 24→12V converter.
- **120/240V AC** from Victron MultiPlus-II 48/5000 inverter/charger.
- **Solar:** 1.0–1.3 kW into 48V via Victron MPPT.
- **Alternator charging:** 12V high-output alternator + 12→48V boost
  chain (or future 48V alternator).
- **Shore:** 30A inlet → EMS → MultiPlus AC input.

## Files

- `load-study.csv` — daily Wh per circuit, source-of-truth for bank
  and inverter sizing.
- `oneline.drawio` — system one-line diagram (TBD).
- `kicad/diy-earthroamer.kicad_pro` — KiCad project (TBD).
- `panel-schedule-dc.csv` — every DC fuse, breaker, and feed.
- `panel-schedule-ac.csv` — every AC breaker.
- `wire-list.csv` — every cable: from, to, gauge, length, voltage drop.

## Compliance targets

- ABYC E-11 (DC + AC on boats, applied here for marine-grade harness).
- NEC Article 551 for AC distribution where applicable.
- All terminations heat-shrink crimp; no wire nuts.
- ABYC color code; tinned copper throughout.
- Single-point DC ground at battery negative bus bar.
- AC neutral-ground bond at inverter when off shore power.
