# Handoff (Nov 5, 2026): S54 partly done, policy levers (switch landed, pilot running)

## Step status
S54 is **partly done**. Items 1-3 and 5 are done. Item 6's stages 1 and 2 (seeds 1-50) are running on Actions. Remaining: the analysis script, stage 3 (confirmation on seeds 51-100), the pilot report, and the list for S47.

## What shipped
- compassionism-simulation [#68](https://github.com/BetterToBest/compassionism-simulation/pull/68) (squash e6da050): reading `dev/reports/s54-levers-reading.md`; row option `lv` (the policy levers) with joining that sees what joining pays; 4 unit tests; DECISIONS (S54); TESTBED_SPEC row; lineage link. Guard test identical; validate, unit (241), domtest (153) pass.
- compassionism-simulation [#69](https://github.com/BetterToBest/compassionism-simulation/pull/69): its HANDOFF.md.
- compassionism-sim-results [#14](https://github.com/BetterToBest/compassionism-sim-results/pull/14) (squash 17cf7af): `runner/jobs/levers.js` (stages 1 and 2; `--check` PASS; multi-process join checked against single-process runs).
- research-update [#43](https://github.com/BetterToBest/research-update/pull/43) (merge 07e321b): `prereg/2026-11-levers-addendum.md` (study N) and study programme Amendment 8, merged before any run.

## In flight
- Study `s54-levers1` (stage 1, 520 rows per environment): run [42099920669](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42099920669), 25 shards, about 10-15 minutes each.
- Study `s54-levers2` (stage 2, 1,164 rows per environment): run [42099926032](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42099926032), 50 shards, about 11 minutes each.
- Both use engine e6da0506188d67fc542f1bd2c430e733a44bd921, seeds 1-50, `levers.js --stage=N --env=all --procs=4`. They are done when `DONE` is in `s54-levers1-e6da050/` and `s54-levers2-e6da050/` in compassionism-sim-results. A failed shard: "Re-run failed jobs" on that run.

## Next session (S54 continued)
1. Before reading any result, write `dev/tools/s54_levers.py` in compassionism-simulation to the addendum's Analysis section: paired bootstrap 2,000, seed 54; lever effects; the three break-even tax rates; Morris effects; the Pareto front over the 3-environment means; stage 3 selection by rule 4.
2. List stage 3's rows in a dated addendum amendment. Add `--stage=3` to `levers.js`, reading the list. Dispatch seeds 51-100.
3. Pilot report `dev/reports/s54-levers.md` (plain words, labelled pilot): what works, what does nothing and why, the front, confirmed settings, and what S47 carries.

## Decisions waiting
- None new. Any design change the results suggest becomes a ledger decision (addendum rule 6).

## Next step
**S54** (continued): the pilot is running; then stage 3 and the report. S47 waits on S54.

## Pitfalls
- Seed-1 tests, not results: the uncapped protected account paid with new money ran away (about 1,200% inflation a year). The flat wage contribution (`fflat`) removes inflation but raises basket poverty. Every-year indexation equals the surge protocol in Reference, because inflation is above 5% every year anyway.
- Stress's released tax is 18% (not 12%). The job passes `tref` = the design's own tax, so deterrence is measured from each environment's released rate.
- Output is large: about 120 MB at 50 seeds. S47 must trim keys or compress before 500 seeds.
- Both studies commit to compassionism-sim-results main when done. If one commit job fails on a push race, re-run that job.
- The first version of `levers.js` dropped the first piece's rows when joining processes. Fixed before merge and checked. Always compare a multi-process join with a single-process run.
