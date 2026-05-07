# ADR-0015: Fresh Water Tank — 2× 60 gal Split

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** REQUIREMENTS.md §8; `plumbing/tank-layout.md`,
  `plumbing/pid.md`

## Context

Fresh capacity is 100–120 gal (D11). A single 120 gal tank is hard to
fit between F550 frame rails and concentrates 1,000 lb of water in one
location.

## Decision

Two 60 gal polyethylene tanks, plumbed in parallel via a tee with
ball-valve isolation per side; gravity fill manifold + city water
inlet upstream; mounted forward of the rear axle, low and inboard of
the frame rails on subframe outriggers, one each side of centerline.

## Consequences

- Side-to-side weight balance.
- Redundancy: contamination or damage to one tank still leaves 60 gal.
- Cross-feed valve allows isolation for service.
- Slight plumbing complexity increase: +1 fill manifold, +1 pair of
  isolation valves.
- Weight model updated to two tanks at +1,800 mm forward of rear
  axle.

## Open questions

- Off-the-shelf vs custom poly tank vendor.
- Fill manifold details (single vented inlet vs dual inlets).
