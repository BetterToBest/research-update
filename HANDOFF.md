# Handoff (Nov 2, 2026): S51 done, backing as a mechanism (pilot reported)

## Step status
S51 is **done**. The 50-seed pilot finished on Actions (25 shards, checksums verified). The preregistered analysis ran, and the plain-words pilot report with the list for S47 is merged.

## What shipped
- compassionism-simulation [#63](https://github.com/BetterToBest/compassionism-simulation/pull/63), merged `MERGE63`. It adds `dev/reports/s51-backing-mechanism.md` (the pilot report, for Duke), `dev/reports/s51-backing-tables.md` (every preregistered table), `dev/tools/s51_diag.js` (a 10-seed explanatory check, not preregistered) and `dev/DECISIONS.md` (the pilot read). No engine change.
- compassionism-sim-results `s51-backing-6428b96/` (already on main): per-seed values, run.txt, SHA256SUMS, DONE.
- research-update (this PR): `prereg/2026-11-backing-addendum.md` Amendment 1 (two sensitivities added after the pilot, for S47); PLAN.md S51 marked done, S47 list extended.

## What the pilot found (pilot; not figures of the model)
- The C2.2 design cuts basket poverty with no backing at every wage indexation, in all three environments.
- The release row needs backing for basket poverty only at 75% wages (46%, 31%, 54%). For wealth poverty it needs 32-75% even at full wages.
- Under the main reading (only added output absorbs new money, 8% ceiling), the mechanism backs about 1% of the release row's payout. 0 of 36 main-reading settings reach break-even.
- With no ceiling, the main reading backs at most 19.5% (projects at 2.3 times earned income) and still does not reach break-even. Only "proceeds retire the money" with no ceiling does (6 of 216; none in Stress).
- Wealth poverty's rise is money savings losing value to about 51% inflation a year. With savings that keep up with prices (`sv`), it becomes a fall (10-seed check).
- The release row's surge protocol raises the BU only in years when inflation exceeds 5%, so at 2-5% inflation the BU wears down. This is the dip in arm A near full backing; the BU raised every year removes it (10-seed check).

## In flight
Nothing.

## Decisions waiting
- D12 (new): the release row's payout cannot be backed under the main reading. Which design lever, if any: a smaller or slower payout, a conversion tax or the Source taking back project proceeds, octave capacity, or the C2.2 way of protecting the BU? Default: no design change; C2.2 stays the headline design, and the release row is reported as released with these results.

## Next step
**S52** (outside supply-shock environment), then S53, then the S47 freeze. S47 now also builds the S51 Amendment 1 rows (466 rows per environment).

## Pitfalls
- Two stray branches in compassionism-simulation carry a model name in their commit trailer, against the rule: `claude/s51-backing-pilot-report` (this session, never merged, no PR) and, in compassionism-sim-results, `claude/s51-backing` (last session). The proxy refuses branch deletes; Duke can delete both on GitHub. Use the `Co-Authored-By: Claude <noreply@anthropic.com>` trailer only.
- The 10-seed check is explanatory and was not preregistered; Amendment 1 says so. Do not quote its numbers as results.
- Under 90% wages the release row's median wealth at year 20 falls to about $130 (year-0 dollars, 10 seeds): read wealth figures with their savings treatment.
- One seed of the backing job takes about 315 s on one process for all three environments (350 rows each).
