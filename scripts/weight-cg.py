#!/usr/bin/env python3
"""
weight-cg.py — Compute total mass, CG, and per-axle loads for the
build, and flag GAWR / GVWR / tire-load violations.

Reads:  weight/master.csv
Writes: stdout report; optional --csv weight/axle-report.csv

Coordinate convention (cad/README.md):
  Origin = center of rear axle, at ground.
  +X forward, +Y up, +Z to driver side (LH).
  station_x_in is column 5 of master.csv (in inches, +X forward).
  Wheelbase is the F550 baseline from cad/00-vehicle/SPECS.md (176").

F550 4x4 SRW with 41" tires limits (typical):
  Front GAWR:  7,000 lb (Dana 60 / Sterling)
  Rear  GAWR: 13,500 lb (Sterling 10.5 / OEM)
  GVWR:       19,500 lb
  Tire load:  ~4,400 lb per 41" LT tire (verify with selected tire)
              -> Front pair max 8,800 lb, single-rear-wheel rear pair
                 8,800 lb. With 41" super-single conversion the rear
                 may run two tires per side, doubling to ~17,600 lb.

Three scenarios reported:
  DRY    — empty tanks; no consumables; truck + build only
  CRUISE — half-fluid; 2 occupants; cooking/cleaning consumables
  WET    — all tanks full; all gear; bikes + occupants

Usage:
    python3 scripts/weight-cg.py
    python3 scripts/weight-cg.py --csv weight/axle-report.csv
    python3 scripts/weight-cg.py --wheelbase 176 --front-gawr 7000 \
                                 --rear-gawr 13500 --gvwr 19500 \
                                 --tire-load 4400
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CSV_PATH = REPO / "weight" / "master.csv"


@dataclass
class Item:
    subsystem: str
    name: str
    mass_lb: float
    station_x_in: float

    @property
    def is_full_fluid(self) -> bool:
        s = self.name.lower()
        return " full" in s

    @property
    def is_empty_fluid(self) -> bool:
        s = self.name.lower()
        return "tank" in s and " empty" in s


@dataclass
class Scenario:
    name: str
    descr: str
    include_full: bool       # full-fluid rows
    extra_consumables: float = 0.0  # extra lb at galley station for food/etc.


SCENARIOS = [
    Scenario("DRY",    "empty tanks, no consumables", include_full=False,
             extra_consumables=0.0),
    Scenario("CRUISE", "half tanks, 2 occupants, food",
             include_full=False,  # we'll halve full rows below
             extra_consumables=80.0),
    Scenario("WET",    "all tanks full + gear + 2 occupants",
             include_full=True,
             extra_consumables=120.0),
]


def load_items(path: Path) -> list[Item]:
    items: list[Item] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        # header: id,subsystem,item,mass_lb,station_x_in,note
        for row in reader:
            if len(row) < 5:
                continue
            try:
                mass = float(row[3]) if row[3] else None
                station = float(row[4]) if row[4] else None
            except ValueError:
                continue
            if mass is None or station is None:
                continue
            items.append(Item(
                subsystem=row[1].strip(),
                name=row[2].strip(),
                mass_lb=mass,
                station_x_in=station,
            ))
    return items


@dataclass
class AxleReport:
    scenario: str
    total_lb: float
    cg_x_in: float          # forward of rear axle
    front_axle_lb: float
    rear_axle_lb: float
    items: list[tuple[Item, float]] = field(default_factory=list)


def compute(scenario: Scenario, items: list[Item], wheelbase_in: float) -> AxleReport:
    total = 0.0
    moment = 0.0
    rows: list[tuple[Item, float]] = []
    for it in items:
        m = it.mass_lb
        if it.is_full_fluid:
            if scenario.name == "WET":
                pass  # full
            elif scenario.name == "CRUISE":
                m *= 0.5
            else:
                m = 0.0
        # Tank-empty (poly shell) always counts.
        if m <= 0:
            continue
        rows.append((it, m))
        total += m
        moment += m * it.station_x_in

    # Add consumables / occupants approximately at galley (X ≈ 84 in)
    if scenario.extra_consumables > 0:
        total += scenario.extra_consumables
        moment += scenario.extra_consumables * 84.0
        rows.append((Item("consumables", "food/water/clothing",
                          scenario.extra_consumables, 84.0),
                     scenario.extra_consumables))

    cg = (moment / total) if total else 0.0
    # Sum of moments about rear axle: F_front * WB = total * cg
    front = (total * cg) / wheelbase_in
    rear = total - front
    return AxleReport(scenario.name, total, cg, front, rear, rows)


def fmt(n: float, w: int = 9) -> str:
    return f"{n:>{w},.0f}"


def report(scenario: Scenario, rep: AxleReport,
           front_gawr: float, rear_gawr: float, gvwr: float,
           tire_load: float, dual_rear: bool) -> str:
    out: list[str] = []
    out.append(f"--- {rep.scenario}  ({scenario.descr}) ---")
    out.append(f"  Total mass  : {fmt(rep.total_lb)} lb")
    out.append(f"  CG forward of rear axle: {rep.cg_x_in:>7.1f} in")
    out.append(f"  Front axle  : {fmt(rep.front_axle_lb)} lb"
               f"   (GAWR {fmt(front_gawr)} lb)")
    out.append(f"  Rear axle   : {fmt(rep.rear_axle_lb)} lb"
               f"   (GAWR {fmt(rear_gawr)} lb)")
    out.append(f"  GVWR check  : {fmt(rep.total_lb)} / {fmt(gvwr)} lb")

    front_pair_cap = 2 * tire_load
    rear_tire_count = 4 if dual_rear else 2
    rear_pair_cap = rear_tire_count * tire_load
    out.append(f"  Tire load   : front {fmt(rep.front_axle_lb)} / "
               f"{fmt(front_pair_cap)} lb (2 tires)")
    out.append(f"                rear  {fmt(rep.rear_axle_lb)} / "
               f"{fmt(rear_pair_cap)} lb "
               f"({rear_tire_count} tires)")

    flags = []
    if rep.front_axle_lb > front_gawr: flags.append("FRONT GAWR EXCEEDED")
    if rep.rear_axle_lb  > rear_gawr:  flags.append("REAR GAWR EXCEEDED")
    if rep.total_lb      > gvwr:       flags.append("GVWR EXCEEDED")
    if rep.front_axle_lb > front_pair_cap: flags.append("FRONT TIRE LOAD EXCEEDED")
    if rep.rear_axle_lb  > rear_pair_cap:  flags.append("REAR TIRE LOAD EXCEEDED")
    if flags:
        out.append("  !!  FLAGS: " + "; ".join(flags))
    else:
        out.append("  OK: within all limits")

    # Reserve to GVWR
    reserve = gvwr - rep.total_lb
    out.append(f"  Reserve to GVWR: {fmt(reserve)} lb "
               f"({reserve / gvwr * 100:>4.1f}%)")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wheelbase", type=float, default=176.0)
    ap.add_argument("--front-gawr", type=float, default=7000.0)
    ap.add_argument("--rear-gawr", type=float, default=13500.0)
    ap.add_argument("--gvwr", type=float, default=19500.0)
    ap.add_argument("--tire-load", type=float, default=4400.0)
    ap.add_argument("--dual-rear", action="store_true",
                    help="Set if running dual rear wheels (super-single off)")
    ap.add_argument("--csv", type=Path, default=None)
    args = ap.parse_args()

    items = load_items(CSV_PATH)
    if not items:
        print(f"No usable rows in {CSV_PATH}", file=sys.stderr)
        return 1

    print(f"Loaded {len(items)} items from "
          f"{CSV_PATH.relative_to(REPO)}\n")
    print(f"Wheelbase: {args.wheelbase:.1f} in")
    print(f"Limits   : front GAWR {args.front_gawr:.0f}, rear GAWR "
          f"{args.rear_gawr:.0f}, GVWR {args.gvwr:.0f}, "
          f"tire {args.tire_load:.0f} lb each, "
          f"{'dual' if args.dual_rear else 'single'}-rear\n")

    reports: list[AxleReport] = []
    for s in SCENARIOS:
        rep = compute(s, items, args.wheelbase)
        reports.append(rep)
        print(report(s, rep, args.front_gawr, args.rear_gawr,
                     args.gvwr, args.tire_load, args.dual_rear))
        print()

    if args.csv:
        out_csv = args.csv.resolve() if args.csv.is_absolute() else (Path.cwd() / args.csv).resolve()
        with out_csv.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["scenario", "total_lb", "cg_x_in",
                        "front_axle_lb", "rear_axle_lb",
                        "front_gawr_lb", "rear_gawr_lb", "gvwr_lb"])
            for r in reports:
                w.writerow([r.scenario, f"{r.total_lb:.0f}",
                            f"{r.cg_x_in:.1f}",
                            f"{r.front_axle_lb:.0f}",
                            f"{r.rear_axle_lb:.0f}",
                            int(args.front_gawr), int(args.rear_gawr),
                            int(args.gvwr)])
        try:
            print(f"Wrote {out_csv.relative_to(REPO)}")
        except ValueError:
            print(f"Wrote {out_csv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
