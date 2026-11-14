# Handoff (Nov 14, 2026): S68 done (round 2 written down, tested together; the candidate main row)

## Step status
S68 is **done**. Part 1 (financing identity, within-year costs, per-run reset) shipped earlier today; part 2 shipped items 1, 3, 4 and 7. One change to the plan: the S69 packet's zip is built at the start of S69, after S72 and S73 add their switches to the candidate main row (PLAN S68 and S69 notes). The tools are built and checked.

## What shipped
- compassionism-simulation [PR 101](https://github.com/BetterToBest/compassionism-simulation/pull/101) (merged, f910774): MODEL_SPEC section 14, ODD section 8, TESTBED_SPEC section 7 (plain names of every row option); the candidate main row `r2MainRow`; on-together tests `r2PairCheck` / `dev/tools/s68_pairs.js`; 10,000-adult checks `dev/tools/s68_big.js`; three fixes; packet tools for S69; report `dev/reports/s68-round2-spec-tests.md`; 341 unit tests, guard, validate, domtest, lineage all pass.
- research-update: PLAN notes for S68, S63, S69, S70; this file.

## Findings (plain words)
- **The switches work together.** Each round-2 switch got one other reading. Each one alone and every pair (121 rows) ran on the candidate main row in three environments at 5 seeds. All 363 runs pass: books balance, 8 draws per adult-year, no non-numbers, each switch's own checks. Run order changes nothing.
- **Fixed:**
  - Adults outside the labour force set not to convert gave non-numbers under a programme.
  - When a PTH member died (ageing), the heir's home's books missed the inheritance; this was true of the published ageing reading too. New switch part `fx.pe`, on in the main row.
  - A double count of idle capacity (price-rule slack with the spending layer's slack) is now refused.
- **Limit:** with no debt relief, the creditor side leaves 8-11% of its ledger unplaced under high inflation, so that reading runs with the creditor side off (as S59 and S71 did).
- **10,000 adults:**
  - The tail moves inflation by under 0.01 points.
  - The creditor totals agree per adult within 1.3%.
- **Not round 2's:** the hours response depends on population size in the frozen engine (C2.2: +11% at 500 adults, +1.8% at 10,000). It must be traced before an hours figure is quoted (S63, S70).

## In flight
- Nothing running.

## Decisions waiting
- None new. S63 files the main-row decision; the candidate main row is now `r2MainRow` (Claude's recommendation).

## Next step
**S72** (government budget line and the financing frontier; `/start-session S72`): it waits only on S68. S73 can follow; S69, S70 and S63 wait on both. S72 adds `fx.fin 'debt'` and its switch to `R2_MAIN` and `R2_ALT`, then reruns `dev/tools/s68_pairs.js`.

## Pitfalls
- A refusal inside `tbStudy`'s per-row setup must come before any switch is set; my first one threw too late, and the switches it had set leaked into every later unit test. Put new refusals in the loop at the top of `tbStudy`.
- `crUn` is in dollars, not a share: compare it with the creditor ledger.
- A worker restart kills background jobs; rerun them and check the result files exist.
- Commit trailers: `Co-Authored-By: Claude <noreply@anthropic.com>` (no model name).
- The remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x` and earlier session branches in research-update still need deleting by hand.
