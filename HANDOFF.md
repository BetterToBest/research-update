# Handoff (Nov 9, 2026): S57 done, distribution measures (reporting only)

## Step status
S57 is **done**. S7 stays held until round 2 is ready for release (PLAN.md).

## What shipped
- research-update `prereg/2026-11-s57-distribution-measures.md` (committed before the build; Amendment 1: Holm reads the normal tail of the mean over its bootstrap standard error, because a 2,000-replicate bootstrap tail share cannot reach Holm's first threshold for 378 cells); PLAN.md; this file. Pull request [78](https://github.com/BetterToBest/research-update/pull/78).
- compassionism-simulation [PR 89](https://github.com/BetterToBest/compassionism-simulation/pull/89): study option `dm` (reporting only): top 1%/10% and bottom 50% shares of wealth and income, income Palma, wealth top-10-to-bottom-40 ratio (only where the bottom 40% hold positive wealth), 21-point real percentile grid, wealth-fifth mobility, labour's share, debt depth; weights ready for S59 (all 1). Guard test identical, lineage linked, validate, unit (272), domtest (153) pass. Report `dev/reports/s57-distribution-measures.md`; tools `dev/tools/s57_dm.js`, `s57_table.py`; findings data file `data/studies/s57-distribution.json` (new; no published number moved).
- compassionism-sim-results [PR 24](https://github.com/BetterToBest/compassionism-sim-results/pull/24): `s57-distribution-f156393` (seeds 1-100, three environments; run.txt, SHA256SUMS, DONE); merged (4b48276).

## Findings (plain words; pilot at 100 seeds, intervals unadjusted; 366 of 378 estimates exclude zero, 359 survive Holm)
- Start with no programme: top 10% hold 64.6% of wealth (CBO 69% / 60%), bottom half 3.6% (CBO 6%), top 1% 20.8% (Fed 32.5%): the top 1% gap is for S59.
- Reference, end of year 20: top 10% wealth share 58.9% without the programme; -27.0 points (release row), -33.3 (C2.2 design). Income shares: release row +1.0 point at the top 10%, C2.2 design -1.7. Families in debt 22.0%; -12.4 and -21.2 points.
- Real-dollar wealth falls under the release row because its prices rise about 32% a year (median real wealth equals the engine's `medWealthReal`); shares and Ginis are not affected.
- Rank mobility rises, partly because compressed wealth reorders ranks easily; labour's share is near 100% by construction; median debt sits on the -$10,000 floor.

## In flight
- Nothing.

## Decisions waiting
- None.

## Next step
**S58** (opus, xhigh; may take 2 sessions): the price rule. S66 (opus, high) can also start. S59 now waits only on S56 and S57 (done).

## Pitfalls
- Key suffixes: `S` (start) and `E` (end), never `0`: `dmWt1` + `0` collided with `dmWt10`.
- The Holm step needs a p-value finer than the bootstrap tail share (see Amendment 1).
- `no_figure_change.py` fails on any engine change by design; for a reporting-only engine step the guard test and lineage are the proof, and the check was read for data files and reports only.
- Run pilots from a clean worktree (`git worktree add`); remove the worktrees `sim-pilot`, `sim-main` afterwards.
