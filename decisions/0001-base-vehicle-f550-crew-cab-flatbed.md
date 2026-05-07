# ADR-0001: Base Vehicle — Ford F550 4x4 Crew Cab Flatbed

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** REQUIREMENTS.md §2

## Context

Need a chassis with the GVWR, off-road capability, and serviceability to
carry a 21' composite habitat plus full systems for 2 adults / 4 seats.
Must accept 41" tires, Liquid Springs CLASS suspension, and a
cab-to-house pass-through.

## Options considered

1. **F550 crew cab flatbed (chosen).** Four DOT seats, broad cab-roof
   footprint for the cabover bed pass-through, widely available drivetrain.
2. **F550 super cab flatbed.** Lighter, shorter wheelbase; pass-through
   geometry tighter; only two rear seats.
3. **F550 single cab flatbed.** Best off-road geometry; only 2–3 seats;
   minimal interface area for cabover pass-through; rejected for travel
   capacity.
4. **Ram 5500 / Kenworth K270.** Stronger payload but worse parts/
   service availability and aftermarket; rejected.

## Decision

Ford F550 4x4 crew cab cab-and-chassis with custom flatbed.
Super cab is the only fallback if cabover/pass-through analysis fails.

## Consequences

- Wheelbase + flatbed length set by Global Trekker subframe spec
  (ADR-0003) and 21' shell (ADR-0002). Total exterior ≈ 23'.
- Four DOT seats available for travel (driver, passenger, two rear).
- Heavier and longer than super cab; departure angle preserved by tail
  taper and by mounting bike lift box high in stowed position.

## Open questions

- Final wheelbase choice (169" vs 176" vs 192") pending shell + flatbed
  CAD layout.
- Aluminum vs steel flatbed (O1).
