# Heat Load Analysis — Globe Trekker 21' on F550

Calculation drives both **heating BTU sizing** (closes O4 — hydronic
unit) and **cooling BTU sizing** (closes O3 — mini-split unit).
All numbers committed to `heat-load.csv` so they recompute as inputs
change.

## Envelope assumptions

| Surface | Area (sf) | U-value | R-value | Source |
|---|---|---|---|---|
| Side walls (2x) | 294 | 0.067 | R-15 | Composite shell vendor spec |
| End walls (2x) | 98 | 0.067 | R-15 | |
| Roof | 147 | 0.050 | R-20 | (panels add ~R-1, ignored) |
| Floor | 147 | 0.067 | R-15 | (over subframe + radiant assembly) |
| Windows (6 dual-pane acrylic, ~6 sf ea) | 36 | 0.350 | R-2.9 | Tern / Seitz datasheet |
| Door | 18 | 0.150 | R-6.7 | Composite plug door |
| **Total envelope** | **740** | | | |

Interior volume: 21' × 7' × 7' = **1,029 ft³** (less cabover nose volume,
plus cabover volume, ≈ same).

Infiltration: assumed **0.3 ACH** (well-sealed composite with gasketed
door + dual-pane acrylic).

## Design days

| Mode | Outdoor | Indoor | ΔT |
|---|---|---|---|
| Heating design | -10 °F | 70 °F | 80 °F |
| Cooling design | 110 °F | 75 °F | 35 °F |

## Heating sensible load

```
Q = Σ (U × A × ΔT)  +  infiltration  +  internal-gain credit
```

| Source | BTU/hr |
|---|---|
| Side walls | 1,576 |
| End walls | 525 |
| Roof | 588 |
| Floor | 788 |
| Windows | 1,008 |
| Door | 216 |
| Infiltration (0.3 ACH × 1,029 × 0.018 × 80) | 444 |
| Internal gain credit (2 people + electronics) | -800 |
| **Cabin sensible heat load (design)** | **~4,345** |

## Auxiliary hydronic loads (simultaneous worst case)

| Load | BTU/hr |
|---|---|
| Radiant floor (≈ 100 sf × 25) | 2,500 |
| Heated towel rack | 700 |
| Tank-bay freeze loop | 1,000 |
| **Aux subtotal** | **4,200** |

## Domestic hot water (peak)

| Load | BTU/hr |
|---|---|
| Shower (2 gpm × 60°F rise × 500) | 60,000 (peak, 5–10 min) |
| Galley/bath sink (intermittent) | 10,000 (peak) |

DHW is **buffered by a hydronic reservoir** (typically 4–6 gal in the
heater unit), so the burner doesn't need to source the full 60 kBTU/hr;
it needs to recover the reservoir between draws. Sizing rule: burner
≥ 1.5× simultaneous cabin + aux + average DHW recovery.

## Cabin cooling load

| Source | BTU/hr |
|---|---|
| Envelope conduction (740 sf, U-avg 0.07, ΔT 35) | 1,813 |
| Window conduction (36 sf × 0.35 × 35) | 441 |
| Window solar gain (36 sf × 150 avg) | 5,400 |
| Roof solar (panels shade most of it, residual) | 1,000 |
| Internal gains (2 people, electronics, lighting) | 1,200 |
| Infiltration sensible | 230 |
| **Sensible cooling** | **~10,084** |
| Latent (2 people × 200 + cooking) | 600 |
| **Total cooling** | **~10,700** |

## Recommendations

### Heating — close O4

Required burner output (cabin + aux + DHW recovery, simultaneous):
≈ 4.3k + 4.2k + 6k = **~14.5 kBTU/hr** sustained, **~25 kBTU/hr** peak.

| Unit | Output (BTU/hr) | Verdict |
|---|---|---|
| Webasto Dual Top Evo 6 | ~20,500 | tight in deep cold |
| **Webasto Dual Top Evo 8** | **~27,300** | **recommended** — covers peak with margin |
| Aqua-Hot 250D | ~50,000 | over-spec, heavier, more parts |
| Timberline | ~24,000–30,000 | competitive; check service network |

**Recommended:** Webasto Dual Top Evo 8 — best fit for BTU need,
weight, and integration density.

### Cooling — close O3

Required mini-split: ~10,700 BTU/hr → 12,000 BTU class with ~15% headroom.

| Unit | BTU | Voltage | Verdict |
|---|---|---|---|
| **Mabru SCS 12000** | 12,000 | **48 V DC** | **recommended** — direct 48V, marine-grade, quiet |
| Velit 12000 | 12,000 | 24 V DC | requires 48→24 conversion, decent |
| Webasto FCF Platinum 16000 | 16,000 | 120 V AC | over-spec; runs through inverter |

**Recommended:** Mabru SCS 12000 (48 V DC native) — matches the 48V bus
without conversion losses.

## What this changes

- **ADR-0009** (drafted) closes O4 with Webasto Dual Top Evo 8.
- **ADR-0010** (drafted) closes O3 with Mabru SCS 12000.
- BOM updated: hydronic + mini-split lines specify the chosen models.
