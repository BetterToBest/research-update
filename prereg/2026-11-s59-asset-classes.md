# Preregistration: wealth held by asset class (S59, part 1: switch RETURNS)

Committed Nov 10, 2026 by S59, before the switch is built and before any run of the rows below. Engine: compassionism-simulation at commit `814501fd3861c64cdd84a35bf1e8cfe0d9c9c562` (main); the switch lands on branch `claude/s59-asset-classes` from it, off by default (guard test identical). The engine commit of the pilot is recorded in Amendment 1 before the pilot runs.

This file covers the first part of S59: what a household's net worth is made of, and how each part moves with prices. The weighted top tail (`WEALTH_TAIL`), returns that differ by wealth, and business ownership with its income are the second part, preregistered in their own file before they are built.

## Why
Today every adult's wealth is one number of dollars. It earns nothing and is never revalued. The programme's modelled inflation is 30-45% a year, so after 20 years prices are about 400 times their start, and a household that began with a $300,000 house is recorded as holding $300,000 of year-20 dollars. The Nov 9 audit (finding 1) called this the largest single weakness of the wealth results, and the S66 trace measured it: the erosion of opening balances is 90-96% of the programme's year-20 real-wealth gap in every design and environment.

In the United States most household net worth is not cash. In the 2022 Survey of Consumer Finances, for the families the engine starts from (head aged 25-66 with wage income), homes are 35% of net worth, shares 26%, private businesses 24%, other real estate 9%, vehicles and other goods 5%, nominal assets (deposits, bonds and the like) 20%, and debts 18% (16 points of them fixed-rate). Nominal assets less all debts are 2% of net worth (`sources/s59_portfolio.py`, computed for this file; no engine run involved).

## What will be built (switch `RETURNS`, study row option `rt`; off = identical)
1. **The opening split.** At year 0 each household's net worth W is split by its wealth group (seven groups: below zero; then zero to the 25th, 50th, 75th, 90th and 99th percentile, and above, of the starting population's net worth). Gross assets G = W/(1 − lev), debts lev × G, where lev is the group's debts over its assets; assets by the group's shares into home, other real estate, shares, private business, other goods (the real assets) and nominal assets; debts by the group's shares into fixed-rate and floating. The split depends only on the household's starting net worth, so both runs of a pair start identical. No random draw.
2. **Each year**, with π the year's change in the price level the engine already uses for wealth in real terms:
   - a real asset of class c grows by (1 + ix × π)(1 + ρ_c) − 1. Main: ix = 1 (it moves with the price level); ρ = the long-run real price gain, homes 0.94% and shares 4.02% a year (Shiller's data, 1953-2022, `sources/s59_real_gains.py`), other real estate as homes, private business as shares (no price series: a modelling assumption), other goods 0;
   - nominal assets grow by φ × π. Main: φ = 0.46 (per 100 basis points of the policy rate, deposit rates rise 46: Drechsler, Savov and Schnabl, *QJE* 2017, opened: "the spread between the Fed funds rate and the deposit rate increases by 54 bps"; the policy rate is taken to move one for one with inflation, a modelling assumption);
   - fixed-rate debt keeps its dollar value; floating debt grows by ψ × π, main ψ = 1 (it reprices in full);
   - the year's saving (everything else that changes the adult's wealth) first repays floating debt, then goes to nominal assets; a shortfall draws nominal assets to zero, then adds floating debt. Real assets are not sold and fixed debt is not repaid (modelling assumptions; interest and repayments are inside the cost of living, as today).
   - the −$10,000 floor on net worth stays as it is.
3. **Reporting keys:** mean real wealth in three parts, for all adults and by fifth of starting wealth: E, the opening nominal position held untouched (opening nominal assets and floating debt with their interest, less fixed debt); V, the opening real assets held untouched; S, the rest (saving since year 0 and what it earned). E + V + S is real wealth exactly. The programme's effect on each is the paired difference: erosion of opening nominal balances (E), revaluation (V), change in real saving (S). Also the top 1% of adults' share of private business equity, start and end.
4. **Unit tests, fixed now:** (a) off, or on with every asset nominal and φ = ψ = 0, gives today's path exactly; (b) with every asset real, ρ = 0, ix = 1 and no debt, an untouched balance keeps its real value under any inflation; (c) E + V + S equals real wealth; (d) the yearly step alone, against hand arithmetic; (e) both runs of a pair hold the same opening split.

Not built: a creditor side (a debt inflated away has no one who loses it); capital income (dividends, rents, business income); house purchases and sales; mortgage repayment. Each is stated as a limit in the report.

## Questions
1. With wealth held by asset class, what is the programme's effect on wealth poverty (adults under $25,000 of real wealth), median real wealth, the wealth Gini, top shares and families in debt, beside today's all-cash reading?
2. How much of the programme's year-20 real-wealth effect is each of the three parts, by fifth of starting wealth? Does the erosion share fall from S66's 90-96%?
3. Which of the swept assumptions (φ, ix, ρ, where new saving goes) moves the answer to 1?
4. Does the no-programme run change (its inflation is the outside rate, about 2-3% a year), and does the start match the SCF less or more closely? (The start is unchanged by construction; the 20-year drift is the question.)

## Design
- Rows: the frozen release row and the C2.2 design, each with its own no-programme run (`frozenRow`, `c22Design`, as S61 and S66), in Reference, Adverse and Stress; seeds 1-100; 500 adults; 20 years; paired by seed. Free: session machine or Actions.
- Readings of `rt`, each on both designs: **off** (today); **main** (ix 1, ρ main, φ 0.46, ψ 1, new saving nominal); and one change at a time from main: φ 0; φ 1; ix 0.5; ρ 0; ρ at the 1983-2022 window (homes 1.81%, shares 5.71%); ρ at 1890-2022 (0.59%, 2.32%); new saving split by the group's asset shares (`ns: 'port'`). A check row: every asset nominal with φ = ψ = 0 must equal off on every key.
- Basket poverty and the cost of living are reported for every reading (guardrail 6).

## Outcomes
Primary: the programme's effect (programme minus no programme, paired) on wealth poverty (`pov`), at year 20, under main, beside off. Secondary: median real wealth, the wealth Gini (debts kept, and debts as zero), top 1% and top 10% wealth shares, bottom 50% share, families in debt, basket poverty, cost of living, programme inflation; the three parts by fifth; the top 1% share of business equity; the no-programme run's year-20 wealth distribution beside its start.

## Analysis
Paired differences over seeds with the 2.5th-97.5th percentile interval of 2,000 paired bootstrap replicates (fixed generator), unadjusted, as S61 and S66. The S66 erosion decomposition is rerun as the three-part table. No significance stars; every reading in the table.

## Decision rules
- No constant is tuned. The SCF shares, Shiller's rates and the 0.46 are what the sources give; φ, ix, ρ and the saving rule are swept and every reading is published.
- The SCF and the Fed's Distributional Financial Accounts are comparisons, never targets; gaps are reported.
- Recommendation to S63 (the freeze): `rt` main becomes a main-row candidate if the unit tests and the guard test pass and no accounting identity fails; the off reading stays beside it as "all wealth is cash". If a swept assumption changes the sign of the primary outcome, the report says the sign is not established and names the assumption.
- A pilot is a mechanism check at 100 seeds, not a result; the frozen 500-seed batch decides.

## Reporting
compassionism-simulation `dev/reports/s59-asset-classes.md` (plain words), tables in `dev/runs/s59-assets/`; per-seed results in compassionism-sim-results `s59-assets-<engine commit>` with run.txt and SHA256SUMS. Every reading is published, including nulls and the Adverse and Stress environments.

## Amendments
(none yet)
