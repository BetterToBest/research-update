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

### Amendment 1 (Nov 14, 2026, S63 part 2, before any run of the batch): the engine pinned, the job, the ends, and the readings made concrete
Nothing above changes: no outcome, rule, environment, seed range or horizon. This records what "Before the first run" items 1, 2 and 4 fixed, and the places where the Design text needed a concrete reading. The dry run (item 3) and its timings follow in Amendment 2.

**Engine (item 1).** S69's two reporting corrections are built in compassionism-simulation as two parts of the `fx` row option, each off by default and off identical (guard test passed; 360 unit tests, two of them new): `fx.ez`, earnings below 1e-9 dollars a year count as zero; `fx.rk`, the weighted distribution measures rank on the value rounded to the cent, ties by index. `fx.rk` also reaches the weighted tail's measures (`wtm`: its Gini, shares and median), which use the same ranking: they are weighted distribution measures too, and a percentile moves by under a cent. The frozen main row is `harness.js` `r2FreezePair`: `r2MainRow` unchanged (so S68-S70 and S69's packet reproduce), the two corrections on, and the programme run at full backing (`o.a` 1; D25). Today's price rule (no `pr`; D26, answered Nov 14: today's rule with S69's two corrections, Claude's recommendation). Engine commit: `104691f3993ac6f37d6ff1b8ccd4690120cfe949` (compassionism-simulation pull request 107, merged; engine lineage link 10229932ee84 -> 3426ee3611d2: the six release panels unchanged). Results folders carry `104691f`.

**The job (item 2).** `runner/jobs/r2.js` in compassionism-sim-results, with `r2-ends.json` beside it. Four parts, one results folder per part, environment and horizon, `r2-<part>-<env>-<years>-<engine 7>`: **M** the main rows (the no-programme run, C2.2, the release design, and the financed main rows with their own no-programme run), every output key at full precision; **S** the Source rows; **F** the financed rows; **B** the main pair at 10,000 adults, every key. Parts S and F store 28 keys and four derived ones at 7 significant digits (`ppovA` and `pmedWA`, the means of the yearly readings over years 1 to T-1, as S70 computed `ppovA`; at 40 years `ppov20` and `pmedW20`). The engine's yearly series hold the reading at the end of year t + 1 at index t (the 20-year run's `pov` is its `ppov_19`), so year 20 of a 40-year run is index 19. `--check` passes: Source rows 107 distinct points, 296 row-runs per environment, seed and horizon; financed rows 126 points, 366 row-runs; M 6, B 3. Its full output (every point, pair end and bound end) is `prereg/checks/2026-11-s63-r2-check.txt`. `--selftest` passes: every setter at its main reading reproduces the untouched main rows exactly (2,880 series, both blocks, seeds 1-2); the 20-year run equals the first 20 years of the 40-year run (every yearly key, seed 1); every point of both blocks runs (3 years, seed 1) with finite output. With `--procs` the output is the same bytes as one process.

**Pair ends and bound ends** (Design items 3 and 4), fixed by `dev/tools/s63_ends.js` (compassionism-simulation) from the S70 shards, before any round-2 run. Pair ends: S70's rule-3 reading in the pair's own cells, summed over the cells as |effect at the end| / threshold. Bound: every carried input at the end the sign of its μ (over the steps where it acts; Reference and Adverse pooled; the design's full-backing cell on the Source rows, its financed cell on the financed rows) marks as unfavourable; an input at one reading takes it only when it lies on the unfavourable side. The financed rows carry the policy-rate rule's output-gap weight (`gvB`) by S70 rule 7, so 35 inputs are carried there (34 in full, `bgM` at one reading). Source-row bound for C2.2 (others in the check file): basic living `sc` 0.593, `rho` 0.3, `lfConv` none, `lfPm` 1, `rtPhi` 1, `rtNs` port, `bgM` 1, `poHire` 0.02, `poPay` price, `wtM` 6; inflation `wIdx` 0.75 only (the price rule's readings are inactive at full backing, S70 rule 6).

**Readings made concrete** (each with its reason):
1. *Single readings that act only under another reading* (S70 rule 6): the markdown `bgM` acts only with a bargaining pass-through above 0, and the policy-rate rule's coefficients `gvA`, `gvB`, `gvRs` only under that rule. At main they would change nothing, so their single readings and pairs are taken at pass-through 0.10 (S60's outer reading) or under the rule, and compared with that reading's own point (the pair's base). The bound applies the ends as the screen found them, without this.
2. *The price rule at no assumed backing* (item 5): 5 points, not 9: the ends equal to main (`prK` 1; `prR`, `prA`, `prBd` 0) are the backing curve's `a` 0 point, drawn once.
3. *The backing curve's mechanism points* (item 5): S51's main reading (only added output absorbs new money, ceiling 8% of earned income, lag 2 years, wear 5%) at the most productive setting S51 shows (f 100%, output 0.32 a year per dollar), and the same without the ceiling; `a` 0 under both.
4. *Named readings* (item 6): 15 points: `rt` off; the creditor side off with no debt relief (`chi` 1); `wt` off; `lf` off; the liquid share 0.046; the floor reading; the borrowing limit at $0 and $10,000; the capacity price rule at S58's main values (`pr: true`); the quarterly reading; `inc` hold and hedge, `pop` 1, `out` 0; S69's corrections off. Three readings item 6 names are already single readings and are drawn once: the velocity drift (`prBd` 0.132 at today's rule), the bargaining pass-through 0.10 and `conv: 'none'`.
5. *Fixed PTF share rows* (item 7): `pa: {fix: s, grow: false}` on the programme runs, shares 10% to 100%; the no-programme run is the main point's (it has no PTF).
6. *The financed rows* are built as S70 and S72 built them: backed share 0 (who pays is the question there), the government account on, no weighted tail. The C2.2 financed row's base is all money income and the release design's is wages, so the base's single readings are three points, each run for the designs whose main it is not: 49 single points (the Design text's 48 counted two).
7. *The financed rows' screened-out figures* (largest μ* over the threshold, and the cell), Reference and Adverse only: `poW` 0.37 (Reference, C2.2, programme debt at year 20); `crOut` 0.28 (Adverse, C2.2, wealth poverty yearly average); `crInc` 0.26 (Adverse, C2.2, wealth poverty yearly average); `crPop` 0.15 (Adverse, C2.2, programme debt at year 20); `prRs` 0.10 (Adverse, C2.2, programme inflation); `poRes` 0.02 (Adverse, C2.2, cost of living).

**Cost, recounted.** 668 row-runs per environment, seed and horizon at 500 adults (296 + 366 + 6), against about 690 costed in part 1, plus the 10,000-adult pair. Still below `prereg/RUNNING.md`'s 1,000 core-hour mark; Amendment 2 replaces the estimate with the dry run's timings. Shard files are compressed (`--gzip`, as S47).

**Dry run dispatched (item 3), Nov 14:** `run-study`, study `r2dry`, engine `104691f3993ac6f37d6ff1b8ccd4690120cfe949`, `job=r2.js`, `job_args=--part=all --procs=4`, seeds 1-2 in 2 shards ([workflow run 100](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43635868201)); folder `r2dry-104691f` with `DONE`. Its timings, the shard sizes and the 24 dispatch lines go in Amendment 2, before the batch.

### Amendment 2 (Nov 14, 2026, S63 part 3, before any run of the batch): the dry run's timings, the shard sizes, the 24 dispatch lines, and S69's program on the frozen row
Nothing above changes: no outcome, rule, environment, seed range or horizon. This records "Before the first run" item 3 (the dry run) and item 5 (S69's program on the full-backing main row). It replaces the cost estimate in "Where it runs, and the cost" with measured figures.

**The dry run (item 3).** Folder `r2dry-104691f` in compassionism-sim-results ([workflow run 100](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43635868201)): engine `104691f`, `job_args=--part=all --procs=4`, seeds 1 and 2, one shard each, every part, environment and horizon, on GitHub-hosted runners (4 processors). Both shards passed the workflow's checks (engine commit, clean engine, seed ranges). Every one of the 351,156 stored values is finite. Seed 1 took 1,168 seconds and seed 2 took 1,343 (different runners; the second about 15% slower), peak memory 468 MB. Seed 1's main rows (part M: the no-programme run and C2.2, Reference, 20 years) equal the frozen packet built for S69's program below on every key (958 and 990 keys).

**Timings and shard sizes.** Seconds per seed are the slower of the two runners, per part, environment and horizon (each includes its processes' start-up, so they are upper bounds). Shards are sized so that the longest shard, at the slower runner's rate, takes at most 90 minutes: a third in hand under the 2-hour limit and well inside the workflow's 350-minute stop. One shard count per part and horizon, the same in all three environments.

| Part | Years | Seconds per seed: Reference, Adverse, Stress | Runner-hours, 500 seeds, 3 environments | Shards per dispatch | Seeds per shard | Longest shard, minutes | Compressed output per folder, MB |
|---|---|---|---|---|---|---|---|
| M | 20 | 3.4, 3.8, 3.2 | 1.4 | 1 | 500 | 32 | 18-19 |
| M | 40 | 4.8, 5.2, 4.6 | 2.0 | 1 | 500 | 44 | 21-22 |
| S | 20 | 60.7, 61.3, 60.0 | 25.3 | 6 | 84 | 86 | 11-12 |
| S | 40 | 118.0, 115.9, 106.2 | 47.2 | 11 | 46 | 90 | 12-13 |
| F | 20 | 73.2, 75.3, 70.0 | 30.4 | 7 | 72 | 90 | 12-13 |
| F | 40 | 141.8, 136.2, 130.3 | 56.7 | 14 | 36 | 85 | 13-14 |
| B | 20 | 19.8, 20.5, 19.5 | 8.3 | 2 | 250 | 85 | 10 |
| B | 40 | 36.6, 37.5, 34.3 | 15.1 | 4 | 125 | 78 | 11-12 |

Output sizes are from the two dry-run seeds compressed together with `gzip -9`, scaled to 500 seeds (an estimate; more seeds compress somewhat better).

**Cost, measured.** About 186 runner-hours in all (the estimate in part 1 was 160), 138 shards. The engine's own process time is about 285 hours (the sum of every row's seconds at the slower runner's rate, times 250); the runners' 4 processors give an upper bound of about 750 processor-hours. Both are below `prereg/RUNNING.md`'s mark of about 1,000 core-hours in one study, and no process runs 6 hours. At most 20 runners at once: about 9.3 hours of wall-clock time if the queue stays full. GitHub Actions, no cost. About 340 MB of compressed shard files in 24 folders.

**The 24 dispatch lines.** Workflow `run-study` in compassionism-sim-results; for every line `engine=104691f3993ac6f37d6ff1b8ccd4690120cfe949`, `job=r2.js`, `seeds=1-500`. Study `r2-<part>-<env>-<years>`, folder `r2-<part>-<env>-<years>-104691f`. S64 dispatches them, in this order (the longest first), and adds each workflow run's link here.

| # | study | job_args | shards | workflow run |
|---|---|---|---|---|
| 1 | `r2-f-ref-40` | `--part=F --env=ref --years=40 --procs=4 --gzip` | 14 | [101](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651639762) |
| 2 | `r2-f-adv-40` | `--part=F --env=adv --years=40 --procs=4 --gzip` | 14 | [102](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651661946) |
| 3 | `r2-f-str-40` | `--part=F --env=str --years=40 --procs=4 --gzip` | 14 | [103](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651664636) |
| 4 | `r2-s-ref-40` | `--part=S --env=ref --years=40 --procs=4 --gzip` | 11 | [104](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651672044) |
| 5 | `r2-s-adv-40` | `--part=S --env=adv --years=40 --procs=4 --gzip` | 11 | [105](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651674969) |
| 6 | `r2-s-str-40` | `--part=S --env=str --years=40 --procs=4 --gzip` | 11 | [106](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651677670) |
| 7 | `r2-f-ref-20` | `--part=F --env=ref --years=20 --procs=4 --gzip` | 7 | [107](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651685905) |
| 8 | `r2-f-adv-20` | `--part=F --env=adv --years=20 --procs=4 --gzip` | 7 | [108](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651689053) |
| 9 | `r2-f-str-20` | `--part=F --env=str --years=20 --procs=4 --gzip` | 7 | [109](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651691746) |
| 10 | `r2-s-ref-20` | `--part=S --env=ref --years=20 --procs=4 --gzip` | 6 | [110](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651699395) |
| 11 | `r2-s-adv-20` | `--part=S --env=adv --years=20 --procs=4 --gzip` | 6 | [111](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651702056) |
| 12 | `r2-s-str-20` | `--part=S --env=str --years=20 --procs=4 --gzip` | 6 | [112](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651704417) |
| 13 | `r2-b-ref-40` | `--part=B --env=ref --years=40 --procs=4 --gzip` | 4 | [113](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651710994) |
| 14 | `r2-b-adv-40` | `--part=B --env=adv --years=40 --procs=4 --gzip` | 4 | [114](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651713580) |
| 15 | `r2-b-str-40` | `--part=B --env=str --years=40 --procs=4 --gzip` | 4 | [115](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651716499) |
| 16 | `r2-b-ref-20` | `--part=B --env=ref --years=20 --procs=4 --gzip` | 2 | [116](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651723174) |
| 17 | `r2-b-adv-20` | `--part=B --env=adv --years=20 --procs=4 --gzip` | 2 | [117](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651725721) |
| 18 | `r2-b-str-20` | `--part=B --env=str --years=20 --procs=4 --gzip` | 2 | [118](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651728627) |
| 19 | `r2-m-ref-40` | `--part=M --env=ref --years=40 --procs=4 --gzip` | 1 | [119](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651736705) |
| 20 | `r2-m-adv-40` | `--part=M --env=adv --years=40 --procs=4 --gzip` | 1 | [120](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651739513) |
| 21 | `r2-m-str-40` | `--part=M --env=str --years=40 --procs=4 --gzip` | 1 | [121](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651742916) |
| 22 | `r2-m-ref-20` | `--part=M --env=ref --years=20 --procs=4 --gzip` | 1 | [122](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651745558) |
| 23 | `r2-m-adv-20` | `--part=M --env=adv --years=20 --procs=4 --gzip` | 1 | [123](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651748769) |
| 24 | `r2-m-str-20` | `--part=M --env=str --years=20 --procs=4 --gzip` | 1 | [124](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43651751304) |

**Dispatched Nov 14, 2026, 23:07-23:09 UTC (S64)**, as listed above: all 24 lines on main of compassionism-sim-results (commit `62d6d42`), with the arguments in the table and nothing else changed. Lines 1-3, 4-6, 7-9, 10-12, 13-15, 16-18 and 19-24 were sent in groups of equal shard count; the run numbers follow the order of sending. Within a group the run-to-study match is by order of sending; each folder's `run.txt` names its workflow run, and the session that reads the folders checks the match there and corrects this table if any pair is swapped.

If a shard fails or a runner is much slower than the dry run's, the dispatch is run again whole under a new study id with a suffix (`-r2`) and the same arguments; seeds are paired, so the split changes no figure. Any change of shard count is recorded here with the reason.

**S69's program on the full-backing main row (item 5).** The packet was rebuilt on the frozen row: compassionism-simulation `dev/packets/s69-frozen-row.zip`, built by `make_s69_reference.js --frozen` from engine `104691f`, with seeds 1-500 in Reference, Adverse and Stress. The Python program now applies S69's two corrections when the row sets them. The six runs (no programme and C2.2 main row, three environments, seeds 1-500) agree with the engine exactly: every key in every seed, 958 and 990 keys, relative difference under 1e-9. No key and no effect fails the two-standard-error test. On the candidate row, 10 to 313 keys per run differed in some seeds through rounding, and the two corrections remove all of them. Results: compassionism-simulation `dev/reports/s69-independent-implementation/results-frozen/` (pull request 108). This meets S69's condition for dispatch.

**What remains before S64 dispatches:** item 6. Duke updates the file's OSF registration so that it carries Amendments 1 and 2.

### Amendment 3 (Nov 15, 2026, S64 part 2, after the results were read): the batch checked, and five points of reading
Nothing above changes: no outcome, rule, environment, seed range or horizon, and no run was repeated or added to the batch. This records the checks of the 24 folders and five places where the analysis needed a concrete reading. Items 3 and 4 were settled after the first tables were read; each says so.

**The batch, checked (Nov 15).** All 24 workflow runs (101-124) finished with success between 07:59 and 09:56 UTC. Each folder's `run.txt` names the study, engine `104691f3993ac6f37d6ff1b8ccd4690120cfe949`, the job arguments, the shard count and the workflow run in the table above: no pair within a group was swapped, so the table stands. Every folder has its full shard count and a `DONE` file; every `SHA256SUMS` passes; the shards cover seeds 1-500 exactly once; all 87,789,000 stored values are finite. No dispatch failed, so nothing was rerun under `-r2`. The tables tool (compassionism-simulation `dev/tools/s64_tables.py`) adds three checks, all passed: the 20-year run equals the first 20 years of the 40-year run in every yearly series of part M; the main point of parts S and F equals part M's main rows to the 7 significant digits stored (largest relative difference 5.0e-7).

**Points of reading.**
1. *The mechanism's point on the backing curve (Q4).* The realised backed share of the two mechanism points (`bkA`) is not among part S's stored keys. The two points' programme rows (part S points 75 and 76) were replayed on the session machine at the pinned engine with `bkA` added to the stored keys (`r2.js` otherwise unchanged; seeds 1-500, three environments, both horizons). The replay is the same computation: every key the batch stored must equal it, and the tables tool checks this. It is a reading of rows already run, not a new row. Result: in all 12 cells (two designs, three environments, two horizons) every stored key of the replay equals the batch's exactly; the mechanism reaches a backed share of 0.2-1.9% (main reading) and 13.6-19.6% (no ceiling). The replay's files are in compassionism-sim-results `r2-tables-104691f/replay/`.
2. *The year debt passes GDP on the financed curves (Q2, Q5).* Read as the programme run's own year (median over seeds; the horizon plus one means not within the run), not as a difference from the no-programme run, whose debt never passes GDP. Rule 2 cannot be read on that difference; the curve counts the points at which debt passes GDP within the run instead.
3. *Rule 7 with rule 3 (settled after the first tables were read).* The test of a low-share optimum: the most favourable of the ten fixed shares is 10-30%, and its paired difference from the 100% share excludes zero in the favourable direction, at both horizons. Applied without rule 3's materiality, it flagged differences of a hundredth of a point of inflation and $1,400-7,200 of median wealth (materiality: $10,100-20,000). Rule 3 applies to every effect, so the tables apply it here too and print both lists.
4. *Rule 5's label (settled after the first tables were read).* "Unsustainable" when the median year debt passes GDP falls within the run (20 or 40 years).
5. *Outputs not in the batch.* Two secondary outputs need data the batch does not store: the erosion share of each wealth figure (S66's trace needs each adult's opening balance and both runs' price paths) and basket poverty by labour-force reason (S61's key was not among the engine's outputs at `104691f`). They are reported as not yet computed, and S64 part 3 computes the erosion share with S66's trace on the frozen main row (the session machine; free).

### Amendment 4 (Nov 15, 2026, S64 part 3, before the erosion trace was run): the erosion share under asset classes, and basket poverty by labour-force reason
Nothing above changes: no outcome, rule, row, environment or seed range of the batch. This fixes, before any of it is run, how the two outputs that Amendment 3 (item 5) left for part 3 are computed. No erosion or labour-force figure had been computed on the frozen row when it was written.

**Why S66's term needs a new definition.** S66 measured the erosion of opening balances as each adult's opening net worth times the gap in the two runs' price deflators, W0 × (1/P_prog − 1/P_none). That is right when every dollar of wealth is cash earning nothing, which was the model's assumption then. The frozen main row holds wealth by asset class (S59, row option `rt`): homes, other property, shares and businesses are revalued with prices, and only money claims lose real value when prices rise. So S66's term overstates the erosion here, and it is printed only as an upper bound.

**The erosion term (the main reading).** For each adult present at year 0 in both runs of a seed (matched by the engine's adult id), in each year t: the real value of the adult's opening money claims, held untouched at the engine's own returns on them, in the programme run minus the no-programme run. The money claims are the engine's own trackers of the opening balances: nominal assets (deposits, bonds, the non-stock part of funds, `b.en`, which earn 0.46 of inflation less the creditor charges of S71), less floating-rate debt (`b.ed`, which keeps up with prices) and fixed-rate debt (`b.df`, which does not). Each run's balance is deflated by its own basket price level. Adults who enter after year 0 have no opening balance; their term is zero. The same computation on the opening real holdings (the five real classes, `b.v`) is printed as a check: they keep up with prices, so it should be near zero, moved only by the creditor charge on shares.

**What is reported.** For both designs (C2.2 and the release design) against the no-programme run, three environments, seeds 1-500, at the main row (`r2FreezePair`, each row run alone as part M runs it), from 40-year runs read at year 20 and year 40 (Amendment 3's check: the 20-year runs equal the first 20 years of the 40-year runs):
1. Wealth poverty, yearly average, at 20 and 40 years (the headline): published, and recomputed with each adult's programme real wealth less the erosion term ("without erosion"). The erosion share is the part that is erosion divided by the published effect.
2. Wealth poverty at year 20 and year 40, the same way.
3. Median real wealth: the weighted end-of-run median (`wtMedE`, the headline) at 20 and 40 years, the unweighted yearly average (`pmedWA`), and year 20 and 40, each published and without erosion, with the share.
4. The mean real-wealth gap per matched adult at years 20 and 40, the mean erosion term, its share, the real-holdings check and S66's all-cash bound; and by fifth of opening net worth.
5. Beside each share in 1-3, the share on S66's all-cash bound.

Intervals: paired bootstrap over seeds, 2,000 resamples, numpy `default_rng(6301)` as the tables tool; the share is a ratio of means and gets the bootstrap's percentile interval. Where the published effect is not material (rule 3), the share is printed but not read. The trace runs on the session machine (free) at engine `104691f`; the tool, compassionism-simulation `dev/tools/s64_erosion.js`, runs the batch's rows unmodified with a read-only year hook and stops unless its wealth poverty and median wealth in every year, the weighted median and basket poverty equal the engine's own keys exactly.

**Basket poverty by labour-force reason (Q6, Q7).** S61's item was not built as an engine key, but each adult carries its reason (`a._lf`: disability, early retirement, care, school; none if in the labour force; the status moves year to year under S73's flows). The same trace counts, in each year, adults and adults whose income is below their basket by status, and basket poverty by status is the adult-years below the basket over adult-years, from year 0 to the horizon (the definition of `fgt0PY`, which the counts must sum to exactly). Reported for the no-programme run and both designs, with the paired effect and interval by status. This is descriptive: no rule is applied to it.
