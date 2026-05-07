# Electrical System One-Line

ASCII one-line of the locked architecture (ADR-0004). KiCad project
will replace this with a proper schematic once parts/symbols selected,
but this is the source of truth for sizing today.

```
                             SOLAR ARRAY
                       4× ~330W panels in 2s2p
                          (Voc/Isc per array)
                                |
                                v
                     ┌────────────────────────┐
                     │ Combiner box (roof)    │ MC4 + 15A fuses
                     └────────────────────────┘
                                | 10 AWG
                                v
                     ┌────────────────────────┐
                     │ Victron MPPT 250/100   │
                     └────────────────────────┘
                                | 6 AWG, 100A breaker
                                v
                +---------------------------------+
                |        48V DC BUS BAR           |   <-- single source
                +---------------------------------+
                  ^               ^                ^
                  |               |                |
                  |               |                |
        Class T 250A          50A breaker      100A fuse
                  |               |                |
       ┌──────────┴──┐     ┌──────┴──────┐  ┌──────┴────────┐
       │  EPOCH 48V  │     │  ORION XS   │  │  MULTIPLUS-II  │
       │  4× 100Ah   │     │   48 / 24   │  │   48 / 5000    │
       │  20.5 kWh   │     │  50A out    │  │  120V AC out   │
       │ heated BMS  │     │             │  │  240V split    │
       │ CAN to GX   │     └──────┬──────┘  └──────┬────────┘
       └─────────────┘            |                |
                                  v                v
                  +---------------+--+    +--------+--------+
                  |   24V SUB-BUS    |    |   AC LOAD CENTER|
                  +------------------+    +-----------------+
                    |        |     |       |  |  |  |  |
                  loads ...lights pump   GFCIs branches outlets
                    |
                    v
              +-----+--------+
              | 24→12V  20A  |  for legacy 12V accessories only
              +--------------+
                    |
                    v
                 12V loads
```

```
SHORE INLET (30A)
   |  10 AWG, 30A
   v
[SmartPlug 30A]
   |
   v
[Progressive EMS]
   |
   v
[Galvanic isolator]
   |
   v
[Multiplus AC IN]
```

```
ALTERNATOR PATH
F550 OEM alternator (200A, 12V)
   |  4/0 AWG short run
   v
[Wakespeed regulator]
   |
   v
12V starter battery
   |  4 AWG via auto-disconnect relay
   v
[12V → 48V boost charger, 30A out @48V]   (e.g., Sterling, Renogy boost,
   |                                       or Victron Orion XS 12/48 if
   |                                       available at required A)
   v
48V DC bus
```

## Bonding & grounding (ABYC E-11)

- **DC negative:** single-point ground at the 48V negative bus bar;
  bus bar bonded to the chassis at one location only.
- **AC neutral-ground bond:** at the inverter output side of the
  transfer switch; **broken when on shore** (Multiplus does this
  automatically).
- **Galvanic isolator** in the shore-power ground.
- **Bonding** for safety: chassis, shell skin, inverter case, battery
  rack, all to a common bonding bar.

## Fault protection

| Branch | Device | Rating |
|---|---|---|
| Battery to bus | Class T fuse | 250 A |
| Bus to MultiPlus | DC breaker | 200 A (peak) |
| Bus to MPPT | DC breaker | 100 A |
| Bus to Orion XS | Breaker or fuse | 50 A |
| Solar combiner per string | MC4 inline fuse | 15 A |
| 24V sub-bus to fuse blocks | ANL or MRBF | 60 A |
| 24V branches | ATC fuses | 5–20 A per circuit |
| AC main | breaker | 30 A |
| AC branches | 15 A or 20 A breakers (GFCI on wet) | per branch |

## Disconnects

- 48V battery main disconnect (Blue Sea m-Series or Victron BatteryProtect).
- Solar isolator switch (rooftop accessible).
- AC shore main on the inlet side.
- Inverter remote on/off at galley + bedside (Cerbo touch).

## Monitoring

- Victron Cerbo GX with GX Touch 50.
- Victron SmartShunt 500A on battery negative.
- Temperature sensors on each Epoch module + inverter heatsink.
- App: VictronConnect + VRM via Starlink/cellular.
