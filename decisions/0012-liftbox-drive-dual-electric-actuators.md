# ADR-0012: Bike Lift-Box Drive — Dual Electric Linear Actuators

- **Status:** Accepted
- **Date:** 2026-05-07
- **Related:** ADR-0006; `cad/30-exterior/liftbox-kinematics.md`

## Context

Closes O5. The enclosed motorized bike box (ADR-0006) needs a lift
drive choice between dual electric linear actuators, a hydraulic
micro-pack, or a scissor lift.

## Decision

Dual electric linear actuators (Linak LA36 or Progressive Auto PA-04
class, IP67 marine-grade, 1,500 lbf, 18" stroke), running off the 24V
sub-bus, with synchronized control and mechanical travel locks at
both ends.

## Consequences

- No hydraulic fluid in the system → lower maintenance and no leak
  risk in living-space-adjacent installations.
- Force margin: 6× over design lift mass (350 lb × 25% SF).
- Power draw 5–10 A @ 24V intermittently — easily inside sub-bus
  capacity.
- Manual override = built-in crank end on selected actuator models.

## Open questions

- Final actuator vendor + model selection.
- Travel-lock pin design and engagement signaling.
- Synchronization controller (off-the-shelf or simple H-bridge w/
  position feedback).
