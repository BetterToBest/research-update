# Handoff (Nov 16, 2026): S11 (BLEI visuals), sub-steps 1-3 done; the release 2 series run is on Actions

## Step status
**S11 partly done.** The tool, the preregistration and the runner job are landed, and the 500-seed run of release 2's main row is running on GitHub Actions (free). Left: sub-step 4, rebuilding `suite.html` from the new series once the run is done.

## What shipped
- compassionism-simulation PR 135 (merged, engine commit `5b62481`): `dev/tools/explore_export.js --r2`. It runs release 2's three main rows (no programme, C2.2, release design) the way the round-2 batch's part M ran them, and stops unless every engine output key, row by row and seed by seed, equals release 2's stored part M values. So the new run is release 2 exactly, even on today's engine (round-3 switches present, off). Reporting only; old modes give identical output; decision in `dev/DECISIONS.md`.
- compassionism-sim-results PR 50 (merged, `52f8f0d`): `runner/jobs/series-r2.js`.
- research-update PR 152: `prereg/2026-11-x2-series-addendum.md` (job X2), committed before the run; this handoff; the PLAN.md S11 note.

## In flight
- run-study workflow run 125 in compassionism-sim-results (dispatched 21:03 UTC): study `x2`, engine `5b62481326f3b82cc714e20e4cd4ec3726357dd2`, job `series-r2.js --env=all --years=20,40 --n=500`, seeds 1-6, 6 shards (one per environment and horizon, 500 seeds each). Plan job passed; shards were queued when checked. Expected 0.5-1.5 hours a shard.
- Results land in `x2-5b62481/` on compassionism-sim-results main; finished when `x2-5b62481/DONE` exists. A shard that fails the release 2 comparison exits with an error and the folder is never written.

## Decisions waiting
Nothing new. D30 answered (new run on Actions). S12 (which visuals go on which page) stays Duke's.

## Next step
S11 again, sub-step 4: check `x2-5b62481/` (`run.txt`, `SHA256SUMS`, each shard's `_meta.selfCheck` says "every engine key ... equals release 2's part M"), then rebuild `suite.html` as a new release data folder, keeping v5.6's files untouched. If run 125 failed, read the failing shard's log first; the prereg's decision rules say what to do (new study id `x2b`, dated amendment).

## Pitfalls
- Do not mix engines on one page: job X (`x-ce8d030`, frozen round-1 rows) and X2 (release 2, engine 104691f re-run at 5b62481) are different models. Label each panel.
- The suite files hold levels with the 10th-90th percentile spread across seeds, not paired differences: any statement comparing rows quotes release 2's published effects (`r2-tables-104691f`).
- The engine's `dev/CODEMAP.md` is stale (rebuilding it changes about 700 lines unrelated to this step); left as it was.
- The GitHub plugin server failed to connect at session start; the deferred `mcp__github__*` tools worked.
- Old remote branches to delete by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`. JSON-LD carries Duke's personal email (S42 fixes).
