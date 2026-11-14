# Handoff (Nov 14, 2026): S64 part 1, round 2 dispatched

## Step status
S64 is **partly done**. Part 1 (dispatch) is done: all 24 lines of the freeze file's Amendment 2 were sent on Nov 14, 23:07-23:09 UTC, as frozen, with nothing changed. Still to do: read the 24 folders once each has `DONE`, check them, write the tables tool and the reports.

## What shipped
- research-update [PR 104](https://github.com/BetterToBest/research-update/pull/104), **open, not merged**: its `links` check is queued behind the batch, which holds all 20 of the account's runners, and auto-merge is off in this repository. Part 2 merges it first, once the check passes. Its contents: freeze file Amendment 2 now has a workflow-run column (runs 101-124) and a dated "Dispatched" note. Indexes rebuilt.
- compassionism-sim-results: no commit by this session. The runs commit their own folders to main.

## In flight
- The round-2 batch, `run-study` workflow on GitHub Actions (free), compassionism-sim-results, runs [101](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651639762) to [124](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651751304). 138 shards in all.
- Engine pinned at `104691f3993ac6f37d6ff1b8ccd4690120cfe949`, job `r2.js`, seeds 1-500. The workflow ran on results commit `62d6d42`.
- Results land in `r2-<part>-<env>-<years>-104691f/` (24 folders), each with `run.txt`, `SHA256SUMS` and the shard files. A folder is finished when it has a `DONE` file.
- Expected wall-clock time: about 9-10 hours at 20 runners at once, so done around 08:00-09:00 UTC on Nov 15.
- Last check (about 23:11 UTC): all 24 runs had been accepted. Run 101's plan job had passed (inputs checked, seeds cut into 14 shards of about 36) and its shards were queued for runners. The other plan jobs were still checking out the repository. No shard had finished, so none had passed or failed yet.

## Decisions waiting
- Nothing.

## Next step
**S64 part 2** (opus, high), once all 24 folders have `DONE`. Do these in order:
0. Merge research-update PR 104 once its `links` check passes.
1. Check every `run.txt` against Amendment 2's table. Runs in a group of equal shard count were sent at the same moment, so a pair could be swapped; correct the table if so.
2. Check that each folder has its full shard count, that `SHA256SUMS` passes, and that every value is finite.
3. Rerun any failed dispatch whole under `-r2`, with the same arguments, and record it in Amendment 2.
4. Write the tables tool (compassionism-simulation `dev/tools/`) and the reports.
5. Tabulate round 1's backing curve (`m-ce8d030`) with `dev/tools/s51_backing.py`, beside round 2's.

## Pitfalls
- The results repository is large (about 4,800 files). Each job's checkout takes several minutes. 20 plan jobs at once held all 20 runners at first.
- In this session the GitHub MCP plugin server failed to connect, but the `mcp__github__*` tools loaded through ToolSearch worked for dispatch.
- Actions runners are shared across the account, so every other repository's checks wait until the batch frees runners.
- The workflow refuses a study id whose folder is already `DONE`. Reruns use `-r2`.
- Remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and older session branches in research-update still need deleting by hand.
