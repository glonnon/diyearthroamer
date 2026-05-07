# Flatbed Material — Aluminum vs Steel (closes O1)

## Bed envelope

| Param | Value |
|---|---|
| Length (shell footprint + tail taper) | ~7,000 mm (~23 ft) |
| Width (over frame, inside outriggers) | ~2,134 mm (~84") |
| Top deck thickness (treadplate) | 3.2 mm (1/8") |
| Frame members | 2"×3" rectangular tube ladder + cross members |

## Mass estimate

| Component | Steel A36 | Aluminum 6061-T6 |
|---|---|---|
| Density | 490 lb/ft³ | 169 lb/ft³ |
| Deck plate (23' × 84" × 1/8") | ~330 lb | ~115 lb |
| Frame ladder (2"×3"×3/16" tube, ~80 ft total) | ~480 lb | ~165 lb |
| Cross members + brackets | ~180 lb | ~62 lb |
| Side rails / kick rails | ~120 lb | ~42 lb |
| Hardware | ~40 lb | ~30 lb |
| **Total bare flatbed** | **~1,150 lb** | **~415 lb** |
| Painted/powdercoated finish | +40 lb | — (anodize) |
| **Final** | **~1,190 lb** | **~415 lb** |

**Aluminum saves ~775 lb** vs steel for the same envelope. That's ~4%
of GVWR — significant on a build that already runs heavy.

## Cost (rough, 2026 prices)

| Stack | Material | Fab labor | Finish | Total |
|---|---|---|---|---|
| Steel | $900 | $2,500 | $400 | **~$3,800** |
| Aluminum | $2,800 | $3,200 | $400 (anodize) | **~$6,400** |

Delta: aluminum ~$2,600 more. At $3/lb to remove a pound of curb
weight on the rest of the build (a typical lightweighting cost in
overland circles), the 775 lb of weight saved is worth ~$2,300 in
equivalent value, and aluminum has corrosion benefits steel can't
match without ongoing maintenance.

## Other factors

| Factor | Steel | Aluminum |
|---|---|---|
| Salt corrosion (winter, coast) | needs paint touch-up + drainage | benign — surface oxide |
| Weldability for repairs | easy, every shop | TIG required, fewer shops |
| Stiffness per pound | lower | higher (Al is stiffer for equal mass) |
| Galvanic corrosion w/ steel chassis | n/a | mitigate with isolation washers + Tef-Gel |
| Vibration damping | better | poorer (rings) — add dynamat or rubber pads |
| Repaint life | 5–8 yr | n/a |

## Vendor options

- **Highway Products** — aluminum truck flatbeds, custom layouts.
- **Eby** — popular in commercial; aluminum + steel options.
- **Bradford Built / Pickup Specialties** — steel; popular but heavier.
- **Aluma** — aluminum trailers + flatbeds.
- **Custom fab** — local welding shop with TIG capability; allows exact
  match to subframe mount pattern.

## Decision

**Aluminum (6061-T6 frame + 5052-H32 deck plate).** The 775 lb
savings is decisive on a build that's already weight-bound. Galvanic
isolation handled at every steel-to-aluminum interface (subframe,
brackets, hitch).

Captured in **ADR-0013**.

## Mitigations

- Galvanic isolation: nylon shoulder washers + Tef-Gel at every steel
  fastener landing into aluminum.
- Cathodic-friendly fastener choice: 18-8 stainless with anti-seize.
- Drain holes at every closed cavity (deck-to-frame).
- Powder coat or anodize for visual + extra surface protection.
- Inspection schedule: galvanic interfaces checked annually.
