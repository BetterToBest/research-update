# Handoff (Nov 14, 2026): S68 part 1 done (who pays the programme; costs at the within-year price level; per-run reset)

## Step status
S68 is **partly done**. Part 1 covered the items the Nov 13 audit added, (5) and (6), plus item 2's per-run reset. **Part 2 remains:** MODEL_SPEC section 14, ODD and TESTBED_SPEC with the plain-names table (item 1; add `fx.fin` and `wy`); pairwise on-together tests with item 7's pairs and the 10,000-adult checks (item 3); the packet for S69 (item 4). The Nov 13 audit's patch is applied here (it could not push from Chat).

## What shipped
- research-update [PR 89](https://github.com/BetterToBest/research-update/pull/89): the Nov 13 audit (`audits/2026-11-13-simulation-audit.md`, check script, PLAN S68/S63/S70 amended, S72 and S73 added, D23); `prereg/2026-11-s68-financing-identity.md` (before the build; Amendment 1 before the pilot); PLAN notes for S68, S63, S72; this file.
- compassionism-simulation [PR 100](https://github.com/BetterToBest/compassionism-simulation/pull/100) (merged, 24625e7): financing identity (`ACCT` id `fin`) for every financing reading; `fx: {fin: 'report' | 'money'}` (not in `fx: true`; 'debt' refused until S72); `o.wy` (reporting only); per-run reset of seven module states. Off identical (guard test), lineage linked, unit 336 (8 new), validate, domtest. Report `dev/reports/s68-financing-identity.md`.
- compassionism-sim-results [PR 33](https://github.com/BetterToBest/compassionism-sim-results/pull/33) (merged, ae8fcb6): `s68-financing-e03aa73` (seeds 1-100, three environments; run.txt, SHA256SUMS, DONE).

## Findings (plain words; pilot, seeds 1-100, 500 adults)
- **The C2.2 design paid by a flat contribution is not paid for.**
  - The rate averages 84% of wages and is at its 90% cap in year 20 in every seed.
  - 38% (Reference), 51% (Adverse) and 45% (Stress) of its cost has no payer.
  - Counted as new money, as the other taxes already are, its inflation is 21-33% a year (not 0.1%).
  - Basket poverty still falls 8.6-17.6 points against no programme.
  - Wealth poverty rises 37-62 points (all-cash wealth); hours fall 24-28%.
- **The release design and C2.2 under the Source are paid for**: unpaid under 0.2% of payout, so they are carried unchanged.
- **Smaller gaps:** the release design under the flat contribution leaves 5-7% unpaid; C2.2 under `hybrid` 3-4%.
- **Costs at the within-year price level** (prices rise 6-15% during the year; households were charged opening prices):
  - The release design's cut in basket poverty is 2.2-3.7 points smaller; C2.2's is 0.7-1.4 smaller.
  - No sign changes.
  - S63 carries this reading beside every basket-poverty headline (rule fixed before the run).

## In flight
- Nothing running.

## Decisions waiting
- D23 is answered (Duke, Nov 14): the financed C2.2 row is carried beside the main rows; the Hub does not lead with it until S72's frontier is in, then Duke decides again. S68's figures confirm the audit's.
- S63 files the main-row price-rule decision (S67's recommendation, both views).

## Next step
**S68 part 2** (`/start-session S68`; read its "Part 1 done" note first). S70 can also start now. S72 and S73 wait on S68.

## Pitfalls
- The Chat audit's patch applied cleanly with `git apply`. A commit whose trailer carries a model name was refused here: use `Co-Authored-By: Claude <noreply@anthropic.com>`.
- The leak S60 reported (`pdC*` in a no-programme row) was not reproduced on any row tried, even at the engine before the change. The reset makes it impossible anyway; part 2's pairwise tests should try S60's own rows.
- Never quote inflation or wealth for a flat-contribution or `hybrid` row without `fx.fin` set. `fx: true` does not include it.
- `o.wy` differs from the published measure only on a split year (`pr` with `q` > 1 under the capacity rule).
- The identity's check count exceeds rows × years: taxed rows run a year-0 pre-pass.
- The remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x` and earlier session branches in research-update still need deleting by hand.
