# Handoff (Nov 18, 2026): S82 part 3a (the batch read, a defect fixed, the batch rerun)

## Step status
**S82 partly done.** Part 3a is done: the first batch was read, and inspection found a defect in the design's sharing rule. It is fixed (v5.9.19) and the batch is rerun (Amendment 5). **Part 3b is left:** once the six rerun folders show `DONE`, the tables, the plain-words report and the findings-page text.
**S88 done** (other session). **S89 is Duke's** (his old Reddit posts on gold and crypto). **S90 added** (the BU-relief cycle, below).

## What shipped
- compassionism-simulation [PR 156](https://github.com/BetterToBest/compassionism-simulation/pull/156) (v5.9.19, merged `aa2a4e0`): the design's sharing rule (`sh` 'bu') now cuts exactly the sector's share. Under that rule only, the year's poverty accounting is queued and run with this year's totals (`slFlush`). Guard test identical, lineage recorded, 394 unit tests. At seeds 1-2, 179 of 231 job rows are identical to the first batch; only the rule's 52 rows below full backing moved. Release notes v5.9.19; v5.9.17 moved to CHANGELOG with a v5.9.18 entry.
- compassionism-simulation [PR 157](https://github.com/BetterToBest/compassionism-simulation/pull/157) (tools, merged `ed0e766`): `dev/tools/s82_tables.py` (every table the preregistration fixes; checks 11-12 with `--first eb0969c`); `dev/tools/s70_table.js` reads Stress and block FT; `dev/runs/s82-screen/`.
- compassionism-sim-results [PR 54](https://github.com/BetterToBest/compassionism-sim-results/pull/54) (merged `7b40b05`): the screen's analysis in its three folders (question 7 stands); `SUPERSEDED.txt` in the six first-batch folders.
- research-update: Amendment 5 in `prereg/2026-11-s82-v6-supply-indexing.md`; PLAN.md (S82 part 3a note with the screen's reading; new step S90).

## What was found (Amendment 5)
- Every preregistered check passed on the first batch (engine `eb0969c`). Then inspection: the design's rule cut two to four times its target. It divided this year's cut by last year's totals, and the share bought with cash swings yearly. Decision rule 1: whole batch rerun, only the rerun reported. The first batch's figures are not to be quoted.
- The swing comes from a damped two-year cycle in the BU's relief to the cost of living, even in the main row. It predates S82 and is listed as step S90.
- Duke (Nov 18): after v5.9.19 the next version is v5.9.21 (v5.9.20 skipped, as v5.9.10 was).

## In flight (GitHub Actions, run-study runs 137-142, dispatched 10:39 UTC Nov 18)
- Engine `aa2a4e0c5b4a2b425596f4728051bd2d3cbcbdde` (the merge of PR 156). Job `s82.js` at `4881a84`, unchanged. Results land in compassionism-sim-results `main`: `s82-v6-{ref,adv,str}-{20,40}-aa2a4e0/` (seeds 1-500, 20 shards each).
- Done when each folder has `DONE`. About 4-5 hours (120 jobs).
- The screen is not rerun (no supply limit in it).

## Decisions waiting
- D33 (do the headline cards' headings name the full-backing condition? default: no change).

## Next step
**S82 part 3b** (opus, xhigh), once the six folders show `DONE`:
- `python3 dev/tools/s82_tables.py <results> <out> --engine aa2a4e0 --first eb0969c`; checks 11 and 12 must pass.
- Then the report `dev/reports/s82-supply-indexing.md` (questions 1-7; the screen's reading is in PLAN.md's S82 note) and the findings-page text (decision rule 5).
- If not done yet: S90 (engine reading only) or S85's preregistration can start.

## Pitfalls
- Never switch branches in a checkout while a test is reading from it. The guard test was rerun cleanly after this happened once.
- `slCutSh` (realised) runs about (T−1)/T of `slR*` (target) even for an exact rule: year 0 has no cut, and the last target is for a year never run.
- Under the supply limit, basket poverty counts a household as short only when its income, less the money a shortage left unspendable on needs, falls below its cost. A better-off household can be cut without being counted. The shortfall-by-fifth table (question 5) counts every cut. Say so in the report.
- The unit suite takes about 45 minutes on the session machine; CI's checks job about 15.
