#!/usr/bin/env python3
# whs-professional/scripts/frequency_rates.py
"""
WHS frequency rate calculator — deterministic arithmetic for board-grade outputs.

Computes TRIFR, LTIFR, MTIFR, RWIFR, AIFR and severity rate, point-in-time or
as a rolling 12-month series anchored to the last closed period. Use this
instead of in-context arithmetic: consistent rounding, no transposition errors.

Conventions
-----------
- Default basis: per 1,000,000 hours worked (AU convention).
  Use --basis 200000 for the US OSHA convention if required.
- Recordable set for TRIFR: Fatalities + LTI + RWI + MTI (consistent with
  references/analytics.md and glossary.md — do not silently vary this set).
- LTIFR numerator: LTIs only (per glossary.md and analytics.md; fatalities are
  counted in TRIFR and AIFR, not LTIFR).
- AIFR numerator: recordables + FAIs (broadest measure, per analytics.md).
- Rolling 12-month: numerator = sum of events in the 12 closed months ending
  at the anchor period; denominator = sum of hours over the same 12 months.

Usage
-----
Point-in-time:
    python3 frequency_rates.py --hours 4823500 \
        --fatalities 0 --lti 6 --rwi 9 --mti 22 --fai 31

Rolling 12-month series from a CSV (columns: period,hours,fatalities,lti,rwi,mti
and optionally fai, where period is YYYY-MM; rows must be closed months):
    python3 frequency_rates.py --csv monthly.csv --rolling

Severity rate (days lost per million hours):
    python3 frequency_rates.py --hours 4823500 --days-lost 312 --severity
"""

import argparse
import csv
import json
import sys
from collections import OrderedDict

DEFAULT_BASIS = 1_000_000
EVENT_FIELDS = ("fatalities", "lti", "rwi", "mti", "fai")


def rate(numerator: float, hours: float, basis: float = DEFAULT_BASIS) -> float:
    """Frequency rate = events x basis / hours worked. Rounded to 2 dp."""
    if hours <= 0:
        raise ValueError("Hours worked must be > 0.")
    return round(numerator * basis / hours, 2)


def all_rates(hours: float, fatalities: int = 0, lti: int = 0, rwi: int = 0,
              mti: int = 0, fai: int = 0, days_lost: float = None,
              basis: float = DEFAULT_BASIS) -> OrderedDict:
    recordable = fatalities + lti + rwi + mti
    out = OrderedDict()
    out["basis_hours"] = basis
    out["hours_worked"] = hours
    out["TRIFR"] = rate(recordable, hours, basis)
    out["LTIFR"] = rate(lti, hours, basis)  # LTIs only, per glossary.md/analytics.md
    out["MTIFR"] = rate(mti, hours, basis)
    out["RWIFR"] = rate(rwi, hours, basis)
    out["AIFR"] = rate(recordable + fai, hours, basis)  # includes FAIs
    out["recordable_count"] = recordable
    if days_lost is not None:
        out["severity_rate"] = rate(days_lost, hours, basis)
    return out


def rolling_12(rows: list, basis: float = DEFAULT_BASIS) -> list:
    """rows: list of dicts with period (YYYY-MM), hours, and event fields,
    sorted ascending, closed months only. Returns a rolling 12-month series —
    each entry is anchored to (ends at) that closed period."""
    rows = sorted(rows, key=lambda r: r["period"])
    series = []
    for i in range(11, len(rows)):
        window = rows[i - 11: i + 1]
        hours = sum(float(r["hours"]) for r in window)
        events = {f: sum(int(r.get(f, 0) or 0) for r in window) for f in EVENT_FIELDS}
        entry = OrderedDict(anchor_period=rows[i]["period"],
                            window_start=window[0]["period"])
        entry.update(all_rates(hours, basis=basis, **events))
        series.append(entry)
    return series


def _read_csv(path: str) -> list:
    with open(path, newline="") as f:
        return [dict(r) for r in csv.DictReader(f)]


def main() -> int:
    p = argparse.ArgumentParser(description="WHS frequency rate calculator")
    p.add_argument("--basis", type=float, default=DEFAULT_BASIS,
                   help="Rate basis in hours (default 1,000,000; US convention 200,000)")
    p.add_argument("--hours", type=float, help="Hours worked for the period")
    p.add_argument("--fatalities", type=int, default=0)
    p.add_argument("--lti", type=int, default=0, help="Lost Time Injuries")
    p.add_argument("--rwi", type=int, default=0, help="Restricted Work Injuries")
    p.add_argument("--mti", type=int, default=0, help="Medical Treatment Injuries")
    p.add_argument("--fai", type=int, default=0,
                   help="First Aid Injuries (AIFR numerator only; not recordable)")
    p.add_argument("--days-lost", type=float, default=None,
                   help="Total days lost (enables severity rate)")
    p.add_argument("--severity", action="store_true",
                   help="Require severity rate (errors if --days-lost missing)")
    p.add_argument("--csv", help="Monthly CSV: period,hours,fatalities,lti,rwi,mti")
    p.add_argument("--rolling", action="store_true",
                   help="Output rolling 12-month series from --csv")
    a = p.parse_args()

    if a.severity and a.days_lost is None:
        p.error("--severity requires --days-lost")

    if a.csv:
        rows = _read_csv(a.csv)
        if a.rolling:
            result = rolling_12(rows, basis=a.basis)
        else:
            hours = sum(float(r["hours"]) for r in rows)
            events = {f: sum(int(r.get(f, 0) or 0) for r in rows) for f in EVENT_FIELDS}
            result = all_rates(hours, basis=a.basis, days_lost=a.days_lost, **events)
    else:
        if a.hours is None:
            p.error("provide --hours, or --csv")
        result = all_rates(a.hours, a.fatalities, a.lti, a.rwi, a.mti, a.fai,
                           days_lost=a.days_lost, basis=a.basis)

    json.dump(result, sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
