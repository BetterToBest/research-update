# Handoff (Nov 10, 2026): S59 part 1 done, wealth held by asset class

## Step status
S59 is **partly done**: part 1 (the asset classes, the Nov 9 audit's finding 1) is built, piloted and reported. Part 2 remains: the weighted top tail, returns that differ by wealth, business ownership and its income, the check against the Fed's accounts, the owners rule (PLAN.md, S59, "Part 2"). S7 stays held.

## What shipped
- research-update `prereg/2026-11-s59-asset-classes.md` (committed before the build; Amendments 1 and 2); PLAN.md (S59 part 1, findings); this file. Branch `claude/wizardly-davinci-16utgd`.
- compassionism-simulation [PR 92](https://github.com/BetterToBest/compassionism-simulation/pull/92): switch `RETURNS` (row option `rt`), off identical (guard test, lineage linked), 7 unit tests; sources `sources/s59_portfolio.py` (SCF 2022) and `sources/s59_real_gains.py` (Shiller); pilot tool, tables, report `dev/reports/s59-asset-classes.md`; DECISIONS (S59, part 1).
- compassionism-sim-results [PR 27](https://github.com/BetterToBest/compassionism-sim-results/pull/27), merged (9f76000): `s59-assets-1d2cf29` (seeds 1-100, three environments; run.txt, SHA256SUMS, DONE).

## Findings (plain words; pilot, seeds 1-100, 500 adults; intervals unadjusted)
- **The model treated all wealth as cash; the survey says the model's families hold little net cash.** Nominal assets are 20% of net worth, debts 18% (mostly fixed-rate mortgages); the rest is homes, shares, businesses.
- **With wealth held by asset class the programme's wealth-poverty harm becomes a reduction** in every environment under the main reading. Reference: release +21.5 → −12.7 points; C2.2 +0.7 → −18.2.
- **Part of that is debt relief nobody pays for** (the model has no lender). With fixed-rate debt repricing too: −6.7 and −13.3.
- **If homes, shares and businesses follow only half of the programme's inflation, the release design raises wealth poverty in Adverse (+9.1) and Stress (+3.6).** Release: sign not established. C2.2: a reduction in 26 of 27 cells, nil in one.
- Basket poverty, the cost of living and inflation do not move. The earlier fall in the wealth Gini and top shares was the all-cash assumption (top 1% share: −12.4 points → −1.0).
- The top fifth by starting wealth still loses about $240,000 per adult; the other four fifths gain.

## In flight
- Nothing.

## Decisions waiting
- D21: carry the C2.2 design paid for by a contribution on every round-2 outcome (default: yes, as a labelled reading).
- S63 files the main-row price-rule decision after S67.
- Nothing new from S59 part 1.

## Next step
**S59, part 2** (fable, high, under D22; opus, xhigh if fable is not available): preregister, then build the weighted top tail and the returns and business-ownership part. S67 and S60 can start too.

## Pitfalls
- Never quote an `rt` wealth result without the no-debt-relief reading (`chi: 1`) beside it: inflated-away mortgages are a gain with no loser.
- A pilot's "off" rows must carry CPS earnings (`lt: {s: 'all', m: 'all'}`) to match S66's rows; without it basket poverty is 51%, not 27%.
- The no-programme run has no inflation in Reference but has outside inflation in Adverse and Stress.
- A no-programme row's `pd*` keys read the previous run's PTF state: a unit test comparing two studies needs a warm-up study with the same seeds.
- FRED refused scripted downloads this session (it worked for S58); Shiller's files and the Fed's SCF and DFA files were reachable.
- The session's worker restarted once mid-step; clones and downloads survived, the scratchpad path changed.
- The remote branch `claude/s66-low-share-trace` in research-update still needs deleting by hand.
