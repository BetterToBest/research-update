# Preregistration: distribution measures (S57)

Committed 2026-11-09 by S57, before the build and before any run. (Two wording corrections made the same day, before any run: the income Palma flag, and the test in K2(f).) Engine: compassionism-simulation at `6e06c91d0a1c67447386e9aea3bf344817517190` (main, after S61). The build adds a reporting-only study option on a `claude/s57-distribution-measures` branch; the commit each result comes from is written in its `run.txt` (a result is valid only if the guard test, the unit tests and the checks in "Decision rules" passed on that commit).

This is reporting only. It adds measurements to what a run already computes. No random draw, no rule and no figure changes; with the option off, every output is identical to today's.

## Questions
- Q1. Where does the no-programme start sit against the outside distribution figures (checks, never targets)?
- Q2. Under the programme, how do the top shares, the bottom shares, the ratios, the real percentiles and the Gini measures differ from the no-programme run, in each environment?
- Q3. Who gains and who loses: the growth-incidence curve (each wealth and income percentile, programme against no programme, same seed).
- Q4. How much do families move between wealth fifths over the run, with and without the programme?
- Q5. How does labour's share of money income differ with the programme?
- Q6. How deep is debt (median debt, debt against income), beside the share of families in debt?

## Design
- Study option `dm` (true, or an object overriding the defaults), set on a study's options, so it applies to every row of the study, the no-programme rows included. Rows are therefore compared by the analysis tool on the same seed ("both runs of every row").
- Reported at two moments: the end of Year 0 (suffix `S`, the start, after the first year's flows, as the engine's own Year 0 figures are) and the end of the last year (suffix `E`). The run-average labour shares (`PY`) use every year.
- Units: every dollar in Year-0 dollars (nominal divided by the engine's price level for the year, as `tbRepYear` does). Wealth is the adult's net worth with debts kept (`a.wealth`). Income is the adult's disposable income (`a._tbDisp`, the Gini's own income). The unit is the adult; the family is used only for debt, as the engine's families-in-debt figure does.
- Weights: every adult carries a weight `a._w` (1 until S59's tail exists). Every share, percentile and rate below is weighted; at weight 1 each equals the plain version (unit test).
- Studied rows for the pilot (reduced seeds, session machine, free): the frozen yardstick's release row (`frozenRow`, CPS earnings, today's safety net) and the C2.2 design, each against its no-programme run; the three environments (Reference, Adverse, Stress); seeds 1-100; 500 adults; 20 years. The frozen batch (S47/S48) stores no per-adult data, so none of these measures can be recomputed from it except `eGiniWN`, which it already holds; the batch's rows are listed for S63, which decides whether the main rows run again with `dm` on.
- No money is spent; nothing runs on Runpod.

## Outcomes
Family: preregistered secondary (the study programme's five primary outcomes and their Holm adjustment are unchanged by this step). Every table names its family and whether its intervals are adjusted (review item A4).

Per run and moment (keys `dm<measure><S|E>`, S the end of Year 0 and E the end of the last year; the matrix and grid keys carry an index):
1. Gini of wealth with debts counted as zero, `eGiniW`, and with debts kept, `eGiniWN` (both already in every run; named in full in every table).
2. Top 1% and top 10% share of wealth, and of disposable income, in percent of the total (wealth net worth with debts kept, so a share can exceed what a debt-free reading gives).
3. Bottom 50% share of wealth (can be negative where debts exceed assets), and of income.
4. Palma ratio of income: the top 10% over the bottom 40% of disposable income (flag key `dmYpOk` = 1 when the bottom 40% hold positive income; the ratio is 0 otherwise and left out of every table).
5. Wealth top-10-to-bottom-40 ratio, named exactly that, reported only where the bottom 40% hold positive wealth (flag key `dmWrOk` = 1; otherwise the ratio is set to 0 in the key and left out of every table).
6. Real wealth and real income at percentiles 1, 5, 10, 15, ..., 95, 99 (21 points; P10, P25, P50, P75, P90, P99 among them). P99.9 and the top 0.1% share are not reported: 500 adults cannot support them, and S59's tail comes first.
7. Growth-incidence curve: the difference between the programme run's and the no-programme run's value at each of the 21 percentiles, wealth and income, last year, same seed (derived by the analysis tool from item 6; it compares the same rank in the two distributions, not the same person, which the tool states).
8. Mobility: the 5 by 5 matrix of the share of adults (percent of each Year-0 wealth fifth) found in each wealth fifth at the end of the last year. Only adults present at Year 0 are followed (those replaced by ageing are not); the count followed is reported. Fifths are assigned by weighted rank, ties broken by position in the list.
9. Labour's share: wages over money income (`tbCashIncome`: wages, conversion proceeds, transfers, Social Security), and wages plus conversion proceeds over the same, at Year 0, the last year and as the ratio of real sums over all years (`PY`). A modelling choice: the model has no separate capital income, so this is the labour share of money income, not of national income.
10. Debt: share of families in debt (as the engine's `hhDebt20`: a family is a household, or an adult where households are off); median debt among families in debt (Year-0 dollars; 0 if none); debt against income (sum of debt of indebted families over the sum of their members' disposable income; 0 if none). The members' disposable income is the engine's per-adult figure summed, which for couples is the household's pooled figure per adult.
11. Number of adults, and number followed in the mobility matrix.

## Analysis
- Estimates per environment and design: the programme run minus the no-programme run on the same seed, as the mean of the paired differences; for a start-of-run check, the no-programme mean with its interval.
- Intervals: paired bootstrap over seeds, 2,000 replicates, resampler seed 57, the same resample for every cell; 95% percentile interval. Ratios and shares are computed per seed first, then averaged (no ratio of means).
- Tests per family: cells = environments (3) x designs (2) x measures reported; a cell's two-sided bootstrap p-value is twice the smaller tail share (floor 1/2001). The report gives the number of cells whose interval excludes zero beside the number that survive Holm within the family, and says the intervals shown are not adjusted. "Interval excludes zero" is never written as "material".
- Checks of the no-programme start (never targets), Year 0, all three environments, the Reference environment first: CBO (Oct 2024, 2022 wealth): top 10% hold 60% of family wealth counting Social Security wealth, 69% without; bottom half 6%. Federal Reserve Distributional Financial Accounts, Q2 2026: top 1% hold 32.5%. The engine's net worth excludes Social Security wealth, so the comparison is made with the 69% figure; the 60% figure is shown beside it. Every gap is reported; no constant is changed for them (the engine's wealth start comes from the SCF's percentile table, and the SCF omits the Forbes 400; S59 addresses the top).
- Mobility summaries from the matrix by the tool: share staying in the same fifth (the diagonal mean), share moving up, share moving down, and the share of the bottom fifth reaching the top two fifths.

## Decision rules
Written before the build; each is a pass/fail on the engine, not on the results.
- K1. With `dm` off, a full-output diff against main is identical and the guard test passes; with it on, every key the engine already reports is identical (reporting only).
- K2. Unit tests: (a) weights all 1 equal the plain quantile and shares; doubling one adult's weight equals listing the adult twice; (b) shares: top 10% >= top 1%, the bottom 50% + the top 50% = 100%; a perfectly equal population gives shares 1, 10, 50 and Palma 0.25; (c) the mobility rows sum to 100 and the identity case gives the identity matrix; (d) the labour share is between 0 and 100 with no programme income equal to wages; (e) debt keys on a hand-made set of families; (f) in a run, the families-in-debt share in the last year equals the engine's own `hhDebt20`, and `eGiniW` and `eGiniWN` are both reported in every run (`eGiniWN` can exceed `eGiniW` or fall below it; no order is assumed).
- K3. The `lineage` record, the three checks (`validate`, `unit`, `domtest`) and `no_figure_change.py` pass; the new data file is new, so no published number moves.
- If the no-programme top 10% share at Year 0 differs from the CBO/DFA checks by more than 10 points, the report says the start is not matched and which way, and S63 is told; the step makes no change to the start.
- The pilot's statements are limited to what the intervals support: a measure is said to differ with the programme only where the paired interval excludes zero, and the report does not describe a difference as large or small without the dollars or points beside it.

## Reporting
Every cell is published: the full tables and the per-seed estimates (every row, environment, measure and moment, null results included) in compassionism-sim-results, folder `s57-distribution-<engine commit, 7 chars>`, with run.txt and SHA256SUMS; the report in compassionism-simulation `dev/reports/s57-distribution-measures.md` in plain words, naming the family and the adjustment state of each table; the findings page's data file `data/studies/s57-distribution.json` (a new file; the guided sections' numbers do not move).

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.

### Amendment 1 (2026-11-09, after the pilot's first analysis, before it was published)
- The Holm step reads the normal tail of each cell's mean over its bootstrap standard error, not the bootstrap tail share. Reason: a 2,000-replicate bootstrap tail share cannot go below 1/2,001, which is above Holm's first threshold (0.05/378) for a family of 378 cells, so no cell could survive; the first analysis showed 0 of 366. The bootstrap tail share stays in `estimates.csv` as `p_boot`. Intervals are unchanged (percentile, 2,000 replicates, seed 57).
- Pilot rows: the no-programme run, the release row and the C2.2 design on the frozen yardstick, as the Design section says; Adverse and Stress share one no-programme run (they differ only in the programme's settings), so their no-programme columns are identical. Year 0 is identical in all three environments.
