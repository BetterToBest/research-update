# Handoff (Nov 8, 2026): S55 part 3, pilot checked and the nine 500-seed jobs dispatched

## Step status
S55 is **partly done**. Parts 1-3 (sub-steps 1-5) are done. Remaining: part 4 (sub-step 6), the report, once all nine result folders hold `DONE`. Nothing is a result yet; the pilot (seeds 1-50) is a check only.

## What shipped
- research-update PR for this session: pilot record, run manifest Amendment 7 (shards, run links), PLAN.md and this file. No engine or runner change this session (engine `0c93593`, compassionism-simulation PR 82; results PR 21 stand).
- Pilot check: T's members-only rows equal study A's (`prog-a-ce8d030`) for seeds 1-50 on all 55 kept measures, in all six rows. U, V, W, Y have the Amendment 6 row counts per environment (32, 62, 20, 12); every seed array has 50 values, none non-finite.
- Pilot glimpse, not a result: with growth on, the PTF share reaches the 0.49 demand ceiling by year 10 under Reference and Adverse and only by year 19 under Stress.

## In flight (GitHub Actions workflow `run-study`, engine `0c93593e1ea502555387e42215b79f290a60f127`, seeds 1-500, `job=program.js`, `job_args=--study=<S> --env=all --procs=4`)
Runs in dispatch order (confirm each against its folder's `run.txt`): T [86](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472393103) (10 shards) · U [87](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472395687) (4) · U10 [88](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472398061) (20) · V [89](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472400373) (10) · V10 [90](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472402724) (20) · VJ [91](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472404743) (10) · W [92](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472407087) (5) · W10 [93](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472409538) (20) · Y [94](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472411721) (4). 103 shards, about 96 runner-hours, 20 runners at once, so roughly 5-6 hours in all.
- Results land in `prog-<t|u|u10|v|v10|vj|w|w10|y>-0c93593/` in compassionism-sim-results, with `DONE` when every shard passed `check-shards.js`. A failed shard: "Re-run failed jobs" on its run.

## Decisions waiting
- None new.

## Next step
**S5** (participation threshold; sonnet, medium) can start now. **S55 part 4** (opus, xhigh; the report) starts when all nine folders hold `DONE`. S39 can also start. S7 waits on S5 and S55.

## Pitfalls
- Run links above were matched to studies by dispatch order and time stamps (the runs were still in their plan stage when checked). The folder's `run.txt` is the authority.
- Shard counts differ from Amendment 6 for VJ, W, W10, Y (finer, from the timings); nothing else changed. Amendment 7 records it.
- `earlier-engine.html` carries the page's script. Run `python3 dev/tools/sync_earlier.py` after any engine edit, or domtest fails on drift.
- A `PA` object built by hand in a test now needs the growth defaults (`Object.assign({}, PA_DEFAULTS, ...)`).
- The reporting hook is called twice for year 0. Count years by index, not by calls.
