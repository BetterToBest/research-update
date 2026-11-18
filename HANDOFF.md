# Handoff (Nov 18, 2026): S91 part 1 (the ageing defect found, fixed, and its rerun dispatched)

## Step status
**S91 partly done.** Fixed, proved, and the rerun dispatched; the participation pilot corrected. **Left (part 2):** read the six rerun folders once they show `DONE`, then update the S82 report's section 9 and tables. **S90** is still open. **S89 is Duke's.**

## What shipped
- compassionism-simulation [PR 160](https://github.com/BetterToBest/compassionism-simulation/pull/160) (merged `ab11c05`): `lfDraw` stores `_lfP = DR_PL`. Guard test identical, 395 unit tests, domtest 162/162, lineage link recorded, `earlier-engine.html` resynced. Decisions: `dev/DECISIONS.md` "S91". No version change.
- compassionism-simulation [PR 161](https://github.com/BetterToBest/compassionism-simulation/pull/161): the participation report's dated correction and `dev/runs/s73-participation/tables-ageing-corrected.md` (see "In flight" if not merged).
- compassionism-sim-results [PR 56](https://github.com/BetterToBest/compassionism-sim-results/pull/56) (merged `9264ebe`): `s73-ageing-b362152/` (the pilot's ageing rows rerun at 100 seeds, spliced in) and `s73-participation-d12fd0f/CORRECTED.txt`.
- research-update: the addendum to Amendment 6 in `prereg/2026-11-s82-v6-supply-indexing.md` (cause, fix, proofs, check 13, reach, dispatch table); PLAN.md S91 note.

## What was found
- **Cause:** with ageing and the yearly labour-force flows (on in the main row), a newcomer drawn out of the labour force at entry kept its wage, already in that year's prices, but not the price level of the draw. A return raised the wage by every price rise since year 0, counting prices twice, and the newcomers' wage index compounded it. Amendment 6's "`ag` alone" run still had the main row's flows.
- **Proof:** S82 job, 231 rows, seeds 1-2: 229 identical; only E.age.a0 and E.age.a1 moved. Seed 1, share 0, wage over prices at year 20: $929,458 before, $93,763 after ($94,891 without ageing).
- **Reach:** only S82's ageing rows and the participation pilot's agP/agS. Corrected pilot: full-coverage cut with ageing 38.3-45.1 points (38.5-45.6 before); programme inflation with ageing 4-11 points a year higher; the ageing-minus-no-flows contrasts much smaller. The release's v5.3 ageing rows have no flows.

## In flight
- GitHub Actions, run-study runs 143-148 (dispatched 21:31 UTC), engine `ab11c05`, job `s82.js --rows=134-136`, seeds 1-500, 10 shards each. Results land in compassionism-sim-results `s82-v6-age-{ref,adv,str}-{20,40}-ab11c05/`; each is done when it has `DONE`.
- PR 161 was waiting on CI at the end of this session; merge it if green.

## Decisions waiting
- D33 (the headline cards' headings and the full-backing condition; default: no change).

## Next step
**S91 part 2** (opus, high): check 13 (E.age.none equals the batch `aa2a4e0` in every key and seed), then E.age.a0/a1 replace the batch's rows in question 6. `dev/tools/s82_tables.py` needs an option to substitute the rerun folders for rows 134-136. Then replace the "Update" paragraph in the report's section 9 (`dev/reports/s82-supply-indexing.md`), lift the full-backing "provisional" label, add a `SUPERSEDED`-style note for the ageing rows in the `aa2a4e0` folders, and check whether the findings page shows any ageing figure. Then S90, then S85.

## Pitfalls
- domtest fails after any engine edit until `python3 dev/tools/sync_earlier.py` is run and the lineage link is recorded (`node dev/tools/engine_lineage.js prove "..."`, ~10 minutes).
- The S73 pilot's tables tool prints "engine d12fd0f" in its headers even for the spliced file; `run.txt` says so.
- In the S73 contrast tables the last column is programme inflation, not wealth.
- Adverse and Stress have outside inflation, so ageing rows with the flows move even with no programme there.
- `dev/tools/set_version.py` runs only when Duke says "release". The next version label is v5.9.21.
