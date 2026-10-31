# Handoff (Oct 31, 2026): S6 C2.2 coverage and adequacy, done (pilot)

## Step status
S6 **done**. The design options are modelled and preregistered (study K). The 100-seed pilot ran on Actions and its report is written. Which option the design adopts is Duke's call: ledger decision D8. Study K's 500-seed rows run in the S48 batch.

## What shipped
- compassionism-simulation [#53](https://github.com/BetterToBest/compassionism-simulation/pull/53), merged `3e79adb`: the switch `C22` (row option `c22`). It models the Act's status rule (`u`, 4.1% and 5.6%, Pew 2023), automatic distribution (`auto`), and the BU indexed to the price of food, housing and medical care (`idx: 'needs'`). It adds `c22NeedsBU()` ($1,788.43 a month, MIT 2026) and coverage keys. Off by default; guard test identical.
- compassionism-simulation [#54](https://github.com/BetterToBest/compassionism-simulation/pull/54), merged `395dd5b`: a rounding tolerance in the coverage tally (preregistration amendment 1).
- compassionism-simulation [#55](https://github.com/BetterToBest/compassionism-simulation/pull/55): the report `dev/reports/c22-coverage-adequacy.md`, with tables in `dev/runs/c22-pilot/` written by `dev/tools/c22_pilot.py`.
- compassionism-sim-results [#9](https://github.com/BetterToBest/compassionism-sim-results/pull/9), merged: `runner/jobs/c22.js`. Results `pilot-k-3e79adb` (first run, kept) and `pilot-k-395dd5b` (the one used); both have run.txt and SHA256SUMS.
- research-update #21, #22 and this PR: `prereg/2026-11-c22-coverage-adequacy.md` with amendment 1; study programme Amendment 3; S47 note; section 102 items in `audits/corrections-package-s5.md`.

## What the pilot shows (100 seeds; Reference, 20 years, CPS unless stated)
- As released, the BU reaches 83% of adult-years (43% in Stress) and covers housing, food and medical care in **none**: it pays about 65% of those needs.
- Coverage closes only with automatic distribution and no status rule. Adequacy closes in no row. The "C2.2 design" (automatic, all residents, needs level, needs-indexed) covers 95% of adult-years; the rest are single parents (a quarter-BU child allowance is below a child's needs).
- Adults left out by the status rule end with too little wealth 8 to 53 points more often than with no programme, in all 12 cells.
- The C2.2 design is better than the release row on cost of living and on wealth in all 12 cells, at $23,700-38,700 more per adult-year. Automatic distribution alone is mixed: worse on wealth in Adverse and Stress.

## In flight
Nothing running.

## Decisions waiting
- **D8** (Duke): adopt a C2.2 design change? The default keeps the design as written; NEEC's C2.2 hold (its decision 69.4) stands, and the findings are published.

## Next step
**S14** (population-weighted cost-of-living line), opus, high: next in the Order table. S13 and S50 follow; all before S47.

## Pitfalls
- A BU set exactly to the needs failed `>=` through rounding in 1 adult-year in 10 (amendment 1). Compare money with a relative tolerance.
- `gh` works through REST only (`gh api`), not GraphQL. `gh workflow run` fails; dispatch with `gh api -X POST .../dispatches`.
- Never force-push; after a merged PR, restart the session branch from main and push normally.
- `c22` on the none row only marks who is left out (identical outputs), so the same adults can be paired.
- If Duke changes the design under D8, the release row changes: a dated amendment to both preregistrations before S47.
