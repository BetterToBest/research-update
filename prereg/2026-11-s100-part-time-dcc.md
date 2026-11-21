# Preregistration: part-time work and the child and dependent care credit in the no-programme yardstick

Committed Nov 21, 2026 by S100, before any programme row was run. Engine: compassionism-simulation, the merge of branch `claude/s100-part-time-dcc` (commit recorded in "Engine commit" below before the first run). Ledger I15 (opened by S34).

Claude's reading: compassionism-simulation `dev/reports/s100-part-time-reading.md`. Values: `sources/s100_earnings_by_household.py` and `.json` (CPS ASEC 2026 public-use file; IRS SOI Table 3.3, tax years 2022 and 2023; IRS Publication 503 (2025), all opened Nov 21, 2026). Job script: compassionism-sim-results `runner/jobs/s100.js`.

## What was read before this was written
Only no-programme runs (the yardstick), at 20 to 500 seeds, Reference, 20 years, to build and check the readings: today's main row has EITC reach 8.8% as it reports it (take-up 80.8%) and 10.9% at full take-up; the CPS figure the earlier check compared with (15.3%) counts the adult's SPM unit, and the like-for-like figure (own tax unit) is 11.8%. By household type, single parents 37.1% against 49.8%, couples with children 19.7% against 16.5%. With pay by household type: 48.7% and 16.5%; overall 11.2% at full take-up. The care credit reaches 17.8% of households with a child under 13 (take-up as measured) and pays $842 per receiving household; basket poverty in the no-programme run moves from 36.1% to 36.5% (50 seeds). Two seeds of every row below were run to time the job; no programme figure from them was read (the file was deleted unread).

## Questions
- Q1. **The yardstick.** With each reading, how close is the no-programme run to US data on: EITC reach overall and by household type (own tax unit, full take-up), refundable CTC reach by type, the care credit's reach and mean against the tax data, and the overall earnings distribution (still the CPS's)?
- Q2. **The effect.** How much does each reading change the programme's effect on the five primary outcomes, by design, environment and horizon?
- Q3. **Synergy.** Do pay by household type and the credit interact (the 2×2 interaction contrast)?
- Q4. **Bounds.** How much do the answers depend on the credit in the programme run (paid only in the no-programme run), partners' pay correlation (0), and the credit read for every family?

## Design
- **Readings** (row options; engine `index.html` `EARN_HH`, `ehTypes`, `ehAdjust`, `CFG.EH`; `snBen`, `CFG.SN_CDC`): `off` (the release main row); `eh` (pay by household type, partners' normal-score correlation 0.2198); `cdc` (the credit, tax year 2025 rules, for households that pay for care: 25.5% of single parents, 32.0% of couples, by a fixed hash); `both`; `pc0` (both, correlation 0); `call` (both, the credit read for every household with a child under 13).
- **Rows**, per environment and horizon (22): for each reading, `none.R` (no programme), `c22.R` (full-coverage design), `rel.R` (opt-in design); `c22.bound` and `rel.bound` (pay by type, no credit in the programme run; paired with `none.both`); `none.off.full` and `none.both.full` (no programme, tax-credit take-up 1). Every row is the release's main row: `harness.js` `r2FreezePair` with the private BU price at the sale (`sp.vAt 'sale'`), and `sn.rep` true (reporting keys only).
- Environments Reference, Adverse, Stress; horizons 20 and 40 years; 500 adults; seeds 1-500, paired across every row.
- Runs on GitHub Actions (compassionism-sim-results `run-study.yml`): study `s100-<env>-<years>`, job `s100.js`, job arguments `--env=<env> --years=<years> --procs=4`, seeds 1-500, 10 shards. Folders `s100-<env>-<years>-<engine 7>`.

## Checks (before any outcome is read)
1. `none.off`, `c22.off`, `rel.off` equal the published at-sale rows (`s90-sale-<env>-<years>-b8ccd8d`: `none`, `c22.sale`, `rel.sale`) per seed on every key those rows hold.
2. Every folder has DONE, run.txt and SHA256SUMS (each sum verified), shards cover seeds 1-500 once, the engine commit is the one below, and every row has 500 values per key.
3. The engine's guard test, unit tests (including the seven care-credit and pay-by-type tests) and `validate` pass at the engine commit.

## Outcomes
- **Primary** (as the at-sale rerun's): `bNAPy` below 30 days of basic living; `fgt0PY` basket poverty; `ppovA` too little wealth (mean of `ppov_1..ppov_{T-1}`); `wtMedE` median real wealth (weighted); `endoAnn` programme inflation. Each as the programme's effect: programme row minus its no-programme row, paired by seed.
- **The change**: effect under reading R minus effect under `off`, paired by seed (a difference in differences).
- **Yardstick** (no-programme rows): `snEitc`, `snCtc`, `snCdcK`, `snCdcR` and the by-type keys `snEitcSg/Sp/Cn/Ck`, `snCtcSp/Ck`; levels of the five primary outcomes.
- **Secondary:** `fgt2PY`, `Er`, `dmYp50E`, `cost`, `wtF0E`, `wtPovE`, `snCdcM`, `snEitcM`, `snCtcM`.

## Analysis
- Means over seeds 1-500; 95% intervals by paired bootstrap, 2,000 resamples, generator seed 9001 (numpy `default_rng`), the same resample for every row; Holm across the five primary outcomes within each cell (design × environment × horizon) for "the change is not zero".
- Q3: interaction = (both − cdc) − (eh − off) on each primary effect, with its bootstrap interval; a synergy is stated only where the interval excludes zero.
- Yardstick gap rule (the earlier check's): a share more than 3 points from the US figure, a dollar amount below 0.80 or above 1.25 times it.
- US comparison figures (fixed now): EITC reach, own tax unit, full take-up: all 11.77%, single adults 8.62%, single parents 49.77%, couples without children 4.55%, couples with children 16.54%; refundable CTC, own tax unit: single parents 45.31%, couples with children 19.00%; care credit: 21.37% of families with a child under 13 (5.72 million returns, tax year 2023, over 26.76 million families), $606 per return.

## Decision rules
1. If a check fails, no outcome is read until the cause is found and fixed; a fix to the engine is an amendment and a full rerun.
2. **The yardstick reading.** `both` is the reading Claude recommends for the release main row if, at Reference and 20 years, its overall EITC reach (full take-up) is within 3 points of 11.77% and the by-type reach of at least three of the four household types is within 3 points of its US figure, and it is closer to the US than `off` on the sum of the four types' absolute gaps. The size or sign of any programme effect plays no part in this rule (no target result).
3. **Into the main row** only by a ledger decision (Duke's: a change to the main row). Default while it is open: the release keeps today's main row, and its text states the limit with this study's measured changes (D35).
4. **What the text says**: for every primary outcome whose change has a Holm-adjusted 95% interval excluding zero in a cell, the change is stated with its interval, in whichever direction. Changes whose interval includes zero are reported as "no measurable change". The bound rows are printed beside the main reading in every table.
5. The care credit's mean against the tax data is reported as a gap if it exceeds 1.25 times $606 (the pilot found $842); it is not tuned.

## Reporting
Every row, environment and horizon goes to compassionism-sim-results (six folders and a tables folder) and to the findings page's section on the yardstick, including null and unfavourable results, the Adverse and Stress environments, and the bounds.

## Engine commit
compassionism-simulation `e50a3b359018e2be1929d700b49630f07f337473` (main, the merge of PR 180; guard test, unit 423 of 423, validate, domtest 162 of 162, lineage proved). Recorded Nov 21, 2026, before the first run. Results folders: `s100-<env>-<years>-e50a3b3`. 20-year cells 10 shards, 40-year cells 20 shards (the number of shards changes no figure).

## Amendments
- **Nov 21, 2026, after the run (reading notes; the design, the analysis and the decision rules are unchanged).** Three choices made while reading the tables, stated in the report (compassionism-simulation `dev/reports/s100-part-time-dcc.md`) and `dev/DECISIONS.md`: (1) Question 1's "overall earnings distribution" was not a key the job reports, so it is read as a derived calculation from the engine's four household-type distributions weighted by the model's household shares (quartiles and the 90th percentile within 1% of the CPS; the 10th percentile 17% high, as with the single distribution), labelled as a calculation, not a run result; (2) the care credit's reach is compared with the tax data at take-up as measured, because the tax data count claims (18.30% against 21.37%: a gap by the rule, 0.07 points past it); (3) the interaction: 12 of 60 intervals exclude zero, all at most 0.005 points; the report states them with their size and calls them negligible. Results: compassionism-sim-results `s100-tables-e50a3b3` (checks pass in all six folders; decision rule 2 holds).
