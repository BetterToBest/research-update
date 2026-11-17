# Preregistration addendum: job X4, the visual suite's series for release 2 counted by weight (S81)

Committed Nov 17, 2026 by S81, before any run. Engine: compassionism-simulation at commit `ENGINE_SHA` (the merge of compassionism-simulation PR 144, which adds weighted keys to `dev/tools/explore_export.js --suite`; `harness.js` and `index.html` as at that commit, unchanged from release 2's engine block). Job script: compassionism-sim-results `runner/jobs/series-r2.js` (unchanged since job X3). Like jobs X2 and X3, it runs on GitHub Actions (free), not Runpod.

## Why this run
Release 2's main rows give 18 of the 500 simulated adults the place of rare, very rich families and count each at its share of the population (a weight, `a._w`). Job X2's series (`x2-5b62481`) took plain means, shares and medians over the 500 adults, so those 18 count once each. For the average days of basic living from savings this is decisive: 550,000-730,000 days against medians of 1,500-3,800, a figure that describes the 18, not the average adult. The suite page therefore shows no averages for release 2 (v5.9.8). The shares and medians are affected less, but they too count the 18 at the wrong weight. This run records the same series counted by weight, so the page can show weighted averages beside the medians. It is a reporting run: it adds no setting, row or claim. It re-runs release 2's main row and records the same quantities a second way.

## Questions
Q1. What are the average days of basic living from savings, from pay and from the allowance, when every adult counts at the weight the engine gives it?
Q2. Do the weighted medians, tier shares, shares below 30 days, relative poverty and share taking part differ from X2's plain ones, and by how much? (Any other plain mean, share or median in the suite files that mixes in the 18 tail adults is found by this comparison.)
All descriptive: an answer is the series with its spread across seeds, not a test.

## Design
- Rows, environments (`ref`, `adv`, `st`), horizons (20 and 40 years), seeds (1-500, paired; life seed 1), checks' panel: exactly as job X2's (`prereg/2026-11-x2-series-addendum.md`, Design), and the same command `node dev/tools/explore_export.js ENV YEARS 500 1 --r2 --suite --panel=RESULTS/r2-m-ENV-YEARS-104691f/shard-0000.json.gz` per shard.
- Where and how: GitHub Actions, compassionism-sim-results' run-study workflow; study `x4`; engine `ENGINE_SHA`; job `series-r2.js`; arguments `--env=all --years=20,40 --n=500`; seed range `1-6`, 6 shards. Results folder: `x4-ENGINE7/` with `run.txt` and `SHA256SUMS`.

## Outcomes
All descriptive; for each row and year the mean over seeds and the 10th and 90th percentile across seeds of
- the weighted parts of the BLEI: `wmeanSav`, `wmeanInc`, `wmeanBu` (weighted means, which add up) and `wmedSav`, `wmedInc`, `wmedBu` (weighted medians), days;
- `wmed_all`, `wmed_part`, `wmed_non`: the weighted median BLEI, days; `wtier0`-`wtier5` (`_all`, `_part`, `_non`): the share in each tier, % by weight;
- `wbO`, `wbN`, `wrelPov`, `wpart`: the share below 30 days (BLEI paper's reading, same-rules reading), below 60% of the weighted median cash income, and taking part, % by weight.
Also every key X2 wrote, unchanged (the plain keys), so the file replaces nothing: X2's folder stays.
Weighted median: the value at which the cumulative weight, counted to each adult's midpoint, reaches one half, interpolating between neighbours (equal to the plain median when every weight is 1).

## Checks (a failed check stops the shard; nothing is written)
1. As X2's check 1: every engine output key of every row and seed equals release 2's stored part M values (engine 104691f).
2. As X2's checks 2 and 3.
3. New: after the run, every plain key of every row, year and environment equals job X2's stored value (`x2-5b62481`), to the printed precision; the weighted keys are new.
4. The workflow's own checks (range, engine commit, clean engine; `run.txt`, `SHA256SUMS`, `DONE`).

## Analysis
No tests. The suite page shows weighted averages beside the medians, labelled by weight. For any plain key whose weighted counterpart differs by more than the spread across seeds, the page and the report say so. Weighted shares below 30 days differ from the engine's own published share (which counts adults once each); that difference is reported, not corrected here, because the headline basic-living effects are release 2's stored results.

## Decision rules
- All six shards pass and check 3 holds: the weighted series feed the suite page's release 2 view through `data/releases/r2/`, and the "averages are not shown" wording goes.
- Check 1 or 3 fails: the series are not used; the cause is recorded as a dated amendment here, and a fixed run goes under a new study id (`x4b`).
- A shard fails for time or a runner fault: rerun the whole study under a new id with an amendment saying why; no shard is patched in.

## Reporting
Every outcome goes to compassionism-sim-results (`x4-ENGINE7/`) for all three environments and both horizons, and to the suite page's release 2 view, the Adverse and Stress environments included. Each is labelled release 2 (engine 104691f, re-run at `ENGINE_SHA`, checked equal).

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
