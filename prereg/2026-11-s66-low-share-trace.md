# Preregistration: tracing the low end of the fixed-share curve, the erosion of opening balances, and the wealth harm with adults outside the labour force (S66)

Committed Nov 10, 2026 by S66, before any run of the rows below. Engine: compassionism-simulation at commit `78e1dd7` (main; full hash recorded in every output file), unchanged: no engine change is made in this step. The one check run before this file was written (two seeds, Reference, the 10% fixed-share row and its no-programme row) only confirmed that this commit reproduces S55's published per-seed values for those rows exactly (compassionism-sim-results `prog-w-0c93593` and `prog-a-ce8d030`, keys `pov` and `endoAnn`); it is repeated as check 1 below on more seeds and keys.

This is a diagnostic trace, not a study of the programme. Nothing here is a headline result, and nothing here changes a published figure.

## Why
1. **The dip.** S55 (compassionism-simulation `dev/reports/s55-open-access.md`, section 4) held every zone's PTF share of essential sales at 10%, 20%, ..., 100% under open access. Under the C2.2 design in Reference and Adverse at 20 years, the programme's effect on wealth poverty (adults with wealth under $25,000 at year-0 prices, sign set so that positive is better) is +1.16 points at 10%, −0.34 at 20% and +0.04 at 30% (10,000 adults), with lower inflation at 10% (34.72 points a year against 35.07 and 35.15). The same holds at 500 adults; it does not hold at 40 years (8.46, 8.77, 9.17). Both outside reviews asked why (review triage `audits/2026-11-s39-s55-review-triage.md`, A5). S63 must know before it writes the fixed-share rows, and the findings page before it uses the curve.
2. **Erosion of opening balances.** The model holds all wealth as nominal dollars with no return and no revaluation (Nov 9 audit, `audits/2026-11-09-simulation-audit.md`, finding 1). So every dollar an adult owns at the start loses real value at the programme's inflation. How much of each published wealth result is that, and nothing else?
3. **The wealth harm with adults outside the labour force.** S61 found that with `lf` (adults 25-64 outside the labour force) the C2.2 design's wealth-poverty harm grows from +0.7 to +9.8 points in Reference (Adverse +35.4, Stress +45.0). S61 named a likely mechanism and did not trace it.

## Rows (all on the frozen engine, as the batch builds them)
Every row is built exactly as compassionism-sim-results `runner/jobs/program.js` builds its rows: `relMainCfgs(tbPresets(P))` with the published spending share and `sn {abawd, slope}`, then `frozenRow`; `applyNR6()`, `tbSetG(TB_PROFILE_G)`; study options `{fin: 'tax', aT: 0, a: 0, X: 0, sc}` plus `REL_V52_STUDY`; the CPS yardstick (`lt {s: 'all', m: 'all'}`); 500 adults.
- **Part A (the curve).** The C2.2 design (`c22Design`) with every part on, open access with every zone's share held (`pa: {fix}`, no growth), at shares 5, 10, 15, 20, 25, 30, 35, 40 and 50%; the members-only C2.2 row; the no-programme row. 20 years in Reference, Adverse and Stress; 40 years at 10, 20, 30 and 40% (and members-only) in Reference and Adverse.
- **Part A switch-offs**, each applied alone to the fixed-share rows at 10, 20, 30 and 40%, 20 years, three environments (the no-programme row has no PTF and is unchanged by every one of them; it is run once):
  - **K1, the 40% price-cut rule off:** every share gets the higher food price cut (`CFG.PTFS_LOW_DENS` set to 0, so the low-density epsilon 1.65 never applies; this also removes the test from the reporting tallies).
  - **K2, PTF damping of inflation off:** the line that multiplies the outside inflation rate by (1 − 0.5 × share) does not run. PTH's damping stays. In Reference the outside inflation rate is 0, so K2 must equal the main reading there exactly (a check).
  - **K3, conversion income off:** the engine's existing pathway switch (`pw: {conversion: true}`): no BU is converted into dollars (projects, business premium and ESP payroll premium all 0). The BU itself, PTF and PTH price cuts stay.
  - Two more, added here because the code shows they are the other places the share enters below 55% (theta and the 55% test do nothing below 55%):
  - **K4, the surplus split held at 10%:** wherever the ESP surplus split reads an adult's zone share (the PTFs' part of the business premium, the private ESPs' price pass-through on BU spent outside PTFs, and the PTF price pool's customer base), it reads 10% whatever the row's share. Everything else reads the row's share.
  - **K5, the PTF price cut held at 10%:** the scale on each adult's PTF price cut (`ptfsCut`: the cut times the zone share) and the forgone-profit accounting read 10% whatever the row's share. The 40% test still reads the row's share.
  K4 and K5 are implemented in the trace tool only, as exact text substitutions in its own copy of the engine (each asserted to match exactly once); `index.html` is not edited. K1 and K3 use existing settings. K2 is a text substitution of the same kind.
- **Part B (erosion).** The frozen batch's members-only main rows and their no-programme rows: the release design (`rls`) and the C2.2 design, 20 years, three environments (study A's rows `*.cps.main` and `*.cps.none`).
- **Part C (`lf`).** S61's row L: the frozen yardstick with today's safety net (`sn {abawd, slope}`, `lt {s: 'all', m: 'all'}`) and `lf: {}`, the C2.2 design against its no-programme row, 20 years, three environments; and the same rows without `lf` (S61's F0) for comparison.

Seeds 1-100 for every part (reduced seeds; the session machine). No 500-seed run.

## What is recorded (per seed, per year, reporting only: no draw added, no state any rule reads is changed)
The trace tool reads the engine's own accumulators through a read-only probe in its own copy of the engine script; it writes nothing into the run.
- **Money (per adult, year-0 dollars):** the Source's payout (BU at face value plus net conversion), the conversion tax withheld, output matched to it, new money U and its share of cash income (U/Y); the business premium pool and its split (the PTFs' part; the private ESPs' price pass-through; PTF reinvestment; the PTF price pool; worker profit shares).
- **PTF price cuts:** the PTF price-cut dollars per adult, the share of adults whose own cost is cut by the PTFs that year, and the mean cut per adult receiving one.
- **Prices:** the basket price level and the year's inflation.
- **Adults (means, and medians where stated):** real wage income, real conversion income, real disposable income, real own cost of essentials (consumption of essentials at the prices the adult pays); nominal and real wealth (mean, median), the share in debt and the mean debt of those in debt, wealth poverty, and the density of real wealth around $25,000 (shares in $2,500 bands from $0 to $50,000, and the share within $5,000 either side of the line).
- **Part B, per adult present at year 0 and at the last year in both runs of a seed (matched by the engine's adult id):** opening wealth W0 (start-of-year-0 nominal balance), each run's last-year real wealth, and the erosion term W0 × (1/P_prog − 1/P_none), with P each run's last-year basket price level against year 0.
- **Part C:** the same as Part B, split by adults outside the labour force and in it, with each group's real wage, conversion and other income, own cost, and wealth poverty.

## Outcomes and analysis
All differences are paired by seed (programme row minus no-programme row, or one row minus another on the same seed), means over seeds 1-100 with the 2.5th-97.5th percentile interval of 2,000 paired bootstrap replicates over seeds (fixed generator). Intervals are unadjusted; this is a trace, and no test count is corrected.
- **A1, the curve.** Wealth-poverty effect (positive = better), inflation, median and mean real wealth, at each share. The dip: the 10% − 20% and 30% − 20% differences in the wealth-poverty effect.
- **A2, where the rows part.** For 10% against 20% and 30%: the year-by-year paths of every money and adult measure above, and the year in which the gaps open.
- **A3, the switch-offs.** The 10% − 20% difference in the wealth-poverty effect under each of K1-K5, beside the main reading.
- **A4, threshold or real.** Whether the dip appears in median and mean real wealth, or only in the count under $25,000 (from the density around the line).
- **B1.** For each design and environment: the mean gap in last-year real wealth, the mean erosion term, and its share of the gap, overall and by fifth of opening wealth. **B2.** The wealth-poverty effect recomputed with each adult's opening balance deflated at the no-programme run's price level instead (programme real wealth + W0 × (1/P_none − 1/P_prog)): the part of the published wealth-poverty effect that is the erosion of opening balances.
- **C1.** B1 and B2 for adults outside the labour force and for adults in it, with and without `lf`. **C2.** Each group's wealth-poverty effect and the income and cost paths behind it.

## Decision rules (fixed now)
1. **Check 1 (gate).** The trace tool's copy of the engine with the probe, and with no switch-off, must reproduce the harness's own outputs exactly (every kept key, seeds 1-5, every Part A row at 20 years in Reference). If not, nothing from the tool is reported and the step stops there.
2. **Check 2.** K2 equals the main reading exactly in Reference (no outside inflation there).
3. **A mechanism produces the dip** if, with it switched off, the 10% − 20% difference in the wealth-poverty effect is no longer positive with its interval excluding zero, while in the main reading it is. If more than one switch-off removes it, the note says so and names them all. If none does, the note says the cause was not found.
4. **No low-share optimum is claimed** unless the dip appears in median or mean real wealth as well as in the count under $25,000, at both 20 and 40 years, and the mechanism behind it is a rule of the design (not the timing of a single year or the position of the $25,000 line). Otherwise the note says the dip is a feature of the measure or of the model's mechanics, and S63 reads the curve that way.
5. **Erosion.** The note states, for every design and environment, the share of the year-20 real-wealth gap and of the wealth-poverty effect that is the erosion of opening balances, as measured. It is a property of the all-wealth-is-nominal assumption (S59's asset classes address it); no published figure changes here.

## Outputs
- compassionism-simulation: the tool `dev/tools/s66_trace.js`, the summary script `dev/tools/s66_table.py`, tables `dev/runs/s66-trace/`, the plain-words note `dev/reports/s66-low-share-trace.md` (read by S59 and S63).
- compassionism-sim-results: `s66-trace-78e1dd7` with every per-seed file, `run.txt` and `SHA256SUMS`.
