# ADR-0013: Flatbed Material — Aluminum (6061-T6 + 5052-H32)

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** ADR-0001, ADR-0003; `cad/10-subframe/flatbed-material.md`

## Context

Closes O1. Flatbed envelope is ~23' × 84". Mass model shows a
~775 lb delta between steel and aluminum constructions for the same
envelope, with corrosion and maintenance benefits in favor of
aluminum.

## Decision

Aluminum flatbed: 6061-T6 frame ladder (2"×3"×3/16" tube), 5052-H32
deck plate (1/8" treadplate), TIG-welded by a competent fab shop.
Anodize finish.

## Consequences

- ~775 lb saved vs steel — meaningful contribution to staying under
  GVWR with a 20% reserve.
- Galvanic-isolation discipline at every steel chassis / steel
  fastener interface (nylon shoulder washers + Tef-Gel).
- Aluminum welding skill required for any repairs; budget for an
  on-call fab shop relationship.
- Deck stiffness adequate; ride harshness mitigated by rubber pads
  between subframe and bed where the OEM Global Trekker subframe
  doesn't already isolate.
- Cost ~$2,600 higher than steel; offset by weight savings value.

## Open questions

- Off-the-shelf vendor (Highway Products / Eby / Aluma) vs custom
  fab — pick after subframe mount pattern is in CAD from Global
  Trekker.
