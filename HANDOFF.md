# Handoff (Nov 2, 2026): S52 done, the outside supply shock (pilot report)

## Step status
S52 is **done**. The pilot (study O, seeds 1-50) finished, every checksum verified. The plain-words report and the list for S47 are written.

## What shipped
- compassionism-simulation [#65](https://github.com/BetterToBest/compassionism-simulation/pull/65): `dev/reports/s52-supply-shock.md` (labelled pilot; decision rules 1-6; "What S47 must carry"), `dev/reports/s52-supply-shock-tables.md`, and presentation fixes in `dev/tools/s52_shock.py`. The fixes: programme inflation shown in points, the missing secondary outcomes added, empty groups shown as such. No engine change.
- research-update (this PR): addendum Amendment 1 (`prereg/2026-11-supply-shock-addendum.md`) and PLAN.md (S52 done; S47's S52 line updated).
- Earlier this step: compassionism-simulation #64 (engine switch `sx`), compassionism-sim-results #12 (`shock.js`), research-update #37 (addendum).
- Results: compassionism-sim-results `s52-shock-98b6100/`.

## What the pilot says (pilot; not figures of the model)
- The BU, not PTF or PTH, absorbs most of the shock. Under the release row, adults outside all three parts pay all of it and other participants 44-58%. Under C2.2 about a fifth reaches anyone's money costs.
- PTF's markup removal saves members 2-5 points of the shock (rule 1 met everywhere). All-local sourcing adds 3-7 points, as an upper bound.
- PTH protects only through the BU.
- Basket poverty of non-participants is not harmed (rule 4 not triggered).
- Unfavourable: the shock adds 0.6-1.6 points a year to the programme's own inflation. The year-20 price level ends 11-25% higher, against 2.7% with no programme. Wealth poverty rises 0.7-3.0 points more with the programme in five of six cells, non-participants included.

## In flight
- Nothing.

## Decisions waiting
- None new. The report invites Duke to say if PTF should hold a price reserve or PTH should buy energy for residents; either would be a new row and a dated amendment.

## Next step
**S53** (security outcomes beyond wealth; per-year series for S19): it waited on S51 and S52, both now done. Then S54 and the S47 freeze.

## Pitfalls
- The first tables printed `endoAnn` (a fraction) under a "points" label, which read as 0.01 points instead of 1.3. Check units before quoting any table.
- PTF members pay a larger share of the shock than other participants. That gap is not PTF's doing: the pilot's outputs cannot split it. Amendment 1 adds a breakdown of costs by payer for the full study.
- The volatility measure is a percentage of money cost. Participants' smaller money costs make the same dollar change look larger, so read it beside the dollar-based measure once that exists.
- Adverse and Stress share one no-programme economy, so their no-programme figures are identical. That is not a bug.
- Use the `Co-Authored-By: Claude <noreply@anthropic.com>` trailer only. The two stray branches named earlier are still there for Duke to delete.
