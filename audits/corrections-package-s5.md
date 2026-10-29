# Corrections Package, Session 5 Addendum (C23–C30)

Sep 27, 2026 · Compassionism Simulation, next round, workstream B · hub repos checked at `research-hub` `4e8d3af` and `bettertobest.github.io` `a468ea2` (the session 4b package is not pushed yet)

Read with: `corrections-package.md` (C01–C22) and `session-5-handoff.md`. Apply these after C01–C22. Every item is a decision, and each is drafted at its default.

The claims ledger CSV was not in the project box this session, so the new records below carry their own IDs (S5-01 to S5-13). The next ledger build should merge them.

## What was checked

The four research-summary claims that were still untraced, and the five BLEI worked-example figures held since session 4b. Each was traced to its paper on the hub and, where the paper gives numbers, the arithmetic was reproduced in a script (`s5_checks.py`).

| ID | Claim (research summary) | Traced to | Result | Class | Status |
|---|---|---|---|---|---|
| S5-01 | $1.5 trillion in prohibition costs | Drug policy paper, §4.1 | Matches none of the paper's own totals | Unsupported | Retire (C23) |
| S5-02 | $847 billion in potential savings over 25 years | Drug policy paper, §7.1 | Is one line of one scenario, not the net | Unsupported | Retire (C23) |
| S5-03 | 15–20% market penetration within a decade | Real estate paper, conclusion | Contradicted by the paper's own rollout table | Unsupported | Restate (C24) |
| S5-04 | $70,000 average household wealth | Real estate paper, §4.3 | The paper's figure is over 20 years; no model is published | Target (projection) | Restate (C24) |
| S5-05 | ROI of $1,847 per beneficiary | Development paper, §4.2 | An NPV, not an ROI, and does not follow from the paper's formula | Unsupported | Retire (C25) |
| S5-06 | $85,000 in interest savings (avalanche method) | PTH financing paper, §2.2–2.3 | Not reproducible from the paper's own example | Unsupported | Retire (C26) |
| S5-07 | Sustainability demonstrated at 30–40 households | PTH financing paper, §6.1 | An assumed break-even table, not a demonstration | Design parameter | Restate (C26) |
| S5-08 | 18.3 days (baseline BLEI) | BLEI paper, Appendix B.1 | Reproduces: $1,249.96 ÷ $68.33 = 18.3 | Derived | Keep |
| S5-09 | 71.3 days at entry | BLEI paper, Appendix B.2 | The paper's own derivation gives 70.7 | Derived (misstated) | Restate (C27) |
| S5-10 | 730+ days at month 33 | BLEI paper, Table 3 | Depends on a saving rate the paper never states | Derived (unstated assumption) | Restate (C27, C28) |
| S5-11 | ~33 months, range 28–47 across ε_food | BLEI paper, Table 2 text | No derivation published | Derived (unreproducible) | Restate (C28) |
| S5-12 | FBS $2,281/month | BLEI paper, Appendix B.4 | Reproduces, using the EDC target of 0.025 | Derived, conditional (d13) | Keep, label (C29) |
| S5-13 | Gini ≤0.22 (EDC-adjusted), ≤0.25 (nominal) | Front page and research summary | The measure is never named (d20) | Target | Restate (C30) |

## C23. Drug policy blurb: retire both figures

**Location:** `research-summary.html`, paper index, Drug Policy Reform entry.

**Current:** Cost-benefit analysis revealing $1.5 trillion in prohibition costs versus $847 billion in potential savings over 25 years.

**Proposed:** A cost-benefit framework comparing drug prohibition with regulatory alternatives over 2- to 50-year horizons, using the paper's own cost estimates.

**Why:**
- The paper's cost table (§4.1, 1953–2024) sums to **$4,616B**. Its four columns total $1,210B (enforcement), $1,047B (incarceration), $857B (social) and $1,502B (opportunity costs), and every row and column adds up. The abstract's "$1.52 trillion" matches none of these; it is closest to the opportunity-cost column alone. The conclusion calls it "direct costs", which the table puts at $1,210B.
- "$847 billion" is the *health cost reductions* line of the paper's **traditional** regulatory scenario (Scenario 2). The paper's own net benefit is **$3,870B** for that scenario and **$5,044B** for the integrated one (both reproduce). The abstract attributes $847B to integrated governance as the net.
- The table's line items are not traced to data. The Sources paragraph names agencies (BJS, DEA, CDC, BLS) but no series.

**Options:** retire the figures (default); restate them with the table's own totals, labeled as the paper's unsourced estimates.

**Paper body (for the session 7 pass):** the abstract, §1 and §10 need to agree with §4.1 and §7.1.

## C24. Real estate blurb: restate

**Location:** `research-summary.html`, paper index, "Transforming the US Real Estate Market Through Public Trust Housing".

**Current:** Modeling shows PTH achieving 15–20% market penetration within a decade, with average household wealth accumulation of $70,000 — without displacing private homeownership.

**Proposed:** Sets out a phased rollout reaching 200,000–400,000 participating households by years 8–12, and projects average Acre Equity of $70,000 per household over 20 years (the paper's projection; no model is published) — without displacing private homeownership.

**Why:**
- The paper's own rollout table (§4.2, Phase 3, years 8–12) gives **8–12%** penetration, not 15–20%.
- Neither percentage fits the paper's own household counts. 200,000–400,000 households is 0.45–0.91% of the 44 million renter households the paper cites, and it does not say which market the percentage refers to.
- The $70,000 is over **20 years** (the paper's abstract and §4.3). The summary pairs it with "within a decade" (session 4b finding 3).
- The paper says "mathematical modeling demonstrates" but publishes no model.

**Options:** restate as above (default); drop the penetration figure and keep only the $70,000 projection.

**Also noted:** this paper gives operational sustainability at 40–60 households, while the PTH financing paper gives 30–40 (see C26).

## C25. Development blurb: retire the ROI figure

**Location:** `research-summary.html`, paper index, "Community-Based Monetary Innovation for Development".

**Current:** Development economics framework targeting poverty reduction below 5% within 15 years, with a superior ROI of $1,847 per beneficiary compared to traditional foreign aid models

**Proposed:** Development economics framework targeting poverty below 5% within 15 years (a design target), with an illustrative net-present-value comparison against microfinance, conditional cash transfers and foreign aid under assumed benefit streams

**Why:**
- $1,847 is a net present value, not a return on investment.
- It does not follow from the paper's own formula: −$300 + Σ(t=1..10) $180 × 1.1^t ÷ 1.05^t = **$2,046**. With growth starting in year 2 it is **$1,832**. Neither is $1,847.
- The three comparator NPVs do reproduce ($236, $19.5 and −$382), so the arithmetic method is sound and only the CCO figure is off.
- The CCO benefit stream ($180 a year growing 10%) is an assumption, not an estimate.

**Options:** retire the figure (default); restate as "an illustrative NPV of about $2,000 per beneficiary under assumed benefits".

## C26. PTH financing blurb: retire $85,000, restate 30–40

**Location:** `research-summary.html`, paper index, "PTH Independent Financing Models".

**Current:** including the "avalanche method" for collective mortgage payoff — achieving $85,000 in interest savings — with sustainability demonstrated at just 30–40 participating households.

**Proposed:** including the "avalanche method" for collective mortgage payoff, and the paper's assumed break-even thresholds for each financing model (30–40 households for pay-in-focused trusts).

**Why:** the paper's five-homeowner example (§2.2) does not support the figures.

- **Same payments.** At the example's own pooled payments ($7,050 a month), paying the highest rate first retires all five mortgages in **18.3 years**, against an 18.4-year individual average, and saves about **$900** of interest. It does not save $85,000, and it does not finish in 10 years.
- **What a 10-year payoff takes.** It needs about **$10,000 a month**. At that level the saving comes from paying more each month, not from pooling.
- **The example's own inputs are off.** Homeowner C ($150,000 at 7.2%, $1,200 a month) needs 19.3 years, not 15. The individual average is therefore 18.4 years, not 17.6.
- **The 30–40 households.** This comes from a break-even table of assumed values (§6.1), not from a demonstration.

**Options:** as proposed (default); retire the whole clause.

**Paper body:** §2.3's timeline and savings need a worked schedule or restating.

## C27. BLEI table row: correct the entry figure, qualify month 33

**Location:** `research-summary.html`, key metrics table, BLEI row.

**Current:** 18.3 days (baseline) → 71.3 days at entry → 730+ days at month 33 (Flourishing tier)

**Proposed:** 18.3 days (baseline) → 70.7 days at entry → about 730 days by month 33 if the household also saves about 10% of its financial bandwidth (Flourishing tier; illustrative)

**Why:**
- **Entry figure.** Appendix B.2 computes $2,239.96 ÷ $31.67 = 70.7 days and then writes "≈ 71.3 (rounding)"; 70.7 does not round to 71.3. At ε_food = 2.64 instead of $2.75 per food BU (C13), it would be 69.5 days.
- **Months 12, 33 and 60.** Appendix B derives Month 0 only. The later figures need a cash-saving rate the paper does not state. I reconstructed the path with the paper's base parameters: γ 0.20, h_AE 0.60, and $600 a month into Acre Equity at 4%. Saving about **$232 a month (10% of the $2,281 FBS)** reproduces month 12 exactly (303 days) and gives 714 days at month 33 and 1,270 at month 60, against the stated ~730 and ~1,328. It crosses 730 at month 34.
- With no cash saving, the same household reaches only 472 days by month 33.

**Options:** as proposed (default); keep 730+ at month 33 and add the saving assumption to the paper first.

## C28. Flourishing-entry horizon: label as illustrative

**Locations:** `research-summary.html` and `index.html` (headline metrics list); `ai-index.json` and `ai-manifest.json` (`near_poverty_flourishing`, `blei_flourishing_horizon`); `research-index.json` (BLEI paper abstract).

**Current (summary and front page):** BLEI Flourishing entry (near-poverty): ~33 months (sensitivity range: 28–47 months across ε_food ∈ [1.50, 3.00])

**Proposed:** BLEI Flourishing entry (near-poverty, illustrative): ~33 months under the BLEI paper's optimal parameters and an assumed saving of about 10% of financial bandwidth; the paper reports 28–47 months across ε_food ∈ [1.50, 3.00] but does not publish that derivation

**For the AI-facing files:** append "(illustrative, under optimal parameters and an assumed saving rate)" to both string values. If session 4b's C-items already restate these locations, keep that wording and add the saving-rate clause.

## C29. FBS $2,281: keep, and say what it assumes

**Locations:** `research-summary.html` (3) and `index.html` (2).

**Change:** after "$2,281/month", add "(assuming the EDC target of 0.025 is met)".

**Why:** Appendix B.4 reproduces exactly: $2,083 + $1,200 − $950 − 0.025 × $2,083 = $2,280.92. But the 0.025 is the CCO-PTH EDC target, and d13 labels results that use it as conditional on the target being met.

## C30. Gini targets: name the measure (d20, decided by Claude)

**Locations:** `index.html` and `research-summary.html`, integrated metrics, the two Gini target items.

**Change:**
- In the EDC-adjusted item, after "(EDC-adjusted)" in the label, add: "disposable income".
- In the nominal item, after "(nominal)" in the label, add: "disposable income, OECD definition".
- At the end of the nominal item, add: "The simulation reports a wealth Gini, so it cannot yet test either target."

**The decision:**

| Option | For | Against |
|---|---|---|
| **Disposable income, both levels kept (adopted)** | The nominal target is offered for comparison with published benchmarks, which are income Ginis. ≤0.25 is at the low end of what OECD countries achieve today, which makes it ambitious but observed. | ≤0.22 (EDC-adjusted) has no external benchmark, because the adjustment is the framework's own. |
| Disposable income, retire the EDC-adjusted target | One target, fully benchmarked | Drops a framework measure you may want |
| Wealth | Matches what the simulation reports | Wealth is far more unequal than income everywhere, so ≤0.25 would have no real-world precedent |

**Source for the benchmark:** OECD, *Society at a Glance 2024*, ch. 6. In 2021 the disposable-income Gini ranged from around 0.22 in the Slovak Republic to more than twice that in Chile and Costa Rica. The Nordic and some central European countries had the lowest inequality.

**Simulation follow-up:** an income Gini in `headline` is part of the A5 reporting upgrade (session 7).

## Found, for the paper-body pass (no summary change)

- **BLEI paper, EPPM 5.80×.** It uses a baseline EDC of 0.625. The paper's own Appendix B.3 computes 0.744 for the same household and notes that this is outside its stated 0.625–0.72 range. At 0.744 the EPPM would be 8.5×. This belongs with C13.
- **Real estate paper, pay-in pathway.** It gives an average 20-year accumulation of $168,000 or more, against the paper's $70,000 average. That is not necessarily a conflict across pathways, but the paper does not reconcile the two.
