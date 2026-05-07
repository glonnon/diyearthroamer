# Electrical System One-Line

Locked architecture (ADR-0004). KiCad project will replace this with a
proper schematic once sub-sheets are drawn, but this is the source of
truth for sizing today.

## Mermaid view (renders inline on GitHub; SVG via `scripts/render-diagrams.sh`)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#fff','primaryTextColor':'#000','primaryBorderColor':'#000','lineColor':'#1f2937','fontFamily':'Inter, system-ui, sans-serif','fontSize':'15px'}}}%%
flowchart TB
    classDef bus fill:#fed7aa,stroke:#7c2d12,stroke-width:3px,color:#000
    classDef batt fill:#bbf7d0,stroke:#14532d,stroke-width:2px,color:#000
    classDef inv fill:#bfdbfe,stroke:#1e3a8a,stroke-width:2px,color:#000
    classDef solar fill:#fde68a,stroke:#78350f,stroke-width:2px,color:#000
    classDef ac fill:#fbcfe8,stroke:#831843,stroke-width:2px,color:#000
    classDef load fill:#ddd6fe,stroke:#4c1d95,stroke-width:2px,color:#000
    classDef proto fill:#e5e7eb,stroke:#1f2937,stroke-width:2px,color:#000

    PVarr[4x 320W panels<br/>2s2p ~75 Voc]:::solar
    Combiner[Combiner<br/>15A MC4 fuses]:::proto
    MPPT[MPPT 250/100]:::solar
    Epoch[Epoch 48V x4<br/>~20 kWh]:::batt
    ClassT[Class T 250A]:::proto
    Shunt[SmartShunt 500A]:::batt
    BusPos[+48V Bus]:::bus
    BusGnd[GND DC]:::bus
    Multi[MultiPlus-II<br/>48 / 5000]:::inv
    Orion[Orion XS 48-24]:::inv
    Mabru[Mabru SCS 12000]:::load
    Bus24[+24V Sub-Bus]:::bus
    Bus12[+12V Legacy]:::bus
    Loads24[Lights / Pumps / Fans / Heater / Lift-box]:::load
    Shore[Shore 30A SmartPlug]:::ac
    EMS[EMS]:::ac
    LoadCenter[120V Load Center]:::ac
    ACLoads[Galley / Cooktop / Microwave / Bath / Bed / Ext]:::load
    Alt[F550 alternator]:::ac
    Boost[12-48V boost]:::inv
    Cerbo[Cerbo GX]:::inv

    PVarr --> Combiner --> MPPT --> BusPos
    Epoch --> ClassT --> BusPos
    Epoch --> Shunt --> BusGnd
    BusPos --> Multi & Orion & Mabru
    Orion --> Bus24 --> Loads24
    Bus24 --> Bus12
    Alt --> Boost --> BusPos
    Shore --> EMS --> Multi --> LoadCenter --> ACLoads
    Multi -. VE.Bus .-> Cerbo
    MPPT -. VE.Direct .-> Cerbo
    Shunt -. VE.Direct .-> Cerbo
    Epoch -. CAN BMS .-> Cerbo
```

## ASCII one-line (full detail)

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
