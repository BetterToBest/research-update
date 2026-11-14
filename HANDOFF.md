# Handoff (Nov 14, 2026): S70 done, the round-2 screen read

## Step status
S70 is **done**. Both blocks of the screen finished on Actions. The preregistered rules are applied, the plain-words note is written (compassionism-simulation `dev/reports/s70-screen.md`), and the readings S63 must carry are in PLAN S63 ("From S70").

## What shipped
- compassionism-simulation [PR 106](https://github.com/BetterToBest/compassionism-simulation/pull/106): the analysis tool, now applying rules 3, 5 and 6 too (no rule or verdict changed), the tables in `dev/runs/s70-screen/`, the report, and a DECISIONS entry.
- compassionism-sim-results [PR 37](https://github.com/BetterToBest/compassionism-sim-results/pull/37) (merged, 0c8a1ea): the tables beside `s70-screen-s-8b96cdd/` and `s70-screen-f-8b96cdd/`, with `analysis.txt` and an extended `SHA256SUMS`.
- research-update [PR 99](https://github.com/BetterToBest/research-update/pull/99): prereg Amendment 2, PLAN S70 marked done, the S63 list, this file.

## What the screen found
- At full backing (the main row) every point of the box lowers all three poverty measures, and programme inflation stays at 0-0.2 points a year. Few readings move a poverty outcome by a point: the income effect (release design), and conversion outside the labour force and the yearly flows (C2.2's cost-of-living poverty). The spending share dominates median wealth.
- At no assumed backing (inflation 30-142 points a year) and in the financed rows (debt up to 1.6 million % of GDP), the model runs away and almost every reading matters.
- Rules as written ("any cell"): Source rows 22 carried in full, 3 at one reading, 8 held. Financed rows 34 in full (the output-gap weight by rule 7), 1 at one reading, 6 held. Rule 5 gives 28 and 66 interaction pairs.

## In flight
Nothing.

## Decisions waiting
- D23 (filed again Nov 14). Default: the financed rows are carried beside the main rows with rate, base, cap and deficit, and the Hub leads with none of them.

## Next step
**S63**, preregister and freeze round 2 (opus, high). Read PLAN S63, including the new "From S70" paragraph. Its first job is to cost the batch the S70 list implies: 32 single-reading points on each Source curve and 48 on the financed rows, plus the pairs and the bound, times designs, three environments, 500 seeds and two horizons. A smaller curve needs a dated amendment to the S70 rules, with the reason, before any batch run.

## Pitfalls
- **Commits are blocked in Auto mode.** Switch to "Accept edits" before the first commit.
- The results repository is large. Clone it sparse (`--filter=blob:none --sparse`, then `git sparse-checkout set --no-cone '/*' '!/*/' '/runner/' '/.github/'`) and add study folders by name.
- The screen's design holds no main-row point: never quote a screen figure as the main row's effect.
- The remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and earlier session branches in research-update still need deleting by hand.
