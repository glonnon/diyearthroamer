# ADR-0007: Heating — Integrated Diesel Hydronic

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** REQUIREMENTS.md §7, §11; ADR-0010 (heated floors), ADR-0011 (towel rack)

## Context

Need cabin heat, domestic hot water, heated floor (living/galley/bath),
heated towel rack, and tank/wet-bay freeze protection. All-electric
heat at 48V is possible but burns battery in winter. No propane.

## Options considered

1. **Standalone diesel air heater + separate DHW.** Two boxes, two
   fuel taps, no easy radiant; cheaper per BTU but operationally
   fragmented.
2. **Truma Combi D6.** Compact air + DHW; no native radiant; weaker
   in deep cold.
3. **Integrated diesel hydronic (Webasto Dual Top Evo / Aqua-Hot 250D
   / Timberline) (chosen).** One box does cabin air (via fan-coils),
   DHW, radiant floor zones, towel rack, and tank loop. Best for
   four-season use.
4. **All-electric heat pump + tank water heater.** Loses to diesel on
   battery duty cycle in winter.

## Decision

Integrated diesel hydronic system (specific unit selection deferred —
O4) plus standalone diesel air heater retained as redundant cabin
backup.

## Consequences

- Hydronic loop adds plumbing complexity and ~30–60 lb of fluid +
  hardware vs air-only.
- Single fuel tap from main diesel tank (with anti-siphon and protected
  pickup) plus optional small day tank.
- Mini-split heat pump (§7) handles shoulder-season cooling and
  supplemental heat — both systems coexist.

## Open questions

- O4: Webasto Dual Top Evo 8 vs Aqua-Hot 250D vs Timberline.
- Reservoir / expansion-tank location and access.
- Combustion air intake / exhaust routing (must not be near vents).
