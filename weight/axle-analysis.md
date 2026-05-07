# Axle Load Analysis — First Run

Source: `weight/master.csv` (50 items, corrected stations).
Tool: `scripts/weight-cg.py`.
Wheelbase: 176" (4,470 mm).

## Summary table

| Scenario | Total (lb) | CG fwd of rear axle (in) | Front (lb) | Rear (lb) | GVWR reserve |
|---|---|---|---|---|---|
| DRY (empty tanks) | 17,012 | 64.3 | 6,213 | 10,799 | 12.8% |
| CRUISE (half tanks + 2 ppl) | 17,926 | 63.3 | 6,450 | 11,476 | 8.1% |
| **WET (full tanks + gear + 2 ppl)** | **18,800** | **62.4** | **6,668** | **12,132** | **3.6%** |

F550 limits used: front GAWR 7,000 lb, rear GAWR 13,500 lb, GVWR
19,500 lb, tire load 4,400 lb each.

## Findings

### 1. Tire selection — Continental MPT 81 military-spec resolves it

Initial run flagged a tire-load issue with civilian 41" tires at
~4,400 lb each. **Continental MPT 81 (365/85R20 NATO troop-carrier
tire) is rated 6,779 lb each**, which makes single-rear-wheel a fully
viable configuration.

| Configuration | Front pair | Rear pair | WET rear (12,132 lb) | Verdict |
|---|---|---|---|---|
| Civilian 41" SRW (×2 @ 4,400 lb) | 8,800 | 8,800 | 138% of cap | **fails** |
| Civilian 41" DRW (×4 @ 4,400 lb) | 8,800 | 17,600 | 69% of cap | passes |
| **Continental MPT 81 SRW (×2 @ 6,779 lb)** | **13,558** | **13,558** | **89% of cap** | **passes with 11% margin** |

**Decision (locked): Continental MPT 81** (or equivalent military-spec
NATO tire — Michelin XZL 395/85R20 is a direct substitute).

Captured in **ADR-0016**.

### 2. GVWR reserve thin in WET case (3.6% vs 20% target)

REQUIREMENTS.md §1 sets a 20% payload reserve target (≥ 3,900 lb
under GVWR). WET case currently shows only 700 lb reserve. Three
levers:

| Lever | Saves (lb) | Notes |
|---|---|---|
| Switch fresh capacity from 120 → 80 gal (full case only) | 333 | hurts boondock duration |
| Lighter hydronic (Truma Combi vs Webasto Dual Top Evo 8) | 30 | gives up radiant + towel rack |
| Aluminum cabinet skeleton vs steel | already in plan | n/a |
| **F550 GVWR upgrade — Carlisle / Pickup Specialties to 22,000+ lb** | n/a; raises ceiling | well-known F550 mod via reinforced suspension + brake upgrade + axle re-rate |
| Trim build mass (shave 50 lb across 30 components) | 1,500 | tedious; do alongside CAD |
| Drop spare tire to under-bed (kept) and skip swing-out | 50 | minor |

**Recommended path:** combine (a) F550 GVWR upgrade to 22,000 lb
(documented modification, retains warranty for many shops) and (b)
ongoing weight discipline as CAD locks in. Track in `weight/master.csv`
on every CAD release.

Captured as a **mitigation**; will become **ADR-0017** when GVWR
upgrade vendor is selected.

### 3. Front axle at 95% GAWR in WET case

6,668 / 7,000 = 95%. Also tight, but acceptable. Levers if it goes
over:

- Move spare tire from front-mount (if added) → rear under-bed.
- Move tools / recovery storage forward of rear axle, not at front
  bumper.
- Shorter front winch bumper to reduce moment arm.

Watch this in subsequent runs as CAD adds detail.

### 4. The forward-bias rule is working

CG sits 62–64" forward of the rear axle. With WB=176", that's
**36% of mass on the rear axle in WET** (12,132 / 33,200... wait, 
12,132 / 18,800 = 64.5% rear, 35.5% front). For a long flatbed
expedition truck the rule of thumb is 35–40% on the front axle, so
this is correct.

## Open questions

- Confirm F550 OEM GVWR for the chosen MY (some 2024+ F550 SuperDuty
  4x4 crew cab cab-and-chassis ship with 19,500 GVWR; some at 18,000;
  pull from Ford body builder's guide).
- Validate vendor GVWR uprate path (Carlisle, Pickup Specialties, or
  re-spec at chassis order).
- Decide tire model (dual rear) — pin specific load index.

## Reproduce

```sh
# Single-rear case (current default)
python3 scripts/weight-cg.py

# Dual rear (recommended)
python3 scripts/weight-cg.py --dual-rear

# Custom limits (e.g., GVWR uprate to 22,000 lb)
python3 scripts/weight-cg.py --dual-rear --gvwr 22000
```

Output CSVs:

```sh
python3 scripts/weight-cg.py --dual-rear --csv weight/axle-report.csv
```
