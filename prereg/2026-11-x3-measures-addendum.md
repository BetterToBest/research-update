# Preregistration addendum: job X3, the BLEI paper's other measures and the measures study for release 2 (S79)

Committed Nov 16, 2026 by S79, before any run. Engine: compassionism-simulation at commit `6d095a1eefe71abbb025b82e8942cd80cfe9a34a` (the merge of compassionism-simulation PR 138, which adds `dev/tools/explore_export.js --r2 --study`; `harness.js` and `index.html` as at that commit, unchanged from release 2's engine block). Job script: compassionism-sim-results `runner/jobs/series-r2.js --study` (PR 51, merged as results commit `e88585d`). Like job X2, it runs on GitHub Actions (free), not Runpod.

## Why this run
The visual suite (`suite.html`) has a release 2 view with the BLEI series from job X2 (`x2-5b62481`). For the BLEI paper's other five measures and for the measures study, it says they exist for release 1 only. Release 2's stored results (`r2-*-104691f`) do not hold them. A check made before this run (compassionism-simulation `dev/reports/s79-r2-measures-check.md`) found that the engine can report all of them for release 2's main row without changing the model. EDC and FBS need two reporting switches that release 2's rows did not carry. The rest is computed per adult from quantities the engine already keeps. This is a reporting run: it adds no setting, row or claim. It re-runs release 2's main row and records more of what happens in it.

## Questions
Q1 (EDC). What share of income goes to rent paid to landlords and interest on debt (the measured Extractive Drain Coefficient), over person-years, under no programme, the C2.2 design and the release design? How does each design change it against no programme?
Q2 (EPPM). How far do people's real resources go with the programme against the same person without it (each adult against their no-programme twin on the same seed), for participants, non-participants, the poorest fifth and other groups, and from which parts (cash, interest, allowance, other basket changes)?
Q3 (FBS). What is the monthly surplus above basic living, for every adult in both runs, and what share of participant-years reaches the surplus at which the chance of advancing a tier is even?
Q4 (CSI). What share of adults have two years or more of basic living, on the ladder and adding Acre Equity, and what is community-housing members' median Acre Equity, in days?
Q5 (IPBI, partly modelled). What public costs (prisons, hospital and psychiatric stays, homelessness) does each design avoid per adult a year, against the programme's cost?
Q6 (measures study). By income fifth (the twin's cash income), household type, age band and membership: who is under 30 days, what the programme gives and takes, who is better off than their twin; how adults move between the six tiers (into and out of Crisis); and the wealth Gini, ordinary and net of drain.
All descriptive: an answer is the figure with its spread across seeds (and, where stated below, a paired difference with a 95% interval), not a test.

## Design
- Rows: release 2's main row (`harness.js` `r2FreezePair`, ledger D25 and D26): no programme (`base`), the C2.2 design (`c22`) and the release design (`release`), with release 2's study options (`r2MainStudy`), 500 adults and the wealth floor not changed. Added to every row: the measured EDC (`em`) and the FBS50 tally with each adult's own advancement rate (`fb {dist 'lambda', scale 1}`, the rule release 2 ran), both reporting only. The accounting check (ACCT) runs for the per-adult flows. Each seed's three rows run one after another, each in its own study call on that seed. No other row.
- Environments: Reference, Adverse and Stress (`ref`, `adv`, `st`; part M's `str`).
- Horizons: 20 and 40 years, each its own run.
- Seeds: 1-500, paired across rows (common random numbers).
- Where and how: GitHub Actions, compassionism-sim-results' run-study workflow; study `x3`; engine `6d095a1eefe71abbb025b82e8942cd80cfe9a34a`; job `series-r2.js`; arguments `--env=all --years=20,40 --n=500 --study`; seed range `1-6`, 6 shards (shard I runs environment and horizon I over seeds 1-500 in one process). Per shard: `node dev/tools/explore_export.js ENV YEARS 500 1 --r2 --study --panel=RESULTS/r2-m-ENV-YEARS-104691f/shard-0000.json.gz`. Results folder: `x3-6d095a1/` with `run.txt` and `SHA256SUMS`. Expected time: about 30-45 minutes for a 20-year shard and 60-90 minutes for a 40-year shard (local test: 3.3 seconds per seed for the three rows at 20 years, 6.5 at 40).

## Outcomes
All descriptive. Definitions: compassionism-simulation `dev/tools/study_fields.js` (the measures study) and `index.html` (EDC_KEYS, FBS_KEYS).
- `study` (for each row and year: the mean over seeds and the 10th and 90th percentile across seeds), all 152 series keys the export writes, including: EPPM `eppm_*` and its parts `eD_* eI_* eB_* eP_*` and the share better off than the twin `up_*` (groups all, part, non, pq1, pth, ptf, q1-q5, hs, hc, hk, a1-a4); the monthly surplus `sur_*` and the share with none `sur0_*`; cash `cash_*`; Acre Equity in days `eqd_*`, `eqdMedPth`, `pthShare`; two years or more of basic living `b730_*` (ladder) and `c730_*` (with Acre Equity); by fifth `bO_q* sur_q* recv_q* paid_q* snD_q*`; `bOw_* bOt_*` (under 30 days, with and against the twin); the wealth Gini `giniW`, `giniWN`, net of drain `giniWnet`, `giniWnetN`; price level `lf`; means of wages, interest, allowance and price cuts.
- `studyRun` (per run at the last year, mean and 10th-90th percentile across seeds): tier transitions `trC5_*`, `trC10_*`; `startCrisis`, `yrsCrisis`, `everCrisis`, `reentry2`, `exitN`, `firstExitYrs`, `neverExit`.
- `measures` (per row, mean and 10th-90th percentile across seeds): the measured EDC `edcM` (mean over person-years), `edcMagg` (aggregate), `edcMPth`, `edcMOut`, `edcProxy`; FBS `fbsAbove`, `fbsAboveKids`, `fbs50Med`; `cost`, `epPY`, `fgt0PY`, `fgt1PY`. For the two designs: IPBI's modelled part `unhousedAvoided`, `avoidLo`, `avoidHi`, `avoidW`, `avoidWHi`, `avoidJail`, `avoidHealth` (from the means, as release 1's panel computes them); paired differences against no programme with 95% intervals for `edcM`, `edcMagg`, `cost`, `epPY`, `fgt0PY`, `fgt1PY`.
A group with no adults (participants under no programme) is null, not 0. The poverty measures beside these on the suite page are basket poverty and wealth poverty (job X2's series and release 2's published effects), so no statement rests on one measure alone.

## Checks (a failed check stops the shard; nothing is written)
1. Every engine output key of every row and seed equals release 2's stored part M values (`r2-m-ENV-YEARS-104691f/shard-0000.json.gz`, engine 104691f; non-finite values as null). The only keys allowed beyond part M's are the two reporting switches' own (EDC_KEYS, FBS_KEYS). This proves the run is release 2's main row and the switches changed nothing.
2. Seed 1's adults' flags add up to the engine's yearly shares.
3. Measures study: no accounting identity fails; the per-adult below-30-days count equals the engine's; the wealth Gini equals the engine's at Year 7 and the last year; every adult of a programme run has a twin; EPPM's parts add up. Every row has `edcM` and `fbsAbove`.
4. The workflow's own checks: each shard records its range, the engine commit and a clean engine; `run.txt`, `SHA256SUMS` and `DONE` are written.

## Analysis
Levels with the 10th-90th percentile across seeds. EPPM and `up_*` are already paired (each adult against their twin). Where the page states a change in EDC, cost, extreme poverty or the poverty gap, it quotes the paired difference and its 95% interval from this run; for basic living, basket poverty, wealth poverty, inflation and median wealth it quotes release 2's published effects, as before. IPBI's avoided costs are computed from means and carry no interval; the page says so. The interval covers the model's randomness only. No synergy is measured here.

## Decision rules
- All six shards pass: the measures are release 2's and feed the suite page's release 2 view (S79 sub-step 3) through `data/releases/r2/`; v5.6's files stay untouched; the "release 1 only" wording goes.
- A shard fails check 1: the measures are not used; the cause is found and recorded as a dated amendment here, and a fixed run goes under a new study id (`x3b`).
- A shard fails for time or a runner fault: rerun that whole study under a new id with an amendment saying why; no shard is patched in.

## Reporting
Every outcome above goes to compassionism-sim-results (`x3-6d095a1/`) for all three environments and both horizons, and to the suite page's release 2 view, the Adverse and Stress environments included, nulls included. Each card is labelled release 2 (engine 104691f, re-run at `6d095a1eefe71abbb025b82e8942cd80cfe9a34a`, checked equal). Release 1's and release 2's rows are never drawn on one chart.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
