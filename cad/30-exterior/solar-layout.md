# Roof Solar — Layout & Tilt (closes O6)

## Roof envelope

| Param | Value |
|---|---|
| Shell exterior length | 21' habitat + 2' tail = 23' (7,000 mm) |
| Shell exterior width | 96" (2,438 mm) |
| Walking lane reservation (centerline) | 18" (457 mm) |
| Front clearance for cabover transition | ~24" (610 mm) |
| Rear clearance for tail taper | ~24" (610 mm) |

Penetrations / obstructions on the roof:

- **MaxxAir Deluxe ×2:** 14"×14" base + 4" clearance ring → ~22"×22"
  reserved per fan. Place one over galley, one over bed.
- **Bath vent fan:** ~10"×10" reserved.
- **Starlink Mini / Standard:** ~24"×16" reserved (Mini) or 24"×24"
  (Standard) — pick Mini.
- **Cellular antenna(s):** 4"×4" reserved each.
- **Solar combiner box:** ~8"×6", placed near the roof gland.
- **Roof gland (single):** ~3" diameter Scanstrut for all PV wiring.

## Panel options

| Panel | Watts | Dim (in) | Area (sf) | W/sf |
|---|---|---|---|---|
| Renogy 200W mono rigid | 200 | 65×27 | 12.2 | 16.4 |
| HQST 320W mono | 320 | 65×39 | 17.6 | 18.2 |
| **Sunpower / Maxeon 410W** | **410** | **67×45** | **20.9** | **19.6** |
| LG NeON 400W (legacy) | 400 | 67×40 | 18.6 | 21.5 |

## Layout candidates

### Layout A — 4× 200W in 2×2 (800 W)

Compact, leaves the most roof for vents/Starlink. Below target.

### Layout B — 4× 320W in 2×2 (1,280 W) ✓

```
+---------------+---------------+
|               |               |
|   320 W       |   320 W       |   ← front pair (over cabover/galley)
|               |               |
+---------------+---------------+
|  walking lane (18", combiner box, gland)  |
+---------------+---------------+
|               |               |
|   320 W       |   320 W       |   ← rear pair (over bath/bed)
|               |               |
+---------------+---------------+
```

Each panel ~65"×39" → array footprint ~134" × 84" (with center lane).
Fits within 21' (252") roof leaving:

- Front: 18" reserved for cabover front edge + bath vent
- Rear: 252" − 134" − 18" − ~10" gland zone = ~90" remaining for
  MaxxAir, Starlink, antennas at the rear.

Side margins: shell 96" exterior − 84" array − ~12" fillet at edges.
Edges respected; panels recessed ~6" inboard each side for hand-rails.

**Total: 1,280 W. Hits 1.0–1.3 kW target.**

### Layout C — 3× 410W in row (1,230 W)

3 panels along centerline lengthwise. Loses walkability and a fan
location. Not preferred.

## Decision: **Layout B — 4× 320W flat-mounted, no tilt.**

### Why no tilt

- **Transit risk:** tilt brackets must be folded/locked for travel;
  one missed step → wind catches a panel at 65 mph.
- **Wind load:** tilted panels add side load to roof bond; expedition
  use means we leave the truck unattended for hours; wind gusts can
  exceed 50 mph in the desert/mountain.
- **Yield benefit is small in practice:** ~30% winter peak gain only
  applies when the truck is stationary at a chosen latitude/azimuth.
  Most expedition users are mobile and rarely sit somewhere long
  enough to bother tilting.
- **Weight + complexity:** brackets + actuators add ~40–60 lb +
  another failure mode.
- **Mitigation:** a portable 200W panel (folding suitcase or rigid)
  with Anderson SB50 input port at the side of the vehicle gets you
  the same shoulder-season boost without the always-on penalty.

### Mounting

- **No roof penetrations.** Bonded standoffs (3M VHB tape primed +
  Sika 252 fillet) per Total Composites / Global Trekker recommended
  practice for FRP composite roofs.
- Aluminum standoffs raise panels ~1" off roof for airflow + thermal
  derating.
- Panels grounded to a single bonding lug at the combiner.

### Wiring

- Two strings of two panels in series (2s2p) → ~75 V Voc per string,
  ~18 A Isc per string, total Voc ~75 V, Isc ~36 A.
- Combiner: each string fused 15A MC4 inline; both strings paralleled
  to a single 10 AWG run through one Scanstrut roof gland.
- Single Victron MPPT 250/100 sized for headroom (or 150/70 if pairing
  to lower Voc strings — final pick after exact panel datasheet).

### Future capacity

If 1,280 W proves insufficient, add a portable Anderson SB50 panel
input at the curb side (already in REQUIREMENTS.md §6) for an extra
200 W when needed.

Captured in **ADR-0014**.
