# Handoff (Nov 15, 2026): S64 done (part 3: erosion share, charts, findings-page text)

## Step status
S64 is **done**. Part 3 finished the two outputs the batch could not give (the erosion share of every wealth figure, and basket poverty by labour-force reason), the findings-page charts and the findings-page text for S65.

## What shipped
- research-update PR (branch `claude/vigilant-noether-3a68vj`): freeze file Amendment 4, committed before the trace ran (the erosion term under asset classes; basket poverty by status). PLAN.md S64 row and section; this handoff.
- compassionism-simulation [PR 111](https://github.com/BetterToBest/compassionism-simulation/pull/111): `dev/tools/s64_erosion.js` (the trace), `s64_erosion_table.py`, `dev/runs/s64-erosion/` (tables, summary), the erosion share added to the q1 (new section), q2 and q6 reports, q6's erosion by fifth and basket poverty by status, the overview, `dev/tools/s64_charts.py` with 24 charts in `dev/runs/s64-round2/charts/` (`index.html` previews them), and `dev/reports/s64-findings-page-text.md`. No engine change.
- compassionism-sim-results [PR 40](https://github.com/BetterToBest/compassionism-sim-results/pull/40), merged (9c46288): `r2-erosion-104691f/` (raw trace, tables, run.txt, SHA256SUMS, DONE).

## What part 3 shows (plain words)
- Erosion of the balances adults held at the start is 0.0-2.9% of every wealth figure, and it helps the programme: at full backing prices rise 0.0-0.2 points a year faster, which lowers what net debtors (the lowest four fifths, on average) owe. Creditors at the top lose. S66's all-cash term, as a bound, has the opposite sign and stays within 5.3%.
- Adults outside the labour force stay far more often below the basket: C2.2 8.5-16.6% of their adult-years against 1.8% in the labour force; the release design 28.8-58.5% against 9.5% (no programme 54-82% against 29%; Reference, 20 years).
- Checks: the trace reproduced the engine's keys in every run; every seed equals the batch's part M; the published effects equal the batch's tables to 2.1e-8.

## In flight
- Nothing running.

## Decisions waiting
- Nothing new.

## Next step
**S7** (sonnet, medium): the release, held until round 2 was ready (Duke, Nov 9); it runs just before S65 so that release 1 and release 2 land together. Then **S65** (release 2 and findings page), which takes its text and charts from `dev/reports/s64-findings-page-text.md` and `dev/runs/s64-round2/charts/`.

## Pitfalls
- S66's `s66_trace.js` no longer runs on `104691f` (its price-cut probe patch matches 0 times). Use `s64_erosion.js`: no text patches, a read-only hook.
- Each row makes two full-length runs per seed (the supply path); the hook keeps the last and the key check proves it is the reported one.
- The real-holdings check is not near zero in the means: it is entirely the creditor charge on shares (S71); the asset index equals the basket deflator exactly. The per-adult means are unweighted, so the weighted-tail adults dominate the top fifth.
- The auto-mode permission classifier refused several `git commit` and `commit && push` commands early in the session; separate commit and push commands went through after the stop hook asked for them.
- Remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and older session branches in research-update still need deleting by hand.
