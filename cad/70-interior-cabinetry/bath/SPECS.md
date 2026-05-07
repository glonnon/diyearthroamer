# Bath — Parametric Module Spec

Aft port-side dry bath. Composite-pan shower, vanity with vessel
sink, flush toilet (Dometic 320) into the 35 gal black tank.
Hydronic radiant floor (zone tap from Webasto) and hydronic towel
rack.

## Envelope

| Param | Value (mm) | Value (in) | Note |
|---|---|---|---|
| Bath module length (X) | 1,300 | 51 | aft section of port wall |
| Bath module depth (Z) | 1,000 | 39 | from port wall inboard |
| Floor-to-ceiling | 2,000 | 78.7 | usable headroom |
| Door opening | 600 × 1,930 | 24 × 76 | bi-fold or sliding pocket |
| Shower pan footprint | 760 × 760 | 30 × 30 | low-threshold molded |
| Shower wall height | 1,830 | 72 | full height; ceiling skylight optional |
| Vanity counter height | 870 | 34 | comfortable for sink use |
| Toilet centerline from wall | 380 | 15 | side clearance |

## Layout (curb-to-port across the 39" bath depth)

```
+------------------------+
|        SHOWER          |  30x30 corner shower
|   (bi-fold door)       |
+----------+-------------+
|          |             |
|  TOILET  |   VANITY    |
|          |   + SINK    |
+----------+-------------+
|       BATH DOOR        |
+------------------------+
```

## Modules

| Module | Width (mm) | Depth (mm) | Notes |
|---|---|---|---|
| Shower stall | 760 | 760 | molded composite pan + FRP walls |
| Toilet enclosure | 460 | 600 | partition + grab bar; opens to bath floor |
| Vanity cabinet | 760 | 460 | drawers + door; vessel sink atop |

## Construction

- **Pan + walls:** marine FRP molded shower pan (Specialty Recreation,
  Better Bath); bonded to subfloor with Sika 252.
- **Walls:** FRP panel sheet (white textured) over composite shell skin;
  full sealing at every seam with marine-grade silicone.
- **Vanity:** hybrid 6061 angle frame + Baltic birch ply with
  HPL/Fenix face; vessel sink (above-counter) for easier sealing.
- **Door:** bi-fold composite + magnetic catch + travel-lock detent.
- **Toilet base:** flange bolted to floor with reinforcement plate;
  black tank below.

## Hydronic radiant + towel rack

- **Radiant zone:** 6 m² PEX-Al-PEX in heat-transfer plates under
  finish floor; thermostatic mixing valve target 75–82°F floor
  surface. Zone valve at hydronic manifold (`hvac/`).
- **Towel rack:** Runtal or Myson hydronic rail, low-temperature
  glycol loop, mounted on the wall opposite the shower.
- **Vent:** dedicated bath exhaust fan (humidity-triggered) ducted
  to roof; separate from main MaxxAir circulation.

## Plumbing rough-ins

| Service | Where | Detail |
|---|---|---|
| Hot/cold in | shower | thermostatic mixer (Whale Elegance) |
| Hot/cold in | vanity | vessel-sink mixer faucet |
| Cold in | toilet | flush valve; vacuum breaker on supply |
| Drain out | shower pan | 1.5" trap to grey |
| Drain out | vanity | 1.5" trap to grey |
| Drain out | toilet | 3" to black tank below |
| Vent | toilet/black | true roof vent (no AAV) |

## Power rough-ins

| Service | Where |
|---|---|
| 120V GFCI | vanity (wet-zone GFCI required) |
| 24V dimmable LED | overhead, vanity light, toe-kick |
| 24V exhaust fan | bath fan (humidity sensor) |
| 24V towel rack | only if electric fallback (hydronic preferred) |

## Hardware

| Item | Spec |
|---|---|
| Shower valve | Whale Elegance thermostatic + pause |
| Shower wand | Oxygenics or Eco Camel marine |
| Faucet | Scandvik / Whale low-flow |
| Toilet | Dometic 320 china flush (1.0 gpf) |
| Towel rack | Runtal hydronic 18"×30" |
| Bi-fold door | composite, soft-close hinges |
| Lock | privacy latch + secondary travel lock |

## Weight estimate

| Component | Mass (lb) |
|---|---|
| Shower pan + walls + door | 90 |
| Toilet (Dometic 320) | 30 |
| Vanity cabinet + counter + sink + faucet | 75 |
| Hydronic towel rack | 20 |
| Radiant floor assembly | 25 |
| Hardware + finish + sealants | 20 |
| **Bath total** | **~260** |

(Matches the 260 lb row for "Bath module + shower + vanity + toilet
+ plumbing" in `weight/master.csv`.)

## CAD files (planned)

```
cad/70-interior-cabinetry/bath/
  SPECS.md
  build-bath.FCMacro
  bath-master.FCStd
  modules/
    shower-stall.FCStd
    vanity-cabinet.FCStd
    toilet-enclosure.FCStd
```
