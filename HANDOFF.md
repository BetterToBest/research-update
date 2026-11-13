# Handoff (Nov 13, 2026): S71 done, a creditor side for debt that inflation wipes out

## Step status
S71 is **done** in one session. It added no step. S7 stays held.

## What shipped
- research-update: `prereg/2026-11-s71-creditor-side.md` (committed before the build and before any coefficient was computed; Amendment 1 before the pilot), PLAN.md (S71 findings; what S63, S68 and S70 must carry), PLAN-done.md, the prereg index, this file. Branch `claude/session-s71-28eecp`.
- compassionism-simulation [PR 97](https://github.com/BetterToBest/compassionism-simulation/pull/97): merged (a00a24f), checks green. Option `cr` of `rt` (off identical: guard test, lineage; 7 unit tests); `sources/s71_creditors.py` (who holds household fixed-rate debt: the Fed's Financial Accounts, the Survey of Consumer Finances, Doepke and Schneider 2006); report `dev/reports/s71-creditor-side.md`; tables `dev/runs/s71-creditors/`; a dated wording note in the S59 report (no figure changed).
- compassionism-sim-results [PR 30](https://github.com/BetterToBest/compassionism-sim-results/pull/30), merged (9c3b82d): `s71-creditors-f7572fd` (seeds 1-100, three environments; run.txt, SHA256SUMS, DONE).

## Findings (plain words; pilot, seeds 1-100, 500 adults; intervals unadjusted)
- **Who holds a dollar of household fixed-rate debt** (end of 2022, traced to final owners): households 32 cents (24 as deposits, 8 as bonds), businesses 32 (their shareholders), the government 27, foreigners 8.
- **Part of the loss was already in the model:** savers are paid 46% of inflation, so 11 cents of each dollar of debt relief were already being lost by the model's savers. The option adds 2 cents on their bond-like savings and 20 on their shares. 66 cents fall outside the model (government 30, foreigners 16, households not in the model, mostly retired, 20).
- **Wealth poverty does not change:** −12.5 points (release design, Reference) with or without the creditor side; −12.4 when every dollar falls on the model's households; −6.7 with no debt relief. The poorest fifth get $40,900 of relief each and bear $580 of the new charges.
- **The programme still lowers the top 1% share** in all five creditor readings and all three environments (−1.02 main; −0.67 with nothing left outside; −1.14 before). By the preregistered rule the direction is established for both designs, among creditor readings.
- **The sign turns on whether debt relief happens, not on the lender.** The no-debt-relief reading (+1.23) removes the borrower's gain; a creditor side adds the saver's loss. S59's wording is corrected by a dated note.
- **S59's two readings are not bounds** for the top 10% share, the bottom half's share and the Gini (the creditor readings are more equalising than S59's main reading), nor for average wealth with nothing outside. Average real wealth falls further (−$96,000 per adult against −$57,700); the median adult still gains (+$31,500).
- **Nothing else moves** (inflation, cost of living, basket poverty: 0.06 point or less).
- **Recommendation for S63, fixed before the results:** the creditor side (main incidence) as a main-row candidate for wealth and concentration outcomes; beside it S59's main and no-debt-relief readings, holders of record, shareholders not charged, the model as all households, and nothing outside as the upper bound.

## In flight
- Nothing.

## Decisions waiting
- D21: carry the C2.2 design paid for by a contribution on every round-2 outcome (default: yes, as a labelled reading).
- S63 files the main-row price-rule decision (S67's recommendation, both views).
- Nothing new from S71.

## Next step
**S60** (bargaining power): the first open row of the Order table. S62 waits on S60; S68 and S70 wait on S60 and S62.

## Pitfalls
- A commit message carrying a model name is refused by the session's safety check (and by the project's rule). Use the trailer `Co-Authored-By: Claude <noreply@anthropic.com>`.
- The no-debt-relief reading is not "the creditor side at its strongest". Never present it as a bound for creditor readings; quote both beside any wealth result.
- The main creditor reading charges shareholders the lenders' loss without the gain businesses make on their own fixed debt (not modelled). Always show "shareholders not charged" beside it. Lenders do not fail in the model.
- The model's top 1% bear 26% of the new charges; the Fed's distributional accounts, for all households, suggest 46-48%. A limit, stated in the report.
- `cr` is the one rule that reads adults' weights (through four yearly totals). With unweighted totals (`w: 0`) the `cr*` keys are not comparable in dollars with other rows.
- Totals taken before the year's loop left a ledger gap of 3 parts in a million (a pathway exit pays equity into wealth in between); a full-run ledger test caught it. Keep such tests.
- These rows read wealth at year 20 only; S63 must read yearly averages too (S67).
- `node domtest.js` needs `npm install`, then `python3 dev/tools/sync_earlier.py` and the lineage proof after any engine edit. Run pilots from a clean worktree, in pieces that each save a file.
- The remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x` and earlier session branches in research-update still need deleting by hand.
