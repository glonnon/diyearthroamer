# Cost Summary

Computed from `bom/master.csv` (158 line items). Costs are 2026
estimates pending real vendor quotes.

## Top-line totals

| Subsystem | Items | Cost (USD) |
|---|---|---|
| chassis | 11 | $109,650 |
| shell | 6 | $101,450 |
| exterior | 8 | $15,850 |
| electrical (incl. solar) | 30 | $26,608 |
| hvac | 13 | $16,485 |
| plumbing | 21 | $5,656 |
| kitchen | 7 | $5,430 |
| bathroom | 5 | $2,030 |
| bed | 4 | $2,730 |
| interior (cabinetry, finish) | 16 | $11,140 |
| bike-box | 7 | $6,200 |
| comms | 8 | $4,400 |
| lighting | 7 | $5,420 |
| fasteners + sealants | 6 | $978 |
| labor (subframe, shell, ABYC, plumbing) | 4 | $30,500 |
| **TOTAL (materials + labor)** | **158** | **~$344,500** |

## Sanity check vs comparable production builds

| Build | Approx price | Notes |
|---|---|---|
| Earthroamer LTi | $750k–950k | smaller, similar systems |
| Storyteller HILT | $300k–400k | direct comparison |
| EarthCruiser EXP | $400k+ | smaller |
| **DIY this build** | **~$345k materials** | + your time + tooling overhead |

## Re-compute

```sh
python3 - <<'PY'
import csv
from collections import defaultdict
total = defaultdict(float)
n = defaultdict(int)
with open('bom/master.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        if row.get('id', '').startswith('note'):
            continue
        sub = row.get('subsystem', '')
        try:
            ext = float(row.get('extended_cost_usd') or 0)
        except ValueError:
            continue
        total[sub] += ext
        n[sub] += 1
for sub in sorted(total):
    print(f"{sub:20} {n[sub]:3}  ${total[sub]:12,.0f}")
print("-" * 40)
print(f"{'TOTAL':20} {sum(n.values()):3}  ${sum(total.values()):12,.0f}")
PY
```

## Levers if cost is too high

| Lever | Saves (USD) | Tradeoff |
|---|---|---|
| Used / takeoff F550 chassis | -$30k–40k | finding a clean one |
| Smaller shell (19') | -$15k | less interior volume; rejected (ADR-0002) |
| 2× Epoch instead of 4× (10 kWh vs 20) | -$7k | shorter no-sun reserve |
| Drop backup diesel air heater | -$1.1k | less redundancy |
| Skip Starlink + comms gear | -$2.5k + sub | mobile internet hurts |
| DIY bike-box vs custom fab | -$1.5k | requires welding skill |
| Drop second hydronic fan-coil | -$400 | one less zone |
| Drop secondary roof bar lighting | -$1.1k | less night driving |

## Fund-flow plan (suggested phasing)

| Phase | Spend (USD) | When |
|---|---|---|
| Design freeze + first tooling | $5,000 | months 0–2 |
| Chassis + suspension + tires | $115,000 | month 3 |
| Shell + subframe + flatbed | $115,000 | month 6 |
| Electrical + solar + HVAC | $50,000 | month 8 |
| Plumbing + kitchen + bath + cabinetry | $30,000 | month 10 |
| Lighting + comms + finish + fasteners | $14,000 | month 12 |
| Labor reserve | $30,500 | rolling |
| Contingency 10% | $34,500 | rolling |
| **Total** | **~$394,000** | over ~14 months |
