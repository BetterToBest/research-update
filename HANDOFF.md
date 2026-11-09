# Handoff (Nov 9, 2026): S61 done, baseline scope (adults outside the labour force; borrowing for ordinary spending)

## Step status
S61 is **done**. Duke asked at the start (Nov 9) to hold S7 until round 2 is ready for release: S7 now runs just before S65, and S57 and S58 no longer wait on it (PLAN.md).

## What shipped
- research-update (branch `claude/friendly-ptolemy-lh8djy`): `prereg/2026-11-s61-baseline-scope.md` (criterion C1-C4 fixed before the build; Amendment 1, build choices; Amendment 2, the own-income table corrected to 0.5-point steps after a check against its source); PLAN.md (S7 held; S61 done; S63 carry-forward; D19 and D20 as answered); this file.
- compassionism-simulation [PR 88](https://github.com/BetterToBest/compassionism-simulation/pull/88): switch `LF_SCOPE` (row option `lf`) and the debt reading extended (`dr`: `lim` moved with prices, main $2,500 from the SCF 2025; `liq`; `fl: 'fpl'`); sources `sources/lf_scope.py`, `sources/s61_borrowing.py`; pilot tool and tables; report `dev/reports/s61-baseline-scope.md`; DECISIONS.md. Guard identical, lineage linked, validate, unit (264), domtest (153) pass.
- compassionism-sim-results [PR 23](https://github.com/BetterToBest/compassionism-sim-results/pull/23): folder `s61-scope-1d9ab84` (pilot, seeds 1-100, three environments; run.txt, SHA256SUMS, DONE).

## Findings (plain words; pilot at 100 seeds)
- A positive borrowing limit changes how deep households fall, not how many fall into debt: families in debt at Year 20 (Reference) 22.0% frozen, 21.6% with the $2,500 cap; only a limit of zero gives 12.3%. The gap to the SCF's 9.3% stays open; no constant was tuned to it.
- Adults outside the labour force (17.3%) bring the share with earnings to 82.7% (CPS 80.9%) and official poverty from far below the survey to somewhat above it (the model's households hold no other relatives).
- No reading changes the sign or significance of the C2.2 design's effects, but with `lf` its wealth-poverty harm grows from +0.7 to +9.8 points in Reference. Not yet traced.
- Recommended to S63: the cap at $2,500 and `lf` as main-row candidates, the other readings beside them.

## In flight
- Nothing.

## Decisions waiting
- None new. D19 and D20 were answered by Duke in the ledger (not the defaults): the Source pays a PTF cost gap as an explicit subsidy; the density tests become a smooth curve. PLAN.md (S62, S63) records both.

## Next step
**S57** (sonnet, high): distribution measures, reporting only; it now waits only on S56. S66 and S58 can also start; S60 now has S61 and waits on S58.

## Pitfalls
- `lf` reuses the engine's retiree state (`a._ret`); any rule reading `a._ret` as "67 and over" must check `a._lf`. Zero-income adults have wage 0: guard every ratio to the wage.
- Check engine input tables against their source's means: the 5-point percentile table overstated income by up to 280% (care) through its top bin.
- Run pilots from a clean worktree (`git worktree add`), so each output's manifest is clean.
