# Handoff (Nov 14, 2026): S63 done, round 2 frozen, registered on OSF, ready to dispatch

## Step status
S63 is **done** (parts 1-3). I19 is **done**: Duke registered the freeze file with Amendments 1 and 2 on OSF, https://osf.io/msdzk/overview (Nov 14, 2026; reported by Duke, not opened by Claude: the OSF API needs a login). Nothing blocks S64.

## What shipped
- compassionism-simulation [PR 108](https://github.com/BetterToBest/compassionism-simulation/pull/108): S69's packet on the frozen main row (`dev/packets/s69-frozen-row.zip`, built with `make_s69_reference.js --frozen` from engine `104691f`). The Python program now applies `fx.ez` and `fx.rk`. Results are in `dev/reports/s69-independent-implementation/results-frozen/`: all six runs (no programme and C2.2, three environments, seeds 1-500) agree with the engine exactly, in every key and every seed. On the candidate row, up to 313 keys per run had differed through rounding; the two corrections removed all of those differences.
- research-update, this branch: freeze file Amendment 2. It holds the dry run's timings, the shard sizes, output sizes, the cost (about 186 runner-hours, 138 shards, about 9.3 hours on 20 runners, about 340 MB compressed), the 24 dispatch lines (longest first) and S69's result. It also changes PLAN S63, the Order table and the indexes.
- The dry run `r2dry-104691f` in compassionism-sim-results: both shards passed and every value is finite. Seed 1's main rows equal the frozen packet.

## In flight
- Nothing running.

## Decisions waiting
- Nothing. (I19, the OSF registration, is done.)

## Next step
**S64** (opus, high). I19 is done, so dispatch the 24 `run-study` lines in Amendment 2's table, in its order. Each line is `engine=104691f3993ac6f37d6ff1b8ccd4690120cfe949`, `job=r2.js`, `seeds=1-500`, with that row's `job_args` and `shards`. Add each workflow run's link to Amendment 2. The batch takes about 9-10 hours of wall-clock time on 20 runners, so dispatch, check that the runs started, and end the session. A later S64 session reads the folders once every one has `DONE`. Then write the tables tool (`dev/tools/`, compassionism-simulation) and the reports.

## Pitfalls
- The dry run's two runners differed by about 15% in speed. The shards are sized for 90 minutes at the slower rate, which leaves a third in hand under the 2-hour limit.
- The workflow refuses a study id whose folder is already `DONE`. To rerun a failed dispatch, use the same arguments under a suffixed id (`-r2`) and record it in Amendment 2.
- The Python program took 5-7 minutes per 500-seed run on 4 processes, about 37 minutes for all six. The engine's packet references took about 11 minutes per environment, run in parallel.
- Remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and older session branches in research-update still need deleting by hand.
