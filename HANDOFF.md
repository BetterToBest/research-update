# Handoff (Nov 14, 2026): S63 part 2, round 2's engine pinned, job built, dry run dispatched

## Step status
S63 is **partly done**. Parts 1 and 2 are done. Part 3 remains: read the dry run, write Amendment 2 (timings, shard sizes, the 24 dispatch lines), and rerun S69's program on the frozen main row (PLAN S63, "Part 3").

## What shipped
- compassionism-simulation [PR 107](https://github.com/BetterToBest/compassionism-simulation/pull/107), merged as `104691f3993ac6f37d6ff1b8ccd4690120cfe949` (**the engine pin**). It builds S69's two corrections as `fx.ez` (earnings below 1e-9 dollars count as zero) and `fx.rk` (weighted measures rank on the cent), both off identical. It adds `r2FreezePair` (the frozen main row: `r2MainRow`, the two corrections, full backing) and `dev/tools/s63_ends.js` with output `dev/runs/s63/r2-ends.json`. Guard, unit (360), validate, domtest and the lineage proof all pass.
- compassionism-sim-results [PR 38](https://github.com/BetterToBest/compassionism-sim-results/pull/38), merged: `runner/jobs/r2.js` (parts M, S, F, B; `--check`, `--selftest`, `--part=all`) and `runner/jobs/r2-ends.json`. `--check` passes: 107 Source and 126 financed points, 668 row-runs per environment, seed and horizon, plus the 10,000-adult pair. `--selftest` passes.
- research-update, this branch: freeze file Amendment 1, run manifest Amendment 8, `prereg/checks/2026-11-s63-r2-check.txt` (every point, pair end and bound end), PLAN S63, the indexes and this file.
- Ledger: D26 answered by Duke (today's price rule with S69's corrections); I18 marked resolved by Duke.

## In flight
- The dry run: `run-study` [run 100](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43635868201), study `r2dry`, engine `104691f`, `--part=all --procs=4`, seeds 1-2 in 2 shards (about 20-30 minutes a shard). Results land in compassionism-sim-results `r2dry-104691f/`; it is finished when `DONE` is there. Each shard file's `_meta.timings` has seconds per part, environment and horizon (`rowSeconds` per point).

## Decisions waiting
- None open. I18 (OSF registration): Duke marked it resolved. The file now has Amendment 1, so register (or update) the OSF copy after Amendment 2, before S64 dispatches.

## Next step
**S63 part 3** (opus, high): from the dry run, size shards so none runs over 2 hours (S and F at 40 years are the long ones); write Amendment 2 with the timings, the shard sizes, the output sizes (with `--gzip`) and the 24 dispatch lines (`r2-<p>-<env>-<years>`; `job_args=--part=P --env=E --years=Y --procs=4 --gzip`). Then rerun S69's program on the frozen row: `dev/packets/make_s69_reference.js` builds on `r2MainPair` (backed share 0, no corrections), so it needs a frozen-row option first. Check whether `s69_main.py` implements `o.a` 1 and the two corrections before running 500 seeds. S64 dispatches only after both.

## Pitfalls
- CI caught two things the local runs missed: the unit-test count markers (README, CONTRIBUTING; `node harness.js unit --write-counts`) and `earlier-engine.html`, which must be resynced after any engine edit (`python3 dev/tools/sync_earlier.py`). Run both before opening the pull request.
- The engine's yearly series hold the end of year t + 1 at index t (the 20-year `pov` is `ppov_19`). r2.js reads year 20 of a 40-year run from index 19.
- `fx.rk` also moves the weighted tail's measures (`wtB50E` and the like) by under a cent, because they share `dmSort`. This is expected and recorded.
- Commits worked in this session's mode. Remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and older session branches in research-update still need deleting by hand.
