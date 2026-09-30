#!/usr/bin/env python3
# whs-professional/scripts/rate_confidence.py
"""
WHS rate confidence calculator — exact statistics for frequency rates.

A frequency rate is an estimate built on a count, and small counts bounce.
This script puts an exact interval around a rate, tests whether two rates
differ by more than chance, and sets funnel-plot control limits for comparing
units. Use it instead of in-context arithmetic, on the same counts and hours
given to frequency_rates.py. Standard library only. Supports analytics.md §9
(statistical treatment of rates).

Conventions
-----------
- Default basis: per 1,000,000 hours worked (AU convention), as in
  frequency_rates.py. Use --basis 200000 for the US OSHA convention.
- Counts are treated as Poisson: independent events over a known exposure.
  Enter the same injury counts given to frequency_rates.py so the interval
  matches the reported rate. Injuries from one event are not independent:
  where a multi-casualty event is in the count, the interval understates
  the uncertainty, so rerun on event counts as a sensitivity check. Where
  events cluster more generally (overdispersion), every interval and limit
  here is too narrow.
- ci: exact Poisson interval (Garwood 1936). For x events at confidence
  level 1 - a: lower = chi-square quantile (a/2; 2x) / 2, upper = chi-square
  quantile (1 - a/2; 2x + 2) / 2, each x basis / hours. Zero events: lower
  limit 0, upper limit -ln(a/2) events (3.69 at 95%). The interval is
  conservative — coverage is at least the stated level.
- compare: rate ratio = rate B / rate A (A is the baseline). Exact
  conditional test: given the total events, the events falling in B are
  binomial with probability hours B / (hours A + hours B) when the true
  rates are equal. Interval = Clopper-Pearson limits on that probability,
  converted to a ratio. Two-sided p-value = 2 x the smaller tail (capped at
  1), so p < 0.05 exactly when the 95% interval excludes 1. R's
  poisson.test(c(events B, events A), c(hours B, hours A)) gives the same
  ratio and interval, but its two-sided p sums every outcome no more likely
  than the one observed. With unequal hours that p can be as little as half
  the p here (4 events in 1,000,000 hours for A v 3 in 4,000,000 hours for
  B: 0.067 here, 0.033 in R), enough to change a call at 0.05, and R's p
  can then disagree with R's own interval. The p here cannot.
- funnel: target rate = pooled rate of the units supplied, or --target-rate
  (group or benchmark rate, at the basis). Limits are set at 95% and 99.8%
  (about 2 and 3 standard deviations; Spiegelhalter 2005). A unit is outside
  a limit when the exact Poisson probability of a count at least as extreme
  as its own, given the target rate and the unit's hours, is below 0.025
  (95%) or 0.001 (99.8%) — the same as the unit's own exact interval at that
  level excluding the target rate. units_outside_95 includes the units
  outside 99.8%. Each unit also carries its own exact 95% interval
  (rate_ci95_lower, rate_ci95_upper), whatever the funnel level.
- Funnel limit values are the rates at which that tail probability is
  reached, interpolated between whole counts through the incomplete gamma
  function. They are conservative: an in-control unit falls outside a limit
  with probability below the nominal level. Flags agree at whole counts with
  Spiegelhalter's (2005) method (method 1 in Manktelow and Seaton, PLoS ONE
  2012), but he interpolates linearly between whole counts, so plotted limit
  values can differ slightly from other funnel tools. Tools using Manktelow
  and Seaton's less conservative method 3 draw limits about one count lower
  and can flag a borderline unit that is inside here. A null lower limit
  means the unit has too few hours for even a zero count to fall below it.
- dispersion_ratio = mean of the squared z-scores, (observed - expected)^2 /
  expected, with expected counts from the pooled rate even when
  --target-rate is supplied, so a gap between the group and a benchmark
  does not inflate it. dispersion_p_value tests their sum
  (pearson_chi_square) against a chi-square on units - 1 df: a ratio well
  above 1 with a small p signals overdispersion. Treat it as a screen: it is
  unreliable with few units or expected counts below about 5, and one
  small-exposure unit can dominate it. Not computed with one unit or no
  events.
- Rounding: rates and rate limits 2 dp (as frequency_rates.py; for rare
  events such as fatalities use --basis 100000000 so rates do not round to
  0.00); count limits 4 dp; rate ratios 4 significant figures, with ratio
  and percentage-change limits rounded outward (extra figures kept where
  rounding would reach 1 or 0%), so the printed interval always contains the
  exact one and never contradicts the test; percentage change 1 dp; p-values
  and tail probabilities 4 significant figures (more where needed to stay
  below the test threshold). A p-value or tail probability below 1e-300 is
  reported as 1e-300, a floor ("< 1e-300" in text output).
- Input: --confidence takes a fraction (0.95) or a percentage (95), from 50%
  up to but not including 100%. Hours and counts accept 1200000, 1_200_000,
  1.2e6 or 1,200,000 (quote a value with commas in a CSV); a decimal comma
  is rejected. Counts are whole numbers up to 1,000,000,000. Unit names must
  be present and unique.
- Output: JSON (default, as frequency_rates.py); --text for a plain-text
  summary. Exit status 0 on success, 1 when the self-test fails, 2 on a
  usage or input error.

Usage
-----
Exact interval for a rate (9 recordables in 1,200,000 hours):
    python3 rate_confidence.py ci --events 9 --hours 1200000

Zero events, 99% interval, US basis:
    python3 rate_confidence.py ci --events 0 --hours 500000 \
        --confidence 0.99 --basis 200000

Two periods or two units (A = baseline, B = comparison):
    python3 rate_confidence.py compare --events-a 14 --hours-a 1250000 \
        --events-b 9 --hours-b 1200000

Funnel limits, units given inline as NAME:EVENTS:HOURS against a group rate:
    python3 rate_confidence.py funnel --target-rate 6.0 \
        --unit A:3:210000 --unit B:44:4200000 --unit C:0:300000

Funnel limits from a CSV (columns: unit,events,hours), pooled target rate,
plain-text table:
    python3 rate_confidence.py funnel --csv units.csv --text

Self-test against published reference values, independent summation and
the behaviour of every sub-command:
    python3 rate_confidence.py --self-test --quiet
"""

import argparse
import csv
import json
import math
import os
import re
import subprocess
import sys
import tempfile
from collections import OrderedDict

DEFAULT_BASIS = 1_000_000
DEFAULT_LEVEL = 0.95
FUNNEL_LEVELS = (("95", 0.95), ("99_8", 0.998))
MAX_EVENTS = 1_000_000_000  # accuracy and run time are checked to this count
P_FLOOR = 1e-300            # smallest p-value or tail probability reported

_EPS = 1e-15     # relative convergence target for series / continued fractions
_TINY = 1e-300   # floor that keeps the Lentz recurrences away from zero
# A number written with correctly grouped thousands separators: 1,200,000.
_THOUSANDS = re.compile(r"[+]?\d{1,3}(?:,\d{3})+(?:\.\d*)?")


# --------------------------------------------------------------------------
# Numerical core: incomplete gamma and beta functions, and their inverses
# --------------------------------------------------------------------------

def _gamma_pq(a: float, x: float) -> tuple:
    """Regularised incomplete gamma functions (P(a, x), Q(a, x)), Q = 1 - P.

    Power series when x < a + 1, modified-Lentz continued fraction otherwise,
    so the smaller of the two tails is always the one computed directly and
    keeps its relative precision."""
    if a <= 0:
        raise ValueError("Shape parameter must be > 0.")
    if x <= 0:
        return 0.0, 1.0
    log_front = -x + a * math.log(x) - math.lgamma(a)
    max_iter = 1000 + int(50 * math.sqrt(a + x))
    if x < a + 1.0:
        term = 1.0 / a
        total = term
        for n in range(1, max_iter):
            term *= x / (a + n)
            total += term
            if term < total * _EPS:
                break
        else:
            raise ArithmeticError("Incomplete gamma series did not converge.")
        p = min(1.0, total * math.exp(log_front))
        return p, 1.0 - p
    b = x + 1.0 - a
    c = 1.0 / _TINY
    d = 1.0 / b
    h = d
    for i in range(1, max_iter):
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        if abs(d) < _TINY:
            d = _TINY
        c = b + an / c
        if abs(c) < _TINY:
            c = _TINY
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < _EPS:
            break
    else:
        raise ArithmeticError("Incomplete gamma fraction did not converge.")
    q = min(1.0, h * math.exp(log_front))
    return 1.0 - q, q


def _bisect(f, lo: float, hi: float) -> float:
    """Root of an increasing function with f(lo) <= 0 <= f(hi). Plain
    bisection: slower than Newton, but it cannot diverge or leave the
    bracket, and it runs to the limit of floating-point resolution."""
    for _ in range(2000):
        mid = 0.5 * (lo + hi)
        if mid <= lo or mid >= hi:
            break
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
        if hi - lo <= 2e-15 * hi:
            break
    return 0.5 * (lo + hi)


def gamma_quantile(a: float, tail: float, upper: bool = False) -> float:
    """x such that P(a, x) = tail, or Q(a, x) = tail when upper is True.
    Pass the small tail directly (0.025, not 0.975) to keep precision."""
    if not 0.0 < tail < 1.0:
        raise ValueError("Tail probability must be between 0 and 1.")
    if upper:
        def f(x):
            return tail - _gamma_pq(a, x)[1]
    else:
        def f(x):
            return _gamma_pq(a, x)[0] - tail
    hi = max(a, 1.0)
    while f(hi) < 0:
        hi *= 2.0
    return _bisect(f, 0.0, hi)


def chi_square_quantile(p: float, df: float) -> float:
    """Chi-square quantile: the value with lower-tail probability p."""
    if p <= 0.5:
        return 2.0 * gamma_quantile(df / 2.0, p)
    return 2.0 * gamma_quantile(df / 2.0, 1.0 - p, upper=True)


def _beta_cf(a: float, b: float, x: float) -> float:
    """Continued fraction for the incomplete beta function (modified Lentz)."""
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < _TINY:
        d = _TINY
    d = 1.0 / d
    h = d
    for m in range(1, 1000 + int(50 * math.sqrt(a + b))):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < _TINY:
            d = _TINY
        c = 1.0 + aa / c
        if abs(c) < _TINY:
            c = _TINY
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < _TINY:
            d = _TINY
        c = 1.0 + aa / c
        if abs(c) < _TINY:
            c = _TINY
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < _EPS:
            return h
    raise ArithmeticError("Incomplete beta fraction did not converge.")


def beta_inc(a: float, b: float, x: float) -> float:
    """Regularised incomplete beta function I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    front = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                     + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1.0) / (a + b + 2.0):
        return min(1.0, front * _beta_cf(a, b, x) / a)
    return max(0.0, 1.0 - front * _beta_cf(b, a, 1.0 - x) / b)


def beta_quantile(a: float, b: float, tail: float) -> float:
    """x such that I_x(a, b) = tail (lower-tail probability)."""
    if not 0.0 < tail < 1.0:
        raise ValueError("Tail probability must be between 0 and 1.")
    return _bisect(lambda x: beta_inc(a, b, x) - tail, 0.0, 1.0)


# --------------------------------------------------------------------------
# Poisson and binomial tail probabilities
# --------------------------------------------------------------------------

def poisson_upper_tail(k: int, mu: float) -> float:
    """P(X >= k) for X ~ Poisson(mu)."""
    if k <= 0:
        return 1.0
    return _gamma_pq(k, mu)[0]


def poisson_lower_tail(k: int, mu: float) -> float:
    """P(X <= k) for X ~ Poisson(mu)."""
    if k < 0:
        return 0.0
    return _gamma_pq(k + 1, mu)[1]


def _binom_upper_tail(k: int, n: int, p: float) -> float:
    """P(X >= k) for X ~ Binomial(n, p)."""
    if k <= 0:
        return 1.0
    if k > n:
        return 0.0
    return beta_inc(k, n - k + 1, p)


def _binom_lower_tail(k: int, n: int, q: float) -> float:
    """P(X <= k) for X ~ Binomial(n, 1 - q). Takes q = 1 - p so a small
    lower tail is computed directly, not as 1 minus a number near 1."""
    if k >= n:
        return 1.0
    if k < 0:
        return 0.0
    return beta_inc(n - k, k + 1, q)


# --------------------------------------------------------------------------
# Calculations
# --------------------------------------------------------------------------

def _sig(value: float, digits: int = 4) -> float:
    """Round to significant figures (p-values and tail probabilities)."""
    return float(f"{value:.{digits}g}")


def _p_out(p: float, thresholds: tuple = ()) -> float:
    """A p-value or tail probability for output: 4 significant figures, with
    more kept while rounding would lift a value that is below a threshold
    (0.05, 0.025, 0.001) up to it. Below P_FLOOR, P_FLOOR itself: a floor."""
    if p < P_FLOOR:
        return P_FLOOR
    shown = _sig(p)
    for digits in range(5, 18):
        if not any(p < t <= shown for t in thresholds):
            break
        shown = _sig(p, digits)
    return shown


def _outward(value: float, up: bool, sig: int = None, places: int = None,
             pivot: float = None) -> float:
    """Round a confidence limit outward (down for a lower limit, up for an
    upper limit) to `sig` significant figures or `places` decimals, so the
    printed interval always contains the exact one. Where the exact limit
    lies on one side of `pivot` (1 for a ratio, 0 for a change), figures are
    added until the rounded limit does too."""
    if value == 0.0:
        return 0.0
    if places is None:
        places = sig - 1 - math.floor(math.log10(abs(value)))
    step = math.ceil if up else math.floor
    for extra in range(16):
        d = places + extra
        if d >= 0:
            rounded = step(value * 10.0 ** d) / 10.0 ** d
        else:
            rounded = step(value / 10.0 ** -d) * 10.0 ** -d
        if (pivot is None or value == pivot
                or ((value < pivot) == (rounded < pivot)
                    and rounded != pivot)):
            break
    return rounded + 0.0  # + 0.0 turns -0.0 into 0.0


def _tidy(x: float):
    """Hours and basis for output: a whole number as an int, otherwise the
    value without floating-point noise (12 significant figures)."""
    x = float(f"{x:.12g}")
    return int(x) if x.is_integer() else x


def _require_finite(result):
    """Reject a result holding inf or nan, which valid JSON cannot carry."""
    if isinstance(result, float) and not math.isfinite(result):
        raise ValueError("Result is outside floating-point range: check the "
                         "hours and basis.")
    if isinstance(result, dict):
        for value in result.values():
            _require_finite(value)
    elif isinstance(result, list):
        for value in result:
            _require_finite(value)
    return result


def _check_inputs(events, hours, basis=DEFAULT_BASIS, level=DEFAULT_LEVEL):
    if (isinstance(events, bool) or not isinstance(events, int)
            or not 0 <= events <= MAX_EVENTS):
        raise ValueError("Events must be a whole number from 0 to "
                         f"{MAX_EVENTS:,}.")
    if not (hours > 0 and math.isfinite(hours)):
        raise ValueError("Hours worked must be a finite number > 0.")
    if not (basis > 0 and math.isfinite(basis)):
        raise ValueError("Basis must be a finite number > 0.")
    if not 0.0 < level < 1.0:
        raise ValueError("Confidence level must be between 0 and 1.")


def garwood_limits(events: int, level: float = DEFAULT_LEVEL) -> tuple:
    """Exact (Garwood) confidence limits on a Poisson count: (lower, upper).
    Same as chi-square quantile (a/2; 2x) / 2 and (1 - a/2; 2x + 2) / 2."""
    _check_inputs(events, 1.0, level=level)
    tail = (1.0 - level) / 2.0
    lower = 0.0 if events == 0 else gamma_quantile(events, tail)
    upper = gamma_quantile(events + 1, tail, upper=True)
    return lower, upper


def rate_interval(events: int, hours: float, level: float = DEFAULT_LEVEL,
                  basis: float = DEFAULT_BASIS) -> OrderedDict:
    """Rate with its exact Poisson (Garwood) confidence interval."""
    _check_inputs(events, hours, basis, level)
    lower, upper = garwood_limits(events, level)
    out = OrderedDict()
    out["method"] = "Exact Poisson (Garwood) confidence interval"
    out["basis_hours"] = _tidy(basis)
    out["hours_worked"] = _tidy(hours)
    out["events"] = events
    out["confidence_level"] = level
    out["rate"] = round(events * basis / hours, 2)
    out["rate_ci_lower"] = round(lower * basis / hours, 2)
    out["rate_ci_upper"] = round(upper * basis / hours, 2)
    out["count_ci_lower"] = round(lower, 4)
    out["count_ci_upper"] = round(upper, 4)
    return _require_finite(out)


def _ratio_exact(events_a: int, hours_a: float, events_b: int, hours_b: float,
                 level: float) -> tuple:
    """Unrounded (ratio, lower, upper, p) for rate B / rate A. ratio is None
    when A has no events; upper is None when it is unbounded."""
    n = events_a + events_b
    tail = (1.0 - level) / 2.0
    scale = hours_a / hours_b
    ratio = None
    if events_a > 0:
        ratio = (events_b / hours_b) / (events_a / hours_a)
    if n == 0:
        return ratio, 0.0, None, 1.0
    lower = 0.0
    if events_b > 0:
        p_low = beta_quantile(events_b, events_a + 1, tail)
        lower = p_low / (1.0 - p_low) * scale
    upper = None
    if events_a > 0:
        q_up = beta_quantile(events_a, events_b + 1, tail)
        upper = (1.0 - q_up) / q_up * scale
    total_hours = hours_a + hours_b
    p_null, q_null = hours_b / total_hours, hours_a / total_hours
    p_value = min(1.0, 2.0 * min(_binom_lower_tail(events_b, n, q_null),
                                 _binom_upper_tail(events_b, n, p_null)))
    return ratio, lower, upper, p_value


def _ratio_fields(ratio, lower, upper, p_value, level: float,
                  total_events: int) -> OrderedDict:
    """Rounded ratio, interval, percentage change, p-value, verdict and
    reading. The limits are rounded outward and the p-value keeps enough
    figures that the printed numbers always agree with the verdict."""
    alpha = 1.0 - level
    out = OrderedDict()
    shown = None
    if ratio is not None:
        shown = _sig(ratio)
        for digits in range(5, 18):
            if shown != 1.0 or ratio == 1.0:
                break
            shown = _sig(ratio, digits)
    out["rate_ratio"] = shown
    out["rate_ratio_ci_lower"] = _outward(lower, False, sig=4, pivot=1.0)
    out["rate_ratio_ci_upper"] = (None if upper is None
                                  else _outward(upper, True, sig=4, pivot=1.0))
    out["change_pct"] = (None if ratio is None
                         else round((ratio - 1.0) * 100.0, 1) + 0.0)
    out["change_pct_ci_lower"] = _outward((lower - 1.0) * 100.0, False,
                                          places=1, pivot=0.0)
    out["change_pct_ci_upper"] = (None if upper is None
                                  else _outward((upper - 1.0) * 100.0, True,
                                                places=1, pivot=0.0))
    out["p_value"] = _p_out(p_value, (round(alpha, 12),))
    detectable = p_value < alpha
    out["detectable_difference"] = detectable
    pct_level = f"{level * 100:g}%"
    if total_events == 0:
        out["reading"] = "No events in either period: nothing to compare."
    elif not detectable:
        out["reading"] = (f"No detectable difference at the {pct_level} "
                          "level: the interval for the rate ratio includes 1.")
    else:
        word = "lower" if upper is not None and upper < 1.0 else "higher"
        out["reading"] = (f"Rate B is {word} than rate A by more than chance "
                          f"explains at the {pct_level} level.")
    return out


def compare_rates(events_a: int, hours_a: float, events_b: int, hours_b: float,
                  level: float = DEFAULT_LEVEL,
                  basis: float = DEFAULT_BASIS) -> OrderedDict:
    """Rate ratio (B / A) with exact conditional binomial interval and test."""
    _check_inputs(events_a, hours_a, basis, level)
    _check_inputs(events_b, hours_b, basis, level)
    ratio, lower, upper, p_value = _ratio_exact(events_a, hours_a,
                                                events_b, hours_b, level)
    out = OrderedDict()
    out["method"] = ("Exact conditional binomial test (Clopper-Pearson "
                     "interval; two-sided p = 2 x smaller tail)")
    out["basis_hours"] = _tidy(basis)
    out["confidence_level"] = level
    for key, events, hours in (("a", events_a, hours_a),
                               ("b", events_b, hours_b)):
        lo, hi = garwood_limits(events, level)
        side = OrderedDict()
        side["events"] = events
        side["hours_worked"] = _tidy(hours)
        side["rate"] = round(events * basis / hours, 2)
        side["rate_ci_lower"] = round(lo * basis / hours, 2)
        side["rate_ci_upper"] = round(hi * basis / hours, 2)
        out[key] = side
    out.update(_ratio_fields(ratio, lower, upper, p_value, level,
                             events_a + events_b))
    return _require_finite(out)


def funnel_count_limits(expected: float, level: float) -> tuple:
    """(lower, upper) funnel limits on a count with Poisson mean `expected`.

    upper: the count u at which P(X >= u) = (1 - level) / 2; a unit at or
    above it is outside the limit. lower: the count l at which
    P(X <= l) = (1 - level) / 2, or None when even a zero count is not that
    unlikely. Both are interpolated between whole counts through the
    incomplete gamma function, so they agree exactly with the Poisson tail
    probabilities at whole counts."""
    if not expected > 0:
        raise ValueError("Expected count must be > 0.")
    tail = (1.0 - level) / 2.0
    hi = expected + 1.0
    while _gamma_pq(hi, expected)[0] > tail:
        hi *= 2.0
    upper = _bisect(lambda a: tail - _gamma_pq(a, expected)[0], 1e-12, hi)
    lower = None
    if math.exp(-expected) < tail:
        lower = _bisect(lambda a: _gamma_pq(a + 1.0, expected)[1] - tail,
                        0.0, expected)
    return lower, upper


def funnel(units: list, target_rate: float = None,
           basis: float = DEFAULT_BASIS) -> OrderedDict:
    """Funnel-plot control limits (95% and 99.8%) for a list of units.

    units: list of (name, events, hours). target_rate: group or benchmark
    rate at the basis; defaults to the pooled rate of the units supplied.
    The dispersion statistics always use the pooled rate."""
    if not units:
        raise ValueError("Provide at least one unit.")
    seen = set()
    for name, events, hours in units:
        label = str(name).strip()
        if not label:
            raise ValueError("Every unit needs a name.")
        if label in seen:
            raise ValueError(f"Unit {label!r} appears more than once: "
                             "combine its events and hours, or rename it.")
        seen.add(label)
        try:
            _check_inputs(events, hours, basis)
        except ValueError as exc:
            raise ValueError(f"Unit {label!r}: {exc}")
    total_events = sum(u[1] for u in units)
    total_hours = math.fsum(u[2] for u in units)
    pooled = total_events / total_hours
    if target_rate is None:
        if total_events == 0:
            raise ValueError("No events in any unit, so the pooled rate is 0 "
                             "and there is no funnel to draw. Give "
                             "--target-rate to test the units against a "
                             "benchmark.")
        source, per_hour = "pooled", pooled
    else:
        if not (target_rate > 0 and math.isfinite(target_rate)):
            raise ValueError("Target rate (--target-rate) must be a finite "
                             "number > 0.")
        source, per_hour = "supplied", target_rate / basis
    thresholds = tuple(round((1.0 - level) / 2.0, 12)
                       for _, level in FUNNEL_LEVELS)

    results = []
    outside = {label: 0 for label, _ in FUNNEL_LEVELS}
    for name, events, hours in units:
        expected = per_hour * hours
        if not 0.0 < expected <= MAX_EVENTS:
            raise ValueError(f"Unit {name!r}: {expected:.4g} expected events "
                             "at the target rate is out of range (above 0, "
                             f"up to {MAX_EVENTS:,}); check the target rate, "
                             "basis and hours.")
        factor = basis / hours
        high = poisson_upper_tail(events, expected)
        low = poisson_lower_tail(events, expected)
        lo95, hi95 = garwood_limits(events, DEFAULT_LEVEL)
        row = OrderedDict()
        row["unit"] = name
        row["events"] = events
        row["hours_worked"] = _tidy(hours)
        row["rate"] = round(events * factor, 2)
        row["rate_ci95_lower"] = round(lo95 * factor, 2)
        row["rate_ci95_upper"] = round(hi95 * factor, 2)
        row["expected_events"] = round(expected, 2)
        flag = "inside"
        for label, level in FUNNEL_LEVELS:
            lower, upper = funnel_count_limits(expected, level)
            row[f"limit_{label}_lower"] = (None if lower is None
                                           else round(lower * factor, 2))
            row[f"limit_{label}_upper"] = round(upper * factor, 2)
            if min(high, low) < (1.0 - level) / 2.0:
                flag = f"outside_{label}"
                outside[label] += 1
        above = events >= expected
        row["tail_probability"] = _p_out(high if above else low, thresholds)
        row["tail"] = "this many or more" if above else "this many or fewer"
        row["flag"] = flag
        row["direction"] = (None if flag == "inside"
                            else "high" if high < low else "low")
        results.append(row)

    out = OrderedDict()
    out["method"] = ("Funnel limits from exact Poisson tail probabilities "
                     "against the target rate")
    out["basis_hours"] = _tidy(basis)
    out["target_rate"] = round(per_hour * basis, 2)
    out["target_source"] = source
    out["units"] = len(units)
    out["total_events"] = total_events
    out["total_hours_worked"] = _tidy(total_hours)
    out["units_outside_95"] = outside["95"]
    out["units_outside_99_8"] = outside["99_8"]
    out["dispersion_basis"] = "pooled rate"
    chi_square = df = ratio = p_disp = None
    if total_events > 0 and len(units) > 1:
        chi = math.fsum((e - pooled * h) ** 2 / (pooled * h)
                        for _, e, h in units)
        df = len(units) - 1
        chi_square = round(chi, 2)
        ratio = round(chi / len(units), 2)
        p_disp = _p_out(_gamma_pq(df / 2.0, chi / 2.0)[1])
    out["pearson_chi_square"] = chi_square
    out["dispersion_df"] = df
    out["dispersion_ratio"] = ratio
    out["dispersion_p_value"] = p_disp
    out["results"] = results
    return _require_finite(out)


# --------------------------------------------------------------------------
# Input parsing and text output
# --------------------------------------------------------------------------

def _number(value, what: str = "Hours") -> float:
    """Parse a finite number. Accepts 1200000, 1_200_000, 1.2e6 and
    correctly grouped thousands separators (1,200,000); rejects a decimal
    comma (1,5), text, inf and nan."""
    s = str(value).strip()
    t = s.replace(",", "") if _THOUSANDS.fullmatch(s) else s
    try:
        number = float(t)
    except ValueError:
        hint = " (a decimal comma is not accepted)" if "," in s else ""
        raise ValueError(f"{what} {s!r}: expected a number{hint}.") from None
    if not math.isfinite(number):
        raise ValueError(f"{what} {s!r}: expected a finite number.")
    return number


def _whole(value, what: str = "Events") -> int:
    """Parse a whole count from 0 to MAX_EVENTS; rejects 3.5, -1, inf and
    text. Digit strings are read exactly, not through a float."""
    s = str(value).strip()
    bad = ValueError(f"{what} {s!r}: expected a whole number from 0 to "
                     f"{MAX_EVENTS:,}.")
    digits = s.replace(",", "") if _THOUSANDS.fullmatch(s) else s
    if re.fullmatch(r"[0-9]+(?:_[0-9]+)*", digits):
        number = int(digits)
    else:
        try:
            x = _number(s, what)
        except ValueError:
            raise bad from None
        if x < 0 or not x.is_integer():
            raise bad
        number = int(x)
    if number > MAX_EVENTS:
        raise bad
    return number


def _count_arg(value: str) -> int:
    try:
        return _whole(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc))


def _number_arg(what: str):
    def parse(value: str) -> float:
        try:
            return _number(value, what)
        except ValueError as exc:
            raise argparse.ArgumentTypeError(str(exc))
    return parse


def _level_arg(value: str) -> float:
    """Confidence level as a fraction (0.95) or a percentage (95, 99.8),
    from 50% up to but not including 100%."""
    try:
        level = float(value)
    except ValueError:
        level = math.nan
    if 50.0 <= level < 100.0:
        level /= 100.0
    level = round(level, 12)  # 99.9 -> 0.999, not 0.9990000000000001
    if not 0.5 <= level < 1.0:
        raise argparse.ArgumentTypeError(
            f"confidence level {value!r}: give a fraction from 0.5 to below "
            "1 (0.95) or a percentage from 50 to below 100 (95)")
    return level


def _parse_unit(spec: str) -> tuple:
    """NAME:EVENTS:HOURS -> (name, events, hours). The name may hold colons."""
    parts = spec.rsplit(":", 2)
    if len(parts) != 3 or not parts[0].strip():
        raise ValueError(f"Invalid unit {spec!r}: expected NAME:EVENTS:HOURS.")
    try:
        return parts[0].strip(), _whole(parts[1]), _number(parts[2])
    except ValueError as exc:
        raise ValueError(f"Invalid unit {spec!r}: {exc}")


def _read_units_csv(path: str) -> list:
    """Units from a CSV with columns unit, events and hours (any order or
    case; an Excel BOM is fine). Rejects a row with more fields than columns
    (the usual sign of an unquoted thousands separator), a missing value, a
    blank name or a repeated name, citing the CSV line."""
    units, seen = [], {}
    with open(path, newline="", encoding="utf-8-sig") as f:  # Excel BOM
        reader = csv.DictReader(f)
        header = [(h or "").strip().lower() for h in (reader.fieldnames or [])]
        absent = [c for c in ("unit", "events", "hours") if c not in header]
        if absent:
            raise ValueError("CSV header must name the columns unit,events,"
                             f"hours; missing {', '.join(absent)}.")
        for r in reader:
            line = reader.line_num
            if None in r:
                raise ValueError(
                    f"CSV line {line}: more fields than columns (unit,events,"
                    "hours); remove thousands separators or quote the value "
                    "(\"1,200,000\").")
            row = {(k or "").strip().lower(): v for k, v in r.items()}
            missing = [c for c in ("unit", "events", "hours")
                       if (row.get(c) or "").strip() == ""]
            if missing:
                raise ValueError(f"CSV line {line}: missing "
                                 f"{', '.join(missing)} (columns: "
                                 "unit,events,hours).")
            name = row["unit"].strip()
            if name in seen:
                raise ValueError(f"CSV line {line}: unit {name!r} already "
                                 f"appears on line {seen[name]}; combine its "
                                 "rows or rename it.")
            seen[name] = line
            try:
                units.append((name, _whole(row["events"]),
                              _number(row["hours"])))
            except ValueError as exc:
                raise ValueError(f"CSV line {line}: {exc}")
    return units


def _num(value, places: int = 2) -> str:
    return "none" if value is None else f"{value:,.{places}f}"


def _p_text(p: float) -> str:
    return "< 1e-300" if p <= P_FLOOR else f"{p!r}"


def _text_ci(r: OrderedDict) -> str:
    level = f"{r['confidence_level'] * 100:g}%"
    return "\n".join([
        f"{r['method']}, {level}",
        f"  Events {r['events']:,} in {r['hours_worked']:,.0f} hours "
        f"(rate per {r['basis_hours']:,.0f} hours)",
        f"  Rate {_num(r['rate'])}   {level} CI {_num(r['rate_ci_lower'])} "
        f"to {_num(r['rate_ci_upper'])}",
        f"  Count limits {_num(r['count_ci_lower'], 4)} to "
        f"{_num(r['count_ci_upper'], 4)}",
    ])


def _text_compare(r: OrderedDict) -> str:
    level = f"{r['confidence_level'] * 100:g}%"
    lines = [r["method"],
             f"  Rates per {r['basis_hours']:,.0f} hours, {level} intervals"]
    for key in ("a", "b"):
        s = r[key]
        word = "event" if s["events"] == 1 else "events"
        lines.append(
            f"  {key.upper()}: {s['events']:,} {word} in "
            f"{s['hours_worked']:,.0f} hours   rate {_num(s['rate'])}   "
            f"CI {_num(s['rate_ci_lower'])} to {_num(s['rate_ci_upper'])}")
    ratio = ("undefined (no events in A)" if r["rate_ratio"] is None
             else f"{r['rate_ratio']!r}")
    upper = ("unbounded" if r["rate_ratio_ci_upper"] is None
             else f"{r['rate_ratio_ci_upper']!r}")
    p = ("p < 1e-300" if r["p_value"] <= P_FLOOR
         else f"p = {r['p_value']!r}")
    lines.append(f"  Rate ratio B/A {ratio}   CI "
                 f"{r['rate_ratio_ci_lower']!r} to {upper}   {p}")
    def pct(value, absent):
        if value is None:
            return absent
        # 1 dp, or the extra places kept so a limit does not round onto 0%
        return (f"{value:+.1f}%" if round(value, 1) == value
                else f"{value:+g}%")

    lines.append(f"  Change B v A {pct(r['change_pct'], 'undefined')}   CI "
                 f"{pct(r['change_pct_ci_lower'], 'none')} to "
                 f"{pct(r['change_pct_ci_upper'], 'unbounded')}")
    lines.append(f"  {r['reading']}")
    return "\n".join(lines)


def _text_funnel(r: OrderedDict) -> str:
    head = ("Unit", "Events", "Hours", "Rate", "Expected", "95% limits",
            "99.8% limits", "Tail p", "Flag")
    rows = [head]
    for u in r["results"]:
        flag = {"inside": "inside", "outside_95": "outside 95%",
                "outside_99_8": "outside 99.8%"}[u["flag"]]
        if u["direction"]:
            flag += f" ({u['direction']})"
        rows.append((
            str(u["unit"]), f"{u['events']:,}", f"{u['hours_worked']:,.0f}",
            _num(u["rate"]), _num(u["expected_events"]),
            f"{_num(u['limit_95_lower'])} to {_num(u['limit_95_upper'])}",
            f"{_num(u['limit_99_8_lower'])} to {_num(u['limit_99_8_upper'])}",
            _p_text(u["tail_probability"]), flag))
    widths = [max(len(row[i]) for row in rows) for i in range(len(head))]
    if r["dispersion_ratio"] is None:
        dispersion = ("  Dispersion: not computed (needs two or more units "
                      "and at least one event)")
    else:
        dispersion = (f"  Dispersion against the pooled rate: ratio "
                      f"{_num(r['dispersion_ratio'])} (mean z^2); chi-square "
                      f"{_num(r['pearson_chi_square'])} on "
                      f"{r['dispersion_df']} df, p "
                      f"{_p_text(r['dispersion_p_value'])}")
    lines = [
        f"{r['method']}",
        f"  Target rate {_num(r['target_rate'])} per "
        f"{r['basis_hours']:,.0f} hours ({r['target_source']}); "
        f"{r['units']} unit{'' if r['units'] == 1 else 's'}, "
        f"{r['total_events']:,} event{'' if r['total_events'] == 1 else 's'}, "
        f"{r['total_hours_worked']:,.0f} hours",
        f"  Outside 95%: {r['units_outside_95']}   Outside 99.8%: "
        f"{r['units_outside_99_8']}",
        dispersion,
        "",
    ]
    for row in rows:
        cells = [row[0].ljust(widths[0])]
        cells += [row[i].rjust(widths[i]) for i in range(1, len(head) - 1)]
        cells.append(row[-1])
        lines.append("  " + "  ".join(cells))
    if any(u[f"limit_{label}_lower"] is None for u in r["results"]
           for label, _ in FUNNEL_LEVELS):
        lines.append("  none = no lower limit: too few hours for even a zero "
                     "count to fall below it")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------

def _poisson_tails_by_sum(k: int, mu: float) -> tuple:
    """(P(X <= k), P(X >= k)) by summing the Poisson probabilities term by
    term — an independent route that never touches the gamma code. Terms
    more than 40 standard deviations below the mean are under 1e-300 and
    skipped."""
    def pmf(i):
        return math.exp(-mu + i * math.log(mu) - math.lgamma(i + 1))
    start = max(0, int(mu - 40.0 * math.sqrt(mu) - 50.0))
    lower = math.fsum(pmf(i) for i in range(start, k + 1))
    terms, i = [], k
    while True:
        term = pmf(i)
        terms.append(term)
        if i > mu and term < 1e-20:
            break
        i += 1
    return lower, math.fsum(terms)


def _binom_tails_by_sum(k: int, n: int, p: float) -> tuple:
    """(P(X <= k), P(X >= k)) by summing the binomial probabilities."""
    def pmf(i):
        return math.exp(math.lgamma(n + 1) - math.lgamma(i + 1)
                        - math.lgamma(n - i + 1)
                        + i * math.log(p) + (n - i) * math.log1p(-p))
    return (math.fsum(pmf(i) for i in range(0, k + 1)),
            math.fsum(pmf(i) for i in range(k, n + 1)))


def _raises(fn, *args, **kwargs) -> str:
    """The message of the ValueError or ArgumentTypeError fn raises, or ''."""
    try:
        fn(*args, **kwargs)
    except (ValueError, argparse.ArgumentTypeError) as exc:
        return str(exc) or "raised"
    return ""


def _value(fn, *args):
    """fn(*args), or the ValueError or ArgumentTypeError it raises, so a
    check that expects a value fails cleanly instead of stopping the test."""
    try:
        return fn(*args)
    except (ValueError, argparse.ArgumentTypeError) as exc:
        return exc


def _run_cli(*args) -> tuple:
    """(exit status, stdout, stderr) of this script run with args."""
    done = subprocess.run([sys.executable, os.path.abspath(__file__)]
                          + list(args), stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, universal_newlines=True)
    return done.returncode, done.stdout, done.stderr


def _strict_json(text: str):
    """Parse JSON, rejecting the non-standard Infinity and NaN tokens."""
    def refuse(token):
        raise ValueError(f"non-standard JSON token {token}")
    return json.loads(text, parse_constant=refuse)


def self_test(verbose: bool = True) -> int:
    """Check the numerical core against published reference values and
    against independent term-by-term summation, then every sub-command end
    to end (rounding, flags, counts, readings, input parsing and the CLI).
    Returns the failure count."""
    failures = []
    count = 0

    def check(label, got, want, tol):
        nonlocal count
        count += 1
        ok = got is not None and abs(got - want) <= tol
        if not ok:
            failures.append(label)
        if verbose or not ok:
            print(f"{'PASS' if ok else 'FAIL'}  {label}: got {got!r}, "
                  f"reference {want!r}")

    def check_true(label, condition):
        nonlocal count
        count += 1
        if not condition:
            failures.append(label)
        if verbose or not condition:
            print(f"{'PASS' if condition else 'FAIL'}  {label}")

    # 1. Chi-square quantiles: NIST/SEMATECH e-Handbook of Statistical
    #    Methods, section 1.3.6.7.4 (critical values, 3 dp).
    nist_upper = [(1, 0.05, 3.841), (1, 0.025, 5.024), (1, 0.001, 10.828),
                  (2, 0.05, 5.991), (2, 0.025, 7.378), (4, 0.025, 11.143),
                  (10, 0.05, 18.307), (22, 0.025, 36.781),
                  (42, 0.025, 61.777), (100, 0.05, 124.342)]
    for df, alpha, ref in nist_upper:
        check(f"chi-square upper-tail {alpha} critical value, df {df} (NIST)",
              chi_square_quantile(1.0 - alpha, df), ref, 0.00051)
    nist_lower = [(2, 0.025, 0.051), (20, 0.025, 9.591), (40, 0.025, 24.433),
                  (100, 0.025, 74.222)]
    for df, alpha, ref in nist_lower:
        check(f"chi-square lower-tail {alpha} critical value, df {df} (NIST)",
              chi_square_quantile(alpha, df), ref, 0.00051)
    for p in (0.001, 0.025, 0.5, 0.975, 0.999):
        want = -2.0 * math.log(1.0 - p)
        check(f"chi-square quantile {p}, df 2, closed form -2 ln(1 - p)",
              chi_square_quantile(p, 2), want, 1e-10 * max(1.0, want))

    # 2. Garwood 95% limits, counts 0-5, 4 dp: McMaster University (P.
    #    Macdonald), "Confidence Intervals for the Mean of a Poisson
    #    Distribution", exact method.
    mcmaster = [(0, 0.0000, 3.6889), (1, 0.0253, 5.5716), (2, 0.2422, 7.2247),
                (3, 0.6187, 8.7673), (4, 1.0899, 10.2416),
                (5, 1.6235, 11.6683)]
    for k, lo_ref, hi_ref in mcmaster:
        lo, hi = garwood_limits(k, 0.95)
        check(f"Garwood 95% lower, count {k} (McMaster)", lo, lo_ref, 0.000051)
        check(f"Garwood 95% upper, count {k} (McMaster)", hi, hi_ref, 0.000051)

    # 3. Exact Poisson limits at six confidence levels, 2 dp: J. Hanley,
    #    McGill University, "Confidence limits for the expectation of a
    #    Poisson random variable" (course table, counts 0-30).
    hanley = [(0.95, 0, 0.00, 3.69), (0.95, 1, 0.03, 5.57),
              (0.95, 6, 2.20, 13.06), (0.95, 9, 4.12, 17.08),
              (0.95, 10, 4.80, 18.39), (0.95, 14, 7.65, 23.49),
              (0.95, 20, 12.22, 30.89), (0.95, 30, 20.24, 42.83),
              (0.998, 0, 0.00, 6.91), (0.998, 1, 0.00, 9.23),
              (0.998, 10, 2.96, 24.13), (0.998, 20, 8.96, 38.04),
              (0.998, 30, 15.87, 51.08),
              (0.99, 10, 3.72, 21.40), (0.98, 10, 4.13, 20.14),
              (0.90, 10, 5.43, 16.96), (0.80, 10, 6.22, 15.41)]
    for level, k, lo_ref, hi_ref in hanley:
        lo, hi = garwood_limits(k, level)
        tag = f"exact {level * 100:g}% limits, count {k} (Hanley)"
        check(f"{tag} lower", lo, lo_ref, 0.0051)
        check(f"{tag} upper", hi, hi_ref, 0.0051)

    # 4. Other published values: R survival::cipoisson documentation
    #    example (lower limit for 4 events, and the two Poisson tail
    #    probabilities it prints); StatsDirect worked example (14 events,
    #    400 person-years); NIST and MedCalc chi-square tables halved for
    #    counts 20, 50 and 100.
    check("cipoisson(4) lower (R survival)",
          garwood_limits(4, 0.95)[0], 1.089865, 5.1e-7)
    check("ppois(4, 10.24153) (R survival)",
          poisson_lower_tail(4, 10.24153), 0.02500096, 5.1e-9)
    check("1 - ppois(3, 1.08986) (R survival)",
          poisson_upper_tail(4, 1.08986), 0.02499961, 5.1e-9)
    lo, hi = garwood_limits(14, 0.95)
    check("14 events / 400 person-years, lower (StatsDirect)",
          lo / 400.0, 0.019135, 5.1e-7)
    check("14 events / 400 person-years, upper (StatsDirect)",
          hi / 400.0, 0.058724, 5.1e-7)
    check("Garwood 95% lower, count 20 = NIST chi-square(0.025; 40) / 2",
          garwood_limits(20)[0], 24.433 / 2.0, 0.00026)
    check("Garwood 95% upper, count 20 = NIST chi-square(0.975; 42) / 2",
          garwood_limits(20)[1], 61.777 / 2.0, 0.00026)
    check("Garwood 95% lower, count 50 = NIST chi-square(0.025; 100) / 2",
          garwood_limits(50)[0], 74.222 / 2.0, 0.00026)
    check("Garwood 95% lower, count 100 = chi-square(0.025; 200) / 2 "
          "(MedCalc)", garwood_limits(100)[0], 162.728 / 2.0, 0.00026)
    check("Garwood 95% upper, count 100 = chi-square(0.975; 202) / 2 "
          "(MedCalc)", garwood_limits(100)[1], 243.254 / 2.0, 0.00026)
    check("exact 99.8% upper, count 100 = chi-square(0.999; 202) / 2 "
          "(MedCalc)", garwood_limits(100, 0.998)[1], 269.849 / 2.0, 0.00026)

    # 5. Closed forms: zero events gives upper = -ln(a/2); one event gives
    #    lower = -ln(1 - a/2).
    for level in (0.80, 0.95, 0.99, 0.998):
        tail = (1.0 - level) / 2.0
        check(f"zero events, {level * 100:g}% upper = -ln(a/2)",
              garwood_limits(0, level)[1], -math.log(tail), 1e-10)
        check(f"one event, {level * 100:g}% lower = -ln(1 - a/2)",
              garwood_limits(1, level)[0], -math.log1p(-tail), 1e-10)

    # 6. Second route: at the Garwood limits the Poisson tail, summed term by
    #    term, must equal a/2. Covers counts well beyond the published tables;
    #    at 100,000 and 1,000,000 a 1e-7 relative error in the tail pins the
    #    limit to within 0.001 of a count.
    for level in (0.90, 0.95, 0.998):
        tail = (1.0 - level) / 2.0
        for k in (1, 2, 10, 44, 100, 1000, 100000, 1000000):
            if k > 1000 and level != 0.95:
                continue
            lo, hi = garwood_limits(k, level)
            upper_at_lo = _poisson_tails_by_sum(k, lo)[1]
            lower_at_hi = _poisson_tails_by_sum(k, hi)[0]
            tag = f"count {k:,}, {level * 100:g}%"
            tol = (1e-9 if k <= 1000 else 1e-7) * tail
            check(f"summed P(X >= k) at lower limit, {tag}",
                  upper_at_lo, tail, tol)
            check(f"summed P(X <= k) at upper limit, {tag}",
                  lower_at_hi, tail, tol)
    # At the cap, a second-order expansion of the Wilson-Hilferty cube-root
    # approximation (k -/+ z sqrt(k) + (z^2 - 1)/3 or (z^2 + 2)/3) is good to
    # about 0.001 of a count; the limits here are held to 0.1 of a count.
    lo, hi = garwood_limits(MAX_EVENTS)
    z, root = 1.959963984540054, math.sqrt(MAX_EVENTS)
    check_true(f"count {MAX_EVENTS:,} (the cap): limits within 0.1 of a "
               "count of the second-order Wilson-Hilferty expansion",
               abs(lo - (MAX_EVENTS - z * root + (z * z - 1.0) / 3.0)) < 0.1
               and abs(hi - (MAX_EVENTS + z * root + (z * z + 2.0) / 3.0))
               < 0.1)
    check_true("a count above the cap is rejected",
               bool(_raises(garwood_limits, MAX_EVENTS + 1)))

    # 7. Rate ratio: published R poisson.test output (Posit Community thread
    #    "2 sample Poisson Test"): counts 9,983 v 10,291 over equal exposure.
    ratio, lo, hi, p = _ratio_exact(10291, 40.0, 9983, 40.0, 0.95)
    check("rate ratio (R poisson.test)", ratio, 0.9700709, 5.1e-8)
    check("rate ratio 95% lower (R poisson.test)", lo, 0.9436314, 5.1e-8)
    check("rate ratio 95% upper (R poisson.test)", hi, 0.9972484, 5.1e-8)
    check("rate ratio p-value (R poisson.test)", p, 0.03107, 5.1e-6)

    # 8. Clopper-Pearson closed forms and term-by-term binomial sums.
    check("Clopper-Pearson upper, 0 of 10: 1 - 0.025^(1/10)",
          1.0 - beta_quantile(10, 1, 0.025), 1.0 - 0.025 ** 0.1, 1e-12)
    check("Clopper-Pearson lower, 10 of 10: 0.025^(1/10)",
          beta_quantile(10, 1, 0.025), 0.025 ** 0.1, 1e-12)
    for xa, ta, xb, tb in ((14, 1250000.0, 9, 1200000.0),
                           (3, 210000.0, 44, 4200000.0),
                           (250, 9.0e6, 310, 8.5e6)):
        n = xa + xb
        _, lo, hi, p = _ratio_exact(xa, ta, xb, tb, 0.95)
        pi_lo = lo * tb / (ta + lo * tb)
        pi_hi = hi * tb / (ta + hi * tb)
        tag = f"{xa} in {ta:,.0f} h v {xb} in {tb:,.0f} h"
        check(f"summed binomial upper tail at ratio lower limit, {tag}",
              _binom_tails_by_sum(xb, n, pi_lo)[1], 0.025, 1e-9)
        check(f"summed binomial lower tail at ratio upper limit, {tag}",
              _binom_tails_by_sum(xb, n, pi_hi)[0], 0.025, 1e-9)
        tails = _binom_tails_by_sum(xb, n, tb / (ta + tb))
        check(f"p-value v summed binomial tails, {tag}",
              p, min(1.0, 2.0 * min(tails)), 1e-9)
        check_true(f"p < 0.05 exactly when the interval excludes 1, {tag}",
                   (p < 0.05) == (lo > 1.0 or hi < 1.0))

    # 9. Edge cases for the ratio.
    ratio, lo, hi, p = _ratio_exact(0, 1.0e6, 0, 1.0e6, 0.95)
    check_true("no events in either period: ratio undefined, p = 1",
               ratio is None and lo == 0.0 and hi is None and p == 1.0)
    ratio, lo, hi, p = _ratio_exact(0, 1.0e6, 5, 1.0e6, 0.95)
    check_true("no events in A: ratio undefined, upper limit unbounded",
               ratio is None and hi is None and lo > 0.0)
    check("5 v 0 events, equal hours: p = 2 x 0.5^5", p, 0.0625, 1e-12)
    ratio, lo, hi, p = _ratio_exact(5, 1.0e6, 0, 1.0e6, 0.95)
    check_true("no events in B: ratio 0, lower limit 0, finite upper limit",
               ratio == 0.0 and lo == 0.0 and hi is not None)

    # 10. Funnel: a unit is outside a limit exactly when its summed Poisson
    #     tail is below (1 - level)/2, when its own exact interval excludes
    #     the target, and when its count is beyond the interpolated limit.
    for expected in (0.4, 1.26, 1.8, 3.7, 9.0, 25.2, 140.0):
        for _, level in FUNNEL_LEVELS:
            tail = (1.0 - level) / 2.0
            lower, upper = funnel_count_limits(expected, level)
            agree = True
            for k in range(0, int(expected * 3) + 12):
                s_low, s_high = _poisson_tails_by_sum(k, expected)
                g_lo, g_hi = garwood_limits(k, level)
                high_flag = s_high < tail
                low_flag = s_low < tail
                agree &= high_flag == (k >= upper)
                agree &= low_flag == (lower is not None and k <= lower)
                agree &= high_flag == (g_lo > expected)
                agree &= low_flag == (g_hi < expected)
                agree &= abs(poisson_upper_tail(k, expected) - s_high) < 1e-12
                agree &= abs(poisson_lower_tail(k, expected) - s_low) < 1e-12
            check_true(f"funnel {level * 100:g}% limits consistent with "
                       f"summed tails and exact intervals, expected "
                       f"{expected:g}", agree)
    check_true("funnel lower limit absent when e^-expected >= 0.025",
               funnel_count_limits(3.68, 0.95)[0] is None
               and funnel_count_limits(3.70, 0.95)[0] is not None)
    check_true("funnel upper limit between the two whole counts that "
               "bracket the tail (expected 25.2, 95%: 35 < limit <= 36)",
               35.0 < funnel_count_limits(25.2, 0.95)[1] <= 36.0)

    # 11. End to end: the docstring examples.
    r = rate_interval(9, 1200000.0)
    check_true("ci example: 9 in 1,200,000 h -> 7.5 (3.43 to 14.24)",
               (r["rate"], r["rate_ci_lower"], r["rate_ci_upper"])
               == (7.5, 3.43, 14.24))
    r = rate_interval(0, 500000.0, 0.99, 200000.0)
    check_true("ci example: 0 in 500,000 h, 99%, basis 200,000 -> 0.0 "
               "(0.0 to 2.12), basis reported as 200000",
               (r["rate"], r["rate_ci_lower"], r["rate_ci_upper"],
                r["basis_hours"], r["confidence_level"])
               == (0.0, 0.0, 2.12, 200000, 0.99)
               and isinstance(r["basis_hours"], int))
    r = compare_rates(14, 1250000.0, 9, 1200000.0)
    check_true("compare example: ratio 0.6696, interval 0.25567 to 1.66102 "
               "printed outward as 0.2556 to 1.662, change -33.0% (-74.5% to "
               "+66.2%), p 0.4628, no detectable difference",
               (r["rate_ratio"], r["rate_ratio_ci_lower"],
                r["rate_ratio_ci_upper"], r["change_pct"],
                r["change_pct_ci_lower"], r["change_pct_ci_upper"],
                r["p_value"], r["detectable_difference"])
               == (0.6696, 0.2556, 1.662, -33.0, -74.5, 66.2, 0.4628, False))
    r = funnel([("A", 3, 210000.0), ("B", 44, 4200000.0),
                ("C", 0, 300000.0)], target_rate=6.0)
    check_true("funnel example: A inside, B outside 99.8% (high), C inside",
               [(u["flag"], u["direction"]) for u in r["results"]]
               == [("inside", None), ("outside_99_8", "high"),
                   ("inside", None)])
    check_true("funnel example: dispersion against the pooled rate, not the "
               "supplied 6.0 (mean z^2 1.16, chi-square 3.49 on 2 df, "
               "p = e^(-3.488/2) = 0.1748)",
               (r["dispersion_ratio"], r["pearson_chi_square"],
                r["dispersion_df"], r["dispersion_p_value"])
               == (1.16, 3.49, 2, 0.1748))

    # 12. Non-default confidence levels flow through ci and compare.
    r = rate_interval(10, 1.0e6, 0.99)
    check_true("ci at 99%: 10 in 1,000,000 h -> 3.72 to 21.4 (Hanley)",
               (r["rate_ci_lower"], r["rate_ci_upper"], r["confidence_level"])
               == (3.72, 21.4, 0.99))
    r99 = compare_rates(14, 1250000.0, 9, 1200000.0, 0.99)
    one = rate_interval(14, 1250000.0, 0.99)
    _, lo99, hi99, _ = _ratio_exact(14, 1250000.0, 9, 1200000.0, 0.99)
    check_true("compare at 99%: side intervals and ratio limits use 99%",
               (r99["a"]["rate_ci_lower"], r99["a"]["rate_ci_upper"])
               == (one["rate_ci_lower"], one["rate_ci_upper"])
               and r99["rate_ratio_ci_lower"] <= lo99 < 0.2556
               and r99["rate_ratio_ci_upper"] >= hi99 > 1.661
               and r99["reading"].startswith("No detectable difference at "
                                             "the 99% level"))

    # 13. Compare: outward rounding, verdict agreement, readings, floors.
    r = compare_rates(42, 1.0e6, 25, 1.0e6)
    check_true("42 v 25 LTIs: detectable, printed upper limit below 1 "
               "(0.9996), change limit below 0, p below 0.05",
               r["detectable_difference"]
               and r["rate_ratio_ci_upper"] == 0.9996
               and r["change_pct_ci_upper"] < 0.0 and r["p_value"] < 0.05
               and "lower" in r["reading"])
    r = compare_rates(7, 1.0e6, 0, 1.0e6)
    check_true("7 v 0: ratio 0, change -100%, p = 2 x 0.5^7 = 0.015625, "
               "rate B lower",
               (r["rate_ratio"], r["rate_ratio_ci_lower"], r["change_pct"],
                r["change_pct_ci_lower"]) == (0.0, 0.0, -100.0, -100.0)
               and abs(r["p_value"] - 0.015625) <= 5.1e-6
               and r["detectable_difference"]
               and r["reading"].startswith("Rate B is lower"))
    r = compare_rates(0, 1.0e6, 7, 1.0e6)
    check_true("0 v 7: ratio undefined, upper unbounded, rate B higher",
               r["rate_ratio"] is None and r["rate_ratio_ci_upper"] is None
               and r["change_pct"] is None
               and r["reading"].startswith("Rate B is higher"))
    r = compare_rates(4, 1.0e6, 3, 4.0e6)
    check_true("4 in 1,000,000 h v 3 in 4,000,000 h: p 0.06669, not "
               "detectable (docstring contrast with R)",
               r["p_value"] == 0.06669 and not r["detectable_difference"])
    r = compare_rates(5000, 1.0e6, 1, 1.0e6)
    check_true("5,000 v 1: small ratio kept at 4 significant figures, not "
               "collapsed to 0",
               r["rate_ratio"] == 0.0002 and 0.0 < r["rate_ratio_ci_lower"]
               < 0.0002 < r["rate_ratio_ci_upper"] < 0.002)
    r = compare_rates(10000000, 1.0e6, 9000000, 1.0e6)
    check_true("10,000,000 v 9,000,000: p below the floor reported as 1e-300",
               r["p_value"] == P_FLOOR and r["detectable_difference"])
    check_true("outward rounding: 0.99958 up -> 0.9996; 0.9999996 up stays "
               "below 1; 1.00004 down stays above 1; -0.042% up -> -0.04%",
               _outward(0.99958, True, sig=4, pivot=1.0) == 0.9996
               and _outward(0.9999996, True, sig=4, pivot=1.0) < 1.0
               and _outward(1.00004, False, sig=4, pivot=1.0) > 1.0
               and _outward(-0.042, True, places=1, pivot=0.0) == -0.04
               and str(_outward(-0.01, True, places=1)) == "0.0")
    check_true("p-value figures: 0.049996 below 0.05 stays below 0.05; "
               "0.050004 shows 0.05",
               _p_out(0.049996, (0.05,)) < 0.05
               and _p_out(0.050004, (0.05,)) == 0.05)
    agree = True
    for xa in range(1, 61):
        for xb in range(0, xa + 1):
            exact = _ratio_exact(xa, 1.0e6, xb, 1.0e6, 0.95)
            f = _ratio_fields(*exact, 0.95, xa + xb)
            shown_excludes = (f["rate_ratio_ci_upper"] < 1.0
                              or f["rate_ratio_ci_lower"] > 1.0)
            pct_excludes = (f["change_pct_ci_upper"] < 0.0
                            or f["change_pct_ci_lower"] > 0.0)
            agree &= f["detectable_difference"] == shown_excludes
            agree &= f["detectable_difference"] == pct_excludes
            agree &= f["detectable_difference"] == (f["p_value"] < 0.05)
            agree &= f["rate_ratio_ci_lower"] <= exact[1]
            agree &= f["rate_ratio_ci_upper"] >= exact[2]
    check_true("A 1-60 v B 0-A events, equal hours: printed interval, change "
               "and p always agree with the verdict and contain the exact "
               "interval", agree)

    # 14. Funnel end to end: flags, counts, limits, tails and dispersion.
    r = funnel([("P", 10, 1.0e6), ("Q", 11, 1.0e6), ("R", 14, 1.0e6),
                ("S", 5, 1.0e6)], target_rate=5.0)
    rows = {u["unit"]: u for u in r["results"]}
    check_true("funnel P/Q/R/S at 5.0: flags inside, outside 95%, outside "
               "99.8%, inside; tails 0.03183, 0.0137, 0.000698, 0.5595",
               [(u["flag"], u["tail_probability"]) for u in r["results"]]
               == [("inside", 0.03183), ("outside_95", 0.0137),
                   ("outside_99_8", 0.000698), ("inside", 0.5595)]
               and rows["R"]["direction"] == "high"
               and rows["S"]["tail"] == "this many or more")
    check_true("funnel P/Q/R/S: 2 units outside 95% (99.8% included), 1 "
               "outside 99.8%",
               (r["units_outside_95"], r["units_outside_99_8"]) == (2, 1))
    check_true("funnel P/Q/R/S limits: 95% 0.68 to 10.3, 99.8% none to "
               "13.67, target 5.0 supplied",
               (rows["P"]["limit_95_lower"], rows["P"]["limit_95_upper"],
                rows["P"]["limit_99_8_lower"], rows["P"]["limit_99_8_upper"],
                r["target_rate"], r["target_source"])
               == (0.68, 10.3, None, 13.67, 5.0, "supplied"))
    check_true("funnel row carries its 95% exact interval (P: 4.8 to 18.39, "
               "Hanley)",
               (rows["P"]["rate_ci95_lower"], rows["P"]["rate_ci95_upper"])
               == (4.8, 18.39))
    r = funnel([("X", 2, 1.0e6), ("Y", 6, 1.0e6), ("Z", 4, 1.0e6)])
    check_true("pooled dispersion, 2/6/4 events in equal hours: chi-square "
               "2.0 on 2 df, mean z^2 0.67, p = e^-1 = 0.3679",
               (r["target_rate"], r["target_source"], r["pearson_chi_square"],
                r["dispersion_df"], r["dispersion_ratio"],
                r["dispersion_p_value"])
               == (4.0, "pooled", 2.0, 2, 0.67, 0.3679))
    r = funnel([("X", 2, 1.0e6), ("Y", 6, 1.0e6), ("Z", 4, 1.0e6)],
               target_rate=9.0)
    check_true("supplied target does not change the dispersion statistics",
               (r["pearson_chi_square"], r["dispersion_ratio"])
               == (2.0, 0.67))
    r = funnel([("A", 1, 1.0e6), ("B", 9, 3.0e6)])
    check_true("pooled target = total events / total hours (2.5, not the "
               "mean of unit rates 2.0)", r["target_rate"] == 2.5)
    r = funnel([("A", 0, 1.0e6), ("B", 0, 2.0e6)], target_rate=3.0)
    check_true("one unit or no events: dispersion not computed",
               r["dispersion_ratio"] is None
               and funnel([("A", 3, 1.0e6)])["dispersion_ratio"] is None)
    check_true("funnel errors: bad target, no events, blank and repeated "
               "names",
               "Target rate" in _raises(funnel, [("A", 0, 1000.0)], -3.0)
               and "Target rate" in _raises(funnel, [("A", 1, 1000.0)],
                                            math.nan)
               and "Target rate" in _raises(funnel, [("A", 1, 1000.0)],
                                            math.inf)
               and "No events" in _raises(funnel, [("A", 0, 1000.0)])
               and "name" in _raises(funnel, [(" ", 1, 1000.0)])
               and "more than once" in _raises(
                   funnel, [("A", 1, 1000.0), ("A", 2, 1000.0)]))
    check_true("a result outside floating-point range is refused, not "
               "reported as Infinity",
               "floating-point" in _raises(rate_interval, 5, 1e-310))

    # 15. Input parsing.
    check_true("--confidence: 95 -> 0.95, 99.8 -> 0.998, 99.9 -> 0.999, "
               "0.9 -> 0.9",
               [_value(_level_arg, v) for v in ("95", "99.8", "99.9", "0.9")]
               == [0.95, 0.998, 0.999, 0.9])
    check_true("--confidence rejects 1, 5, 0.3, 100, 1.0, nan, text",
               all(_raises(_level_arg, v) for v in
                   ("1", "5", "0.3", "100", "1.0", "nan", "abc")))
    check_true("counts: 3, 1,234, 1_000, 3.0, 123456789 read exactly",
               [_value(_whole, v) for v in
                ("3", "1,234", "1_000", "3.0", "123456789")]
               == [3, 1234, 1000, 3, 123456789])
    check_true("counts reject 3.5, -1, inf, 1e400, nan, 1,5, text and a "
               "count above the cap",
               all(_raises(_whole, v) for v in
                   ("3.5", "-1", "inf", "1e400", "nan", "1,5", "abc",
                    str(MAX_EVENTS + 1))))
    check_true("hours: 1,200,000 and 1.2e6 accepted; 1,5, 12,00, inf, nan "
               "rejected",
               _value(_number, "1,200,000") == _value(_number, "1.2e6")
               == 1200000.0
               and all(_raises(_number, v) for v in
                       ("1,5", "12,00", "inf", "nan", "")))
    check_true("--unit: name with colons and thousands separators parsed; "
               "missing name or field rejected",
               _value(_parse_unit, "Site: North:3:1,200,000")
               == ("Site: North", 3, 1200000.0)
               and _raises(_parse_unit, ":3:100")
               and _raises(_parse_unit, "A:3"))
    with tempfile.TemporaryDirectory() as tmp:
        def csv_file(name, body):
            path = os.path.join(tmp, name)
            with open(path, "w", encoding="utf-8-sig", newline="") as f:
                f.write(body)
            return path
        good = csv_file("good.csv", " Unit ,EVENTS,Hours\r\n"
                        "North,3,\"1,200,000\"\r\nSouth,4,3000000\r\n")
        check_true("CSV with BOM, mixed-case headers and a quoted thousands "
                   "separator",
                   _value(_read_units_csv, good)
                   == [("North", 3, 1200000.0), ("South", 4, 3000000.0)])
        errors = {
            "unquoted thousands separator": ("unit,events,hours\n"
                                             "North,3,1,200,000\n",
                                             "more fields"),
            "blank unit name": "unit,events,hours\n  ,3,1000\n",
            "repeated unit name": ("unit,events,hours\nA,1,1000\n"
                                   "A,2,1000\n", "line 2"),
            "missing column": ("unit,events\nA,1\n", "missing hours"),
            "empty file": ("", "header"),
        }
        for what, spec in errors.items():
            body, needle = spec if isinstance(spec, tuple) else (spec,
                                                                 "missing")
            message = _raises(_read_units_csv, csv_file("bad.csv", body))
            check_true(f"CSV rejected: {what}", needle in message)

    # 16. The command line: sub-command usage on errors, strict JSON.
    code, out, err = _run_cli("ci", "--events", "inf", "--hours", "1000")
    check_true("CLI: infinite count -> exit 2 with the ci usage line",
               code == 2 and "rate_confidence.py ci" in err
               and "Traceback" not in err)
    code, out, err = _run_cli("ci", "--events", "5", "--hours", "1e-310")
    check_true("CLI: out-of-range result -> exit 2, no Infinity in output",
               code == 2 and "Infinity" not in out)
    code, out, err = _run_cli("--quiet", "ci", "--events", "1",
                              "--hours", "1000")
    check_true("CLI: --quiet without --self-test -> exit 2",
               code == 2 and "--quiet" in err)
    code, out, err = _run_cli("funnel", "--unit", "A:0:1000",
                              "--target-rate", "-3")
    check_true("CLI: negative target rate -> exit 2 naming the target rate",
               code == 2 and "rate_confidence.py funnel" in err
               and "Target rate" in err)
    code, out, err = _run_cli("compare", "--events-a", "42", "--hours-a",
                              "1,000,000", "--events-b", "25", "--hours-b",
                              "1000000", "--confidence", "95")
    try:
        parsed = _strict_json(out)
    except ValueError:
        parsed = {}
    check_true("CLI: compare 42 v 25 -> strict JSON, upper limit 0.9996",
               code == 0 and parsed.get("rate_ratio_ci_upper") == 0.9996)
    code, out, err = _run_cli("compare", "--events-a", "42", "--hours-a",
                              "1e6", "--events-b", "25", "--hours-b", "1e6",
                              "--text")
    check_true("CLI text: 42 v 25 prints '0.3476 to 0.9996', '-40.5%' and "
               "'-0.04%', and says B is lower",
               code == 0 and "CI 0.3476 to 0.9996   p = 0.0498" in out
               and "Change B v A -40.5%   CI -65.3% to -0.04%" in out
               and "Rate B is lower" in out)
    code, out, err = _run_cli("funnel", "--text", "--unit", "North:3:1200000",
                              "--unit", "South:4:3000000", "--unit",
                              "East:25:3300000")
    check_true("CLI text: funnel footnote explains a 99.8%-only 'none' "
               "lower limit, and counts read '3 units, 32 events'",
               code == 0 and "none to 11.56" in out
               and "none = no lower limit" in out
               and "3 units, 32 events" in out)

    print(f"{count - len(failures)} of {count} checks passed"
          + ("" if not failures else f"; {len(failures)} FAILED"))
    return len(failures)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(
        description="WHS rate confidence calculator: exact Poisson interval, "
                    "two-rate comparison, funnel-plot limits. Exit status 0 "
                    "on success, 1 on a self-test failure, 2 on a usage or "
                    "input error.")
    p.add_argument("--self-test", action="store_true",
                   help="Check the calculator against published reference "
                        "values and exit")
    p.add_argument("--quiet", action="store_true",
                   help="With --self-test: print failures and summary only")

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--basis", type=_number_arg("Basis"),
                        default=DEFAULT_BASIS,
                        help="Rate basis in hours (default 1,000,000; "
                             "US convention 200,000)")
    fmt = common.add_mutually_exclusive_group()
    fmt.add_argument("--json", action="store_true",
                     help="JSON output (the default)")
    fmt.add_argument("--text", action="store_true",
                     help="Plain-text summary instead of JSON")
    level = argparse.ArgumentParser(add_help=False)
    level.add_argument("--confidence", type=_level_arg, default=DEFAULT_LEVEL,
                       help="Confidence level, 0.95 or 95, from 50%% to below "
                            "100%% (default 0.95)")

    sub = p.add_subparsers(dest="command", metavar="{ci,compare,funnel}")
    parsers = {}

    c = sub.add_parser("ci", parents=[common, level],
                       help="Exact Poisson (Garwood) interval for one rate")
    c.add_argument("--events", type=_count_arg, required=True,
                   help="Number of events (injuries, incidents) in the period")
    c.add_argument("--hours", type=_number_arg("Hours"), required=True,
                   help="Hours worked for the period")
    parsers["ci"] = c

    c = sub.add_parser("compare", parents=[common, level],
                       help="Rate ratio B / A with exact test and interval")
    c.add_argument("--events-a", type=_count_arg, required=True,
                   help="Events in A (baseline period or unit)")
    c.add_argument("--hours-a", type=_number_arg("Hours"), required=True,
                   help="Hours worked in A")
    c.add_argument("--events-b", type=_count_arg, required=True,
                   help="Events in B (comparison period or unit)")
    c.add_argument("--hours-b", type=_number_arg("Hours"), required=True,
                   help="Hours worked in B")
    parsers["compare"] = c

    c = sub.add_parser("funnel", parents=[common],
                       help="Funnel-plot limits (95%% and 99.8%%) for units")
    c.add_argument("--unit", action="append", default=[],
                   metavar="NAME:EVENTS:HOURS",
                   help="One unit; repeat for each unit")
    c.add_argument("--csv", help="Units CSV: unit,events,hours")
    c.add_argument("--target-rate", type=_number_arg("Target rate"),
                   default=None,
                   help="Group or benchmark rate at the basis (default: "
                        "pooled rate of the units supplied)")
    parsers["funnel"] = c

    a = p.parse_args()

    if a.self_test:
        if a.command:
            p.error("--self-test runs on its own, without a sub-command")
        return 1 if self_test(verbose=not a.quiet) else 0
    if a.quiet:
        p.error("--quiet works only with --self-test")
    if not a.command:
        p.error("choose a sub-command (ci, compare or funnel) or --self-test")

    cmd = parsers[a.command]
    try:
        if a.command == "ci":
            result = rate_interval(a.events, a.hours, a.confidence, a.basis)
            text = _text_ci
        elif a.command == "compare":
            result = compare_rates(a.events_a, a.hours_a, a.events_b,
                                   a.hours_b, a.confidence, a.basis)
            text = _text_compare
        else:
            if a.csv and a.unit:
                cmd.error("provide units with --unit or --csv, not both")
            if not a.csv and not a.unit:
                cmd.error("provide units with --unit NAME:EVENTS:HOURS "
                          "(repeatable) or --csv")
            units = (_read_units_csv(a.csv) if a.csv
                     else [_parse_unit(u) for u in a.unit])
            result = funnel(units, a.target_rate, a.basis)
            text = _text_funnel
        rendered = (text(result) if a.text
                    else json.dumps(result, indent=2, allow_nan=False))
    except (ValueError, OSError, OverflowError, ArithmeticError,
            csv.Error) as exc:
        cmd.error(str(exc))

    print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
