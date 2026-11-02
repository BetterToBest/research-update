# Handoff (Nov 2, 2026): S53 partly done, security outcomes beyond wealth (pilot dispatched)

## Step status
S53 is **partly done**. The measures, the per-year series for S19, the addendum, the job and both consumer scripts have landed. The pilot (study P, seeds 1-50) is running on Actions. What remains: once `DONE` appears, run the analysis, write the plain-words pilot report, and list what S47 must carry. That is the next session's work.

## What shipped
- compassionism-simulation [#66](https://github.com/BetterToBest/compassionism-simulation/pull/66) (merge `ENGINE_COMMIT`): study option `sec`, reporting only (`index.html` SEC block: `secNew`, `secAcc`, `secYear`, `secRes`, `SEC_KEYS`, `S19_KEYS`). Guard test identical; lineage linked; 4 unit tests in `secUnitSuite`; validate, unit (237), domtest (153) and glossary all pass. Reading `dev/reports/s53-security-reading.md`; choices `dev/DECISIONS.md` (S53). Consumer scripts: `dev/tools/s53_security.py` (study P analysis, `--check`) and `dev/tools/s19_series.py` (S19 loader and check).
- compassionism-sim-results [#13](https://github.com/BetterToBest/compassionism-sim-results/pull/13) (merge d1cbadd): `runner/jobs/security.js` (10 rows per environment; `--check` passes).
- research-update (this PR): `prereg/2026-11-security-addendum.md` (study P), study programme Amendment 7, and PLAN.md (S53 status; S47's S53 line).

## In flight
- Study `s53-security`: engine `ENGINE_COMMIT`, job `security.js`, `job_args` `--env=all --procs=4`, seeds 1-50, 5 shards; run RUN_LINK. Results land in compassionism-sim-results `s53-security-ENGINE7/`. It is done when that folder holds `DONE`.
- Next session: `python3 dev/tools/s53_security.py <folder> --check`, then `python3 dev/tools/s53_security.py <folder> --out dev/reports/s53-security-tables.md`, and `python3 dev/tools/s19_series.py <folder>`. Write `dev/reports/s53-security.md`, labelled pilot.

## What the measures are (no results yet)
- Groups: all adults, those who take part, those who choose not to.
- Uncovered income drops: resources (money plus in-kind help) fall 25% or more, and 20% of savings does not cover the fall.
- Months of need covered without wages: conversion proceeds are left out, the cautious reading.
- Hours a week the basics cost at the adult's usual wage.
- PTH tenancies ended. Forced PTH moves are zero by construction: no rule ends a tenancy.
- Displacement by price: entries into the engine's housing-distress test. This is a proxy, because the model has no moving decision.
- Essentials paid in money, as a share of the budget and of the essentials.
- Hours and exposure are true by construction, and the report must say so.

## Decisions waiting
- None new.

## Next step
**S53** again (the pilot report), once `DONE` is in. Then S54 and the S47 freeze.

## Pitfalls
- The 2-seed local test showed savings-based measures (months covered) can move against the design for non-participants while income-drop measures improve. Do not read 2 seeds; wait for the 50.
- The S19 series run to year 40 in the engine; the job keeps years 0-19 for 20-year rows (0 past the run otherwise).
- `secPx` is non-zero for some adults who chose not to join the CCO: PTH membership is drawn apart from CCO membership.
- Use the `Co-Authored-By: Claude <noreply@anthropic.com>` trailer only. The two stray branches named earlier are still there for Duke to delete.
