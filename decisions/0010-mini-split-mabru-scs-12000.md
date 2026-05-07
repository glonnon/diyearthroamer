# ADR-0010: Mini-Split — Mabru SCS 12000 (48 V DC)

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** REQUIREMENTS.md §7; `hvac/heat-load.md`

## Context

Closes O3. Cooling design load is ~10,700 BTU/hr; need a unit at 12 kBTU
class with native or near-native compatibility with the 48V bus
(ADR-0004).

## Options considered

1. **Mabru SCS 12000 (chosen)** — 12,000 BTU, **48 V DC native**,
   marine-grade, ~520 W typical / 1,100 W max draw, low noise, low
   profile condenser.
2. **Velit 12000 24V** — 12 kBTU but at 24V; would draw current from
   the sub-bus and need conversion losses.
3. **Webasto FCF Platinum 16,000** — 120 V AC; over-spec, runs through
   the inverter.
4. **Nomadic Cooling rooftop 24V** — easier install, higher profile,
   noisier; rejected for living quality.

## Decision

Mabru SCS 12000, indoor head wall- or ceiling-mounted in living area;
condenser in vented exterior locker on the curb side near the systems
bay.

## Consequences

- Direct 48V feed from house bus through dedicated breaker; no
  conversion loss.
- Refrigerant lines, drain, and control wiring routed from condenser
  locker to indoor head — captured in `cad/60-hvac/`.
- Heat-pump mode adds shoulder-season heating without burning diesel.

## Open questions

- Final condenser locker ventilation sizing.
- Indoor head exact placement vs ceiling fan-coils for hydronic heat.
