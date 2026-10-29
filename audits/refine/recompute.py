#!/usr/bin/env python3
"""Recompute every arithmetic point in the refine.ink audit comments (step S29).

Usage: python3 recompute.py

Each check takes the numbers exactly as the Hub page (or its PDF) prints them,
recomputes the stated result, and compares it with (a) the paper's figure and
(b) the audit's claim. Nothing here is a new estimate: the checks only test
whether the printed figures follow from the printed inputs.

Exit status is 0 when every check ran; a check's verdict ("paper wrong",
"audit wrong", ...) is a finding, not a failure.
"""
import math, sys

results = []  # (id, what, paper figure, recomputed, audit claim, verdict)

def check(cid, what, paper, recomputed, audit, verdict):
    results.append((cid, what, paper, recomputed, audit, verdict))

def amort_payment(P, annual_rate, years):
    r = annual_rate / 12; n = years * 12
    return P * r / (1 - (1 + r) ** -n)

def payoff_years(P, annual_rate, payment):
    r = annual_rate / 12
    if payment <= P * r:
        return math.inf
    return -math.log(1 - r * P / payment) / math.log(1 + r) / 12

# B001, B053: steady state of p' = p(1 - le) + (1 - p) lf  ->  p* = lf / (le + lf)
lf = 0.02
p_cco, p_ptf = lf / (0.15 + lf), lf / (0.25 + lf)
check("B001", "steady-state poverty p* (CCO; with PTF)", "theorem: p* < 0.05",
      f"{p_cco:.3f}; {p_ptf:.3f}", "0.118; 0.074", "paper wrong (proof refutes theorem); audit right")
# The page's convergence time T = ln(0.05/p0)/ln(1 - le - lf) ~ 15 years ignores p*: with p* > 0.05
# the rate never reaches 0.05. The formula only gives 15 years if the start rate p0 is about 82%.
p0 = 0.05 / math.exp(15 * math.log(1 - 0.15 - lf))
check("B053", "start rate p0 the '15 years to 5%' formula implies", "15 years to below 5%",
      f"p0 = {p0:.2f}; and with p* = {p_cco:.3f} the 5% level is never reached", "5% is transient, not p*",
      "paper wrong; audit right on p*, but the audit's 'passes through 5%' is also wrong (the path falls toward 11.8% from above and never reaches 5%)")

# B031: half-life
le = 0.15
disc = math.log(0.5) / math.log(1 - le - lf); cont = math.log(2) / (le + lf)
check("B031", "half-life to steady state (years)", "4.1 (discrete formula shown)",
      f"discrete {disc:.2f}; continuous {cont:.2f}", "3.72 discrete; 4.1 = continuous", "paper wrong; audit right")

# B002: midpoint (arc) elasticities, Table 5.4 (economic-modeling-simulation.html), +/-25% => dX/X = 0.5
rows = [("Basic unit amount", 2.8, 1.2, -0.71), ("Participation rate", 3.4, 1.1, -0.89),
        ("PTF uptake", 2.6, 1.4, -0.52), ("Max octave", 2.4, 1.8, -0.31), ("Quality assessment", 2.3, 1.9, -0.19)]
for name, lo, hi, printed in rows:
    e = ((hi - lo) / ((hi + lo) / 2)) / 0.5
    check("B002", f"arc elasticity, {name}", f"{printed}", f"{e:.2f}", "about -1.6 (first row); 'similar gaps' in others",
          "paper wrong; audit right")

# B009: drug-policy cost table (sec 4.1) totals
cols = {"enforcement": 1210, "incarceration": 1047, "social": 857, "opportunity": 1502}
check("B009", "sum of the four cost columns ($B)", "prose: $1.52 trillion", f"{sum(cols.values()):,}",
      "table sums to $4,616B", "paper wrong; audit right")

# B025, B050: open-economy multiplier M = 1 / (1 - c(1 - t) + m)
c, t, m = 0.85, 0.25, 0.15
M = 1 / (1 - c * (1 - t) + m)
check("B025", "multiplier with c=0.85, t=0.25, m=0.15", "2.86", f"{M:.2f} (denominator {1 - c*(1-t) + m:.4f}; 2.86 needs 0.35)",
      "1.95", "paper wrong; audit right")
check("B050", "same multiplier, second instance", "2.86", f"{M:.2f}", "1.95", "paper wrong; audit right")

# B032: $12,000 x 250M adults vs 2023 nominal GDP (BEA, about $27.4-27.7T depending on vintage)
ubi = 12_000 * 250e6
for gdp in (27.36e12, 27.72e12):
    check("B032", f"$3T as share of 2023 GDP (${gdp/1e12:.2f}T)", "14%", f"{ubi/gdp:.1%}", "about 11%", "paper wrong; audit right")

# B033, B061: inflation reductions, Table 5.2 (dual-currency-inflation PDF)
base = (2.5, 2.5, 28.0); ubi_t = (8.3, 6.7, 72.4); cco = (3.8, 3.1, 35.2); ccoptf = (3.2, 2.8, 31.5)
labels = ("year 1", "year 5", "10-yr cumulative")
for lab, b, u, c1, c2 in zip(labels, base, ubi_t, cco, ccoptf):
    check("B033", f"CCO vs UBI inflation, {lab}", "65% lower",
          f"total {1 - c1/u:.0%}; excess over baseline {1 - (c1-b)/(u-b):.0%}", "50-55% total, 78-86% excess", "paper wrong; audit right")
    check("B061", f"CCO+PTF vs UBI inflation, {lab}", "65% lower", f"total {1 - c2/u:.0%}", "61%, 58%, 57%", "paper wrong; audit right")

# B040: Table 7.1 '1.3% annual' = CCO year-1 minus baseline
check("B040", "CCO year-1 inflation minus baseline", "1.3% annual", f"{3.8 - 2.5:.1f} points", "1.3 is the year-1 increment",
      "audit right (labelling only)")

# B047: GiveDirectly 0.1% inflation per 1% of GDP applied to the paper's UBI
check("B047", "price effect implied by 0.1%/1% GDP at $3T", "'significant inflation'", f"{0.1 * ubi/27.36e12*100:.1f}%",
      "about 1%", "audit right (tension, wording)")

# B007, B034: merchant multiplier M = Base x (Ref/Offered)^alpha, example: $12 lunch at 4 BU, '3x'
for a in (0.0, 0.3, 0.5, 1.0):
    Mm = 3 * (12 / 4) ** a
    check("B034", f"multiplier with base 3, ratio 3, alpha {a}", "3x and revenue neutral",
          f"M = {Mm:.2f}; merchant gets 4 x M = {4*Mm:.2f} for a $12 item", "neutral only if alpha = 0",
          "audit right" if a == 0.0 else "not neutral")
check("B007", "alpha implied if Base Rate = 1 and M = 3 at ratio 3", "alpha 0.3-0.5", f"{math.log(3)/math.log(3):.1f}",
      "about 1", "paper inconsistent; audit right")

# B030: minimal-integration budget items vs headline
items = [5, 3, 2, 1.5, 0.5]
check("B030", "investment line items ($B)", "$12.5B (= 250 x $50M)", f"{sum(items):.1f}", "$12.0B", "paper inconsistent; audit right")

# B004: community wealth $12-20B per year on a $12.5B one-time outlay
check("B004", "implied annual return on $12.5B", "$12-20B a year", f"{12/12.5:.0%}-{20/12.5:.0%}", "about 100-160%",
      "audit right (no derivation)")

# B017: five-year cost
flat = 0.5 + 2 + 0.3 + 5 * 1.2
check("B017", "five-year total with $1.2B a year flat ($B)", "$8.5B", f"{flat:.1f}",
      "$8.8B flat; $8.5B with a ramp", "paper inconsistent; the audit's ramp is its own assumption, not in the paper")

# B094: drug policy 5-year cumulative savings, same method as the 2-year line (2 x 83 - 25 = 141)
two, five = 2 * (45 + 38) - 25, 5 * (45 + 38) - 25
check("B094", "2-year and 5-year cumulative savings ($B)", "141; 385", f"{two}; {five}", "390", "paper wrong by $5B; audit right")

# B097: NPV of the CCO stream
npv_printed = -300 + sum(180 * 1.1**t / 1.05**t for t in range(1, 11))
npv_lag = -300 + sum(180 * 1.1**(t-1) / 1.05**t for t in range(1, 11))
check("B097", "NPV_CCO, formula as printed (1.1^t)", "$1,847", f"${npv_printed:,.0f}", "about $2,040",
      "paper wrong; audit's arithmetic right but its units wrong ('$2.04 million')")
check("B097", "NPV_CCO with growth from year 2 (1.1^(t-1))", "$1,847", f"${npv_lag:,.0f}", "$1,847",
      "audit wrong: its explanation gives $1,832, not $1,847")
for name, cost, flow, years, printed in (("MF", 150, 50, 10, 236), ("CCT", 500, 120, 5, 19), ("Aid", 1000, 80, 10, -382)):
    v = -cost + sum(flow / 1.05**t for t in range(1, years + 1))
    check("B097", f"NPV_{name} (same table)", f"${printed}", f"${v:,.0f}", "-", "paper right (to rounding)" if abs(v - printed) <= 1 else "paper wrong")

# B073: drug-related incarceration, two metrics (drug-policy-reform sec 5.3 rate; sec 9.1 incarceration-years)
check("B073", "rate 450 -> 140 per 100k; incarceration-years 45M -> 7M (38M fewer)", "85% reduction",
      f"rate {1 - 140/450:.0%}; years {38/45:.0%}", "69% (rate) vs 85% (years)", "audit right: two metrics, unlabelled")

# B103, B127: 85% -> 98%
check("B103", "percentage-point gain 85% -> 98%", "15", f"{98-85}", "13", "paper wrong; audit right")
check("B127", "same, second instance", "15", f"{98-85}", "13", "paper wrong; audit right")

# B052, B096: '2.5x efficiency' vs 2.5x wealth and 40% cost reduction (Table 6.2)
check("B052", "wealth per dollar if 2.5x wealth at 60% of cost", "2.5x efficiency", f"{2.5/0.6:.2f}x", "about 4.2x",
      "audit right (metric undefined)")

# B079: scaling 5x HUD -> 10x HUD by pathway
for p, a, b in (("pay-in", 1.5, 3.0), ("buy-in", 0.75, 2.0), ("sell-in", 0.5, 1.0), ("earn-in", 0.25, 0.5)):
    check("B079", f"growth factor, {p}", "-", f"{b/a:.2f}x", "buy-in 2.7x, others 2x", "audit right")

# B010: earn-in credits, monthly earning 200-1,000 credits vs timeline
for target, months in ((100, "2-4"), (500, "12-18"), (1000, "24-36"), (2000, "48-60")):
    check("B010", f"months to {target} credits at 200-1,000 a month", f"{months} months",
          f"{target/1000:.1f}-{target/200:.1f}", "much faster than stated", "paper inconsistent; audit right")

# B062: carbon components -31, -18, -24, -19 vs total -45%
comp = (0.31, 0.18, 0.24, 0.19)
check("B062", "largest weighted average of the components", "45%", f"{max(comp):.0%} (any shares summing to 1)",
      "not reproducible", "paper unexplained; audit right")
check("B062", "components compounded, 1 - prod(1 - x)", "45%", f"{1 - math.prod(1 - x for x in comp):.0%}",
      "not reproducible", "neither aggregation gives 45%")

# B023: V(n) = 0.3 n^2 + 0.7 n ln n is convex (V'' = 0.6 + 0.7/n > 0)
check("B023", "V''(n) at n = 1, 100, 1e6", "'diminishing returns above 80%'",
      ", ".join(f"{0.6 + 0.7/n:.3f}" for n in (1, 100, 1e6)), "strictly convex", "audit right")

# B076: Stability = 1 - Var/Mean changes with units (metric in $ vs $1,000)
x = [40_000, 50_000, 60_000]
def stab(v):
    mu = sum(v) / len(v); var = sum((a - mu) ** 2 for a in v) / len(v); return 1 - var / mu
check("B076", "Stability for the same data in $ and in $1,000", "unit-free index",
      f"{stab(x):,.1f} vs {stab([a/1000 for a in x]):.2f}", "not unit-free", "audit right")

# B028: Portugal drug deaths (Greenwald 2009 table as the audit quotes it: 131 -> 20)
check("B028", "fall in drug-related deaths 131 -> 20", "95%", f"{1 - 20/131:.0%}",
      "85%", "audit right on its quoted figures (source to be opened, S23)")

# B011: Bristol Pound GBP 5 billion over 2012-2021 with ~2,000 individual users
check("B011", "spending per individual participant, GBP", "GBP 5 billion total", f"{5e9/2000:,.0f}",
      "about GBP 5 million total", "paper implausible by ~1,000x; audit right (source to be opened, S23)")

# B044: implied dollar weights for deaths prevented (v) and incarceration-years (y)
def weights(c1, g1, d1, i1, n1, c2, g2, d2, i2, n2):
    # n = g + d*v + i*y - c  for both scenarios; solve the 2x2 system
    a1, b1, r1 = d1, i1, n1 + c1 - g1
    a2, b2, r2 = d2, i2, n2 + c2 - g2
    det = a1 * b2 - a2 * b1
    return (r1 * b2 - r2 * b1) / det, (a1 * r2 - a2 * r1) / det
v, y = weights(0.836e12, 1.2e12, 2.0e6, 30e6, 3.9e12, 0.786e12, (2.1 + 0.89) * 1e12, 2.3e6, 38e6, 5.0e12)
check("B044", "common weights implied by the HTML table (per death; per incarceration-year)", "net $3.9T; $5.0T",
      f"${v/1e6:.1f}M; ${y/1e3:,.0f}k", "weights differ by scenario", "paper inconsistent: one set of weights needs a negative value on incarceration")
v, y = weights(0.836e12, 1.2e12, 2.0e6, 30e6, 3.9e12, 0.450e12, (2.1 + 0.89) * 1e12, 2.3e6, 38e6, 4.7e12)
check("B044", "same, with the PDF's $450B and $4.7T", "net $3.9T; $4.7T", f"${v/1e6:.1f}M; ${y/1e3:,.0f}k",
      "weights differ by scenario", "paper inconsistent")

# B005, B038: five-homeowner avalanche example (pth-independent-financing, sec 2.2-2.3)
loans = [("A", 180_000, .065, 1400, 18), ("B", 220_000, .058, 1650, 20), ("C", 150_000, .072, 1200, 15),
         ("D", 200_000, .060, 1500, 19), ("E", 160_000, .068, 1300, 16)]
for n_, P, r, pay, yrs in loans:
    check("B005", f"homeowner {n_}: payment for the stated term; years at the stated payment", f"${pay:,}; {yrs} y",
          f"${amort_payment(P, r, yrs):,.0f}; {payoff_years(P, r, pay):.1f} y", "payments do not amortize", "audit right")
def simulate(avalanche):
    """Monthly amortization. Individual: each pays its own payment until paid off.
    Avalanche: the five keep paying $7,050 in total; every open loan gets its own payment,
    the rest (freed payments of loans already paid) goes to the highest-rate open loan."""
    bal = {k: P for k, P, *_ in loans}; rate = {k: r for k, _, r, *_ in loans}; pay = {k: p for k, _, _, p, _ in loans}
    total = sum(pay.values()); interest = 0.0; month = 0
    while any(b > 0.005 for b in bal.values()) and month < 1200:
        month += 1
        open_ = [k for k in bal if bal[k] > 0.005]
        for k in open_:
            i = bal[k] * rate[k] / 12; interest += i; bal[k] += i
        if not avalanche:
            for k in open_:
                bal[k] -= min(pay[k], bal[k])
            continue
        budget = total
        for k in open_:
            d = min(pay[k], bal[k]); bal[k] -= d; budget -= d
        for k in sorted(open_, key=lambda k: -rate[k]):
            d = min(budget, bal[k]); bal[k] -= d; budget -= d
    return interest, month / 12
i_ind, t_ind = simulate(False); i_av, t_av = simulate(True)
check("B005", "collective payoff time; interest saved by the avalanche", "10 years; $85,000+",
      f"{t_av:.1f} y; ${i_ind - i_av:,.0f} (individual payoff takes {t_ind:.1f} y)", "not verifiable from the paper",
      "paper not reproducible from its own table")
check("B038", "§9.2 vs §2.2 inputs (principal; rate; monthly)", "$950k; 6.2%; $7,500",
      f"${sum(l[1] for l in loans):,}; {sum(l[2] for l in loans)/5:.2%}; ${sum(l[3] for l in loans):,}",
      "the two examples do not match", "audit right")

# B095 (moot on the Hub now): 70-80% of $800-1,400 a month
check("B095", "annual equity at 70-80% of $800-1,400", "$6,000-10,000", f"${800*12*.7:,.0f}-{1400*12*.8:,.0f}",
      "6,720-13,440", "audit right on the arithmetic; its '60% net' rescue is not in the paper")

# B110 (moot on the Hub now): 3 x 1.618 and 4,800 x 4.85
check("B110", "3 x phi; $4,800 x 4.85", "4.85; $23,280", f"{3*1.618:.3f}; {4800*4.85:,.0f}", "label input vs output",
      "arithmetic right; audit right on labelling")

if __name__ == "__main__":
    w = sys.stdout.write
    for cid, what, paper, rec, audit, verdict in results:
        w(f"{cid}  {what}\n      paper: {paper} | recomputed: {rec} | audit: {audit}\n      -> {verdict}\n")
    w(f"\n{len(results)} checks ran.\n")
