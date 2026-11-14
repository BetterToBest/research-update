# Preregistration: round 2 of the Compassionism Simulation (S63, the design freeze for S64)

Committed Nov 14, 2026 by S63 part 1, before any run of round 2. Engine: compassionism-simulation `main` at `6ba80e5` (after S70) is the base. The commit the batch runs is pinned in Amendment 1 (S63 part 2), after S69's two reporting corrections land behind their switches and before the dry run. No outcome of round 2 has been computed. The only figures used to write this file are run times (the costing in "Where it runs") and the S70 screen's published rankings.

## Why
Round 2 rebuilt the engine's weakest parts (S57-S73): wealth by asset class with the lenders who hold household debt; a weighted top tail; adults outside the labour force who move in and out of work; a borrowing limit; bargaining; PTF running costs; a government account; the price rule's derivation; the financing identity. Each step said what S63 must carry. The S70 screen ranked every swept reading together and fixed, by rule, which readings the batch carries. This file fixes the batch, the outcomes, the analysis and the statements each result leads to, before any result exists.

## Plain-words summary
- **One main row**, chosen before results (ledger decision D26): the round-2 candidate main row with full backing, today's price rule and S69's two reporting corrections. The ledger decision states Claude's recommendation and the other views.
- **Around it, a specification curve** for every headline outcome. A specification curve is a chart of every preregistered reading's estimate, ordered by size, each with its interval. The curve holds every reading S70's rules carry (32 single readings on the Source rows), the 28 pairs S70 flagged, and a least-favourable bound.
- **Beside it:** the backing curve (how much of the payout is matched by new output, 0 to 1); the financed rows (the designs paid by a contribution, the rest borrowed), with their own curve; the readings earlier steps named; the fixed PTF share rows.
- **Both designs** (C2.2 and the release design), **three environments** (Reference, Adverse, Stress), **500 seeds**, **20 and 40 years**, 500 adults. The main pair also runs at 10,000 adults (hours and the tail's weights at scale).
- **Cost:** about 630 core-hours, about 160 runner-hours, about 8 hours on GitHub Actions' 20 free runners. Free. No Runpod, no other paid service. The S70 rules need no amendment to fit.
- **Every result is published**, including nulls, unfavourable results and the Adverse and Stress environments. No headline figure appears with its seed interval alone: the range across the curve comes first.

## Questions
- **Q1 (main effects).** At the main row, what is each design's effect on basic living, the cost of living (basket poverty), wealth poverty, median real wealth and programme inflation, against no programme, in each environment at 20 and 40 years? Answered by the paired estimate and its 95% interval.
- **Q2 (robustness).** Across the preregistered readings (the specification curve), does each effect keep its sign? Answered by the share of curve points whose interval excludes zero with the main row's sign, and the curve's range.
- **Q3 (interactions).** For the 28 flagged pairs on the Source rows and 66 on the financed rows, is there an interaction? Answered by the interaction contrast's 95% interval (rule 4 of the research rules: a synergy is claimed only where it excludes zero).
- **Q4 (backing).** How do the outcomes change as the backed share falls from 1 (the design's statement) to 0? At what backed share does programme inflation pass 5% a year, and at what share is wealth poverty no better than with no programme (the break-even shares)? Where on the curve is the share the model's own mechanism reaches?
- **Q5 (financed rows).** Paid for by a contribution with the rest borrowed, what rate does each design need, how large is the deficit, how does the debt move, and what are the poverty and wealth effects? (D23 as answered: carried beside the main rows, never led with.)
- **Q6 (distribution).** At the main row, how does the programme change the top 1% and top 10% shares of wealth and income, the Palma ratio, real wealth and income percentiles, mobility between wealth fifths, labour's share and families in debt (S57's measures), and how much of each wealth result is the erosion of opening balances (S66)?
- **Q7 (work).** At the main row, how does the programme change participation and hours? Every participation figure is printed with programme leavers (share of adult-years), their earnings forgone and what the model does not count (S73 section 6). Hours are printed with the 10,000-adult figure beside them (S68).

## Design

### The main row (ledger decision D26, filed before any result)
Claude's recommendation (option 1 of D26): `r2MainRow` (harness.js) in both runs of the pair, with:
- the programme run's backed share `a` 1 in `r2MainRow`'s study options (Duke's decision D25, Nov 14: full backing is the design's statement; labelled as a design parameter wherever the main row is shown);
- today's price rule (no `pr`; S67 section 9: the derived capacity rule was fitted to an economy that the round-2 engine no longer is, and today's rule is what the frozen engine and the Hub's sentences used);
- the borrowing limit `dr: {lim: 2500}` (S61); `lf: {fl: 'stock', pm: 0.43}` (S61, S73); `bg: {pi: 0, m: 1/1.21}` (S60; identical to off); `rt: {bo, ci, ng: 'base', cr}` with incidence `pass` (S59, S71); the weighted tail `wt` (S59); open PTF access with growth `pa: 'open'` (S55); PTF running costs `po` with the Source paying (S62, D19); the government account `gv: {}` (S72); `fx: {pthb, hb, ab, sp, fin: 'report', pe}` (S68); study options `dm`, `rep52`, `wtm`, `mf`, `wy` (S57, S68);
- S69's two reporting corrections on (GAPS items 22 and 24: earnings below $1e-9 count as zero; the weighted distribution measures rank wealth rounded to the cent, ties by index). Built in S63 part 2, each behind its own switch with off identical; neither moves a headline by more than 1e-5 (S69).

The other views D26 carries: the capacity price rule at S58's main values as the main row (S58's recommendation, replaced by S67's), with today's rule beside it; or option 1 without S69's corrections (the row S69 reproduced). Whichever is chosen, the others run as labelled readings (below).

### Rows: the Source rows (C2.2 and the release design paid by the Source)
Every point below is a pair (the programme run and its own no-programme run, every reading applied to both runs, as `r2MainRow` does). The two designs share a point's no-programme run. Readings are the S70 job's input names (`runner/jobs/s70-screen.js`, compassionism-sim-results), with the same setters and ranges.
1. **The main row** (1 point).
2. **Single readings (S70 rules 2 and 3; 32 points).** Each of the 22 inputs carried in full at each end of its S70 range (each category for a categorical input), the others at main: `wIdx`, `sc`, `rtIx`, `prK`, `lfFl`, `prBd`, `rtPhi`, `rtNs`, `rho`, `prR`, `prA`, `rtChi`, `poPay`, `bgM`, `bgPi`, `lfConv`, `poCost`, `paDem`, `lfPm`, `poHire`, `poTest`, `poBonus`. An end equal to the main reading is the main row and is drawn once. Three at one reading: `wtCut` p90, `wtM` 6, `prH` 0.0446. The price rule's six readings act only where new money reaches prices (S70 rule 6); at full backing they are expected within seed noise of main and are reported as such.
3. **Pairs (S70 rule 5; 28 points).** Each pair in S70's table (`s70-S-tables.md`, "Rule 5") as a 2 × 2: main, each input alone (already in item 2), and both together. Each input takes the end whose effect is larger in the pair's own cells, by S70's rule-3 reading (the slope of the trajectories, or the summed category steps); the job's `--check` prints the ends chosen, and they are recorded in Amendment 1 before dispatch.
4. **The least-favourable bound (5 points per design).** For each headline outcome and design, every carried input at its least favourable end together: the end whose screen μ (the mean elementary effect, full-backing cells, Reference and Adverse pooled) moves the effect against the programme (poverty up, median wealth down, inflation up). Stress was not screened and takes the pooled signs. An input whose μ is 0 to two decimals stays at main. Fixed from `s70-S-summary.json` by the job's `--check` and recorded in Amendment 1.
5. **The backing curve (D25; audit `2026-11-14-d23-backing-and-main-row.md`).** The backed share `a` at 0, 0.25, 0.5 and 0.75 (1 is the main row), plus the mechanism's main reading (`bkm`) and its no-ceiling reading: 6 points, programme runs only (the no-programme run is the main row's). The 1 end is labelled "full backing, as the design states"; the point the model's own mechanism reaches is marked. At `a` 0 the price rule's six readings are carried as in item 2 (they act there; S70 rule 6), 9 points.
6. **Readings earlier steps named that S70 does not already carry** (one point each): `rt` off (all wealth is cash; S59); the creditor side off (no-debt-relief reading; S71, S68); `wt` off (S59); `lf` off and `conv: 'none'` (S61); the liquid share 0.046 and the floor reading (S61); the borrowing limit at $0 and $10,000 (S61; S70 holds `drLim`, so the sweep's two ends only); the capacity price rule at S58's main values, the quarterly-fitted within-year reading `pr: {q: 4, k: 0.0788, k2: 0, r: 0.2333}` and today's rule with the velocity drift `pr: {k: 1, r: 0, a: 0, h: 0, rs: false, bd: 0.132}` (S67); `bg` π 0.10 (S60's outer evidence reading); the creditor readings `inc: 'hold'`, `inc: 'hedge'`, `pop: 1`, `out: 0` (S71; held by S70, carried because S71 named them); S69's corrections off. About 20 points.
7. **Fixed PTF share rows (S66, D16).** The PTF share held at 10%, 20%, ..., 100% with growth off, both designs, the switch year printed beside each (S66). 10 points.

### Rows: the financed rows (D21, D23 as answered; S72)
Run without the weighted tail (S72 Amendment 2: the contribution's bases are not read with the tail on); the tail's absence is stated with every financed figure.
1. **The financed main rows.** C2.2 paid by a contribution on all money income, share 1, cap 0.9, the rest borrowed (`o.fin 'tax'`, `gv: {sh: 1, base: 'all'}`, `o.tauMax 0.9`, `fx.fin 'debt'`), and the release design paid by a flat contribution on wages, the rest borrowed (S72: rule B passes). The no-programme run is shared.
2. **Single readings (48 points).** S70's 34 inputs carried in full at each end (`bgM` at its one reading, 1). Includes `fin` at 'money' (the rest as new money) and 'cap'.
3. **Pairs (66 points)** from `s70-F-tables.md`, as item 3 above.
4. **Bound (5 points per design)**, as item 4 above, from `s70-F-summary.json`.

### Rows: the 10,000-adult main pair
The main row and its no-programme run, both designs, 10,000 adults (S68: no hours figure from 500 adults without this one beside it; S59: the tail's neutrality at scale).

### Environments, seeds, horizons
- Reference (`FULL_INTEGRATION`), Adverse (`ADVERSE_REFERENCE`), Stress (`STRESS_TEST`). All rows run in all three.
- Seeds 1-500, paired across every row (common random numbers; eight draws per adult-year).
- 20 and 40 years, run separately (the 20-year run equals the first 20 years of the 40-year run byte for byte; kept as a check, study programme Amendment 9).
- 500 adults, except the 10,000-adult pair.

## Outcomes
Each is the programme's effect: the programme run minus its own no-programme run, paired over seeds.

**Primary family (the headline can only come from these): 5 outcomes × 2 designs × 3 environments × 2 horizons = 60 tests, on the main row.**
- Basic living: adult-years below 30 days of basic living, design-neutral (`bNAPy`), points.
- The cost of living: adult-years with income below the basket (`fgt0PY`, basket poverty), points.
- Wealth poverty as the average of the yearly readings (`ppovA`, from `ppov_t`), points; the year-20 and year-40 readings (`ppov_20`, `ppov_40`) beside it.
- Median real wealth (`wtMedE`, weighted, year-0 dollars), with the yearly average (`pmedW_t`) and years 20 and 40 beside it.
- Programme inflation (`endoAnn`), points a year.

**Secondary family (reported with intervals; Holm within each table):**
- S57's distribution measures (top 1% and 10% shares of wealth and income, weighted; the Palma ratio; P10-P99.9; the transition matrix; labour's share; families in debt), each wealth figure beside its erosion share (S66 trace a).
- Participation and hours (S73, S68), with leavers, earnings forgone, and the 10,000-adult hours figure.
- The financed rows: contribution rate (`tauMean`), deficit, debt at years 20 and 40 (`gvDebtY`, median over seeds), the year debt passes GDP (`gvY100`), and the five headline outcomes.
- The backing curve's break-even shares (Q4).
- Programme cost; within-year costs (`wy`) beside every basket-poverty figure; basket poverty by labour-force reason (S61's key).

**Exploratory (no test; displayed):** every specification-curve point, pair and bound; the fixed-share rows; the readings of item 6; growth-incidence curves.

Confirmed on basket poverty and wealth poverty, not FGT2 alone (guardrail 6).

## Analysis
- **Estimate and interval:** the mean paired difference over 500 seeds; 95% interval by paired bootstrap, 2,000 resamples, generator seed 6301. Debt keys use the median and its bootstrap interval.
- **Holm:** across the 60 primary tests (two-sided paired t p-values); in the secondary family, within each table. The count of Holm survivors is printed beside the count of intervals that exclude zero (audit A4).
- **Interaction contrast** for a 2 × 2: (both − A alone − B alone + main), paired, with its bootstrap interval. A synergy (or antagonism) is claimed only where the interval excludes zero.
- **Break-even shares:** for each design, environment and horizon, the backed share where the curve crosses the threshold, by linear interpolation between the two grid points either side, with the bootstrap interval of the crossing. When no grid point crosses, reported as "above 1" or "below 0" (never extrapolated).
- **Specification curve** (S70 prereg, "The specification curve"): one per headline outcome × design × environment × horizon on the full-backing main row; separate curves for the backing curve and the financed rows; drawn with the panel of readings below; data as one CSV per curve.

## Decision rules (fixed now)
1. **Headline sentence.** Range across the curve first, then the main row with its seed interval: "Across the N preregistered readings, the C2.2 design lowers basket poverty by X to Y points; at the main row, Z points (seed interval A to B)." No headline figure is published with its seed interval alone.
2. **Robust.** An effect is called robust when every point of its curve has an interval that excludes zero with the main row's sign. **Mostly robust:** at least 90% of points do and none has the opposite sign with an interval excluding zero. **Fragile:** otherwise; the sentence then names the readings that reverse or remove it.
3. **Materiality** (as S70 rule 1): 1 point for the poverty measures; 1 point a year for inflation; 5% of the no-programme median real wealth. An effect below materiality is described as "no material change" even when its interval excludes zero.
4. **Backing.** Full backing is labelled as the design's statement wherever the main row is shown. If the break-even backed share for 5% inflation lies above the mechanism's own point, the findings page says so in the same paragraph as any inflation headline.
5. **Financed rows.** Never led with (D23). Each is printed with its rate, base, cap, deficit and how the deficit is met. A financed row whose debt passes GDP within 40 years is labelled unsustainable.
6. **Wealth.** Every wealth headline names the price-rule reading it rests on (S64) and prints its erosion share beside it; the `lf` wealth-poverty harm is labelled as a consequence of the opening balance's erosion (S66) where it appears.
7. **No low-share optimum** is claimed from the fixed-share rows unless the 20- and 40-year rows both show it with intervals excluding zero (S66).
8. **Failed pieces** are resumed with the same seeds, never redesigned. A row that produces non-finite output is reported as failed, with its count of seeds, never dropped.

## Structural uncertainty (what the seed intervals do not cover)
Seed intervals measure the model's randomness only. They do not cover: the choice of main row (D26) and of full backing (D25, a design statement, not an estimate); readings S70 held at main (listed below) and the ranges S70 swept; the Stress environment, which was not screened; the screen's 20-year horizon and 40 seeds; 500 adults (the 10,000-adult pair covers hours and the tail only); the engine's structure: one price rule for the economy; no central bank (S74); no migration; no value of care, community work or new ventures (S73 section 6); PTFs modelled from the Hub's statements and S62's costs; the creditor side's outside share left outside (S71); the financed rows without the weighted tail. Each limit is stated with every figure it bears on.

**Screened out (S70 rule 4; held at main, with the largest μ* over the threshold and its cell):** Source rows: `crInc` 0.28 (Adverse, C2.2, no assumed backing, median real wealth); `crOut` 0.28 (Reference, C2.2, no assumed backing, median real wealth); `poW` 0.13 (Adverse, C2.2, no assumed backing, inflation); `drLim` 0.10 (Reference, release, full backing, basic living); `wtA` 0.06 (Adverse, C2.2, no assumed backing, median real wealth); `crPop` 0.03 (Adverse, release, no assumed backing, wealth poverty); `poRes` 0.01 (Adverse, C2.2, no assumed backing, inflation); `prRs` 0.00. Financed rows: `poW`, `crOut`, `crInc`, `crPop`, `prRs`, `poRes`, with figures from `s70-F-tables.md` (copied into Amendment 1). Each was dropped on Reference and Adverse evidence only.

## Where it runs, and the cost (measured Nov 14 on the session machine, 4 cores, which S33 found no faster than a GitHub runner)
- Timing of the main pair (no programme, C2.2, release), 500 adults, engine `6ba80e5`: 0.65 s per row-run at 20 years and 1.21 s at 40 years (8 seeds, one process, start-up included); Stress no slower than Reference. S70's batch measured 0.5 s at 20 years on Actions.
- Row-runs per environment and seed: Source rows about 320 (61 points × 3 runs; 10 bound points × 2; the backing curve's 6 points × 2 programme runs and the 9 price-rule points at `a` 0 × 3; about 20 named readings × 3; 20 fixed-share runs); financed rows about 365 (115 points × 3, 10 bound points × 2). About 690 in all.
- 690 × 3 environments × 500 seeds × 1.86 s (both horizons) ≈ 535 core-hours. The 10,000-adult pair adds about 95 (to be timed in the dry run). **Total about 630 core-hours, 160 runner-hours; on 20 runners about 8 hours.** Below `prereg/RUNNING.md`'s 1,000 core-hour mark, and smaller than the S48 batch (650 runner-hours, run on Actions without objection).
- **GitHub Actions** (`run-study` workflow, compassionism-sim-results), no cost. No paid service is used. Results folders `r2-<part>-<engine 7>` with `run.txt` and `SHA256SUMS`.
- If pair corners were run at every end combination (up to 4 joint points per pair) the batch would be about 1,150 core-hours; not preregistered.

## Before the first run (S63 part 2; each recorded in Amendment 1)
1. S69's two corrections behind switches (off identical; guard test; engine lineage), merged; the engine commit pinned.
2. The job script `runner/jobs/r2.js` in compassionism-sim-results: `--check` (design size against this file; prints the pair ends and bound ends), `--selftest` (every setter at main reproduces the main pair exactly).
3. Dry run at seeds 1-2, every part, all three environments, both horizons, on Actions; the timings replace the estimate above; shard sizes set so no shard runs over 2 hours.
4. `prereg/run-manifest.md` amended with round 2's jobs, readers and folders.
5. S69's program rerun on the full-backing main row (packet with `make_s69_reference.js`, then `s69_main.py --seeds 1-500` and `s69_compare.py`).
6. This file, with Amendment 1, registered on OSF on the project's page (Duke; the date is then held by a third party), before S64 dispatches.

## Reporting
Every cell is published: shard files, `run.txt`, `SHA256SUMS`, the tables, every curve's CSV, in compassionism-sim-results; one plain-words report per question in compassionism-simulation `dev/reports/`; the findings page. Nulls, unfavourable results and the Adverse and Stress environments in full.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
