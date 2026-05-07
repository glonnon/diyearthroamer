#!/usr/bin/env python3
"""
voltage-drop.py — quick ABYC E-11 wire size sanity check.

Usage:
    python3 voltage-drop.py 48 105 4 --target-drop 0.03
    python3 voltage-drop.py 24 50 8

Prints required AWG for the given voltage, current, and one-way length
(ft). Defaults to 3% drop (critical loads). Pass --target-drop 0.10 for
non-critical loads.

Resistance values: tinned copper, ABYC table at 75 °C ambient.
"""

import argparse
import math
import sys

# AWG -> ohms per 1000 ft (tinned copper, ABYC at 75 C)
OHMS_PER_KFT = {
    "18": 6.385,
    "16": 4.016,
    "14": 2.525,
    "12": 1.588,
    "10": 0.999,
    "8":  0.628,
    "6":  0.395,
    "4":  0.249,
    "2":  0.156,
    "1":  0.124,
    "1/0": 0.0983,
    "2/0": 0.0779,
    "3/0": 0.0618,
    "4/0": 0.049,
}

ORDER = ["18", "16", "14", "12", "10", "8", "6", "4", "2", "1",
         "1/0", "2/0", "3/0", "4/0"]


def required_awg(voltage, amps, length_ft, target_drop=0.03):
    max_v_drop = voltage * target_drop
    # round-trip length
    rt_ft = 2.0 * length_ft
    for awg in ORDER:
        ohms = OHMS_PER_KFT[awg] / 1000.0
        v = amps * ohms * rt_ft
        if v <= max_v_drop:
            return awg, v
    return None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("voltage", type=float, help="System voltage (V)")
    ap.add_argument("amps", type=float, help="Load current (A)")
    ap.add_argument("length_ft", type=float, help="One-way length (ft)")
    ap.add_argument("--target-drop", type=float, default=0.03,
                    help="Allowable drop fraction (default 0.03 = 3%)")
    args = ap.parse_args()

    awg, v = required_awg(args.voltage, args.amps, args.length_ft,
                          args.target_drop)
    if awg is None:
        print("No standard AWG meets the drop target. Use parallel runs "
              "or higher voltage.", file=sys.stderr)
        sys.exit(1)
    print(f"AWG: {awg}    drop: {v:.3f} V "
          f"({v / args.voltage * 100:.2f}%)")


if __name__ == "__main__":
    main()
