# Handoff (Nov 13, 2026): S67 done, the price rule's derivation, time step and wording

## Step status
S67 is **done** in one session (the plan allowed two). It added no step. S7 stays held.

## What shipped
- research-update: `prereg/2026-11-s67-price-rule-derivation.md` (committed before any regression or run; Amendment 1 before the pilot), PLAN.md (S67 findings; what S63, S68 and S70 must carry), PLAN-done.md, the prereg index, this file. Branch `claude/jolly-davinci-dbcv2x`.
- compassionism-simulation [PR 96](https://github.com/BetterToBest/compassionism-simulation/pull/96): open, checks running (merged once they pass). Three dated correction notes (S58 and S57 reports; no figure changed); the closed form (`dev/tools/s67_closed_form.py`); US price-gap regressions (`sources/s67_pstar.py`) and a panel of high-inflation episodes (`sources/s67_panel.py`); options `q`, `bv`, `bd` of the capacity price rule (off identical: guard test, lineage; 7 unit tests); report `dev/reports/s67-price-rule-derivation.md`; tables `dev/runs/s67-price/`.
- compassionism-sim-results [PR 29](https://github.com/BetterToBest/compassionism-sim-results/pull/29), merged (9f80e61): `s67-price-985f0c3` (seeds 1-100, three environments; run.txt, SHA256SUMS, DONE).

## Findings (plain words; pilot, seeds 1-100, 500 adults; intervals unadjusted)
- **Both price rules assume that sustained new money passes into prices one for one; neither finds it.** The S58 report said the new rule "agrees with the evidence" as a result. Corrected by dated note, with a replacement Hub sentence.
- **The capacity rule's waves are its own arithmetic.** Yearly inflation follows a two-term formula (now written out, and within about 1 point of the engine). The size of the wave is set by one number, how much of last year's inflation carries forward, and defensible values of it give waves from 5 to 68 points.
- **The rule's response speed is not identified.** Estimated on the variable the rule uses (the gap between the money-implied price level and prices; US, 1970-2024) it is −0.001 (standard error 0.05): 0.88 in the 1970s, 0.04 since 1984. With proper standard errors S58's own 0.445 does not exclude zero.
- **In 77 episodes of sustained inflation above 20%** (52 countries): about two thirds of last year's inflation carries over; prices close the gap to money at 0.05-0.18 a year (not distinguishable from zero); inflation ran ahead of money in two thirds of episodes, by 4-6 points a year.
- **A shorter time step halves the waves but does not remove them** (C2.2, Reference: 19.8 points against 39.1 with values fitted to quarterly data; unchanged with the yearly values converted to quarters). The waves come from the values, not the step.
- **The "shortage" under today's rule was the yearly step:** run in quarters, the same results with 1.9% of demand unmet instead of 22.5%, and prices 12.6% above opening levels during the year.
- **Basket poverty and the cost of living do not depend on the price rule** (0.3 point or less). **The year-20 wealth-poverty effect changes sign with the rule (−1.8 to +1.1); the yearly average does not (+1.9 to +3.6).** If inflation runs 13% ahead of money, as the episodes suggest, the programme's inflation is about 6 points a year higher and its wealth-poverty effect 5-7 points worse, under either rule.
- **Recommendation for S63, set by a rule fixed before the results:** today's rule as the main row; the capacity rule, the quarterly reading and the faster-than-money reading beside it; every wealth outcome at year 20, year 40 and as a yearly average. This reverses S58's preregistered recommendation; both views are in the report's section 9.

## In flight
- Nothing.

## Decisions waiting
- D21: carry the C2.2 design paid for by a contribution on every round-2 outcome (default: yes, as a labelled reading).
- S63 files the main-row price-rule decision, now with S67's recommendation and both views.
- Nothing new from S67.

## Next step
**S71** (a creditor side for debts that inflation wipes out): the first open row of the Order table. S60 can start too. S62 waits on S60; S68 and S70 wait on S60, S62 and S71.

## Pitfalls
- Two papers the step named (Hallman, Porter and Small 1991; Cagan 1956) could not be opened from the session (paywalled). Nothing is quoted from them; the forms come from papers that restate them. Anyone with access should check the report's section 1 against the originals.
- Never quote a wealth-poverty or real-wealth figure at year 20 alone under any price rule: give the yearly average beside it. Never quote the "rationed share" or shadow-price figures on a yearly step as facts about the economy.
- The velocity drift (0.132) is one reading of noisy data (0.101 without hyperinflation years; the cross-section slope is 1.06 or 0.84). A reading, never a main value.
- The preregistered wave test passed by a hair in Reference (0.51 against a threshold of 0.5) and would fail in Adverse and Stress (0.31-0.32). The recommendation does not depend on it (the other test failed), but do not describe the waves as "surviving" without those figures.
- `node domtest.js` in compassionism-simulation needs `npm install`, then `python3 dev/tools/sync_earlier.py` and the lineage proof after any engine edit; its failures before that are expected.
- The pilot runner first failed on a quote in a description string; a `node --check` on every new tool before a run costs nothing.
- Never quote a wealth or concentration result under `rt` without the no-debt-relief reading (`chi: 1`) beside it. With the tail on, read only weighted measures.
- The session machine restarts: run pilots in pieces that each save a file. After `node harness.js unit`, grep the whole output for FAIL and check the exit code.
- The remote branches `claude/s66-low-share-trace` and earlier session branches in research-update still need deleting by hand.
