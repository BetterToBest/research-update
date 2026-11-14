# Handoff (Nov 14, 2026): S62 done, PTF realism (running costs and who pays, PTF workers and wages, the density tests)

## Step status
S62 is **done** in one session. It added no step and no decision. S7 stays held.

## What shipped
- research-update: `prereg/2026-11-s62-ptf-realism.md` (committed before the build and any run; Amendment 1 before the pilot), PLAN.md (S62 findings; notes for S63, S68, S70), PLAN-done.md, the indexes, this file. Branch `claude/intelligent-shannon-4w3rqh`.
- compassionism-simulation [PR 99](https://github.com/BetterToBest/compassionism-simulation/pull/99): switch `PTF_OPS` (row option `po`; needs open access); off identical (guard test, lineage linked, `earlier-engine.html` resynced); 10 unit tests (`poUnitSuite`); `sources/s62_ptf_ops.py`; report `dev/reports/s62-ptf-realism.md`; tables `dev/runs/s62-ptf-ops/`. Merge state: see the last line of this section.
- compassionism-sim-results [PR 32](https://github.com/BetterToBest/compassionism-sim-results/pull/32), merged (113df99): `s62-ptf-ops-3500d0b` (seeds 1-100, three environments; run.txt, SHA256SUMS, DONE).

## Findings (plain words; pilot, seeds 1-100, 500 adults; intervals unadjusted)
- **The Hub's PTF prices sit far below what not-for-profit grocers and utilities cost:** food at about 39% of full cost, utilities at 68% (full cost: food 0.968, utilities 0.814 per market dollar; observed sector costs 0.972 and 0.839 agree).
- **The engine already paid nearly all of that gap** as programme cost since plan step 5. At the main reading (D19: the Source pays) the subsidy is about $1,260 per adult a year in the release design (3.6-4.1% of programme cost) and $1,300 in C2.2 (1.8-2.3%). PTF sales cover about 41% of running costs.
- **Prices at full cost instead (no subsidy):** the food discount falls from 54% to 3%; programme cost $1,390-2,360 lower; poverty effects 0.1-1.0 points smaller; the C2.2 price level at year 20 up to 35% higher. **The Hub's costs as stated:** cost $1,240-1,300 lower.
- **PTF workers:** 0.84 jobs per 100 adults. The bonus on workers (as the Hub states it) is a mean 0.25% on converting participants' rates against 6.5% on members; conversion payouts 1.2-2.6% lower.
- **The smooth curve (D20)** lowers the food factor where zones sit just above 40% (2.17 against the step's 2.46). Tests read on members' share: 1.71; on capacity: 2.59. Hiring limits (stress, no source) bind in 21-79% of years.
- **No reading changes the sign of any programme effect.** For S63 (fixed before the run): `po` main in the main row; beside it prices at full cost, the Hub's costs as stated, the papers' step.

## In flight
- Nothing running.

## Decisions waiting
- D21: carry the C2.2 design paid for by a contribution on every round-2 outcome (default: yes, as a labelled reading).
- S63 files the main-row price-rule decision (S67's recommendation, both views).
- Nothing new from S62.

## Next step
**S68** (round 2 written into MODEL_SPEC, ODD and TESTBED_SPEC; per-run module reset; pairwise tests of the round-2 switches; a new packet): its waits (S59, S60, S62, S67, S71) are done. S70 can also start now.

## Pitfalls
- Read compassionism-simulation's own HANDOFF.md pitfalls before an engine change: `domtest` fails until `python3 dev/tools/sync_earlier.py` has resynced `earlier-engine.html` and `node dev/tools/engine_lineage.js prove "..."` has linked the engine (about 10 minutes); `node harness.js unit` fails until the README and CONTRIBUTING test counts are updated.
- The preregistered identity reading was wrong (the Hub's costs cannot reproduce an engine that already counts the subsidy); fixed in Amendment 1 before the pilot. Check identity readings against the cost accounting before writing them into a prereg.
- `po`'s subsidy is `poSub`; `cCut` includes PTH's cut. Under `pay: 'price'` the density tests no longer touch the PTF cut.
- The price level in the C2.2 design is hundreds of times year 0's by year 20; compare readings as ratios, not index points.
- Commit trailers: `Co-Authored-By: Claude <noreply@anthropic.com>` (no model name).
- The remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x` and earlier session branches in research-update still need deleting by hand.
