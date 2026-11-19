# Preregistration: the private businesses' BU price at the sale (S90's fix), rerun of the v5.9 main rows

Committed Nov 18, 2026 by S90, before any run. Engine: compassionism-simulation at commit `b8ccd8d4b8f39a621db6186402877ba60be1904e` (main, the merge of pull request 163), which adds the option `sp.vAt: 'sale'` (off by default; with it off every output equals v5.9's, guard test identical).

## Why
S90 traced the damped two-year swing in the BU each adult spends (main row, Reference, seed 1: $22,838 in years 0-1, then $10,969, $21,452, $13,819, $19,472, $16,202) to the private businesses' lower BU price. The code paid it from last year's premium, shared by last year's BU. Duke's design sets it at the sale ("At a 3x conversion rate, a $9 / $12 / $15 menu becomes $3 / $4 / $5 in BU", Oct 1, quoted in compassionism-simulation `dev/reports/v5-1-private-esp-correction.md`). So the lag is a defect (research rule 9), and the swing reaches incomes, BU spent and expired, project hiring and programme cost by year. The fix: under `vAt: 'sale'` a BU spent at a private business buys 1 + vK dollars, where vK is that BU's premium after the conversion tax, payroll and the workers' match. The cut is paid as an advance that next year's premium repays exactly. Only the premium on payroll BU returned a year later (d73) is still shared a year late. Full record: compassionism-simulation `dev/DECISIONS.md` "S90" and `dev/reports/s90-private-price-at-sale.md`. Every published programme figure since v5.0 (Oct 2, 2026) uses the lagged rule. A first look on seeds 1-2 (inspection, not a result) moved the main row's cut in basket poverty by about 0.6-0.7 points.

## Questions
- Q1. Does the at-sale price remove the swing in every environment? Answer: the swing measure below, at the sale against lagged, per environment.
- Q2. How much do the v5.9 headline effects change (the five headline measures, both designs, three environments, 20 and 40 years)? Answer: the paired change, at the sale minus lagged, with its 95% interval.
- Q3. Does any headline statement on the findings page change in sign or in its stated rounding? Answer: a yes/no per statement, read under decision rule 4.

## Design
- **Rows.** The v5.9 main rows as `r2.js --part=M` builds them (no programme; the full-coverage design; the opt-in design), each programme row run twice: lagged (the published setting) and at the sale (`sp: Object.assign({}, row.sp, {vAt: 'sale'})`). The no-programme row does not read the option (it has no surplus split) and is run once.
- **Environments:** Reference, Adverse, Stress. **Horizons:** 20 and 40 years. **Adults:** 500. **Seeds:** 1-500, paired across all rows (common random numbers).
- **Where:** GitHub Actions (`run-study` in compassionism-sim-results; free), a new job `runner/jobs/s90.js` added by pull request before the dispatch. It builds the rows exactly as `r2.js --part=M` does, adds the at-sale copies, and calls the engine's `startRelease({baseline: true})`. Study ids `s90-sale-ENV-YRS`, folders `s90-sale-ENV-YRS-<engine, 7 characters>` with `run.txt` and `SHA256SUMS`.
- **Swing measure (Q1).** Run on the session machine with `node dev/tools/s90_trace.js` (compassionism-simulation; read-only probes, `--check` proves the copy's outputs equal the harness's), seeds 1-20, 500 adults, 20 years, three environments, lagged and `--sale`. It is the mean over years 2-12 of |BU spent per programme adult this year − last year| / this year.

## Checks (before any outcome is read)
1. The lagged programme rows and the no-programme row equal the published `r2-m-ENV-YRS-104691f` rows per seed, on every output key (the option is off on them).
2. Every folder has 500 seeds per row, its engine commit, a clean engine, and `run.txt` and `SHA256SUMS`.
3. The engine's accounting checks (`ACCT`) pass on the at-sale rows for seeds 1-5 in each environment (no identity fails; the premium identity included), run with the unit suite's method.

## Outcomes
- **Primary** (main row against no programme, per design, environment and horizon; as REPRODUCE.md's "Headline values" table defines them): below 30 days of basic living (unweighted); below the cost of living, basket poverty (unweighted); too little wealth, yearly average (unweighted); median real wealth in year-0 dollars (weighted); programme inflation (basket index above no programme, points a year).
- **Secondary:** FGT2 (poverty severity); mean real income; BU spent and BU expired per programme adult (20-year mean); programme cost (the testbed's cost keys); the weighted versions of the primary measures where the published tables give them.
- Gains are confirmed on basket poverty and wealth poverty, not FGT2 alone.

## Analysis
- For each outcome, cell (design × environment × horizon): the effect against no programme under each rule and the paired change (at the sale − lagged), mean over seeds 1-500, with a 95% paired bootstrap interval (2,000 resamples, generator seed 9001).
- The analysis script is added to compassionism-simulation (`dev/tools/s90_tables.py`) before the results are read; it prints checks 1-2 first and stops if one fails.
- No synergy claim is made (one change, not a factorial).
- Multiple comparisons: Holm across the five primary outcomes within each cell, for the statement "the change is not zero"; every interval is published unadjusted as well.

## Decision rules
1. If check 1, 2 or 3 fails, stop: nothing is read, the defect is found, and the run is redone after a dated amendment.
2. Q1: the fix is taken to work if, in every environment, the at-sale swing measure is below half the lagged one. If it is not, stop and report; the default does not change.
3. If rule 2 holds, the at-sale price is the corrected model. Its figures replace the main rows' figures at the next release (Duke assigns the version), with an entry in the Hub's corrections log. The lagged figures stay published as the v5.9 record (the OSF registration is the frozen v5.9 model). This holds whichever way the figures move.
4. Q3: a findings-page statement changes if the at-sale effect changes sign, or if its rounding as printed changes. Each changed statement is listed with both figures.
5. Every other published study that runs programme rows (the main rows' readings, financed rows and 10,000-adult rows, `r2-s/f/b`; the central-bank study `s74-final-3beb5ff`; the history study `s75-eras-e5649ef`; the supply study S82; the suite folders `x2`, `x3`, `x4`; the v5.0-v5.6 panels) gets a dated note on its page or report: it paid the private price a year late, the main row's change was the figure Q2 found, and a rerun is or is not planned. A rerun of any of them is its own preregistered amendment.

## Reporting
Every cell above is published in compassionism-sim-results and in the plain-words report, including changes against the programme and changes too small to matter.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
