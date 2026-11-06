# Handoff (Nov 5, 2026): S47 partly done, design freeze (part 2 started: supply-path fix built and every correction measured; Actions chosen)

## Step status
S47 is **partly done**. Done: step 1 (the manifest and the freeze's amendments), section 6 item 1 (the four `fx` parts built and measured), and Duke's choice of route: GitHub Actions, not Runpod (manifest Amendment 1). Remaining: section 6 items 2-7, pinning the engine commit, the 2-seed dry run with its timings, and the closing ledger record.

## What shipped
- compassionism-simulation [#74](https://github.com/BetterToBest/compassionism-simulation/pull/74) (merged, squash 8375cb3; all CI checks green): `fx` part `sp`. Each year's essentials capacity now comes from the study's own no-programme testbed run (`tbBaseS`). The programme's own switches and options are set to their defaults for that run, so every row of a seed gets the same path in any row order. A no-programme row's essentials prices now stay exactly still. `fx: true` = all four parts. Two unit tests; guard test identical; lineage linked. Measurement: `dev/reports/s47-fx.md`, `dev/reports/s47-fx-tables.md`, `dev/runs/s47-fx/`, `dev/tools/s47_fx_measure.js`; decision record in DECISIONS.md (S47).
- Measured (seeds 1-50, all three environments, none / release / C2.2):
  - `sp` removes the no-programme drift (0.7% by year 20 in Reference), lowers no-programme basket poverty by 0.3-0.4 points, and lowers programme inflation by 0.24-0.59 points a year.
  - `pthb`, `hb` and `ab` move nothing beyond their intervals.
  - The audit's corrections stay the larger change (the C2.2 design's wealth-poverty cut shrinks by 2.1-5.2 points).
  - No programme effect changes direction. The freeze keeps every part on.
- research-update (this PR): `prereg/run-manifest.md` Amendment 1 (Duke, Nov 5: the batch runs on Actions; if GitHub objects, S48 stops and Runpod becomes a new decision) and Amendment 2 (`sp` built and measured); PLAN.md's S47, S48 and gate lines updated.

## In flight
Nothing.

## Decisions waiting
- D14 (default A, no design change): S47 follows the default.
- None new. Duke's Actions choice is recorded, so step 5 is now a record ("design frozen; S48 runs on Actions"), not a question.

## Next step
**S47 again** (opus, high), part 3, manifest section 6 from item 2:
1. Engine reporting keys: the design-neutral BLEI share at year 20 in 40-year runs; S53's two descriptive measures under `sec`; S52's three descriptive outputs. Then `harness.js testbed ... --frozen` (it must use `tbBaseS` through `fx: true`), and the `dev/tools/explore_export.js` series. Note: explore_export and other harness modes call `s3BaseS` directly. Under `--frozen` they must take the path from `tbBaseS`.
2. Re-derive the 0.593 spending share on the frozen no-programme run (audit E17; a dated amendment if it differs). Then write MODEL_SPEC and TESTBED_SPEC for the frozen model.
3. Jobs in compassionism-sim-results (items 6-7: `program.js` R and G-J, both designs, 2% and 5%, nulls, `au`/`fx` on every row; `--frozen` in the other jobs; backing's 116 rows; levers' trim, gzip and `--sx=main`).
4. Pin the engine; dry-run every job at 2 seeds on Actions; put the timings in manifest section 3; write the ledger record.

## Pitfalls
- The session worker restarted mid-run and killed three local measurement runs. Commit before long local runs, and keep local runs to minutes.
- Run `engine_lineage.js prove` on a clean tree: untracked files can make its manifest dirty. domtest's two "manifest names a commit" checks fail until the proof is recorded.
- `git stash` with only untracked files does nothing. Don't use it to test main; use a second checkout.
- `fx.sp` adds one no-programme run per seed for each distinct set of economy-wide switches. The dry run should time it, mainly in study N (many `lv` rows; `lv` is left out of the path's key on purpose).
- Commit trailers: `Co-Authored-By: Claude <noreply@anthropic.com>` only (no model name).
- The GitHub plugin server failed to connect again; the built-in GitHub tools worked.
