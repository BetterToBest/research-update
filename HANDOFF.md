# Handoff (Nov 7, 2026): S48 part 2, N3 and N3x dispatched

## Step status
S48 is **partly done**. Part 2 did: 22 of 24 batch folders landed with `DONE` and passing checksums; the other two (prog-r, o) hit a push race in the last job and were rerun; N3's list chosen and N3 and N3x dispatched. Left for part 3: confirm prog-r and o landed, wait for N3 and N3x, merge the R-panel, run X's check, and run the loader checks on R and N3/N3x.

## What shipped
- research-update [PR 55](https://github.com/BetterToBest/research-update/pull/55), merged `b058cf9`: levers addendum Amendment 3 (rule 4 on seeds 1-500: no setting meets it in any design or wage; list is the front, 249 rows per environment).
- compassionism-sim-results [PR 17](https://github.com/BetterToBest/compassionism-sim-results/pull/17), merged `3872feb`: `runner/jobs/levers-stage3-batch.json` (SHA-256 `63c441e8...560b`).
- compassionism-sim-results [PR 18](https://github.com/BetterToBest/compassionism-sim-results/pull/18), merged `8852888`: `levers.js` reads a bare `--list=NAME` beside the script (the workflow allows no `/` in job_args). No row changes.
- Checked: `batch_load.py --check` passes on prog-a, a50, b, b10, c, d, d10, f, g, g10, h, i, j. Folders n1, n2, panel, panel-frz, x, k, l, m, p all `DONE`, checksums pass.

## In flight
- Engine `ce8d030`, job scripts at sim-results main `8852888`. Results land as `<study>-ce8d030/` with run.txt, SHA256SUMS, `DONE`.
- Run 79 (id 42404920160): n3, seeds 501-1000, 10 shards. Run 80 (id 42404922598): n3x (`--sx=main`), 20 shards. Together about 40 runner-hours, so done within a day.
- Reruns of the failed last job: run 59 (prog-r, id 42160150701) and run 64 (o, id 42160171648), attempt 2, started Nov 7 19:07 UTC. Done when `prog-r-ce8d030/` and `o-ce8d030/` exist with `DONE`.

## Decisions waiting
- None.

## Next step
**S48 part 3** (opus, medium), once runs 79, 80 and the two reruns have finished. 1) Folders prog-r, o, n3, n3x have `DONE` and `sha256sum -c SHA256SUMS` passes; a failed shard is rerun, never redesigned. 2) R-panel: `merge_parts.py`, then `merge_panel.py` in a copy (never on main); then X's check `explore_export.js ... --panel=FILE`. 3) `batch_load.py --check` on prog-r; `s54_levers.py --check` on n1, n2, n3, n3x. Then S48 is done and S36, S38, S5 can start.

## Pitfalls
- **Last-job push race:** when many runs finish together, the "Commit the folder to main" step can fail after ~15 minutes of retries (prog-r, o). The shards are fine; `rerun_failed_jobs` fixes it while artifacts last (3 days from Nov 6). If a rerun fails too, rerun it again once the queue is quiet.
- **job_args allows only letters, digits and `= , . _ - space`:** no paths. Put job-side files in runner/jobs/ and name them bare.
- **A's two folders** (`prog-a`, `prog-a50`) together are study A. R-panel workflow seeds are shard indices, not seeds.
- **GitHub plugin:** failed to connect again (bad Authorization header); the built-in GitHub tools worked.
