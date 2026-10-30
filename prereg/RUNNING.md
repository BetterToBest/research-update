# Running a study: Actions first, Runpod only for what does not fit

Written Oct 30, 2026 (plan step S33). Applies to every study from S35 on. Money rule (CLAUDE.md): nothing on Runpod before the S47 design freeze, its ledger decision and Duke adding the Runpod key; pilots and tests use GitHub Actions (free) or the session machine.

## 1. Dispatching a study on Actions
The workflow is `run-study` in BetterToBest/compassionism-sim-results (`.github/workflows/run-study.yml`; its README lists the inputs). Steps for a session:
1. The study's preregistration is committed in `prereg/` (research rule 1) and names the engine commit. The engine commit must be a full 40-character hash of BetterToBest/compassionism-simulation.
2. If the study needs a job that does not exist, add a script to `runner/jobs/` of the results repository first (pull request, merge). A job is run in a clean checkout of the engine commit as `node runner/jobs/<job> <job_args> --seeds=A-B --out=shard-NNNN.json`; it must write that file with deterministic content only (no dates, no machine) and `shard-NNNN.timing.json` beside it. `release-pair.js` is the reference: the release testbed's main row and its no-programme pair, every seed's value of every measure; `--procs=K` runs K processes at once inside one shard.
3. Dispatch: the GitHub tool `actions_run_trigger` with `method: run_workflow`, `workflow_id: run-study.yml`, `ref: main` and `inputs` `study`, `engine`, `job`, `job_args`, `seeds`, `shards`. Use `--procs=4` in `job_args` (a runner has 4 vCPUs) and a shard count of at least 20 for a long study (20 runners can run at once on the free plan).
4. Check once that it started (`actions_list`, `list_workflow_runs`, the run shows `in_progress` or `queued`). Do not wait or poll.
5. Record in HANDOFF.md: the study id, engine commit, the run's link, the dispatch command, and where the results will land (`<study>-<engine, 7 characters>/` in the results repository, with `DONE` when every shard is in). End the session. The next session finds `DONE`, runs its analysis and publishes (research rule 2).
6. If a shard fails, "Re-run failed jobs" on the run (the Actions tab, or `rerun_failed_jobs`) repeats only that shard. A study folder is written only after every shard passes `runner/check-shards.js` (seed range, engine commit, clean engine, one value per seed).

The final job commits to `main` of the results repository with the workflow's own `GITHUB_TOKEN` (contents: write, nothing else, no secret). Dispatching is the one place a session does not use a pull request: the folder is new, named by study and engine commit, and the workflow refuses a study id whose folder is already `DONE`.

## 2. What was tested (all on the pinned engine d33de07, all in the results repository)
- Smoke test `s33-smoke-d33de07`: 4 seeds, 2 shards. Its two shard files are byte for byte (sha256) the files a local run of the same seeds writes (f1054689... and b02fa0f3...).
- `s33-smoke-procs-d33de07`: 8 seeds, 2 shards, 4 processes each. Again byte for byte equal to a local single-process run (026b25d1... and 48e718e3...). Splitting seeds, across shards or processes, changes no number.
- A bug found on the way: a concurrency group on the commit job cancelled all but one waiting job when several studies finished together (four benchmark runs were cancelled and redone). The group is gone; the commit step retries the push with a rebase.

## 3. Runtime benchmarks
Unit measured: the release testbed's main row and its no-programme pair (two rows, with today's safety net), Reference environment, per seed, on a GitHub-hosted runner, one process. Folders `s33-bench-*` in the results repository. Seconds per seed include start-up.

| Adults | 20 years: seconds per seed | peak memory | 40 years: seconds per seed | seeds timed |
|---|---|---|---|---|
| 500 | 0.68 | 192 MB | 1.29 (peak 260 MB) | 5 (20 y), 3 (40 y) |
| 2,000 | 1.49 | 238 MB | not timed | 3 |
| 10,000 | 9.2 | 341 MB | 22.5 (peak 323 MB) | 2 (20 y), 1 (40 y) |
| 50,000 | 62.7 | 1,141 MB | not timed; 2 to 2.5 times the 20-year figure is expected | 1 |

Notes: the session machine (4 cores) gave 0.80, 2.7, 13.5 and 77.6 seconds at the same four sizes, so the runner is no slower. Cost grows a little faster than the number of adults above 2,000 (5 times the adults, 6.8 times the time, from 10,000 to 50,000). The 40-year figures roughly double the 20-year ones. Single-seed timings carry noise; S35 re-times with real study rows.

## 4. Limits of GitHub-hosted runners (public repository; read from GitHub's documentation, Oct 30, 2026)
- Standard runner `ubuntu-latest`: 4 vCPU, 16 GB memory, 14 GB disk. No charge for public repositories.
- A job may run up to 6 hours. A workflow run is cancelled after 35 days. A matrix may have up to 256 jobs.
- Concurrent jobs on the free plan: 20 (Pro 40, Team 60). So one run uses at most 20 runners at once, 80 vCPUs with 4 processes each; further shards wait their turn.
- Artifacts: shard files pass between jobs as artifacts (3-day retention); the free plan's artifact storage is 500 MB, and a 500-seed shard file is about 5 MB, so a study stays far below it.
- Caution to check before the full batch (S47): GitHub's terms say Actions is for building, testing and deploying the repository's own software. These runs execute the repository's engine on the repository's own studies, and the pilots (S35) will show whether GitHub objects; the Runpod route below is the fallback.

## 5. Sizing the planned studies
Rule of thumb, from the table: core-hours = (rows / 2) x environments x seeds x (seconds per seed from section 3) / 3,600. One runner supplies 4 core-hours an hour and at most 24 per job; 20 runners supply 80 an hour.

| Study (S32 plan) | Size | Core-hours | Wall time on Actions, 20 runners | Needs Runpod? |
|---|---|---|---|---|
| Q1 scale, one pair at each of 500, 2,000, 10,000, 50,000 adults, 500 seeds, 3 environments, 20 years | 1,500 seeds per size | 0.3 + 0.6 + 3.8 + 26.1 = 30.8 | about half an hour (the 50,000-adult size is most of it) | no |
| Same, 40 years | | about 2.2 times, 68 | about 1 hour | no |
| Q2 synergy, 32 rows (full factorial over 5 switches), 500 seeds, 3 environments, 500 adults | 16 pair-equivalents | 4.5 (20 y), 8.6 (40 y) | under 15 minutes | no |
| Q2 as above at 10,000 adults, 20 years | | 61 | under 1.5 hours | no |
| Q4 participation, 9 levels, Q5 octave wage on and off, Q6 both yardsticks: each multiplies the rows by 9, 2 and 2 | | multiply the line above | | no unless the product passes about 1,000 core-hours (about 12 hours on 20 runners) |
| Worst case: 32 rows x 3 environments x 500 seeds at 50,000 adults, 40 years | | about 830 | about 10.5 hours | no, but near the point where Runpod would be quicker |

Row cost is taken as half the pair's; synergy rows with more mechanisms may cost more, so S35 times a real row of each kind before S47 fixes the sizes. Memory is never limiting: 1.1 GB for one 50,000-adult process, 4.6 GB with four.

## 6. The Runpod route (only S48, after the S47 design freeze, its ledger decision and Duke adding the Runpod key)
`dev/batch/runpod.sh` in compassionism-simulation runs a named study on one CPU pod: it clones the results repository, checks out the pinned engine commit in a clean worktree, runs the study's job script (`dev/tools/<study>_jobs.sh WORKTREE OUTDIR --max-hours=H`, resumable in pieces; a piece whose file exists is skipped), pushes each finished piece at once, writes `DONE` and terminates the pod. To add a study: a `case` line in `runpod.sh` (study id, engine commit, job script) and a `dev/tools/<study>_jobs.sh` modelled on `study12_jobs.sh`; the job script can call `runner/jobs/release-pair.js` from the results repository for each piece. The folder layout is the same as on Actions (`<study>-<engine, 7 characters>/`, `run.txt`, `SHA256SUMS`, `DONE`). Use it for what section 5 shows does not fit Actions (more than about 1,000 core-hours, a job that must exceed 6 hours in one process, or if GitHub objects to the use). Pod start, token and cost notes are in the header of `runpod.sh`.
