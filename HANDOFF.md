# Handoff (Oct 31, 2026): S14 population-weighted cost-of-living line, done

## Step status
S14 is **done**. The pilot of study L (100 seeds) is analysed as preregistered in section 6 of compassionism-simulation `dev/reports/lw-weighted-line.md`, with every cell's rule 1 label. Study L's 500-seed rows join the S48 batch through S47.

## What shipped
- compassionism-simulation [#57](https://github.com/BetterToBest/compassionism-simulation/pull/57), merged `cc4e853`: report section 6, `dev/tools/lw_pilot.py`, tables in `dev/runs/lw-pilot/` (from compassionism-sim-results `pilot-l-f66dc67`, SHA256SUMS verified), analysis readings in `dev/DECISIONS.md`. No engine change.
- Earlier this step: compassionism-simulation #56 (switch `LW`, `f66dc67`), compassionism-sim-results #10 (`runner/jobs/lw.js`), research-update #25 (preregistration of study L).

## What the pilot found (labelled pilot)
- No programme: at a higher line, 1-3 points more people are below each line (headline: cost of living +1.7 at ext, +2.3 at bea).
- Release row: not changed by the line on all four primary share outcomes in the headline cell, at ext and bea, so robust to the line (rule 2). Five Adverse comparisons are 1.0-1.5 points smaller at the higher line. Cost hardly moves; inflation is 6-8% higher (20 years, Reference), because project pay follows the line.
- C2.2 design: changed by the line, mostly by construction. Its BU follows the line, so its effect grows by about the gap the higher line opens; cost +5.5-8.1%. Its figures are stated with their range across the lines.
- Rule 3: ext and bea are 1.2% apart (more than 1%), so the release keeps $49,370, labelled the unweighted mean.
- Rule 1 labels every inflation comparison "changed" (cumulative inflation compounds; a ±1-point band is meaningless). The report gives inflation as a percentage of the base; S47 should settle a yearly-rate reading for every study (pilot studies report, section 9).

## In flight
Nothing.

## Decisions waiting
- **D9 answered** (Duke: "check the Simulation repo first"). Searched Oct 31: the Simulation (files and full history), NEEC and the Research Hub. None holds the 51 state figures, only the two summary means from the outside review in v4.11 ($23.7355/hr unweighted, $24.6160/hr weighted = ext). Recorded in the report, section 6.
- **D10 answered** (Duke pasted the Money Talks News table). ext re-derived: $51,201.27 against $51,201.28; the eight MIT pages held match exactly (compassionism-simulation [#58](https://github.com/BetterToBest/compassionism-simulation/pull/58), `sources/lw_check_ext.py`; prereg Amendment 1). The 51 figures are not committed (MIT's ten-location limit). bea overstates the weighting by 1.2%. Recommendation to S47: adopt ext as the line, keeping the $49,370 rows beside it.

## Next step
**S13** (outside audits before the freeze: triage the Grok audit and audit the engine), opus, high; then S50. Both come before S47.

## Pitfalls
- MIT asks not to be scraped. More than 10 locations needs a licence, so never pull the 51 state pages.
- Result files write 0 for keys past the run's horizon (year-40 keys in 20-year rows); `lw_pilot.py` reads horizon keys only.
- `gh` has no valid token here; the GitHub tools work for pull requests and workflow runs.
- S47 decides the line (study L rule 3; recommendation: ext, $51,201). S47 must build the batch on the C2.2 design (study programme Amendment 4) and add `lw.js` and `c22.js` to the manifest.
