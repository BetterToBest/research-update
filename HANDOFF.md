# Handoff (Oct 30, 2026): S33 the study runner on GitHub Actions; runtime benchmarks

## Step status
S33 **done**. A study can now be dispatched on GitHub Actions: seed range cut into shards, each shard run on a GitHub-hosted runner in a clean checkout of a pinned engine commit, every shard checked, `run.txt`, `SHA256SUMS` and `DONE` written, folder committed to the results repository. Instructions for sessions: `prereg/RUNNING.md`.

## What shipped
- compassionism-sim-results #4 (merged, ebaa959): `.github/workflows/run-study.yml`, `runner/jobs/release-pair.js` (release main row plus no-programme pair, per-seed values), `runner/check-shards.js`. GitHub accepted the workflow file from the session (the question in PLAN S28 is answered: yes).
- #5 (77da73d): `--procs=K`, K processes per shard, byte-identical to one. #6 (d7f4557): no concurrency group on the commit job (it cancelled waiting jobs when studies finished together). #7 (dd008ea): README.
- Result folders in compassionism-sim-results, each with run.txt, SHA256SUMS, DONE: `s33-smoke-d33de07` (4 seeds, 2 shards) and `s33-smoke-procs-d33de07` (8 seeds, 2 shards, 4 processes), both byte for byte equal to local runs; `s33-bench-*-d33de07`: seconds and memory per seed at 500, 2,000, 10,000 and 50,000 adults (20 years) and 500 and 10,000 adults (40 years).
- research-update: `prereg/RUNNING.md` (dispatch steps, tests, benchmarks, runner limits, sizing of the planned studies, the Runpod route); PLAN.md marks S33 done.

## Findings that change later steps
- Per seed (main row plus no-programme pair, one environment, 20 years): 0.68, 1.5, 9.2, 63 seconds at 500, 2,000, 10,000, 50,000 adults; 40 years about twice. Memory at most 1.1 GB. The whole S32 program fits on Actions: worst case about 830 core-hours, about 10.5 hours on 20 runners. Nothing needs Runpod by these numbers (RUNNING.md section 5).
- S32 sizes seeds from RUNNING.md section 3; S35 should time a real row of each kind (the sizing takes a row as half the pair).
- Before S47: GitHub's terms limit Actions to the repository's own software work; the pilots will show whether this use is accepted; Runpod stays the fallback (ledger issue I16).

## In flight
Nothing. All four results-repository pull requests merged (it has no checks). Ledger synced (version 31).

## Decisions waiting
- D2 (chat exports for S31): still waiting; S31 is skipped.

## Next step
**S32** (preregister the study program), opus, high: waits on S33 and S34, both done. Q6 (the yardstick) and ledger issue I15 must be carried into it. The chain is off (`AUTOCHAIN.md`), so Duke starts it by hand.

## Pitfalls
- A GitHub concurrency group keeps one pending job and cancels the rest; do not put one on a job that several dispatches reach together.
- A dispatch-only workflow can be run only after its file is on the default branch; merge it first (it runs only on dispatch).
- The session branch `claude/jolly-bardeen-7xhcrf` already held older merged history on the remote; this session used `claude/s33-study-runner` here instead (no force-push). Its stray commit e9256a8 can be deleted.
- `pkill -f <pattern>` kills the session's own shell; kill by PID. A guarded `rm -f $VAR/*` is blocked; use literal paths.
- Commit trailers: `Co-Authored-By: Claude <noreply@anthropic.com>` (no model names).
