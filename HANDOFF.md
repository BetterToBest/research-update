# Handoff (Nov 10, 2026): S66 done, the low-share trace and the erosion of opening savings

## Step status
S66 is **done** in one session. No engine change. S7 stays held until round 2 is ready for release (PLAN.md).

## What shipped
- research-update `prereg/2026-11-s66-low-share-trace.md` (committed before any run); PLAN.md (S66 done, findings under its section); this file. Branch `claude/laughing-bell-dqyt1v`.
- compassionism-simulation [PR 91](https://github.com/BetterToBest/compassionism-simulation/pull/91):
  - tool `dev/tools/s66_trace.js`: its own copy of the engine with a read-only probe; `--check` proves the copy equals the harness (7,080 row-keys);
  - `dev/tools/s66_table.py`, tables `dev/runs/s66-trace/`, report `dev/reports/s66-low-share-trace.md`;
  - a dated correction note in `dev/reports/s55-open-access.md`; DECISIONS (S66).
- compassionism-sim-results [PR 26](https://github.com/BetterToBest/compassionism-sim-results/pull/26): `s66-trace-4e9d841` (seeds 1-100; run.txt, check.log, SHA256SUMS, DONE).

## Findings (plain words; seeds 1-100, 500 adults; intervals unadjusted)
- **The low-share dip comes from the ESP surplus split.** Once the PTFs' capital account reaches full capacity, their reinvestment (counted as matched output) stops. That happens within 20 years from 15% up (year 15 at 20%), but never at 5-10%. Result at 20% against 10%: more unmatched money, +0.37 points a year of inflation, a 5% higher price level by year 20, and 1.57 points more adults under $25,000 (Reference). Gone at 40 years (−0.33), so no low-share optimum.
- **PTF damping of inflation is off in every release row** (d86). S55's reading that named it is corrected (dated note; no figure changed).
- **The erosion of opening savings is 90-96% of the programme's year-20 real-wealth gap**, in every design and environment: all wealth is cash, and prices reach about 400 times their start. If opening balances kept their real value, every wealth-poverty harm would be a reduction (release, Reference: +21.5 → −6.8; C2.2: +0.7 → −12.1).
- **The `lf` wealth harm (+9.8) is the same erosion on adults with no wages.** Outside the labour force: +27.6, but −28.6 without the erosion, since their income rises and their costs fall. In it: +6.1.
- **Model question for S62:** in fixed-share rows, the split's switch reads the PTFs' capital against full capacity, not against the share they serve.

## In flight
- Nothing.

## Decisions waiting
- D21: carry the C2.2 design paid for by a contribution on every round-2 outcome (default: yes, as a labelled reading).
- D22: use the stronger model on steps marked "(or fable, ...)" even where it uses usage credits (default: no).
- S63 files the main-row price-rule decision after S67.

## Next step
**S59** (opus, xhigh): asset classes and returns. It now has a measure to beat, because S66 shows almost every wealth result is the all-cash assumption; it should rerun S66's erosion decomposition on its rows. S67 and S60 can start too.

## Pitfalls
- The release rows have damping off: never attribute anything to PTF or PTH damping there.
- Fixed-share rows at year 20 depend on the year the PTFs' capital account crosses full capacity: read 20 and 40 years.
- The erosion reading is accounting, not a run: it holds each opening balance untouched for 20 years.
- A first launch of the trace lacked the wealth bands (keys taken from year 0 only). It was stopped and its files discarded.
- The remote branch `claude/s66-low-share-trace` in research-update was pushed by mistake and could not be deleted through the proxy. It holds only the preregistration commit; delete it by hand.
- Run pilots from a clean worktree; remove `sim-pilot` afterwards.
