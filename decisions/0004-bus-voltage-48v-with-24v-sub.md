# ADR-0004: House Bus Voltage — 48V Primary + 24V Sub-Bus

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** REQUIREMENTS.md §5

## Context

High solar capacity (1.0–1.3 kW), induction cooking, mini-split heat
pump, and a 5 kW inverter argue for 48V to keep conductors small and
inverter efficient. Most marine/RV accessories are 12V/24V.

## Options considered

1. **12V house only.** Simplest accessory selection but enormous
   conductor sizes for the inverter and high I²R losses.
2. **24V house only.** Compromise; halves current vs 12V; some
   accessories available.
3. **48V house + 12V sub-bus.** Smallest conductors on the high side;
   forces big 48→12V converters for all cabin loads.
4. **48V house + 24V sub-bus (chosen).** Best of both: 48V efficiency
   on the high-power side; 24V for the bulk of cabin loads (less
   current than 12V); 12V only for legacy accessories via small
   24→12V converter.

## Decision

48V primary, 24V sub-bus, 12V only for accessories that can't be
sourced at 24V.

## Consequences

- Inverter: Victron MultiPlus-II 48/5000 (or Quattro) — ADR drafted later.
- DC-DC: Victron Orion XS 48/24 (or equivalent), sized ≥ 50 A.
- Lighting/fans/pumps standardized at 24V where possible.
- Alternator path: 12V alternator + 12→48V chain (Wakespeed + boost)
  or high-output 48V alternator. Pick later.

## Open questions

- Final 48→24V converter sizing and redundancy.
- 24V vs 12V fridge model.
