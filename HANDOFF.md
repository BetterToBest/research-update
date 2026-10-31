# Handoff (Oct 31, 2026): S14 population-weighted cost-of-living line, partly done (pilot running)

## Step status
S14 is **partly done**. The derivation and every dollar path are audited, the engine switch is merged, study L is preregistered, and its 100-seed pilot was started on Actions. What remains is the pilot's results section in the report (`dev/reports/lw-weighted-line.md`, section 6), with the decision-rule labels. The next session does this first. Duke's D8 answer is recorded in both preregistrations.

## What shipped
- compassionism-simulation [#56](https://github.com/BetterToBest/compassionism-simulation/pull/56), merged `f66dc67`. It adds the switch `LW` (row option `lw: 'ext' | 'bea'`), which sets the line and refits the basket shares, household ratios and childcare at it (`sources/lw_line.py`), plus project pay. `sources/lw_bea.py` holds the BEA estimate, and the report is `dev/reports/lw-weighted-line.md`. Checks: guard identical, lineage proof (six panels identical), unit 225/0, validate, domtest.
- compassionism-sim-results [#10](https://github.com/BetterToBest/compassionism-sim-results/pull/10), merged: `runner/jobs/lw.js` (9 rows; `--check` passes).
- research-update (this PR): `prereg/2026-11-lw-weighted-line.md` (study L). Study programme Amendment 4 adds study L and Duke's D8 answer. Study K Amendment 2 adds the D8 answer.

## What S14 found
- MIT's terms allow web use of at most 10 locations, and a weighted national mean needs all 51. So MIT's own weighted figure is not computed: ledger decision D9 (licence).
- Two estimates run beside $49,370. ext is $51,201 (+3.7%), an outside figure that was only partly checked. bea is $51,838 (+5.0%), this step's estimate from BEA price parities and the 8 MIT pages already held; leaving one state out gives $51,708-51,995.
- At a higher line the housing share rises (27.6% → 28.8-29.2%). The C2.2 needs level rises from $1,788 to $1,885-1,918 a month.
- No dollar path was found wrongly fixed at $49,370, apart from the fitted sets, which the switch refits. The adult $25,000 wealth line (`pov`) does not follow the line by design, so study L also reports `hhWlthPY`.

## In flight
- Pilot `pilot-l`: run-study workflow in compassionism-sim-results, engine `f66dc67`, job `lw.js --env=all --procs=2`, seeds 1-100, 10 shards. Results land in `pilot-l-<engine 7>/` with run.txt and SHA256SUMS. It is finished when the folder has `DONE`. Run: https://github.com/BetterToBest/compassionism-sim-results/actions/runs/41168320930

## Decisions waiting
- **D9** (Duke): ask MIT's Living Wage Institute to license the 51 state figures? The default makes no request: the release keeps $49,370, labelled the unweighted mean, and study L's rows are published beside it.

## Next step
Finish S14 first: write the pilot's section 6 and the rule labels, then merge (short). Then **S13** (outside audits before the freeze), opus, high, followed by S50. All of these come before S47.

## Pitfalls
- MIT asks not to be scraped. More than 10 locations needs a licence, so never pull the 51 state pages.
- `sync_earlier.py` must run after any edit to `index.html`'s script, or domtest fails ("same script false", and functions "DRIFTED").
- `engine_lineage.js prove` takes about 12 minutes. Run it in the background, then commit `dev/runs/engine-lineage.json`.
- `gh` has no valid token in this environment. Use the GitHub tools for pull requests and workflow dispatch.
- S47 must build the batch on the C2.2 design (study programme Amendment 4) and add `lw.js` and `c22.js` to the manifest.
