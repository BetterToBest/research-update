# Handoff (Nov 6, 2026): S47 part 5, design freeze complete

## Step status
S47 is **done**. Every job passed its 2-seed dry run and loads in the script that reads it (`prereg/run-manifest.md` section 7, result). The manifest now has measured timings and a shard plan (section 3), a cost (section 8) and the status "frozen" (Amendment 4). The ledger record is D15 (default: S48 proceeds on Actions).

## What shipped
- compassionism-simulation [#77](https://github.com/BetterToBest/compassionism-simulation/pull/77) (tools only, no engine change):
  - `s19_series.py` and `s53_security.py --check` read each row to its own horizon (study R holds 20- and 40-year rows in one file).
  - `merge_parts.py` reads `panel.js` pieces.
  - New `batch_load.py`: loads and checks the A-J and R folders. Its `by_design()` gives the pilots' row names.
- research-update (this branch): manifest sections 3, 7 and 8, status frozen, Amendment 4; PLAN.md's S47 and S48 entries.
- Dry-run folders `dry-*-ce8d030/` in compassionism-sim-results (26 folders, all `DONE`, checksums pass). They are the record of the dry run; they are not results.

## In flight
Nothing.

## Decisions waiting
- D15 (default A, proceeds): the design is frozen and S48 runs the manifest on Actions. Duke is asked to read the spending-share change (Amendment 3): basket poverty does not move, and the programmes' effect on wealth poverty changes sharply. Option B holds S48 until Duke has read it.

## Next step
**S48** (opus, medium): dispatch the manifest exactly as section 3 says, on run-study.
- Engine `ce8d030`; job scripts at compassionism-sim-results main (`031861a` or later).
- At most 20 runners at once. Start, confirm they started, record the run IDs here, end.
- Don't dispatch N3 and N3x yet. They wait for N1 and N2: `s54_levers.py --s1 N1 --s2 N2 --select LIST` (rule 4), then a dated amendment to the levers addendum, then dispatch.
- X's panel check waits for the frozen R-panel to be merged.

## Pitfalls
- **Shard counts:** A runs as two dispatches, `--sizes=500,2000,10000` (25 shards of 20 seeds) and `--sizes=50000` (100 shards of 5 seeds).
- **R-panel shards:** `panel.js --n=500 --parts=5`, workflow seeds 1-30. Its seed range is a shard index, not seeds. Each shard runs all 500 seeds for a fifth of the rows.
- **Pre-dry-run estimate:** the R-panel was estimated at 2 runner-hours; it measures 58.
- **Levers processes:** `levers.js --env=all --procs=2` runs 3 processes (one per environment). That is what was timed; keep it.
- **Reading S53 checks:** `s54_levers.py` takes `--s1/--s2/--s3 FOLDER`. A bare folder with `--check` checks nothing and exits 0.
- **Merging the R-panel:** copy the shards to `release-panel[-40]-ENV.partI.json`, run `merge_parts.py DIR ENV YEARS 5 OUT`, then `merge_panel.py`. `merge_panel.py` rewrites `index.html`, so run it in a copy, never on main.
- **GitHub plugin:** the GitHub plugin server failed to connect again; the built-in GitHub tools worked.
