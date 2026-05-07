# ADR-0016: Tires — Continental MPT 81 (Military-Spec)

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** REQUIREMENTS.md §2; `weight/axle-analysis.md`

## Context

Weight model run shows rear axle carries 10,800–12,100 lb across DRY,
CRUISE, and WET scenarios. Civilian 41" tires top out around 4,400–
4,800 lb each — single-rear-wheel pairs (8,800 lb capacity) fail the
load constraint by 30%+ in every scenario.

Two paths forward: (a) dual rear wheels with civilian 41" tires, or
(b) single-rear-wheel with a military-spec high-load tire.

## Options considered

1. **Civilian 41" tire, single-rear-wheel (×2 @ 4,400 lb).** Best
   off-road clearance and ground feel; **fails** rear load by 30%+.
2. **Civilian 41" tire, dual rear wheels (×4 @ 4,400 lb).** Passes
   loads (17,600 lb rear capacity); reduces flotation in sand and
   adds two spare tires; tighter fender clearances.
3. **Continental MPT 81 military-spec, single-rear-wheel (chosen).**
   Rated 6,779 lb each; SRW pair = 13,558 lb capacity; clears WET
   case (12,132 lb rear) with ~12% margin. Available in 365/85R20
   (~41" OD).
4. **Michelin XZL 395/85R20** (alternate). Similar military-spec
   tire, ~9,200 lb load, more common in some regions.
5. **Goodyear MV/T MPT** (alternate). Similar class.

## Decision

Continental MPT 81 (365/85R20 NATO) on 20" forged single-rear wheels.
Michelin XZL 395/85R20 acceptable as a direct substitute if MPT 81
is unobtainable.

## Consequences

- Single-rear-wheel retained → better off-road clearance and reduced
  weight vs DRW.
- Tire load: 13,558 lb each axle → 12% margin in WET case (rear).
  Front carries only 6,668 lb, well under tire and GAWR limits.
- Tires are NATO procurement; sourcing may require a specialty
  vendor (e.g., NWAS, military surplus, Continental fleet).
- Tread is more aggressive than civilian; expect higher road noise
  and slightly lower mpg.
- Spare tire is one more 41" military tire; expensive.
- Wheels: 20" steel or forged aluminum, hub-centric, correct offset
  for fender clearance.

## Open questions

- Final wheel selection (Hutchinson runflats vs simpler steel vs
  forged aluminum).
- Source confirmation for new MPT 81 in North America vs takeoffs.
- Spare tire location (rear swing-out kept, weight already in
  `weight/master.csv`).
