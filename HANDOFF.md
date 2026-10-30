# Handoff (Oct 30, 2026): S35 pilot studies, partly done

## Step status
S35 **partly done**. Everything the preregistration requires before a run has landed, and the seven pilots are running on Actions. Remaining: the pilot report, once every folder has `DONE`.

## What shipped
- compassionism-simulation [#50](https://github.com/BetterToBest/compassionism-simulation/pull/50), merged as `70d23beff2065b554b687a2a4843c1433b19498b`. It adds reporting keys `plv_0`..`plv_39` (price level by year) and `hhDebt20`/`hhDebt40` (families in debt), plus the debt reading (`c.dr`, borrowing limit 0, off by default). Guard test identical; lineage link to 6f35bc221fb7; validate, unit (222) and domtest (153) pass; decisions in `dev/DECISIONS.md` (S35).
- compassionism-sim-results [#8](https://github.com/BetterToBest/compassionism-sim-results/pull/8), merged: `runner/jobs/program.js` (`--study=A|B|B10|C|D|D10|F --env=all`). `--check` passes: row counts match the preregistration, and the main and none rows match `release-pair.js` byte for byte. It keeps 46 measures per row; the full set would be 3.6 GB for study B. Study C's outcomes by age at joining come from the reporting hook (adults matched by id; 100% matched in a test).
- research-update [#18](https://github.com/BetterToBest/research-update/pull/18): preregistration amendment 1 (engine commit, job script, choices the preregistration left open); this handoff.

## In flight
- Seven `run-study` runs in compassionism-sim-results (runs 13-19, dispatched 05:54 UTC; run 13 = pilot-a ... run 19 = pilot-f). All use engine 70d23be, seeds 1-50, `--env=all`.
- Folders: `pilot-a-70d23be` (A at 500, 2,000 and 10,000 adults), `pilot-b-70d23be`, `pilot-b10-70d23be`, `pilot-c-70d23be`, `pilot-d-70d23be`, `pilot-d10-70d23be`, `pilot-f-70d23be`. Each one is done when its `DONE` file exists. Expected within an hour.
- If a shard failed: `rerun_failed_jobs` on that run (RUNNING.md section 1.6).

## Decisions waiting
None.

## Next step
**S35 (continue)**, opus, medium: check the seven `DONE` files, then write `dev/reports/pilot-studies.md` (compassionism-simulation), labelled pilot throughout. It must cover:
- the per-block timings, from each shard's `timing.json`, for S47;
- does any outcome move with population size beyond Monte Carlo error? If not, say so plainly;
- the synergy table, its size and noise;
- age at joining;
- participation curve shape;
- the debt reading against the SCF's 9.3%;
- every output still missing for the full batch.
Then S37 only if the pilots show a community layer is needed.

## Pitfalls
- The release row's price level is about 2,500 times at year 20 (50.8% a year; already in the release panel), and about 18 million times at year 40 in a 100-adult test. Read inflation outcomes with that in mind; the pilots will show it at scale.
- The first CI run of an engine PR fails 2 domtest checks until the engine-lineage link is committed: run `engine_lineage.js prove` before pushing, not after.
- With the debt reading on, Stress still shows about 50% of families in debt at year 40 (one seed): the debt floor's other flows (job loss, shocks) remain.
- The engine's `domtest` takes about 12 minutes while the lineage proof is also running; start them one after the other.
- Commit trailers: `Co-Authored-By: Claude <noreply@anthropic.com>` (no model names). This session's branch for research-update was the harness-assigned `claude/confident-gates-jfn3pw`.
