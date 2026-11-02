# Handoff (Nov 2, 2026): S51 partly done, backing as a mechanism (pilot running)

## Step status
S51 is **partly done**: items 1-3 are done, and item 4's pilot is running on Actions. What remains: when the pilot is `DONE`, run the analysis, write the plain-words pilot report with the list for S47, and mark S51 done (one short session; PLAN.md S51 has the exact commands).

## What shipped
- compassionism-simulation [#62](https://github.com/BetterToBest/compassionism-simulation/pull/62), merged `6428b96`: the row option `bkm`, off by default.
  - What it does: a share of the Source's net payout funds supply-adding projects, and their output backs the new money after a lag. The backed share becomes an outcome.
  - Proof nothing moved: guard test identical, engine lineage proved (six 12-seed panels), 4 new unit tests, all checks green.
  - Also in it: `dev/reports/s51-backing-reading.md` (Claude's reading of the design, for Duke), `dev/tools/s51_backing.py` (the preregistered analysis), and `dev/DECISIONS.md` (S51).
- compassionism-sim-results [#11](https://github.com/BetterToBest/compassionism-sim-results/pull/11), merged `bf52f82`: `runner/jobs/backing.js` (350 rows per environment; `--check` passes).
- research-update (this PR): `prereg/2026-11-backing-addendum.md` (study M), committed before any run; Amendment 5 of the study programme; PLAN.md's S51 section.

## The modelling choices (for Duke to read; all labelled modelling assumptions)
- **Only added output absorbs new money (main reading).** The engine's price rule is the quantity theory's, and the Hub's own inflation equation uses output growth. The other reading, "the projects' proceeds retire the money", is the convention of the released matched output and the every-dollar-backed row. It is swept.
- **Added output is capped at 8% of earned income** (BLS U-6, the underused labour). 16% (Kenya's measured peak) and no ceiling are swept. Without a ceiling, the top setting has the projects out-producing the whole economy's earned income 2.25 times over by year 19.
- The payout is about 60% of earned income every year, so under the main reading little of it can be backed. The study's question is therefore the **break-even share**, and whether any setting reaches it.

## In flight
- Study `s51-backing`, pilot, seeds 1-50, all three environments, 25 shards: workflow run https://github.com/BetterToBest/compassionism-sim-results/actions/runs/41373143374 (dispatched Nov 2, 01:34 UTC; started). Engine `6428b96f95e28bbbda5b0717e8915a09206310a0`. Results land in compassionism-sim-results `s51-backing-6428b96/`; done when `DONE` is in that folder. A failed shard: "Re-run failed jobs" on the run.

## Decisions waiting
None new. D11 was answered (backing is the design's requirement). If the pilot shows no main-reading setting reaches break-even, the design's levers (payout size or pace, conversion tax, octave capacity) are Duke's call: a ledger decision then, not now.

## Next step
Finish **S51** (the pilot report), then **S52** (outside supply-shock environment), then S53, then S47.

## Pitfalls
- domtest also compares `earlier-engine.html`, which carries a copy of the page script. After any engine edit run `python3 dev/tools/sync_earlier.py`, or CI fails ("DRIFTED: tbRunCore", "same script false").
- The proxy refused to delete a stray branch, compassionism-sim-results `claude/s51-backing`. Its commit trailer names a model, against the rule; it was never merged and has no PR. It can be deleted on GitHub by hand.
- A 2-seed pipeline test ran before the preregistration was committed. The addendum discloses it and the one rule it changed (decision rule 2 now also requires wealth poverty to fall, which is stricter).
- The study job takes about 400 s a seed for all three environments on one process (350 rows each).
- Under 90% wage indexation, the release row can lower basket poverty while raising wealth poverty (the 2-seed test). Read both measures.
