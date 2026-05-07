# ADR-0014: Solar — 4× 320W Flat 2×2 Array, No Tilt

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** REQUIREMENTS.md §6; `cad/30-exterior/solar-layout.md`

## Context

Closes O6. Need 1.0–1.3 kW on a 21' roof while preserving walkable
center lane and clearances for two MaxxAir fans, bath vent, Starlink,
antennas, and a combiner gland.

## Decision

Four 320W mono rigid panels arranged 2×2 (front pair over
cabover/galley, rear pair over bath/bed) with an 18" walking lane on
the centerline. Bonded mounts (3M VHB + Sika 252 fillet) on standoffs;
no roof penetrations. Two strings of two panels in series, paralleled
at a combiner with 15A MC4 inline fuses, single Scanstrut gland to a
Victron MPPT 250/100. **No tilt.**

## Consequences

- 1,280 W rated → ~900–1,000 Wh/day in summer mid-latitudes, well
  above the load study floor.
- No transit risk from tilt brackets.
- ~30 lb saved vs a tilt configuration.
- Future capacity expansion via Anderson SB50 portable panel input
  on the curb side (already in REQUIREMENTS.md).

## Open questions

- Final panel make/model — pin to a specific 320W datasheet to fix
  Voc/Isc and recompute MPPT sizing.
- Combiner box exact location vs roof rack walking lane.
