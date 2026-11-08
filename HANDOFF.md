# Handoff (Nov 8, 2026): S48 done, the batch is complete and checked

## Step status
S48 is **done**. All 24 batch folders plus N3 and N3x are in compassionism-sim-results at engine `ce8d030`, each with `DONE` and passing checksums. Every folder loads in its consumer. The R-panel is merged, and X matches the frozen panel exactly.

## What shipped
- compassionism-sim-results [PR 19](https://github.com/BetterToBest/compassionism-sim-results/pull/19), merged `4eb0c52`: `prog-r-ce8d030/` and `o-ce8d030/`. Their shards were over GitHub's 100 MB file limit, so the workflow's last job could not push them; it was not the push race. The shards were recovered from the run artifacts (digests match), passed `check-shards.js`, and were stored as `.json.gz` (`gzip -n -9`, lossless). run.txt says so.
- compassionism-sim-results [PR 20](https://github.com/BetterToBest/compassionism-sim-results/pull/20), merged `0ea9ea7`: `panel-merged-ce8d030/`, the release panel merged (published 51 rows, frozen 52 per environment; 20 and 40 years) by `merge_parts.py` then `merge_panel.py` in a scratch copy, with run.txt and SHA256SUMS.
- compassionism-simulation [PR 78](https://github.com/BetterToBest/compassionism-simulation/pull/78) (tools only): four readers accept `.json.gz` (`batch_load.py`, `s53_security.py`, `s19_series.py`, `s52_shock.py`); `x_panel_check.js` (X's check on the means the X shards store).
- research-update: run manifest Amendment 5 (how R and O are stored, how X was checked; nothing else moves).

## Checks (all PASS, full 500-seed folders)
- `batch_load.py --check` prog-r: 84 rows per environment, seeds 1-500 (its null keys are the allowed kinds).
- `s53_security.py --check` prog-r: 252 rows. `s19_series.py`: prog-r (20 and 40 years) and o (210 rows), largest difference 1.4e-14.
- `s54_levers.py --check`: N1 1,560 rows; N2 3,492; N3 747 (249 per environment, seeds 501-1000); N3x 747.
- `s52_shock.py` reads o end to end (run at 20 bootstrap replicates, as a load test only).
- X: all 2,160 yearly means equal the merged frozen panel.

## In flight
- Nothing.

## Decisions waiting
- None.

## Next step
**S36** (synergy report; opus, high): first in the Order table now that S48 is done. S38, S5 and S39 can also start.

## Pitfalls
- **Big shards:** a job without `--gzip` whose shard passes 100 MB cannot be committed by the workflow. The 2-seed dry run could not show it. Before a new large job, estimate the shard size from the dry run (bytes per seed x seeds per shard) and add `--gzip` if it passes about 90 MB.
- **Run artifacts last 3 days.** A failed last job must be recovered before then (`download_workflow_run_artifact`, then curl the link).
- `s52_shock.py`'s report header still says "PILOT" for any folder; the O report (S7/S36 work) should relabel batch results.
- Loading R (650 MB of JSON) or O (870 MB) in Python takes 2-3 GB of memory; run the readers one at a time.
- **GitHub plugin:** failed to connect again; the built-in GitHub tools worked.
