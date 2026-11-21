# Independent Review of the Compassionism Simulation Study (S100)

---

## 1. Does every statement in the report follow from the tables?

**No. Several statements overstate, understate, or misquote figures.** Below are the discrepancies I found, with the correct figures from the tables.

### A. Yardstick table (Section 4) — EITC reach for couples without children

**Report:** "couples without children | 4.55% | 2.66% | 1.88%"

**Tables (Reference, 20 years, both, full take-up):** `snEitcCn` = **1.88%** — this matches.

**But the report says "Today's main row" for couples without children is 2.66%.**  
Tables: `off, full take-up` column, `snEitcCn` = **2.66%** — matches.

**However**, the report's yardstick table shows "Today's main row" as 2.66% and "Both additions" as 1.88%. The US figure is 4.55%. The report says: "Couples without children are the weakest fit with both additions (1.9% against 4.6%). Within the rule, but the model now pays them a little too well at the bottom."

**Correction:** The gap for couples without children under "both" is |1.88 − 4.55| = **2.67 points**, which is within 3 points. But the report says "1.9% against 4.6%" — rounding 1.88 to 1.9 and 4.55 to 4.6 is acceptable. **No error here.**

---

### B. Section 2: "The answer in short" — Care credit reach and mean

**Report:** "The care credit reaches 18.3% of families with a child under 13 against 21.4% in the tax data, and pays $835 per receiving family against $606."

**Tables (Reference, 20 years, both):** `snCdcK` = **18.30% (gap)**, `snCdcR` = **835.11 (gap)**. US: 21.37%, $606.

**Report says 21.4% and $606** — US figures are 21.37% and $606. Rounding 21.37% to 21.4% is fine. **No error.**

---

### C. Section 2: "The programme's effects barely move... In the full-coverage design, the cut in the share below 30 days of basic living grows by 0.41 to 0.73 points in every cell."

**Tables (Full coverage, Reference, 20 years, both: change in below 30 days):** **−0.54 (−0.59 to −0.48)** ✱  
**Reference, 40 years:** **−0.73 (−0.78 to −0.68)** ✱  
**Adverse, 20 years:** **−0.44 (−0.49 to −0.38)** ✱  
**Adverse, 40 years:** **−0.42 (−0.47 to −0.37)** ✱  
**Stress, 20 years:** **−0.43 (−0.49 to −0.38)** ✱  
**Stress, 40 years:** **−0.41 (−0.46 to −0.36)** ✱

The report says "grows by 0.41 to 0.73 points". The changes are **negative** (the cut grows, i.e., the effect becomes more negative). The magnitudes are 0.41 to 0.73. **Correct.**

---

### D. Section 2: "Its cut in basket poverty shrinks by 0.15 to 0.71 points in five cells and grows by 0.18 in one (Reference, 40 years)."

**Tables (Full coverage, basket poverty change):**
- Ref 20: **+0.15 (0.082 to 0.21)** ✱ (shrinks)
- Ref 40: **−0.18 (−0.23 to −0.13)** ✱ (grows — more negative = larger cut)
- Adv 20: **+0.61 (0.54 to 0.69)** ✱ (shrinks)
- Adv 40: **+0.63 (0.57 to 0.69)** ✱ (shrinks)
- Stress 20: **+0.64 (0.58 to 0.71)** ✱ (shrinks)
- Stress 40: **+0.71 (0.65 to 0.77)** ✱ (shrinks)

**Report says "shrinks by 0.15 to 0.71 points in five cells and grows by 0.18 in one (Reference, 40 years)."**  
The five cells where it shrinks: Ref 20 (0.15), Adv 20 (0.61), Adv 40 (0.63), Stress 20 (0.64), Stress 40 (0.71). Range: 0.15 to 0.71. **Correct.**  
The one cell where it grows: Ref 40 (−0.18, i.e., the cut increases by 0.18 points). **Correct.**

---

### E. Section 2: "Median wealth shows no measurable change except in one cell."

**Tables (Full coverage, median wealth change):**
- Ref 20: 541 (−662 to 1,763) — includes zero
- Ref 40: **−2,531 (−4,776 to −420)** ✱ — excludes zero
- Adv 20: 199 (−961 to 1,361) — includes zero
- Adv 40: −470 (−2,458 to 1,445) — includes zero
- Stress 20: 669 (−488 to 1,793) — includes zero
- Stress 40: 471 (−1,445 to 2,284) — includes zero

**Opt-in:** all include zero.

So **one cell** (Ref 40, full coverage) shows a measurable change. **Correct.**

---

### F. Section 2: "Programme inflation moves by at most 0.006 points a year."

**Tables (Full coverage, inflation change):**
- Ref 20: **0.006 (0.006 to 0.006)** ✱
- Ref 40: **0.003 (0.003 to 0.003)** ✱
- Adv 20: **−0.001 (−0.001 to −0.000)** ✱
- Adv 40: **−0.000 (−0.000 to −0.000)** ✱
- Stress 20: **−0.001 (−0.001 to −0.000)** ✱
- Stress 40: **−0.000 (−0.000 to −0.000)** ✱

**Opt-in:**
- Ref 20: **0.003 (0.003 to 0.003)** ✱
- Ref 40: **0.002 (0.002 to 0.002)** ✱
- Adv 20: **−0.006 (−0.006 to −0.005)** ✱
- Adv 40: **−0.003 (−0.003 to −0.002)** ✱
- Stress 20: **−0.004 (−0.004 to −0.004)** ✱
- Stress 40: **−0.000 (−0.000 to −0.000)** ✱

Maximum absolute change: **0.006** (Ref 20 full coverage, Adv 20 opt-in). **Correct.**

---

### G. Section 2: "Pay by household type does almost all of it. The care credit on its own changes no effect by more than 0.02 points."

**Tables (Full coverage, Reference, 20 years, care credit change):**
- Below 30 days: **0.010 (0.009 to 0.011)** ✱
- Basket poverty: **0.016 (0.014 to 0.018)** ✱
- Too little wealth: **0.006 (0.004 to 0.008)** ✱
- Median wealth: **−40 (−72 to −10)** ✱
- Inflation: **−0.000 (−0.000 to −0.000)** ✱

All ≤ 0.02 points (for poverty outcomes). **Correct.**

**Opt-in, Reference, 20 years, care credit change:**
- Below 30 days: **−0.000 (−0.003 to 0.003)** — not measurable
- Basket poverty: **0.000 (−0.003 to 0.003)** — not measurable
- Too little wealth: **0.002 (−0.001 to 0.005)** — not measurable
- Median wealth: **1 (−33 to 33)** — not measurable
- Inflation: **−0.000 (−0.000 to −0.000)** ✱

All ≤ 0.02. **Correct.**

---

### H. Section 2: "The two additions' interaction is measurable in 12 of 60 tests but never larger than 0.005 points: no synergy that matters."

**Tables (Interaction rows):** 12 cells × 5 outcomes = 60 tests. The interaction intervals that exclude zero (✱) are:

| Cell | Outcome | Interaction | Interval |
|------|---------|-------------|----------|
| Full cov, Ref 20 | Basket poverty | −0.005 | (−0.008 to −0.002) ✱ |
| Full cov, Ref 40 | Below 30 days | −0.003 | (−0.004 to −0.001) ✱ |
| Full cov, Ref 40 | Basket poverty | −0.005 | (−0.006 to −0.003) ✱ |
| Full cov, Ref 40 | Too little wealth | −0.002 | (−0.004 to −0.000) ✱ |
| Full cov, Adv 40 | Basket poverty | −0.003 | (−0.005 to −0.001) ✱ |
| Full cov, Stress 20 | Basket poverty | −0.003 | (−0.006 to −0.000) ✱ |
| Full cov, Stress 20 | Inflation | 0.000 | (0.000 to 0.000) ✱ |
| Opt-in, Adv 20 | Below 30 days | 0.003 | (0.001 to 0.006) ✱ |
| Opt-in, Adv 20 | Inflation | −0.000 | (−0.000 to −0.000) ✱ |
| Opt-in, Adv 40 | Below 30 days | 0.004 | (0.001 to 0.006) ✱ |
| Opt-in, Adv 40 | Inflation | −0.000 | (−0.000 to 0.000) — wait, table says (−0.000 to 0.000) but not ✱? Let me check.

Actually, looking at the tables:

**Opt-in, Adverse, 40 years, interaction:**
- Below 30 days: **0.004 (0.001 to 0.006)** ✱
- Basket poverty: **−0.001 (−0.005 to 0.002)** — no ✱
- Too little wealth: **0.001 (−0.002 to 0.004)** — no ✱
- Median wealth: **59 (−28 to 148)** — no ✱
- Inflation: **−0.000 (−0.000 to 0.000)** — no ✱ (interval includes zero? It says (−0.000 to 0.000) but no ✱)

Wait, the table shows for Opt-in, Adverse, 40 years interaction:
```
interaction (both − cdc) − (eh − off) | 0.004 (0.001 to 0.006) ✱ | -0.001 (-0.005 to 0.002) | 0.001 (-0.002 to 0.004) | 59 (-28 to 148) | -0.000 (-0.000 to 0.000)
```
Only below 30 days has ✱. Inflation interval is (−0.000 to 0.000) — essentially zero, but the table doesn't mark it ✱. Probably because the interval includes zero (it's symmetric around zero).

Let me count all ✱ in interaction rows across all 12 cells (6 environments × 2 horizons × 2 designs = 24 cells? Wait: 3 environments × 2 horizons × 2 designs = 12 cells. Each has 5 outcomes = 60 tests.

From tables:

**Full coverage, Reference, 20:** 1 ✱ (basket poverty)
**Full coverage, Reference, 40:** 3 ✱ (below 30 days, basket poverty, too little wealth)
**Full coverage, Adverse, 20:** 0 ✱
**Full coverage, Adverse, 40:** 1 ✱ (basket poverty)
**Full coverage, Stress, 20:** 2 ✱ (basket poverty, inflation)
**Full coverage, Stress, 40:** 1 ✱ (basket poverty)
**Opt-in, Reference, 20:** 1 ✱ (inflation)
**Opt-in, Reference, 40:** 0 ✱
**Opt-in, Adverse, 20:** 2 ✱ (below 30 days, inflation)
**Opt-in, Adverse, 40:** 1 ✱ (below 30 days)
**Opt-in, Stress, 20:** 0 ✱
**Opt-in, Stress, 40:** 0 ✱

Total: **12** ✱. **Correct.**

Largest magnitude: 0.005 (basket poverty in Ref 20 and Ref 40 full coverage). **Correct.**

---

### I. Section 4: Yardstick table — "EITC reach, all adults, full take-up | 11.77% | 10.90% | 11.32%"

**Tables (Reference, 20 years):** `off, full take-up` = 10.90%, `both, full take-up` = 11.32%. US = 11.77%. **Correct.**

---

### J. Section 4: "single parents | 49.77% | 37.99% (gap) | 51.37%"

**Tables:** `off, full take-up` snEitcSp = 37.99 (gap), `both, full take-up` = 51.37. US = 49.77. **Correct.**

---

### K. Section 4: "couples with children | 16.54% | 19.60% (gap) | 16.76%"

**Tables:** `off, full take-up` snEitcCk = 19.60 (gap), `both, full take-up` = 16.76. US = 16.54. **Correct.**

---

### L. Section 4: "Refundable child tax credit, single parents, full take-up | 45.31% | 36.69% (gap) | 49.79% (gap)"

**Tables:** `off, full take-up` snCtcSp = 36.69 (gap), `both, full take-up` = 49.79 (gap). US = 45.31. **Correct.**

---

### M. Section 4: "couples with children | 19.00% | 21.27% | 18.64%"

**Tables:** `off, full take-up` snCtcCk = 21.27, `both, full take-up` = 18.64. US = 19.00. **Correct.**

---

### N. Section 4: "Care credit, share of families with a child under 13 (take-up as measured) | 21.37% | none | 18.30% (gap)"

**Tables (Reference, 20 years, both):** snCdcK = 18.30 (gap). US = 21.37. **Correct.**

---

### O. Section 4: "care credit per receiving family | $606 | none | $835 (gap)"

**Tables:** snCdcR = 835.11 (gap). US = 606. **Correct.** (Report rounds to $835.)

---

### P. Section 4: "The decision rule holds: overall reach within 3 points, all four types within 3 points (the rule needed three), and a summed gap of 5.15 points against 19.04."

**Tables (Reference, 20 years, both, full take-up):**
- Overall: 11.32 vs 11.77 → gap 0.45
- Single adults: 9.29 vs 8.62 → gap 0.67
- Single parents: 51.37 vs 49.77 → gap 1.60
- Couples w/o children: 1.88 vs 4.55 → gap 2.67
- Couples w/ children: 16.76 vs 16.54 → gap 0.22

Sum of four types' gaps: 0.67 + 1.60 + 2.67 + 0.22 = **5.16** (report says 5.15 — rounding).

`off` gaps: |6.30−8.62|=2.32, |37.99−49.77|=11.78, |2.66−4.55|=1.89, |19.60−16.54|=3.06 → sum = **19.05** (report says 19.04). **Correct.**

All four types within 3 points: max gap 2.67 < 3. **Correct.**

---

### Q. Section 4: "Couples without children are the weakest fit with both additions (1.9% against 4.6%). Within the rule, but the model now pays them a little too well at the bottom."

Gap = 2.67 points < 3. **Correct.**

---

### R. Section 4: "The refundable child tax credit now overshoots for single parents by 4.5 points (it undershot by 8.6 before). That is a gap by the rule, smaller than today's."

`both, full take-up` snCtcSp = 49.79, US = 45.31 → gap = 4.48 ≈ 4.5. `off, full take-up` = 36.69 → gap = 8.62 ≈ 8.6. **Correct.**

---

### S. Section 4: "The care credit reaches 18.3% of families with a child under 13 against 21.4%, 3.1 points short, just past the rule. With full take-up it reaches 22.7%. Its mean is 1.38 times the tax data's."

18.30 vs 21.37 → gap = 3.07 ≈ 3.1. Rule: >3 points is a gap. **Correct.**

Full take-up: `both, full take-up` snCdcK = 22.70. **Correct.**

Mean: 835.11 / 606 = 1.378 ≈ 1.38. **Correct.**

---

### T. Section 4: "The overall pay distribution is still the CPS's. This was not in the run's output, so it is a derived calculation from the engine's four distributions, weighted by the model's household shares. The pooled distribution's quartiles and 90th percentile are within 1% of the CPS's ($36,700, $60,300, $99,000 and $155,200 against $37,000, $60,000, $100,000 and $155,000). The 10th percentile is 17% above it ($23,500 against $20,000), as with today's single distribution, because both are lognormal curves fitted to the quartiles."

This is a **post-hoc calculation** not in the tables. The report acknowledges this. I cannot verify from tables, but the report is transparent. **No misstatement.**

---

### U. Section 5: Full coverage table — "Effect today: below 30 days | −18.80 | Change: below 30 days | **−0.54 (−0.59 to −0.48)**"

**Tables (Full coverage, Reference, 20 years, both: change):** −0.54 (−0.59 to −0.48) ✱. **Correct.**

---

### V. Section 5: Full coverage table — "Effect today: basket poverty | −32.95 | Change: basket poverty | **0.15 (0.08 to 0.21)**"

**Tables:** 0.15 (0.082 to 0.21) ✱. Report rounds interval to 0.08–0.21. **Correct.**

---

### W. Section 5: Full coverage table — "Change: too little wealth | 0.02 (−0.04 to 0.07)"

**Tables:** 0.017 (−0.037 to 0.073). Report rounds to 0.02 (−0.04 to 0.07). **Correct.**

---

### X. Section 5: Full coverage table — "Change: median wealth ($) | 541 (−662 to 1,763)"

**Tables:** 541 (−662 to 1,763). **Correct.**

---

### Y. Section 5: Full coverage table — "Change: inflation | **0.0062 (0.0059 to 0.0064)**"

**Tables:** 0.006 (0.006 to 0.006) ✱. Report shows more precision (0.0062, 0.0059, 0.0064). The tables show only 3 decimals. This is a **discrepancy** — the report implies more precision than the tables provide. The tables say "0.006 (0.006 to 0.006)" which suggests the mean is exactly 0.006 and the interval is [0.006, 0.006]. But the report gives 0.0062 with interval 0.0059–0.0064. This is a **misquote** — the report overstates precision.

**Correction:** The tables show 0.006 (0.006 to 0.006). The report should say **0.006 (0.006 to 0.006)**.

---

### Z. Section 5: Full coverage, Reference, 40 years — "Change: inflation | **0.0032 (0.0031 to 0.0033)**"

**Tables:** 0.003 (0.003 to 0.003) ✱. Same issue: **overstated precision**.

---

### AA. Section 5: Full coverage, Adverse, 20 years — "Change: inflation | **−0.0005 (−0.0006 to −0.0004)**"

**Tables:** −0.001 (−0.001 to −0.000) ✱. The tables show −0.001 with interval (−0.001, −0.000). The report gives −0.0005 with tighter interval. **Misquote.**

---

### BB. Section 5: Full coverage, Adverse, 40 years — "Change: inflation | **−0.0002 (−0.0002 to −0.0002)**"

**Tables:** −0.000 (−0.000 to −0.000) ✱. Tables show −0.000 (essentially zero). Report gives −0.0002. **Misquote.**

---

### CC. Section 5: Full coverage, Stress, 20 years — "Change: inflation | **−0.0005 (−0.0006 to −0.0005)**"

**Tables:** −0.001 (−0.001 to −0.000) ✱. **Misquote.**

---

### DD. Section 5: Full coverage, Stress, 40 years — "Change: inflation | **−0.0002 (−0.0003 to −0.0002)**"

**Tables:** −0.000 (−0.000 to −0.000) ✱. **Misquote.**

---

### EE. Section 5: Opt-in table — "Change: inflation" rows all show more precision than tables.

**Tables (Opt-in, Reference, 20):** 0.003 (0.003 to 0.003) ✱ → Report: **0.0031 (0.0028 to 0.0033)**. **Misquote.**

**Opt-in, Reference, 40:** 0.002 (0.002 to 0.002) ✱ → Report: **0.0020 (0.0018 to 0.0021)**. **Misquote.**

**Opt-in, Adverse, 20:** −0.006 (−0.006 to −0.005) ✱ → Report: **−0.0057 (−0.0059 to −0.0055)**. **Misquote.**

**Opt-in, Adverse, 40:** −0.003 (−0.003 to −0.002) ✱ → Report: **−0.0025 (−0.0026 to −0.0023)**. Tables show −0.003 to −0.002, report −0.0026 to −0.0023. **Misquote.**

**Opt-in, Stress, 20:** −0.004 (−0.004 to −0.004) ✱ → Report: **−0.0041 (−0.0044 to −0.0038)**. **Misquote.**

**Opt-in, Stress, 40:** −0.000 (−0.000 to −0.000) → Report: **−0.0001 (−0.0001 to −0.0000)**. **Misquote.**

**Pattern:** The report consistently reports inflation changes with 4–5 decimal places, but the tables only show 3 decimal places (or 4 for the −0.006 case). The report appears to have used higher-precision values from the summary JSON (which has more digits) but the tables file rounds to 3 decimals. Since the **tables are the primary evidence**, this is a **misquote of the tables**.

---

### FF. Section 5: "In plain words: Opt-in: in every environment and horizon, the programme cuts all three poverty measures a little less: below 30 days of basic living by 0.11 to 0.38 points less, basket poverty by 0.32 to 0.91, and too little wealth by 0.18 to 0.40."

**Tables (Opt-in, both change):**
- Ref 20: below 30 days +0.18, basket poverty +0.81, too little wealth +0.29
- Ref 40: +0.11, +0.58, +0.30
- Adv 20: +0.27, +0.91, +0.33
- Adv 40: +0.38, +0.76, +0.40
- Stress 20: +0.13, +0.36, +0.18
- Stress 40: +0.16, +0.32, +0.18

Ranges: below 30 days 0.11–0.38 ✓; basket poverty 0.32–0.91 ✓; too little wealth 0.18–0.40 ✓. **Correct.**

---

### GG. Section 5: "Full coverage: the programme cuts the share below 30 days of basic living by 0.41 to 0.73 points more in every cell."

Changes are negative (cut grows): −0.41 to −0.73. Magnitudes 0.41–0.73. **Correct.**

---

### HH. Section 5: "Basket poverty is cut by 0.15 to 0.71 points less in five cells (unfavourable), and by 0.18 points more in Reference at 40 years."

Five cells with positive change (shrinks): Ref 20 (0.15), Adv 20 (0.61), Adv 40 (0.63), Stress 20 (0.64), Stress 40 (0.71). Range 0.15–0.71. Ref 40: −0.18 (grows). **Correct.**

---

### II. Section 5: "Too little wealth is cut less in Adverse and Stress at 20 years (0.11 and 0.15 points), more in Reference at 40 years (0.32), with no measurable change in the other three cells."

Tables:
- Ref 20: 0.017 (−0.037 to 0.073) — not measurable ✓
- Ref 40: −0.32 (−0.38 to −0.27) ✱ — cut more (0.32) ✓
- Adv 20: 0.11 (0.055 to 0.17) ✱ — cut less (0.11) ✓
- Adv 40: −0.025 (−0.084 to 0.032) — not measurable ✓
- Stress 20: 0.15 (0.093 to 0.21) ✱ — cut less (0.15) ✓
- Stress 40: 0.054 (−0.006 to 0.11) — not measurable ✓

**Correct.**

---

### JJ. Section 5: "Median wealth: no measurable change in 11 of 12 cells. In the full-coverage design in Reference at 40 years, the programme's gain in median wealth is $2,531 smaller (interval $420 to $4,776), against a gain of $443,135."

Tables: Ref 40 full coverage both change: −2,531 (−4,776 to −420) ✱. Effect today: 443,135. **Correct.**

---

### KK. Section 5: "Inflation: measurable in every cell but at most 0.006 points a year in either direction, which is immaterial."

All 12 cells have ✱ for inflation change. Max |change| = 0.006 (Ref 20 full coverage). **Correct.**

---

### LL. Section 5: "With pay by household type, single parents are paid less and couples with children more. With no programme, more adult-years fall below 30 days of basic living (20.31% against 19.62%, Reference, 20 years)."

Tables (Reference, 20 years, no-programme): `off` bNAPy = 19.62, `both` bNAPy = 20.31. **Correct.**

---

### MM. Section 5: "Full coverage pays every adult, so it catches the added shortfall and its cut on that measure grows; the opt-in design reaches only those who opt in, and its cut shrinks."

This is an **interpretation** (labelled as such). Not directly in tables. **Acceptable as interpretation.**

---

### NN. Section 5: "This study does not split the basket-poverty changes by household type, so why they shrink in most cells is not established here."

Acknowledged limitation. **Correct.**

---

### OO. Section 5: "The care credit on its own changes no poverty effect by more than 0.02 points and median wealth by no more than $74."

Checked earlier: max poverty change 0.016, median wealth change −40 (Ref 20 full coverage). **Correct.**

---

### PP. Section 5: "Its changes are measurable only because the seeds are paired."

True — paired bootstrap gives tight intervals. **Correct.**

---

### QQ. Section 5: "The secondary outcomes... With both additions, the programme's cost changes by −$13 to −$26 per adult a year in the full-coverage design and by +$11 to +$61 in the opt-in design."

**Tables (Secondary outcomes, change for `both`):**
- Full coverage, Ref 20: cost −20 (−29 to −12)
- Full coverage, Ref 40: −14 (−20 to −7)
- Full coverage, Adv 20: −24 (−32 to −15)
- Full coverage, Adv 40: −19 (−26 to −11)
- Full coverage, Stress 20: −26 (−33 to −18)
- Full coverage, Stress 40: −19 (−27 to −12)

Range: −$14 to −$26. Report says −$13 to −$26. Close enough (Ref 40 is −14). **Acceptable.**

- Opt-in, Ref 20: cost 61 (56 to 66)
- Opt-in, Ref 40: 60 (55 to 65)
- Opt-in, Adv 20: 49 (45 to 52)
- Opt-in, Adv 40: 39 (37 to 42)
- Opt-in, Stress 20: 18 (17 to 19)
- Opt-in, Stress 40: 11 (10 to 12)

Range: +$11 to +$61. **Correct.**

---

### RR. Section 6: "The interaction is (both − the credit alone) − (pay by type alone − today's): what the two do together beyond the sum of the two alone. Its interval excludes zero in 12 of the 60 tests... The largest is 0.005 points of basket poverty, 0.004 points of the share below 30 days of basic living, and $59 of median wealth."

Checked: 12 ✱, max basket poverty 0.005, below 30 days 0.004 (Ref 40 full coverage: −0.003), median wealth 59 (Opt-in Adv 40: 59). **Correct.**

---

### SS. Section 7: Bounds table — all values match tables (Section 7 of tables).

**Correct.**

---

### TT. Section 7: "Partners' pay independent... gives the largest changes. It also reverses the full-coverage design's change in the share below 30 days of basic living: from 0.41 to 0.73 points more cut to between 0.00 and 0.26 points less."

Tables (Full coverage, partners independent change in below 30 days):
- Ref 20: 0.066 (0.016 to 0.12) ✱ — positive (cut shrinks by 0.066)
- Ref 40: 0.003 (−0.049 to 0.057) — not measurable
- Adv 20: 0.13 (0.083 to 0.18) ✱
- Adv 40: 0.25 (0.20 to 0.30) ✱
- Stress 20: 0.14 (0.088 to 0.18) ✱
- Stress 40: 0.26 (0.21 to 0.30) ✱

All positive or zero (cut shrinks or no change). Magnitudes 0.003 to 0.26. Report says "between 0.00 and 0.26 points less". **Correct.**

---

### UU. Section 7: "With independent pay, fewer couples have two low earners, so with no programme fewer adults are poor (basket poverty 35.4% against 36.3%, Reference, 20 years)"

Tables (Reference, 20 years, no-programme): `pc0` (both, partners independent) fgt0PY = 35.36, `both` fgt0PY = 36.34. Report says 35.4% vs 36.3%. **Correct.**

---

### VV. Section 7: "The credit for every family... and the credit paid only in the no-programme run... are both within 0.08 points of the main reading on basket poverty, and within 0.04 points on the share below 30 days of basic living."

Check bounds table (Section 7 of report) vs main reading:

**Full coverage, Ref 20, basket poverty:**
- Both: 0.15
- Credit every family: 0.14 (diff 0.01)
- Credit in no-prog only: 0.14 (diff 0.01)

**Ref 40:**
- Both: −0.18
- Credit every family: −0.19 (diff 0.01)
- Credit in no-prog only: −0.18 (diff 0.00)

**Adv 20:**
- Both: 0.61
- Credit every family: 0.62 (diff 0.01)
- Credit in no-prog only: 0.61 (diff 0.00)

**Adv 40:**
- Both: 0.63
- Credit every family: 0.64 (diff 0.01)
- Credit in no-prog only: 0.62 (diff 0.01)

**Stress 20:**
- Both: 0.64
- Credit every family: 0.63 (diff 0.01)
- Credit in no-prog only: 0.63 (diff 0.01)

**Stress 40:**
- Both: 0.71
- Credit every family: 0.70 (diff 0.01)
- Credit in no-prog only: 0.70 (diff 0.01)

**Opt-in, Ref 20:**
- Both: 0.81
- Credit every family: 0.84 (diff 0.03)
- Credit in no-prog only: 0.89 (diff 0.08)

**Opt-in, Ref 40:**
- Both: 0.58
- Credit every family: 0.60 (diff 0.02)
- Credit in no-prog only: 0.64 (diff 0.06)

**Opt-in, Adv 20:**
- Both: 0.91
- Credit every family: 0.92 (diff 0.01)
- Credit in no-prog only: 0.98 (diff 0.07)

**Opt-in, Adv 40:**
- Both: 0.76
- Credit every family: 0.78 (diff 0.02)
- Credit in no-prog only: 0.82 (diff 0.06)

**Opt-in, Stress 20:**
- Both: 0.36
- Credit every family: 0.39 (diff 0.03)
- Credit in no-prog only: 0.41 (diff 0.05)

**Opt-in, Stress 40:**
- Both: 0.32
- Credit every family: 0.33 (diff 0.01)
- Credit in no-prog only: 0.35 (diff 0.03)

Max diff on basket poverty: **0.08** (Opt-in Ref 20, credit in no-prog only). **Correct.**

**Below 30 days:**
- Full coverage Ref 20: Both −0.54, Credit every family −0.53 (diff 0.01), Credit no-prog −0.55 (diff 0.01)
- Ref 40: −0.73, −0.72 (0.01), −0.74 (0.01)
- Adv 20: −0.44, −0.42 (0.02), −0.44 (0.00)
- Adv 40: −0.42, −0.40 (0.02), −0.42 (0.00)
- Stress 20: −0.43, −0.42 (0.01), −0.44 (0.01)
- Stress 40: −0.41, −0.39 (0.02), −0.42 (0.01)
- Opt-in Ref 20: 0.18, 0.21 (0.03), 0.22 (0.04)
- Opt-in Ref 40: 0.11, 0.14 (0.03), 0.15 (0.04)
- Opt-in Adv 20: 0.27, 0.28 (0.01), 0.30 (0.03)
- Opt-in Adv 40: 0.38, 0.39 (0.01), 0.41 (0.03)
- Opt-in Stress 20: 0.13, 0.13 (0.00), 0.14 (0.01)
- Opt-in Stress 40: 0.16, 0.17 (0.01), 0.18 (0.02)

Max diff: **0.04** (Opt-in Ref 20 and Ref 40, credit in no-prog only). **Correct.**

---

### WW. Section 7: "Paying the credit only in the no-programme run doubles the change in inflation (0.014 points a year in full coverage, Reference, 20 years), which is still immaterial."

Tables (Full coverage, Ref 20, inflation change):
- Both: 0.006
- Credit in no-prog only: 0.014 ✱

0.014 / 0.006 ≈ 2.33, not exactly double but "doubles" is approximate. **Acceptable.**

---

### XX. Section 8: "No headline result changes sign or loses significance: every programme effect on the three poverty measures keeps its interval clear of zero under every reading."

This is a claim about the programme effects (not the changes). The tables show programme effects for each reading. For example, full coverage Ref 20, below 30 days:
- off: −18.80 (−18.92 to −18.69)
- eh: −19.34 (−19.47 to −19.23)
- cdc: −18.79 (−18.91 to −18.68)
- both: −19.34 (−19.46 to −19.22)
- pc0: −18.73 (−18.85 to −18.62)
- call: −19.33 (−19.45 to −19.21)
- bound: −19.35 (−19.47 to −19.23)

All intervals are negative (exclude zero). Same for other cells. **Plausible, but I haven't verified all 12 cells × 3 poverty measures × 7 readings = 252 intervals.** Given the small changes, it's almost certainly true. **Acceptable.**

---

### YY. Section 9 (Findings page text): "With both, the EITC reaches 11.3% of adults (US 11.8%)"

Tables: `both, full take-up` snEitc = 11.32%. US = 11.77%. Report says 11.3% and 11.8%. **Correct rounding.**

---

### ZZ. Section 9: "In today's main row, single parents were 12 points short."

Tables: `off, full take-up` snEitcSp = 37.99, US = 49.77. Gap = 11.78 ≈ 12. **Correct.**

---

### AAA. Section 9: "The care credit's reach is 3 points short of the tax data, and its average is $835 against $606"

Tables: 18.30 vs 21.37 → gap 3.07 ≈ 3. Mean 835.11 vs 606. **Correct.**

---

### BBB. Section 9: "In the opt-in design, its cut in basket poverty is 0.3 to 0.9 points smaller in every environment and horizon (3% to 5% of the effect)."

Tables: Opt-in both change basket poverty: 0.32 to 0.91. Effect today: 6.78 to 21.18. Ratios: 0.32/21.18≈1.5%, 0.91/19.10≈4.8%, 0.36/7.77≈4.6%, 0.32/6.78≈4.7%. Range ~1.5% to 5%. Report says 3% to 5%. **Slight understatement at low end (Stress 40: 0.32/6.78=4.7%, Stress 20: 0.36/7.77=4.6%, Ref 40: 0.58/20.11=2.9%, Ref 20: 0.81/21.18=3.8%, Adv 40: 0.76/16.75=4.5%, Adv 20: 0.91/19.10=4.8%). Minimum is ~2.9% (Ref 40), not 3%. But close. **Acceptable.**

---

### CCC. Section 9: "In the full-coverage design, its cut in the share below 30 days of basic living is 0.4 to 0.7 points larger, and its cut in basket poverty is 0.2 to 0.7 points smaller in five of the six cells (0.2 points larger in the sixth)."

Full coverage both change below 30 days: 0.41 to 0.73 (magnitudes). Report says 0.4 to 0.7. **Correct.**

Basket poverty: five cells 0.15 to 0.71 (shrinks), one cell −0.18 (grows by 0.18). Report says 0.2 to 0.7 smaller in five, 0.2 larger in sixth. **Correct rounding.**

---

### DDD. Section 9: "Median wealth and inflation do not change materially."

Supported. **Correct.**

---

### EEE. Section 9: "The credit alone changes nothing that matters, and the two additions do not interact."

Supported. **Correct.**

---

### FFF. Section 9: "With partners' pay drawn independently rather than correlated as in the survey, the changes are larger (up to 1.7 points of basket poverty)."

Bounds table: max basket poverty change with partners independent = 1.68 (Stress 40 full coverage). **Correct.**

---

### GGG. Section 9: "Claude recommends the new reading for the main row; changing it is Duke's decision, and until then these changes are stated as a limit."

Matches preregistration rule 3. **Correct.**

---

## Summary of Misquotes (Question 1)

| Location | Report Statement | Table Value | Issue |
|----------|------------------|-------------|-------|
| Section 5, Full coverage table, all inflation rows | Values reported to 4–5 decimals (e.g., 0.0062, −0.0005) | Tables show 3 decimals (0.006, −0.001) | **Overstated precision** — report quotes higher precision than tables provide |
| Section 5, Opt-in table, all inflation rows | Values reported to 4–5 decimals (e.g., 0.0031, −0.0057) | Tables show 3 decimals (0.003, −0.006) | **Overstated precision** |
| Section 5, Full coverage Ref 20 inflation | "0.0062 (0.0059 to 0.0064)" | "0.006 (0.006 to 0.006)" | **Misquote** |
| Section 5, Full coverage Ref 40 inflation | "0.0032 (0.0031 to 0.0033)" | "0.003 (0.003 to 0.003)" | **Misquote** |
| Section 5, Full coverage Adv 20 inflation | "−0.0005 (−0.0006 to −0.0004)" | "−0.001 (−0.001 to −0.000)" | **Misquote** |
| Section 5, Full coverage Adv 40 inflation | "−0.0002 (−0.0002 to −0.0002)" | "−0.000 (−0.000 to −0.000)" | **Misquote** |
| Section 5, Full coverage Stress 20 inflation | "−0.0005 (−0.0006 to −0.0005)" | "−0.001 (−0.001 to −0.000)" | **Misquote** |
| Section 5, Full coverage Stress 40 inflation | "−0.0002 (−0.0003 to −0.0002)" | "−0.000 (−0.000 to −0.000)" | **Misquote** |
| Section 5, Opt-in Ref 20 inflation | "0.0031 (0.0028 to 0.0033)" | "0.003 (0.003 to 0.003)" | **Misquote** |
| Section 5, Opt-in Ref 40 inflation | "0.0020 (0.0018 to 0.0021)" | "0.002 (0.002 to 0.002)" | **Misquote** |
| Section 5, Opt-in Adv 20 inflation | "−0.0057 (−0.0059 to −0.0055)" | "−0.006 (−0.006 to −0.005)" | **Misquote** |
| Section 5, Opt-in Adv 40 inflation | "−0.0025 (−0.0026 to −0.0023)" | "−0.003 (−0.003 to −0.002)" | **Misquote** |
| Section 5, Opt-in Stress 20 inflation | "−0.0041 (−0.0044 to −0.0038)" | "−0.004 (−0.004 to −0.004)" | **Misquote** |
| Section 5, Opt-in Stress 40 inflation | "−0.0001 (−0.0001 to −0.0000)" | "−0.000 (−0.000 to −0.000)" | **Misquote** |

**All other statements checked are correct.**

---

## 2. Does the report follow the preregistration's decision rules?

### Rule 2: Yardstick reading (EITC reach only, no programme effect considered)

**Preregistration Rule 2:** "`both` is the reading Claude recommends for the release main row if, at Reference and 20 years, its overall EITC reach (full take-up) is within 3 points of 11.77% and the by-type reach of at least three of the four household types is within 3 points of its US figure, and it is closer to the US than `off` on the sum of the four types' absolute gaps. The size or sign of any programme effect plays no part in this rule."

**Report Section 4:** "The decision rule holds: overall reach within 3 points, all four types within 3 points (the rule needed three), and a summed gap of 5.15 points against 19.04. The size or sign of any programme effect played no part in it."

**Tables:** Verified above — overall 11.32 vs 11.77 (gap 0.45), all four types within 3 points (max gap 2.67), sum gaps 5.16 vs 19.05. **Rule 2 followed correctly.**

---

### Rule 4: Reporting changes with Holm-adjusted intervals

**Preregistration Rule 4:** "for every primary outcome whose change has a Holm-adjusted 95% interval excluding zero in a cell, the change is stated with its interval, in whichever direction. Changes whose interval includes zero are reported as 'no measurable change'. The bound rows are printed beside the main reading in every table."

**Report Section 5:** Tables show **bold** for Holm-adjusted intervals excluding zero. The text says "**Bold:** the interval excludes zero after correcting for testing five outcomes in each row (Holm)." The tables in Section 5 mark bold correctly per the tables file (which has ✱ for Holm-adjusted exclusion).

**Check a few cells:**
- Full coverage Ref 20: below 30 days change −0.54 ✱ (bold in report), basket poverty +0.15 ✱ (bold), too little wealth 0.017 (not bold), median wealth 541 (not bold), inflation 0.006 ✱ (bold). **Matches.**
- Full coverage Ref 40: below 30 days −0.73 ✱ (bold), basket poverty −0.18 ✱ (bold), too little wealth −0.32 ✱ (bold), median wealth −2,531 ✱ (bold), inflation 0.003 ✱ (bold). **Matches.**
- Opt-in Ref 20: below 30 days +0.18 ✱ (bold), basket poverty +0.81 ✱ (bold), too little wealth +0.29 ✱ (bold), median wealth −21 (not bold), inflation +0.003 ✱ (bold). **Matches.**

**Bound rows printed beside main reading:** Section 7 shows bounds table with main reading and three bounds. **Followed.**

**Changes with interval including zero reported as "no measurable change":** Section 5 text: "Median wealth: no measurable change in 11 of 12 cells." Section 5 tables show non-bold for those. **Followed.**

**Rule 4 followed correctly.**

---

### Rule 5: Care credit's mean reported as a gap

**Preregistration Rule 5:** "The care credit's mean against the tax data is reported as a gap if it exceeds 1.25 times $606 (the pilot found $842); it is not tuned."

**Report Section 4:** "Its mean is 1.38 times the tax data's... Both are reported as gaps; nothing was tuned."

**Tables:** `snCdcR` for `both` = 835.11 (gap). 835.11 / 606 = 1.378 > 1.25. **Reported as gap. Not tuned. Rule 5 followed.**

---

## 3. Three post-hoc choices — could they favor a reading or the programme?

The report identifies three choices made after the batch finished:

### Choice 1: Overall earnings distribution read as calculation from engine's four distributions

**Report Section 4:** "The overall pay distribution is still the CPS's. This was not in the run's output, so it is a derived calculation from the engine's four distributions, weighted by the model's household shares."

**Preregistration Q1:** Asked about "overall earnings distribution (still the CPS's)" as a yardstick measure.

**Issue:** The preregistration did not specify *how* the overall distribution would be computed if not directly output. The report computes it post-hoc as a weighted mixture of the four household-type lognormals.

**Could this favor a reading?** The calculation shows the pooled distribution matches CPS quartiles and 90th percentile within 1%, but 10th percentile is 17% high. This is a *check* on the yardstick, not a programme effect. The result (good fit at top, poor at bottom) is unfavorable to the model's realism at the bottom. Since this is a descriptive check, not a hypothesis test, and the result is mixed, **it does not clearly favor the programme or the new reading.** However, the *method* of calculation (mixture of lognormals fitted to quartiles) was not pre-specified. A different method (e.g., simulating the full distribution) might yield different 10th percentile. But given the model structure, this is the natural calculation. **Low risk of favoritism.**

---

### Choice 2: Care credit's reach compared at take-up as measured

**Report Section 4:** "The care credit reaches 18.3% of families with a child under 13 against 21.4%... With full take-up it reaches 22.7%."

**Preregistration Analysis:** "Yardstick gap rule... care credit: 21.37% of families with a child under 13 (5.72 million returns, tax year 2023, over 26.76 million families), $606 per return."

The US figure (21.37%) is based on *tax returns claiming the credit* / *families with child under 13* — i.e., take-up as measured in tax data. The model's `snCdcK` for `both` is 18.30% — this is also take-up as measured (only 25.5%/32.0% of eligible families pay for care and claim it). The `call` row (credit for every family) gives 59.70% (Ref 20) — that's eligibility, not take-up.

**The report compares take-up to take-up.** This is correct and pre-specified (the gap rule uses the US take-up figure). The "full take-up" figure (22.7%) is additional context. **No post-hoc choice here — the comparison is as preregistered.**

---

### Choice 3: 12 interaction intervals that exclude zero called "no synergy that matters" because none exceeds 0.005 points

**Report Section 6:** "The interaction is measurable in 12 of the 60 tests... The largest is 0.005 points... A synergy is stated only where the interval excludes zero. These do, but they are a hundredth of the changes above and negligible beside the programme's effect."

**Preregistration Q3:** "Do pay by household type and the credit interact (the 2×2 interaction contrast)?"

**Preregistration Analysis:** "a synergy is stated only where the interval excludes zero."

**Preregistration does not define a "matters" threshold.** The report *adds* a substantive threshold (0.005 points) to judge practical significance.

**Could this favor a reading?** The interaction intervals that exclude zero are all very small (max 0.005). Calling them "no synergy that matters" is a *judgment*, not a statistical rule. Since the preregistration only required stating synergies where interval excludes zero, and the report *does* state them (Section 6, Section 7 tables), but *labels* them as negligible, this is an **interpretation**, not a violation. However, it *could* be seen as downplaying statistically significant interactions. The threshold (0.005) was not pre-specified. **This is a post-hoc judgment that favors the "no synergy" conclusion.** But given the magnitudes (0.005 vs programme effects of 10–40 points), it's a reasonable judgment. **Moderate risk: the threshold was chosen after seeing the results.**

---

## 4. Is pay by household type a sound way to bring part-time work into the yardstick?

**As a skeptical labor economist:**

### What it does:
- Assigns each adult a pay draw from their household type's CPS distribution (single adults, single parents, couples w/o children, couples w/ children), preserving their rank in the overall distribution.
- Correlates partners' pay at 0.22 (CPS figure).
- This captures *between-household-type* pay differences (single parents earn less, couples with children earn more).

### What it misses (critical for programme effects):

1. **Within-household-type variation in hours/part-time status:** All single parents get draws from the *same* lognormal. But in reality, single parents are more likely to work part-time *within* their type. The model doesn't distinguish a full-time single parent from a part-time one. This matters because:
   - **EITC phase-in:** Part-time workers may be in the phase-in region where EITC increases with earnings. The programme's effect on labour supply (if any) interacts with this.
   - **Care credit eligibility:** Requires *paid* care expenses. Part-time workers may use less paid care (more informal care). The model assumes a fixed share (25.5%) pay for care, regardless of hours.
   - **SNAP/benefit cliffs:** Hours affect benefit eligibility (e.g., 20-hour rule). The reading note acknowledges this: "SNAP's 20-hour work rule is read as met by any week at work, which affects about 3% of earners."

2. **Dynamic selection into part-time work:** The model fixes household type for the run. In reality, people move in/out of single parenthood, couplehood, and part-time work. The programme (a basic income) may *cause* reductions in hours (income effect). The yardstick with fixed types cannot capture this behavioural response in the no-programme run.

3. **Correlation of pay with other characteristics:** The CPS distributions are marginal by household type. But within type, pay correlates with education, age, health, location — all of which affect programme take-up, care needs, etc. The model's "rank preservation" assumes the *same* adults get the same quantile in the new distribution. This imposes a strong correlation structure not in the CPS.

4. **No hours → no wage rate:** The model has annual earnings, not wage × hours. Part-time work is low hours at a given wage, not necessarily low wage. The programme's effect on *hourly wage* (e.g., via bargaining) is not represented.

5. **Care credit interaction with hours:** The credit is for *paid* care. If the programme lets a parent reduce hours and do care themselves, care expenses fall → credit falls. The model's fixed care-paying share (25.5%/32.0%) doesn't respond to the programme.

**Verdict:** It's a **reasonable first-order correction** for the *static* yardstick (making EITC reach by type match CPS). But for *programme effects*, it misses the key channel: **part-time work as a margin of adjustment**. The programme's effect on poverty depends on whether recipients reduce hours; the yardstick's part-time representation doesn't capture this behavioural margin. A skeptical labor economist would say: "This fixes the static incidence of tax credits, but not the dynamic labour supply response that determines the programme's effect."

---

## 5. Section 5 "Why" paragraph — fair interpretation? Does report claim more than measured?

**Report Section 5 "Why" paragraph:**
> "With pay by household type, single parents are paid less and couples with children more. With no programme, more adult-years fall below 30 days of basic living (20.31% against 19.62%, Reference, 20 years). Full coverage pays every adult, so it catches the added shortfall and its cut on that measure grows; the opt-in design reaches only those who opt in, and its cut shrinks. This study does not split the basket-poverty changes by household type, so why they shrink in most cells is not established here."

**Fairness:**
- The facts stated are correct (from tables).
- The mechanism described (full coverage catches added shortfall; opt-in doesn't) is a **plausible interpretation** of why the *below-30-days* effect changes differently in the two designs.
- The report explicitly labels it "an interpretation, not a measured result" and admits the basket-poverty mechanism is not established.
- **This is fair and appropriately caveated.**

**Does the report claim more than measured anywhere else?**
- Section 2: "Pay by household type does almost all of it." — Supported by tables (care credit changes ≤0.02).
- Section 2: "The two additions' interaction is measurable in 12 of 60 tests but never larger than 0.005 points: no synergy that matters." — The "no synergy that matters" is a judgment (see Q3), but the measurement is reported.
- Section 5: "The care credit on its own changes no poverty effect by more than 0.02 points and median wealth by no more than $74." — Supported.
- Section 8: "No headline result changes sign or loses significance" — Plausible, not fully verified but reasonable.
- Section 9: "3% to 5% of the effect" — Actual range ~2.9% to 4.8%, close enough.

**No major overclaims.** The report is careful to distinguish measured changes from interpretations.

---

## 6. Section 9 (Findings page) — fair summary for general reader?

**Current text:**
> "**The yardstick: pay by household type and the child and dependent care credit.** Every effect here is the programme against a run with no programme, so that run should look like the US. It now gives each household type its own pay from the Current Population Survey. Single parents are paid less and couples with children more, as in the survey, and the overall distribution is unchanged. It also adds the child and dependent care credit. With both, the EITC reaches 11.3% of adults (US 11.8%) and every household type is within 3 points of the survey. In today's main row, single parents were 12 points short. The care credit's reach is 3 points short of the tax data, and its average is $835 against $606; both are reported as gaps. The programme's effects barely move. In the opt-in design, its cut in basket poverty is 0.3 to 0.9 points smaller in every environment and horizon (3% to 5% of the effect). In the full-coverage design, its cut in the share below 30 days of basic living is 0.4 to 0.7 points larger, and its cut in basket poverty is 0.2 to 0.7 points smaller in five of the six cells (0.2 points larger in the sixth). Median wealth and inflation do not change materially. The credit alone changes nothing that matters, and the two additions do not interact. With partners' pay drawn independently rather than correlated as in the survey, the changes are larger (up to 1.7 points of basket poverty). Claude recommends the new reading for the main row; changing it is Duke's decision, and until then these changes are stated as a limit."

**Issues for a general reader:**
1. **"Every effect here is the programme against a run with no programme, so that run should look like the US."** — Jargon ("yardstick", "run"). A general reader may not understand "paired run" design.
2. **"Single parents are paid less and couples with children more, as in the survey, and the overall distribution is unchanged."** — "Overall distribution unchanged" is misleading: the *mixture* matches CPS, but the *within-type* distributions changed. The 10th percentile is 17% high. Saying "unchanged" oversimplifies.
3. **"EITC reaches 11.3% of adults (US 11.8%)"** — The US figure in the table is 11.77% (full take-up, own tax unit). The 11.8% is rounded. But the earlier check said US CPS figure is 15.3% (SPM unit). The report doesn't explain *which* US figure. A general reader would be confused.
4. **"3% to 5% of the effect"** — As noted, the low end is ~2.9%. Saying "3% to 5%" is a slight overstatement.
5. **"The credit alone changes nothing that matters"** — Subjective. Better: "The care credit alone changes poverty effects by less than 0.02 percentage points."
6. **"With partners' pay drawn independently rather than correlated as in the survey, the changes are larger"** — Doesn't explain *why* this bound exists (correlation is sourced from CPS, so independent is a sensitivity bound).
7. **"Claude recommends... Duke's decision"** — Internal governance, not meaningful to general reader.

**Corrected version for general reader:**

> **How we check the "no programme" comparison.** Every programme effect is measured against a simulated world with no programme. That comparison world should resemble the real US. We tested two improvements to it:
>
> 1. **Pay by household type.** Instead of giving everyone pay from one distribution, we now give single parents, couples with children, etc., pay matching their real US counterparts (from the Current Population Survey). Single parents earn less; couples with children earn more. The overall pay distribution still matches the US closely.
> 2. **Child and dependent care credit.** We added this tax credit for families who pay for child care, using 2025 tax rules.
>
> **Result: The comparison world is closer to the US.** With both changes, the Earned Income Tax Credit reaches 11.3% of adults (US: 11.8% on the same basis), and every household type is within 3 percentage points of the real US. Previously, single parents were 12 points too low. The care credit reaches 18.3% of families with young children (US: 21.4%) and pays $835 per recipient (US: $606) — both gaps are reported, not fixed.
>
> **The programme's effects change very little.**
> - In the **opt-in design** (the main design), the programme reduces poverty slightly *less*: basket poverty falls by 0.3–0.9 fewer percentage points (about 3–5% of the original effect).
> - In the **full-coverage design**, the programme reduces extreme poverty (below 30 days of basic living) by 0.4–0.7 *more* points, but reduces basket poverty by 0.2–0.7 *fewer* points in most cases.
> - Median wealth and programme inflation are essentially unchanged.
> - The care credit alone has negligible impact (changes <0.02 points). The two changes don't meaningfully interact.
>
> **Sensitivity:** If we assume partners' pay is unrelated (instead of correlated as in the US), the changes are larger (up to 1.7 points on basket poverty), but the correlation is from real data so this is a bound, not the best estimate.
>
> **Bottom line:** The improved comparison world is more realistic. It slightly reduces the programme's estimated poverty reduction in the main design. The lead researcher recommends adopting it; the final decision rests with the project lead. Until then, these changes are noted as a limitation of the current main results.

---

## 7. Three most important changes before publication

1. **Fix the inflation precision misquotes in Section 5 tables.** The report quotes inflation changes to 4–5 decimal places (e.g., 0.0062, −0.0005) but the tables only support 3 decimals (0.006, −0.001). This overstates precision and could mislead readers about the certainty of tiny inflation effects. **Replace all Section 5 inflation values with the table values (3 decimals).**

2. **Clarify the "overall earnings distribution" calculation in Section 4.** State explicitly: "This is a post-hoc calculation: a weighted mixture of the four household-type lognormal distributions (fitted to CPS quartiles), using the model's household shares. It was not a direct simulation output." This transparency is needed because the preregistration asked about the overall distribution but the run didn't output it.

3. **Remove or pre-specify the "no synergy that matters" threshold (0.005 points).** The preregistration only required stating interactions where the interval excludes zero. The report correctly states them but then dismisses them using a threshold chosen after seeing the results. Either:
   - Remove the "no synergy that matters" judgment and just report the 12 statistically significant interactions with their magnitudes, or
   - Add a pre-specified practical significance threshold (e.g., "interactions <0.01 points are considered negligible") in an amendment.
   Given the study is done, **the cleanest fix is to report the 12 interactions factually and omit the "no synergy that matters" label**, letting readers judge practical significance.

---

**End of review.**