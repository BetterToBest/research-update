# Handoff (Nov 13, 2026): S59 done, the top of the wealth distribution, business owners and capital income

## Step status
S59 is **done** (part 1 Nov 10, part 2 Nov 12-13). It added one step to the plan: **S71**, a creditor side for debts that inflation wipes out (PLAN.md, S71). S7 stays held.

## What shipped
- research-update: `prereg/2026-11-s59-tail-returns.md` (committed before the build; Amendments 1 and 2), Amendment 3 to part 1's file (a correction), PLAN.md (S59 part 2 findings, S71, Order table), PLAN-done.md, the prereg index, this file. Branch `claude/eloquent-tesla-bemri3`.
- compassionism-simulation [PR 93](https://github.com/BetterToBest/compassionism-simulation/pull/93): open, its checks running when this was written. Switch `WEALTH_TAIL` (row option `wt`), `rt` options `bo`, `ci`, `ng`, `rg`, the owners rule by equity (`own: 'eq'`), weighted measures; off identical (guard test, lineage), 8 unit tests; sources `sources/s59_tail.py`, `sources/s59_capital.py`; report `dev/reports/s59-tail-returns.md`; tables `dev/runs/s59-tail/tables.md`.
- compassionism-sim-results [PR 28](https://github.com/BetterToBest/compassionism-sim-results/pull/28), merged (c71289c): `s59-tail-62a189b` (seeds 1-100, three environments; run.txt, SHA256SUMS, DONE).

## Findings (plain words; pilot, seeds 1-100, 500 adults; intervals unadjusted)
- **The model had no very wealthy households** (its tables stopped at the 99.5th percentile). With a fitted top tail the top 1% of adults hold 30.1% of wealth at the start (28.4 to 31.8), against 20.8% before, 31.5% in the survey for the same families, and 29.3-32.5% in the Fed's accounts.
- **Whether the programme lowers or raises concentration is not established.** Main reading: the top 1% share falls 0.9-1.8 points by year 20, in every environment and every tail reading. With no unpaid-for mortgage relief: it rises 0.1-1.2 points. The bottom half gains share and the Gini falls either way.
- **The tail changes nothing else** (wealth poverty, basket poverty, inflation: inside their intervals). Part 1's wealth-poverty results stand with everything on (Reference: −12.5 release, −18.1 C2.2; −6.7 and −13.3 without debt relief).
- **Wealth pays income, mostly at the top:** about $9,800 per adult at the start (survey about $8,950). 15% of adults own a business.
- **If private owners kept the conversion premium** (not the release reading), the top 1% share of income would rise 1-5 points and basket poverty would fall about 4 points less.
- **Correction to part 1:** the Fed re-issued its survey file in 2025 dollars on Oct 5; part 1's wealth-group edges were 9.4% too high. Rerun: no finding changes (largest move 0.11 points).
- **What the sources said, against the plan's wording:** the "3.5 times" interest figure is the top 0.01% only; the 45.3% and 75.7% of capital gains rank people by income, not wealth; 14.6% of families hold business equity (the Bulletin's 20% counts the self-employed too).

## In flight
- Nothing.

## Decisions waiting
- D21: carry the C2.2 design paid for by a contribution on every round-2 outcome (default: yes, as a labelled reading).
- S63 files the main-row price-rule decision after S67.
- Nothing new from S59. S71 was added without a decision: it is modelling work, free to run, and S63 now waits on it.

## Next step
**S67** (the price rule: derivation, time step and wording; fable, high, under D22; opus, xhigh if fable is not available): it is the first open row of the Order table. S60 and S71 can start too.

## Pitfalls
- Never quote a wealth or concentration result under `rt` without the no-debt-relief reading (`chi: 1`) beside it.
- With the tail on, read only weighted measures (`wt*`, `dm*`, `rt*`); the engine's older Gini and top shares are not valid.
- The Fed re-issues its SCF extracts in the newest survey's dollars: check the dollar year before any price adjustment (`FILE` in `sources/s59_capital.py`).
- The session machine restarted twice: once mid-pilot (the run was lost; rerun in chunks that each save a file) and the scratchpad path changed. Run pilots in chunks.
- One preregistration figure was wrong and is corrected in Amendment 2 (the Forbes 400 adds 1.81 points to the survey's top 1% share, not 1.66); a comparison only.
- The first commit of this session in research-update (6c10ebe), like earlier sessions' commits, carries a model name in its co-author line, against the rule; history is not rewritten. Later commits use a plain co-author line.
- The remote branch `claude/s66-low-share-trace` in research-update still needs deleting by hand.
