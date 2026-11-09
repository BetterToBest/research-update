# Handoff (Nov 9, 2026): S39 done, the outside engine cross-check read

## Step status
S39 is **done** (part 2 this session). Both result folders were complete (`DONE`; checksums verified; no shard rerun). The findings are in the report, read by the preregistered decision rules, and rule 4's ledger decision is filed (D17).

## What shipped
- compassionism-simulation [PR 86](https://github.com/BetterToBest/compassionism-simulation/pull/86): report `dev/reports/s39-outside-crosscheck.md` sections 4-6 and plain-words results; tool `dev/tools/s39_crosscheck.py`, which gains an identity check and rule 5's contrast intervals, both marked as added after the results; tables `dev/runs/s39-crosscheck/tables.md` and `estimates.csv`; DECISIONS.md. This session merges it once its checks (checks, guard) pass; if it is still open, its checks failed or were still running when the session ended: read them first.
- research-update: this file, PLAN.md (S39 done; S7 note on inflation sentences).
- Ledger synced (hub version 96): S39 done, D17, next, log.

## Findings (plain words)
- Given the engine's C2.2 new money (31-46% of household income a year), BeforeIT's consumer prices end within a few percent of its no-payout run. At full scale its pass-through is 0.00 (interval -0.012 to 0.010) after 20 years; the engine's is 1. The price level after 20 years is about 1.00 against the engine's 408. By rule 1, "far less", by a factor of about 400.
- That zero is BeforeIT's assumption, not a measurement. Its source, read after the runs, shows that with the packaged uniform starting prices every firm's cost term stays zero. The CPI then grows each quarter by exactly expected inflation, a forecast from past inflation plus a random draw. This was checked in all 1,365 runs to machine precision, and the food, housing and medical indices equal the CPI. So the engine's rule fixes its answer at 1 and BeforeIT's fixes its answer at 0. The cross-check bounds the question; it does not answer it.
- In BeforeIT the money raises real output (+15.5% after 3 years: unemployment goes to zero and output per worker stretches up to 1.5 times) and government debt (9.8 years of output after 20 years, against 1.1 without the payout). Paid from an income tax instead (the rate rises from 21% to about 60%), almost none of the output gain remains, and prices again do not move.
- Q4-Q8: no price difference anywhere, apart from one chance result (dose 3%, full scale, quarter 12). Essentials cannot be compared (BeforeIT's relative prices never move). The output response is 1-2 points larger at full scale in some readings.

## In flight
- Nothing.

## Decisions waiting
- D17: how Hub sentences on inflation say this. Default: the report's wording (section 6, item 4). Name the placeholder, give BeforeIT's figure with its reason, and say neither model measures the pass-through. Never "an outside model found no inflation".

## Next step
**S7** (sonnet, medium): the Simulation release and findings page; everything it waits on is done. Its inflation sentences follow D17's default (PLAN.md S7).

## Pitfalls
- BeforeIT's sector indices (food, housing, medical, deflator) equal its CPI in every run. This is not a recording bug: the packaged calibration's relative prices never move. Do not cite them as an essentials result.
- The engine round inherits two open questions, with no change now: an outside source for the price rule's pass-through, and the conversion tax not netted from the unmatched money U.
- The results checkout used here was blobless and sparse (`s39-*` folders only), to save time and disk.
