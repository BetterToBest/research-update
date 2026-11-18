# Handoff (Nov 18, 2026): S91 done (the ageing rerun read; S82 report updated)

## Step status
**S91 done.** Parts 1 and 2 are both finished. **S90** (the BU's two-year relief cycle) is next. **S89 is Duke's.**

## What shipped
- research-update: Amendment 7 to `prereg/2026-11-s82-v6-supply-indexing.md` (check 13 corrected before the ageing outcomes were read); PLAN.md S91 notes.
- compassionism-simulation [PR 162](https://github.com/BetterToBest/compassionism-simulation/pull/162): `s82_tables.py --age`, `dev/runs/s82-batch/` regenerated, report section 9, DECISIONS "S91 part 2". No engine change.
- compassionism-sim-results [PR 57](https://github.com/BetterToBest/compassionism-sim-results/pull/57) (merged `63af352`): `s82-tables-ab11c05/`; `SUPERSEDED-AGEING.txt` in `s82-tables-aa2a4e0/` and the six `s82-v6-*-aa2a4e0/` folders.

## What was found
- Check 13 (the rerun's no-programme ageing row matches the batch's) passed in Reference and **failed in Adverse and Stress**: outside inflation moves prices with no programme, so the defect had reached those runs too. The engine diff is the fix alone. Amendment 7 corrected the check and pairs every ageing effect on the fixed engine.
- Corrected ageing (Reference, 20 years, no backing / full): basket poverty −8.67 / −8.81 points beyond the base effect; median real wealth +$20,783 / −$1,102. At 40 years: −14.6 / −15.4 points; +$63,639 / −$160,053 (new adults start with little, so they have had fewer years of the BU).
- Every other S82 table is identical (diffed). The findings page has no ageing figure, and its S82 data are unaffected.

## In flight
- Nothing running.

## Decisions waiting
- D33 (the headline cards' headings and the full-backing condition; default: no change).

## Next step
**S90** (opus, high): find which term drives the BU's damped two-year cycle in the main row, and say whether it is a reading of the design or a defect. Then S85.

## Pitfalls
- A "this run cannot move" check proved in Reference alone can fail in Adverse and Stress, which have outside inflation. Prove such checks in all three environments.
- domtest fails after any engine edit until `python3 dev/tools/sync_earlier.py` is run and the lineage link is recorded (`node dev/tools/engine_lineage.js prove "..."`, ~10 minutes).
- Any script that loops over a run file's keys must skip `_settings` and `_meta`.
- `dev/tools/set_version.py` runs only when Duke says "release". The next version label is v5.9.21.
