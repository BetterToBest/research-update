# Handoff (Nov 14, 2026): S72 done (the government account and the financing frontier)

## Step status
S72 is **done**. Preregistered first (`prereg/2026-11-s72-government-budget.md`), with Amendment 1 before the pilot and Amendment 2 after the frontier ran (a check added, nothing changed).

## What shipped
- compassionism-simulation [PR 102](https://github.com/BetterToBest/compassionism-simulation/pull/102):
  - Row option `gv`: the government account, `fx.fin 'debt'` (borrowing) and `'cap'` (a higher cap), the contribution's share, base and weighted books.
  - `gv: {}` in the candidate main row; `R2_ALT` gains `gv`.
  - 9 unit tests (350 in all); guard identical; lineage linked; domtest 153.
  - On-together tests: 137 rows × 3 environments, all pass.
  - Report `dev/reports/s72-government-budget.md`; MODEL_SPEC 14.14.
- compassionism-sim-results [PR 34](https://github.com/BetterToBest/compassionism-sim-results/pull/34) (merged): `s72-government-df9cfbe` (pilot 100 seeds; frontier 20 seeds, with and without the weighted tail).
- research-update: prereg and amendments; PLAN notes for S72, S70 and S63; this file.

## Findings (plain words)
- **C2.2 cannot be paid for by a contribution on wages.** With the rest as new money, inflation is 32-46% a year. With the rest borrowed, debt passes the size of the economy by year 5 and explodes: 7-9 times GDP by year 20 even with no rate premium. A 99% cap raises less than 90%.
- **The closest financed C2.2 row** taxes all money income at 69-78%, raising the whole payout:
  - Inflation is 6.4-7.8% with the rest as new money.
  - Borrowed instead, inflation is 0.1-0.2% and debt is 12-23% of GDP at year 20, falling.
  - Paid this way, its basket poverty moves only −11.6 to +1.2 points, against −30 to −38 under the Source.
- **The release design can be paid for** on wages plus conversion proceeds, or on all money income, with a cap of 70% or more (inflation 0.7-3.2%). On wages alone it cannot (12% in Adverse). Paid on wages, its basket poverty rises (+1 to +15 points).
- **Under the Source rows**, the programme's inflation erodes nearly all of today's fixed-coupon federal debt, and the government loses about $30,500 per adult as a lender.
- **Found:** the weighted tail's 18 adults act unweighted in decisions and prices, so any rule that charges capital income lets them distort hours and inflation. The frontier was rerun without the tail; that run is read for the wider bases.

## In flight
- Nothing running.

## Decisions waiting
- None new. D23 (whether the Hub may lead with a financed row) is to be filed again by S63 with S72's figures. Claude's recommendation is written in PLAN S63.

## Next step
**S73** (participation margin; `/start-session S73`). It waits only on S68, and adds its switch to `r2MainRow` and `R2_ALT`, then reruns `dev/tools/s68_pairs.js`. S70, S69 and S63 follow.

## Pitfalls
- With the weighted tail on, sums over adults are unweighted. Check any new rule that reads capital income or wealth against a run without the tail.
- Debt keys explode in some readings. Read medians and `gvY100`, not means.
- Run long studies from a clean `git worktree` at the committed engine, so manifests are clean. A second worktree avoids checkout clashes while another job runs.
- Commit trailers: `Co-Authored-By: Claude <noreply@anthropic.com>` (no model name).
- The remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and earlier session branches in research-update still need deleting by hand.
