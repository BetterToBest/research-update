# Handoff (Nov 18, 2026): S82 part 3b (the rerun read, the report, the findings page)

## Step status
**S82 done** (parts 1-3b). One reading is withheld: ageing at no backing measures a defect (Amendment 6). Its fix and the rerun of the ageing rows are step **S91**. **S90** (the BU's two-year relief cycle) is still open. **S89 is Duke's.**

## What shipped
- compassionism-sim-results [PR 55](https://github.com/BetterToBest/compassionism-sim-results/pull/55) (merged `fb4e92c`): `s82-tables-aa2a4e0/`, the batch's tables with `analysis.txt` and `SHA256SUMS`. Checks 1-12 pass in all six environment-horizons.
- compassionism-simulation [PR 158](https://github.com/BetterToBest/compassionism-simulation/pull/158) (merged `babf033`). No engine change; version unchanged. It carries:
  - the report `dev/reports/s82-supply-indexing.md` and the tables `dev/runs/s82-batch/`;
  - the findings page's dated backing note, replaced by the curve under the v6 readings with break-even shares (`site/round2.js`; `data/studies/s82-supply.json` and `s82-breakeven.json`, from `dev/tools/s82_page_data.py`);
  - `dev/DECISIONS.md` "S82 part 3b".
- research-update: Amendment 6 in `prereg/2026-11-s82-v6-supply-indexing.md`; PLAN.md (S82 note, new step S91); the outside reading and its triage (`audits/2026-11-18-s82-results-reading-nemotron.md`).

## What was found
- **Supply limit:** costs at most 0.54 points of basket poverty (sourced) and 3.7 (strict bound), at 20 years. Basket poverty's effect holds everywhere, but it is the only real test, since the limit moves only basket poverty (unspent money goes to other goods and no price moves). The report and page say so.
- **Wages:** at half of programme inflation, never made up, the programme with no backing is worse than no programme on basket poverty. Break-even backed share 0.08-0.26 (20 years), 0.30-0.49 (40 years). Made up a year later: 0.3-1.5 points.
- **The BU's delay** at no backing: monthly 0.7-1.3 points, quarterly 1.5-2.7, yearly 7-11.
- **Ageing defect:** with programme inflation, wages outrun prices (real wage 7-20 times normal at year 20). One seed isolates it to `ag`. Fully noted in PLAN.md S91.

## In flight
- Nothing on GitHub Actions.
- Nothing else. The outside reading of the results is done and triaged: `audits/2026-11-18-s82-results-reading-nemotron.md`. No figure changed; six wording points were fixed.

## Decisions waiting
- D33 (the headline cards' headings and the full-backing condition; default: no change).

## Next step
**S91** (opus, high): find and fix the ageing defect behind the guardrails, then rerun the S82 job's ageing rows (`--rows=134-136`, six environment-horizons) under a dated addendum. It completes S82's record. Then S90; S85 after both (it builds on the engine they inspect).

## Pitfalls
- The tables tool printed a NOTE that the supply rows equal the base row in wealth, basic-living and inflation keys. That is the limit's design (money respent, no price moves), not a defect. Do not read "holds" for those outcomes as evidence.
- The findings page prints no typed figure. New figures go through a data file and `snum()`. Run `node dev/tools/check_round2.js` and `node domtest.js` (162 checks). `python3 dev/tools/reader_codes.py --check` refuses step codes (S82, S70...) in reports and page text.
- `dev/tools/set_version.py` runs only when Duke says "release". The next version label is v5.9.21.
- The outside reading's reply lands in the container that sent it. Commit it before the session ends, or it is lost.
