# ADR-0009: Hydronic Unit — Webasto Dual Top Evo 8

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** ADR-0007; REQUIREMENTS.md §7; `hvac/heat-load.md`

## Context

Closes O4. Heat-load analysis shows ~14.5 kBTU/hr sustained,
~25 kBTU/hr peak (cabin + radiant + towel rack + tank loop + DHW
recovery).

## Options considered

1. **Webasto Dual Top Evo 6** — 20.5 kBTU/hr; tight in deep cold + DHW.
2. **Webasto Dual Top Evo 8 (chosen)** — 27.3 kBTU/hr; ~9% margin
   over peak; combined diesel air + water heater in one box.
3. **Aqua-Hot 250D** — 50 kBTU/hr; large, heavy, well-known but
   over-spec and parts-heavy.
4. **Timberline 24/30** — 24–30 kBTU/hr; competitive but smaller
   service network in North America.

## Decision

Webasto Dual Top Evo 8.

## Consequences

- One unit handles cabin air heat and DHW + radiant + towel rack +
  tank loop via the integrated hydronic reservoir.
- Diesel fuel tap from main F550 tank (anti-siphon + protected pickup).
- Combustion intake/exhaust routing must be ≥ 12" from any opening
  vent or window per Webasto install spec.
- Reservoir + expansion tank placement: forward systems bay (per §1
  weight rule).

## Open questions

- Confirm latest Evo-8 install cutout dimensions; refresh CAD.
- Day tank vs main-tank pickup — decide after fuel system layout.
