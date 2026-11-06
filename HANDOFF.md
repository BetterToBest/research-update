# Handoff (Nov 6, 2026): S48 part 1, the full batch dispatched

## Step status
S48 is **partly done**. Every job in manifest section 3 except N3 and N3x was dispatched on run-study (Nov 6, 04:02-04:04 UTC), exactly as section 3 says. Duke confirmed D15 (A) in the ledger before dispatch. Left for part 2: check each folder for `DONE`, rerun any failed piece, choose N3's list from N1 and N2 (rule 4) with a dated amendment and dispatch N3 and N3x, then merge the R-panel and run X's check.

## What shipped
- No code. The 24 runs below, and this file and PLAN.md (S48 part 1).

## In flight
The 24 runs use engine `ce8d030b8d16a752706c4ea2db71196e11e73831` with the job scripts at compassionism-sim-results main `fd66941`. Their runner scripts are unchanged since `031861a`. Each run commits `<study>-ce8d030/` to compassionism-sim-results main with run.txt, SHA256SUMS and `DONE`. GitHub's free plan runs 20 jobs at once and queues the rest: about 650 runner-hours, so allow about 33 hours plus queueing (finished around Nov 7-8). The run number is in https://github.com/BetterToBest/compassionism-sim-results/actions/runs/<id>, and each run.txt names its run.
| run # (id) | study, shards | run # (id) | study, shards |
|---|---|---|---|
| 55 (42160133662) | n1, 25 | 67 (42160185548) | prog-c, 2 |
| 56 (42160141724) | n2, 100 | 68 (42160188793) | prog-d, 4 |
| 57 (42160144569) | panel, 30 | 69 (42160191537) | prog-f, 2 |
| 58 (42160147554) | panel-frz, 30 | 70 (42160194979) | prog-g, 4 |
| 59 (42160150701) | prog-r, 5 | 71 (42160198409) | prog-h, 4 |
| 60 (42160153696) | x, 6 (workflow seeds 1-6) | 72 (42160201563) | prog-i, 2 |
| 61 (42160162103) | k, 4 | 73 (42160209708) | prog-j, 10 |
| 62 (42160165359) | l, 1 | 74 (42160213184) | prog-d10, 10 |
| 63 (42160168687) | m, 20 | 75 (42160216182) | prog-g10, 20 |
| 64 (42160171648) | o, 4 | 76 (42160219274) | prog-b10, 50 |
| 65 (42160174471) | p, 1 | 77 (42160222115) | prog-a, 25 (sizes 500, 2,000, 10,000) |
| 66 (42160177592) | prog-b, 20 | 78 (42160225254) | prog-a50, 100 (size 50,000) |
The run-to-study mapping follows the dispatch order. Job counts confirmed it for runs 55 (25 shards) and 60 (6 shards over seeds 1-6). When each folder lands, its run.txt is the check.

## Decisions waiting
- None. D15 is answered (A: S48 runs the frozen manifest on Actions).

## Next step
**S48 part 2** (opus, medium), once the batch has finished (check on or after Nov 8). For each of the 24 folders: `DONE` is there and `sha256sum -c SHA256SUMS` passes. A failed shard is rerun with `rerun_failed_jobs` on its run, never redesigned. Then:
1. N3's list: `s54_levers.py --s1 n1-ce8d030 --s2 n2-ce8d030 --select LIST` (decision rule 4). Add a dated amendment to `prereg/2026-11-levers-addendum.md` and commit the list to runner/jobs/ before dispatch. Then dispatch N3 (`levers.js --stage=3 --list=FILE --env=all --procs=2 --frozen --gzip`, seeds 501-1000, 10 shards) and N3x (the same with `--sx=main`, 20 shards). Size the shards to the front's size (section 3: 17.4 and 24.4 runner-hours at 250 rows).
2. The R-panel: `merge_parts.py`, then `merge_panel.py` in a copy (never on main). Then X's check: `explore_export.js ... --panel=FILE`.
3. `batch_load.py --check` on A-J and R.
S36 waits on all of it.

## Pitfalls
- **Queueing:** 479 shards and their plan jobs share one 20-job queue. Later runs' plan jobs wait behind earlier shards. That is expected, not a fault. If GitHub cancels jobs for queue time, rerun the failed jobs on that run (artifacts last 3 days).
- **If GitHub objects or limits the runs** (ledger I16): stop. Moving the rest to Runpod is a new ledger decision, and nothing that costs money runs before Duke answers it.
- **A's two folders** (`prog-a`, `prog-a50`) together are study A. R-panel workflow seeds are shard indices, not seeds.
- **GitHub plugin:** failed to connect again (bad Authorization header); the built-in GitHub tools worked.
