# Handoff (Nov 8, 2026): S39 part 1, the outside engine cross-check built and dispatched

## Step status
S39 is **partly done**. Done: the preregistration, the engine side, the BeforeIT.jl module, the job, a dry run, and both studies dispatched. Remaining (part 2, about one session): once both result folders hold `DONE`, run the analysis tool, write the findings into the report, and apply decision rule 4. S7 can start meanwhile.

## What shipped
- research-update [PR 70](https://github.com/BetterToBest/research-update/pull/70): `prereg/2026-11-s39-outside-crosscheck.md` (committed before any run; the one-seed pilot seen before the decision rules is disclosed), plus this file and PLAN.md.
- compassionism-sim-results [PR 22](https://github.com/BetterToBest/compassionism-sim-results/pull/22) (merged, f67b727): job `runner/jobs/beforeit.js`, module `runner/jobs/beforeit/` (BeforeIT 0.6.0, Julia 1.11.5 pinned, sizes in `shares.json`), `runner/jobs/s39-path.js`, and results `s39-path-ce8d030/` (the engine's year paths, seeds 1-500, three environments; every row reproduces study A's `plv_19` seed by seed).
- compassionism-simulation [PR 85](https://github.com/BetterToBest/compassionism-simulation/pull/85): report `dev/reports/s39-outside-crosscheck.md` (part 1, with what a US calibration would take), tool `dev/tools/s39_crosscheck.py` (written before any BeforeIT result), `dev/runs/s39-crosscheck/tables.md`, DECISIONS.md. Also merged the previous session's [PR 84](https://github.com/BetterToBest/compassionism-simulation/pull/84) (S5; checks were green).

## Findings so far (plain words)
- The engine counts most of the C2.2 payout as new money not backed by output. Under C2.2 (Reference) that is 31-46% of cash income each year: the Source's payout ($59,263 per adult-year) less its matched part ($19,140). It passes into the general price level one for one, a year later, so prices end about 415 times their start after 19 years. Release design: 16-34% a year, about 183 times.
- The conversion tax the Source keeps ($12,336 per adult-year) does not reduce that money (open engine question, rule 4).
- BeforeIT's firms price from costs and expected inflation, with no excess-demand term. In a one-seed pilot at 1:1000, new money of 10-35% of income a year moved prices less than 8% over 20 years. If the full study confirms this, the two engines differ by a factor of hundreds, each resting on one assumption.

## In flight
- compassionism-sim-results, run-study workflow, engine `ce8d030`, job `beforeit.js`:
  - `s39-full` (full scale, 8.9 million agents, 65 shards of about 2.5 hours): run 42511582006, folder `s39-full-ce8d030/`.
  - `s39-k1` (1:1000, 13 shards): run 42511585190, folder `s39-k1-ce8d030/`.
  - `dry-s39`: run 42510677223 (its shard passed).
- Each run is done when its folder has `DONE` (expect about 8-12 hours for `s39-full`). A failed shard is rerun, never redesigned.
- compassionism-simulation PR 85: checks were running at the end. Merge when green (no job depends on it).

## Decisions waiting
- None. Part 2 may add a ledger decision under rule 4: Hub inflation sentences would name the engine's quantity-theory placeholder and give BeforeIT's figure beside it.

## Next step
**S7** (sonnet, medium): unblocked since S5. Then **S39 part 2** (opus, high) once both folders hold `DONE`:
`python3 dev/tools/s39_crosscheck.py --engine RESULTS/s39-path-ce8d030 --full RESULTS/s39-full-ce8d030 --k1 RESULTS/s39-k1-ce8d030 --out dev/runs/s39-crosscheck`

## Pitfalls
- Study A kept the price level only at years 10, 20 and 40, although the run manifest lists `plv_0`-`plv_39` for S39. `s39-path.js` reads the full year path instead.
- Any rerun of study rows must set the runner's reference settings (`applyNR6()`, `tbSetG(TB_PROFILE_G)`) as program.js does. Without them the price level came out at about 300 instead of 415.
- The engine's price level for year k reflects the new money of the years before it. Compare "after k years of payout".
- BeforeIT does not repeat a seed with threads on, so every run is single-threaded. Its no-payout run drifts beyond 12 quarters (unemployment falls to zero), so every 20-year BeforeIT figure carries that caveat.
- S7's findings page: any sentence on inflation should wait for S39 part 2, or say the figure rests on the engine's quantity-theory rule.
