# ADR-0003: Subframe — Buy Global Trekker OEM

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** REQUIREMENTS.md §3

## Context

The shell must be decoupled from chassis flex via a torsion-free or
three-point subframe. Custom design is high-stakes engineering work
(structural, fatigue, fastener pattern bonded to composite panels).

## Options considered

1. **Buy Global Trekker OEM subframe (chosen).** Engineered to the
   shell vendor's panel inserts and fastener pattern; warranty;
   shortens schedule.
2. **Build custom three-point subframe.** Maximum flexibility, lower
   parts cost, but high engineering risk and long iteration loop.
3. **Adapt third-party (Multidrive / GTV).** Possible but adds
   integration risk vs the matched OEM option.

## Decision

Purchase the Global Trekker OEM subframe matched to the 21' shell on
F550 crew cab flatbed.

## Consequences

- Flatbed length and mount-point pattern dictated by the OEM subframe;
  pull dimensions before locking flatbed CAD.
- Owner-side outriggers/brackets still required for side toolboxes,
  steps, and lift-box carrier.
- Bonded/bolted shell-to-subframe interface per vendor spec.

## Open questions

- Vendor lead time and shipping crate dimensions.
- Compatibility with chosen wheelbase and rear bumper / lift-box.
