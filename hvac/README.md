# HVAC

## Heating (locked, ADR-0007) — Diesel Hydronic

One integrated diesel hydronic unit (Webasto Dual Top Evo / Aqua-Hot
250D / Timberline — O4) provides:

1. Cabin heat via fan-coils in living, bedroom, bath
2. Domestic hot water (DHW) — galley, bath, exterior shower
3. Radiant floor zones (living/galley, bath)
4. Heated towel rack (bath)
5. Tank/wet-bay freeze-protection bypass
6. Optional engine pre-heat tap

Backup: standalone diesel air heater (Webasto Air Top 2000 / Autoterm
Air 2D) for redundancy.

## Cooling (preferred) — Mini-split heat pump

DC mini-split (Mabru SCS / Velit / Webasto FCF — O3) sized 9k–13.5k
BTU. Indoor head wall-mounted in living area; outdoor condenser in
vented external locker.

Fallback: rooftop low-profile AC (Nomadic Cooling 24V or RecPro 12V).

## Ventilation

- 2x MaxxAir Deluxe fans (over galley and bed), reversible, rain hood.
- Bathroom dedicated exhaust fan, humidity-triggered.
- Cross-flow openable windows.

## Controls

- Single touchscreen thermostat with per-zone setpoints (Truma CP Plus
  or custom on Cerbo GX with RV-C bridge).
- Schedule + vacation/freeze mode.
- Remote control via app over Starlink/cell.

## Heat-load calc inputs (TBD in `heat-load.csv`)

- Shell U-values per panel
- Window U-values
- Ambient extremes: -10 °F to +110 °F
- Occupancy + appliance internal gains
- Solar gain by window orientation

## Files (planned)

- `heat-load.csv` — sensible + latent loads for heating and cooling
  design days.
- `hydronic-loop.drawio` — P&ID for hydronic system.
- `duct-routing.FCStd` — fan-coil placement and short ducts (lives in
  `cad/60-hvac/`).
