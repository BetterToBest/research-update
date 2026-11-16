# Preregistration addendum: job X2, the visual suite's year-by-year series for release 2 (S11)

Committed Nov 16, 2026 by S11, before any run. Engine: compassionism-simulation at commit `ENGINE_HASH` (the merge of compassionism-simulation PR 135, which adds `dev/tools/explore_export.js --r2`; `harness.js` and `index.html` as at that commit). Job script: compassionism-sim-results `runner/jobs/series-r2.js` (PR 50). Decision D30 (Duke, Nov 16): a new run of release 2's main row on GitHub Actions, free; not Runpod.

## Why this run
The visual suite (`suite.html`, ledger I1) draws the BLEI tiers, the median BLEI and its parts, and the share taking part, year by year. Release 2's stored results (`r2-*-104691f`) hold yearly poverty and median wealth but only end-of-run totals for BLEI poverty, and none of the suite's other series. Job X (`x-ce8d030`) has every series, but for the frozen round-1 rows, a different model. So the series for release 2 need a run of their own. This is a reporting run: it adds no new setting, row or claim; it re-runs release 2's main row and records more of what happens in it.

## Questions
Q1. Year by year, how are adults spread across the six BLEI tiers (Crisis under 7 days of basic living, Precarious 7-30, Threshold 30-120, Stable 120-365, Secure 365-730, Flourishing 730 and over) under no programme, the C2.2 design and the release design of release 2, for all adults, participants and non-participants?
Q2. Year by year, what is the median BLEI (days), and how much of it comes from savings, income and the BU?
Q3. Year by year, what share of adults is below 30 days on the BLEI paper's reading and on the same-rules reading, below 60% of the median cash income, unhoused (extreme poverty), and taking part in the programme?
These are descriptive: what counts as an answer is the series with its spread across seeds, not a test.

## Design
- Rows: release 2's main row (`harness.js` `r2FreezePair`, ledger D25 and D26): no programme (`base`), the C2.2 design (`c22`) and the release design (`release`), exactly as the round-2 batch's part M ran them (500 adults; study options `r2MainStudy`; each row in its own study call; the wealth floor not changed). No other row.
- Environments: Reference, Adverse and Stress (`ref`, `adv`, `st`; part M's `str`).
- Horizons: 20 and 40 years, each its own run (as part M).
- Seeds: 1-500, paired across rows (common random numbers). Life seed (one seed's adults, for the "lives" panels): seed 1.
- Where and how: GitHub Actions, compassionism-sim-results' run-study workflow; study `x2`; engine `ENGINE_HASH`; job `series-r2.js`; arguments `--env=all --years=20,40 --n=500`; seed range `1-6`, 6 shards (shard I runs environment and horizon I, each over seeds 1-500 in one process). Per shard: `node dev/tools/explore_export.js ENV YEARS 500 1 --r2 --suite --panel=RESULTS/r2-m-ENV-YEARS-104691f/shard-0000.json.gz`. Results folder: `x2-<engine, 7 characters>/` with `run.txt` and `SHA256SUMS`. Expected time: about 25-50 minutes for a 20-year shard and 50-100 minutes for a 40-year shard (local test: 2.8 seconds per seed for the three rows at 20 years).

## Outcomes
All descriptive. For each row and year: the mean over seeds and the 10th and 90th percentile across seeds of
- `tier0`-`tier5` (`_all`, `_part`, `_non`): the share of adults in each BLEI tier, %, on the BLEI paper's reading in today's prices;
- `med_all`, `med_part`, `med_non`: the median BLEI, days; `medSav`, `medInc`, `medBu` (medians, which do not add up) and `meanSav`, `meanInc`, `meanBu` (means, which do): its savings, income and BU parts, days;
- `bO`, `bN`: the share below 30 days on the BLEI paper's reading and on the same-rules reading, %;
- `relPov`: cash income below 60% of the same run's median, %; `ep`: extreme poverty (unhoused), %; `part`: the share taking part, %.
Also, as the export always writes them: the bands (10th, 50th, 90th percentile and mean across seeds, by year) of below the cost of living, too little wealth, below 30 days, and median savings; the savings deciles at Year 7 and the last year; seed 1's adults year by year with and without the programme.
A group with no adults (participants under no programme) is null, not 0. The poverty measures the suite shows beside the BLEI series are basket poverty and wealth poverty (bands), so no statement rests on one measure alone.

## Checks (a failed check stops the shard; nothing is written)
1. Every engine output key of every row and seed equals release 2's stored part M values (`r2-m-ENV-YEARS-104691f/shard-0000.json.gz`, engine 104691f; non-finite values as null). This proves the run is release 2's main row.
2. Seed 1's adults' flags add up to the engine's yearly shares (below 30 days, below the cost of living, too little wealth).
3. The suite's share below 30 days equals the engine's, every seed and year; the mean yearly extreme poverty equals the engine's per-run figure.
4. The workflow's own checks: each shard records its range, the engine commit and a clean engine; `run.txt`, `SHA256SUMS` and `DONE` are written.

## Analysis
No tests, no intervals on differences: the output holds the spread across seeds of each row's level, not paired per-seed differences, so the suite shows levels with their 10th-90th percentile band, labelled as the spread across seeds. Any statement that compares rows on the suite page quotes release 2's own published effects (`r2-tables-104691f`), not these series. No synergy is measured here.

## Decision rules
- All six shards pass: the series are release 2's and feed the suite rebuild (S11 sub-step 4), as a new release data folder; v5.6's files stay untouched.
- A shard fails check 1: the series are not used; the cause is found and recorded as a dated amendment here, and a fixed run goes under a new study id (`x2b`).
- A shard fails for time or a runner fault: rerun that whole study under a new id with an amendment saying why; no shard is patched in.

## Reporting
Every series above goes to compassionism-sim-results (`x2-<engine 7>/`), all three environments and both horizons, and to the rebuilt visual suite, the Adverse and Stress environments included. Each suite panel is labelled with its engine (release 2: engine 104691f, re-run at `ENGINE_HASH`, checked equal); job X's round-1 series are not mixed onto the same panel.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
