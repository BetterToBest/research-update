# Handoff (Oct 30, 2026): S32 the study programme preregistered

## Step status
S32 **done**. The programme is fixed in `prereg/2026-11-study-program.md` before any run of S35-S38.

## What shipped
- research-update [#17](https://github.com/BetterToBest/research-update/pull/17): the preregistration (engine d33de07); `prereg/checks/s32_feasibility.js` (design checks; prints no outcome value); PLAN.md marks S32 done.
- Fixed in it:
  - **Headline yardstick:** CPS earnings of adults 25-64 (`lt: {s: 'all', m: 'all'}`), with the released wages beside it on every page.
  - **Headline setting:** octave raise off; every CCO row is also run with it on.
  - **Studies (seeds 1-500, three environments, about 463 core-hours, no Runpod):** seven of them.
    - A: scale, 500 to 50,000 adults.
    - B: full 32-cell synergy factorial.
    - B10: B at 10,000 adults.
    - C: ageing, 20 and 40 years, outcomes by age at joining.
    - D: participation 10-90%.
    - D10: D at 10,000 adults.
    - F: debt reading, I15.
  - **Rules:** primary outcomes, Shapley and interaction definitions, and decision rules for synergy, scale, horizon, participation (S5's figure), raise and yardstick.
- Design checks (60 adults, 2 seeds):
  - All 32 combinations run.
  - All five off equals no programme, so the factorial's empty cell is the no-programme run.
  - SZH alone moves only the design's own BLEI (a term in its formula), so BLEI claims use the design-neutral BLEI.
  - Without CCO the octave raise still acted through preset starting octaves, so it is off in every cell without CCO.

## In flight
Nothing.

## Decisions waiting
None. The yardstick choice is a modelling choice (S34's recommendation, taken), with the reason in the preregistration (decision rule 7).

## Next step
**S35** (pilot studies on Actions), opus, medium. Before any pilot it must land the preregistration's "Before the first run" items, each as a pull request:
1. `runner/jobs/program.js` in compassionism-sim-results, with row-count checks.
2. Three reporting-only measures in the engine: the price level by year to year 40, outcomes by age at joining, families in debt at years 20 and 40.
3. The debt-reading switch, off = bit-identical, guard test passing.

Each engine change gets a dated amendment in the preregistration naming the new commit. The pilots are labelled pilot and go to `pilot-<study>-<engine7>` folders.

## Pitfalls
- In the engine, `c.p.ccoOn: false` on the release row still leaves preset octaves on every adult. Any row without CCO needs `c.pw = {octaveWage: true}`.
- The no-programme row's participant-group measures (`gPart*`, `bOP*`, ...) change with `partRate` (same draw); all-adult measures do not.
- Families in debt is not a per-seed key today (only `dev/tools/baseline_realism.js` computes it).
- `/start-session` and `/end-session` cannot be invoked by Claude; this session followed the end-session file by hand.
- Commit trailers: `Co-Authored-By: Claude <noreply@anthropic.com>` (no model names).
