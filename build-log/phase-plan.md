# Build Phase Plan

Concrete project plan derived from REQUIREMENTS.md §22, every locked
ADR, and the procurement BOM (`bom/master.csv`).

Total **~14 months** end-to-end with the spending profile in
`bom/cost-summary.md`. Phases are sequential where dependencies
require it; some sub-tasks can parallelize within a phase.

## Phase 1 — Design Freeze & Procurement Kickoff

**Duration:** months 0–2  •  **Spend:** ~$5k  •  **Predecessors:** none

| # | Task | Output | Status |
|---|---|---|---|
| 1.1 | Verify weight model is green (`scripts/weight-cg.py`) under selected GVWR | `weight/axle-report.csv` ≤ all limits | [ ] |
| 1.2 | CAD top-level vehicle assembly merges without interference | `cad/00-vehicle/full-vehicle-assembly.FCStd` | [ ] |
| 1.3 | Blender livability walkthrough produced + reviewed | `cad/00-vehicle/walkthrough.glb` | [ ] |
| 1.4 | KiCad schematics drawn for `48V_Bus`, `Solar`, `AC_Distribution` (minimum) and ERC clean | `electrical/kicad/exports/*.pdf` | [ ] |
| 1.5 | Vendor quotes received for top-10 line items (>$2k each) | `vendor-docs/quotes/` | [ ] |
| 1.6 | Final BOM costed within 10% of estimate | `bom/master.csv` updated columns | [ ] |
| 1.7 | All open ADRs closed | `decisions/` index has no Pending | [ ] |

**Acceptance:** every box checked above. Lock the Git tag
`v1.0-design-freeze`.

## Phase 2 — Chassis Prep

**Duration:** months 3–4  •  **Spend:** ~$115k  •  **Predecessors:** 1.7

| # | Task | Vendor | Status |
|---|---|---|---|
| 2.1 | Order F550 4x4 crew cab cab-and-chassis | Ford dealer | [ ] |
| 2.2 | Receive + inspect chassis; baseline weigh | local certified scale | [ ] |
| 2.3 | Install Liquid Springs CLASS suspension front + rear | Liquid Springs / installer | [ ] |
| 2.4 | Re-gear axles to 4.88 (front + rear) | local diff shop | [ ] |
| 2.5 | Install Continental MPT 81 tires + 20" wheels (5 incl. spare) | tire shop w/ DOT cert | [ ] |
| 2.6 | Install Transfer Flow aux fuel tank 50 gal | local installer | [ ] |
| 2.7 | Install hydroboost brake upgrade (if not OEM) | brake shop | [ ] |
| 2.8 | Install CBI front bumper + Warn 16500 winch | DIY or shop | [ ] |
| 2.9 | Install Aluminess rear bumper + spare carrier | DIY or shop | [ ] |
| 2.10 | Install RCI skid plates (engine, trans, tcase, aux fuel) | DIY | [ ] |
| 2.11 | Wakespeed WS500 + Nations 240A alternator install (12V house feed) | DIY w/ ABYC review | [ ] |
| 2.12 | Cab pre-wiring run for cab-to-house bus crossing | DIY | [ ] |
| 2.13 | Re-weigh chassis-prepared (no shell yet); compare to model | scale | [ ] |

**Acceptance:** truck is road-legal, registered, and the chassis
delta vs the model is within 5%.

## Phase 3 — Subframe & Flatbed Fabrication

**Duration:** month 5  •  **Spend:** ~$30k  •  **Predecessors:** 2.13

| # | Task | Vendor | Status |
|---|---|---|---|
| 3.1 | Receive Global Trekker OEM subframe; pull vendor STEP into CAD | Global Trekker | [ ] |
| 3.2 | Owner-side outriggers fab (toolboxes, steps, lift-box carrier) | local TIG shop | [ ] |
| 3.3 | Aluminum flatbed fab (6061 frame + 5052 deck) | local TIG shop | [ ] |
| 3.4 | Bolt subframe to F550 frame; verify torsion-free articulation | DIY + welder | [ ] |
| 3.5 | Mount flatbed to subframe w/ galvanic isolation per ADR-0013 | DIY | [ ] |
| 3.6 | Install side toolboxes, steps, electric retract step | DIY | [ ] |
| 3.7 | L-track install on flatbed | DIY | [ ] |

**Acceptance:** subframe + flatbed mounted, articulated, isolated.
Re-weigh with axle distribution check.

## Phase 4 — Shell Delivery, Mounting, Penetrations

**Duration:** months 6–7  •  **Spend:** ~$95k  •  **Predecessors:** 3.7

| # | Task | Status |
|---|---|---|
| 4.1 | Receive Global Trekker 21' shell w/ tail taper | [ ] |
| 4.2 | Mount shell to subframe per vendor spec | [ ] |
| 4.3 | Mark all penetrations from CAD: door, windows, vents, glands, tank ports, heater intake/exhaust | [ ] |
| 4.4 | Cut + seal each penetration (Sika 252 + 295 UV for glazing) | [ ] |
| 4.5 | Install entry door + step | [ ] |
| 4.6 | Install all dual-pane acrylic windows (incl. cabover egress) | [ ] |
| 4.7 | Install MaxxAir vents (×2) and bath fan | [ ] |
| 4.8 | Install Scanstrut roof gland + solar combiner | [ ] |
| 4.9 | Install shore inlet (SmartPlug) + city water inlet | [ ] |
| 4.10 | Install Webasto combustion intake/exhaust | [ ] |
| 4.11 | Confirm cabover front bulkhead pass-through aligns w/ cab roof | [ ] |
| 4.12 | Pressure-test shell w/ smoke for leaks | [ ] |

**Acceptance:** shell water-tight, all penetrations sealed, no
visible structural issues.

## Phase 5 — Rough-In (Electrical, Plumbing, HVAC, Tanks)

**Duration:** months 7–9  •  **Spend:** ~$40k  •  **Predecessors:** 4.12

| # | Task | Status |
|---|---|---|
| 5.1 | Run all electrical chases: 48V trunk, 24V trunk, AC, signal | [ ] |
| 5.2 | Install battery box (vented, fire-rated, drip pan) | [ ] |
| 5.3 | Mount 4× Epoch modules with shock isolation | [ ] |
| 5.4 | Install MultiPlus, MPPT, Cerbo, Orion XS in panel rack | [ ] |
| 5.5 | Install AC load center + branch breakers | [ ] |
| 5.6 | Install 2× fresh tanks A/B forward of rear axle | [ ] |
| 5.7 | Install grey + black tanks aft of rear axle | [ ] |
| 5.8 | Install heating pads + insulation on all wet tanks | [ ] |
| 5.9 | Install Webasto Dual Top Evo 8 + reservoir + expansion | [ ] |
| 5.10 | Install Mabru SCS 12000 head + condenser locker | [ ] |
| 5.11 | Run hydronic loop trunk + zone manifold | [ ] |
| 5.12 | Install radiant floor PEX-Al-PEX in heat-transfer plates | [ ] |
| 5.13 | Run PEX-A water distribution to manifold + per-fixture shutoffs | [ ] |
| 5.14 | Install pump + accumulator + filters + UV in service bay | [ ] |
| 5.15 | Install dump panel + macerator | [ ] |
| 5.16 | Run AC distribution branches per panel-schedule-ac.csv | [ ] |
| 5.17 | Install solar panels (4× 320W bonded, 2s2p strings) | [ ] |

**Acceptance:** every system has its trunk in place but is not yet
energized or filled.

## Phase 6 — Insulation Augmentation & Vapor Strategy

**Duration:** 2 weeks within month 9  •  **Spend:** ~$1k  •  **Predecessors:** 5.17

| # | Task | Status |
|---|---|---|
| 6.1 | Thermal break at every penetration | [ ] |
| 6.2 | Vapor barrier at floor pre-radiant | [ ] |
| 6.3 | Service-bay liner (insulated + accessible) | [ ] |
| 6.4 | Cabover ceiling acoustic + thermal pad | [ ] |
| 6.5 | Cab-to-house pass-through gasket + insulation | [ ] |

## Phase 7 — Cabinetry CNC + Dry-Fit

**Duration:** month 10  •  **Spend:** ~$10k materials + ~$5k CNC labor  •  **Predecessors:** 6.5

| # | Task | Status |
|---|---|---|
| 7.1 | Run all parametric macros; export STEP + DXF for each module | [ ] |
| 7.2 | Generate G-code per part for chosen CNC router | [ ] |
| 7.3 | CNC cut Baltic birch + sheet aluminum | [ ] |
| 7.4 | TIG-weld aluminum angle frames (galley, dinette, bath, wardrobe, cabover) | [ ] |
| 7.5 | Dry-fit each module in shell; mark adjustments | [ ] |
| 7.6 | Update CAD with as-built tweaks; re-export drawings | [ ] |
| 7.7 | Final sand + edge band + low-VOC finish | [ ] |

## Phase 8 — Wet Systems Commissioning

**Duration:** 3 weeks  •  **Spend:** ~$1k consumables  •  **Predecessors:** 5.17, 7.5

| # | Task | Status |
|---|---|---|
| 8.1 | Pressure-test fresh + hot water lines to 100 psi for 30 min | [ ] |
| 8.2 | Fill fresh tanks; bleed pump; verify no leaks at fixtures | [ ] |
| 8.3 | Hydronic loop fill w/ glycol; bleed; verify circulation through every zone | [ ] |
| 8.4 | Test Webasto fire-up (cold start at -10 °F if possible, or simulated) | [ ] |
| 8.5 | DHW recovery test: shower until cold, time recovery | [ ] |
| 8.6 | Radiant floor commissioning: zone-by-zone temp check | [ ] |
| 8.7 | Mini-split charge verification + dry-run cool/heat cycles | [ ] |
| 8.8 | Tank monitor calibration (SeeLevel) at 1/4, 1/2, 3/4, full | [ ] |
| 8.9 | Drain test: fill grey, dump, verify no leaks | [ ] |
| 8.10 | Toilet flush + black tank rinse | [ ] |

## Phase 9 — Electrical Commissioning

**Duration:** 3 weeks  •  **Spend:** ABYC tech included  •  **Predecessors:** 5.5, 8.10

| # | Task | Status |
|---|---|---|
| 9.1 | Energize battery bank; verify Class T + breakers + voltage at bus | [ ] |
| 9.2 | Bring up MultiPlus; configure VE.Bus to Cerbo; firmware updates | [ ] |
| 9.3 | Solar combiner energize; verify MPPT yield per panel datasheet | [ ] |
| 9.4 | Orion XS 48-24 commissioning; load test 24V sub-bus | [ ] |
| 9.5 | Alternator path: 12-48V boost test under engine on/off | [ ] |
| 9.6 | Branch-by-branch load test (every breaker fired w/ load) | [ ] |
| 9.7 | Shore power: full transfer test + EMS fault simulation | [ ] |
| 9.8 | Lift-box: dual-actuator sync; manual override; interlocks | [ ] |
| 9.9 | ABYC E-11 inspection by certified tech | [ ] |
| 9.10 | Smoke / CO / propane (n/a) detector verification | [ ] |

## Phase 10 — Finish Carpentry, Upholstery, Trim

**Duration:** month 11  •  **Spend:** ~$8k  •  **Predecessors:** 7.7, 9.10

| # | Task | Status |
|---|---|---|
| 10.1 | Bond cabinetry to shell at all hard points | [ ] |
| 10.2 | Counter installation + sealing (galley + bath) | [ ] |
| 10.3 | Backsplash + tile + sealant | [ ] |
| 10.4 | Upholstery (dinette benches, cabover headboard, cushions) | [ ] |
| 10.5 | Wall + ceiling finish (FRP at impact zones; fabric elsewhere) | [ ] |
| 10.6 | Flooring install over radiant assembly (LVP, fully sealed perimeter) | [ ] |
| 10.7 | Final lighting install + dimmer panels | [ ] |
| 10.8 | TV + audio + comms install + cable management | [ ] |
| 10.9 | Final hardware install (latches, hinges, knobs) | [ ] |
| 10.10 | Detail clean + photo walkthrough | [ ] |

## Phase 11 — Shakedown Trips

**Duration:** spread across month 12  •  **Spend:** fuel + camp fees  •  **Predecessors:** 10.10

| # | Trip | Length | Acceptance |
|---|---|---|---|
| 11.1 | Local 1-night near base | overnight | every system fired at least once; leak check |
| 11.2 | Regional 5-night | 5 nights | tank cycles, off-grid power balance, solar yield |
| 11.3 | Continental 14-night | 14 nights | full duty cycle: extreme heat, cold morning, dirt road, off-grid |

After each: punch list in `build-log/shakedown-N.md`. Resolve before
next trip.

## Phase 12 — Final Weigh, CG Verification, Registration

**Duration:** 2 weeks  •  **Spend:** ~$500  •  **Predecessors:** 11.3

| # | Task | Status |
|---|---|---|
| 12.1 | Empty + full weigh on certified 4-corner scale | [ ] |
| 12.2 | Compute per-axle and per-tire loads; compare to model | [ ] |
| 12.3 | Update `weight/master.csv` with measured values | [ ] |
| 12.4 | DOT inspection (state-specific) | [ ] |
| 12.5 | Motorhome registration + plates | [ ] |
| 12.6 | Insurance for built RV (specialty insurer) | [ ] |
| 12.7 | Tag the build `v1.0-shakedown-complete` | [ ] |
| 12.8 | Final photos + spec sheet for documentation | [ ] |

## Critical-path summary

```
Design freeze (1.7) ──> Chassis (2.13) ──> Subframe+flatbed (3.7) ──>
Shell (4.12) ──> Rough-in (5.17) ──> Insulation (6.5) ──>
Cabinetry (7.7) ──> Wet commission (8.10) ──> Electrical (9.10) ──>
Finish (10.10) ──> Shakedown (11.3) ──> Registration (12.8)
```

Critical path: ~14 months. Solar/comms/lighting can run in parallel
with finish in month 11. Cabinetry CNC runs in parallel with rough-in
where shop space allows.

## Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Subframe lead time slip | Medium | High | Order at design freeze (Phase 1.5) |
| Shell lead time slip | Medium | High | Order at design freeze; firm date in contract |
| Tire availability (MPT 81) | Medium | Med | Order spare set early; identify Michelin XZL substitute |
| Webasto Dual Top Evo 8 install complexity | Medium | Med | Hire Heatso / certified installer |
| ABYC tech availability locally | Low | Med | Book at Phase 5 start |
| Weight slip past GVWR | Medium | High | Track every release; consider GVWR uprate (Carlisle / Pickup Specialties) |
| Cabover door / pass-through misalignment | Low | High | CAD verify before shell penetration cut |
