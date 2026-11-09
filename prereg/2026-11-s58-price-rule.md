# Preregistration: a price rule that answers demand and capacity (S58)

Committed Nov 9, 2026 by S58, before the switch is built and before any run of the rows below. Engine: compassionism-simulation at commit `8b10950c95d778883b4cb8da85fef2bb2b3f8515` (main); the switch lands on branch `claude/s58-price-rule` from it, off by default (guard test identical). The engine commit of the pilot is recorded in Amendment 1 before the pilot runs.

## Why
Every wealth result of the programme rests on the engine's price rule. Today the general price level rises each year by exactly the year's new money not matched by output, as a share of the year's cash income (`pmGenStep`: P × (1 + λU/Y), λ = 1, a labelled placeholder; S39 confirmed U = the Source's payout less its matched part, to the dollar). Under the C2.2 design that money is 31-46% of cash income a year, and prices end about 415 times their start after 19 years. The rule has no capacity, no slack, no costs and no expectations, so it cannot say whether output would absorb part of the money, or whether prices would rise faster than the money through wages and expectations. Both outside reviews (audit triage `audits/2026-11-s39-s55-review-triage.md`, B1-B4) asked for a rule that answers demand relative to capacity, with sourced parameters and readings beside it.

This study builds that rule behind a switch, measures what it changes, and answers S39's open question about the conversion tax. It is a choice of model, not a test of the programme.

## 1. Evidence (opened; order-of-magnitude checks, never targets)
Opened in S56 (triage B2; confirmed there): Egger et al. 2022 (Kenya; one-time transfers over 15% of local GDP: average price inflation 0.1%, upper 95% bound 0.22%, under 1% at the peak; slack capacity); Cunha, De Giorgi and Jayachandran 2019 (Mexico; about +0.2%, not significant; larger in remote villages); Filmer et al. 2023 (Philippines; perishable protein prices up in remote and saturated markets); Allen and Gentilini 2025 (review; minimal average effects, larger where supply is inelastic); de Soyres, Santacreu and Young 2022 (about 2.5-2.6 points of US inflation from pandemic fiscal support); Arias, Rubio-Ramírez and Shin 2026 (transfers about 11% of 2019 GDP; GDP deflator roughly 5% higher by end-2021); Comin, Johnson and Jones (binding capacity explains about half of the 2021-22 rise).

Opened for S58:
- McCandless and Weber, "Some Monetary Facts", Federal Reserve Bank of Minneapolis Quarterly Review 19(3), 1995 (PDF sha256 `839622fb…`): over 30 years in 110 countries, money growth and inflation correlate at 0.925 (M0), 0.958 (M1) and 0.950 (M2), with a slope very close to 1; money growth and real output growth are not correlated. This is the long-run check: a rule whose prices do not, in the long run, follow sustained new money about one for one would contradict it.
- FRED, downloaded Nov 9, 2026 (`sources/s58_price_rule.py` records each file's sha256): real GDP (GDPC1) and CBO's potential GDP (GDPPOT); total-industry capacity utilisation (TCU) and food manufacturing (CAPUTLG311S), Federal Reserve G.17; rental vacancy (RRVRUSQ156N), Census HVS; CPI-U (CPIAUCSL).

What the evidence can and cannot say, fixed now: **no study covers new money of 30-50% of household income every year.** The transfer experiments are one-time, local, partly tied to outside markets and at slack capacity; the pandemic estimates are one episode of about 11% of GDP. They bound nothing at the programme's scale. The rule therefore takes its parameters from US aggregate data and the long-run monetary evidence, sweeps them, and the report says plainly that the programme's injections lie far outside the range the parameters were estimated on.

## 2. The rule (what will be built)
Switch `PRICE_RULE` (row option `pr`): `'qt'` = today's rule, bit-identical (default); `'capacity'` = the rule below. Testbed runs only (`tbRunCore`); the price-only mode (`priceRun`) keeps today's rule (a stated limit).

State per run: n, the log of the money-implied demand level; p_k, the log price level of sector k (general basket, food, housing, medical care); all 0 at the start. At the end of each year t, from the year's flows (the same timing as today: the step sets next year's prices):
1. n ← n + ln(1 + λ U_t / Y_t), with U and Y exactly as today (λ = `lamG`, 1).
2. Slack: h_k,t = h0_k + ln(1/(1 − s_t)) − c_k,t, where s_t is the share of the year's income the recession left idle after the spending layer restored wages (0 outside recessions; the engine's recession path and `MULT`), and c_k,t a capacity loss (0 in every row; a hook for the supply-shock unit test).
3. Excess demand at this year's prices: x_k,t = n − p_k.
4. p_k ← p_k + α_k w_t + ρ π^e_t + κ max(0, x_k,t − h_k,t), where w_t = ln(1 + wIdx × π_G,t) is the year's wage indexation to the general level (the engine's rule; programme raises stay under `aw`, unchanged), and π^e_t = ln(B_t/B_t−1) is the year's endogenous basket inflation (expectations adaptive).
5. Prices for next year: P_G = exp(p_gen); essentials k: comp_k = PE_k × exp(p_k), where PE_k is today's essentials rule (θ × the demand gap; kept unchanged); every other basket item: P_G.

So prices answer demand relative to capacity (κ, h), output answers first where there is slack (money up to h raises no price), wages pass into costs (α), expectations carry inflation forward (ρ, so the price level can overshoot the money: pass-through above 1), and pass-through can fall below 1 while slack lasts or while prices lag (κ < 1). With κ = 1, α = ρ = 0 and h = 0 the rule is today's rule (p_gen = n), to rounding, in every year with U ≥ 0. With no new money and no supply shock every term is 0 and prices follow today's path exactly.

Reported each year (keys `pr*`, nothing feeds back): the output response min(max(0, x), h + ū); the rationed share 1 − exp(−max(0, x − h − ū)), demand that no output can meet; the output loss when prices overshoot (x < 0); the shadow price ratio exp(max(0, x − h − ū)), how far the measured price level sits below the one that would clear demand; general pass-through ln P_G / n at years 3, 10, 19 and 39. With them, median real wealth and wealth poverty at shadow prices. The engine has no goods market: demand that output cannot meet is reported, not modelled as queues or forced saving (a stated limit); real figures at measured prices overstate what money buys by about the rationed share, which is why the shadow readings sit beside them.

### Parameters
| Symbol | Main value | Basis | Swept |
|---|---|---|---|
| α (cost pass-through of wages), every sector | 0.5079 | Compensation of employees over gross domestic income, 2025 (BEA NIPA via FRED; the engine's `MULT_LS`, already sourced). One economy-wide share: no sector labour shares were opened (a stated simplification) | 0 (wages do not pass into costs) |
| κ (price response to excess demand, per year, on the log gap) | 0.47 | Derived (file `sources/s58_price_rule.py`): OLS of annual CPI-U inflation (log change of the annual average) on last year's inflation and last year's positive output gap (log GDPC1/GDPPOT, annual mean; the rule's one-sided form), 1960-2024, 65 years: slope 0.472 (s.e. 0.170). Estimated on gaps within about ±9%: the programme's gaps are far outside | 0.25; 1 (prices close the whole gap within a year, as today's rule) |
| ρ (weight of last year's inflation) | 0.27 | Derived, same regression: persistence 0.782 (s.e. 0.072) less α × wIdx (0.508), since the wage channel already carries that much of last year's inflation | 0 (1984-2024: persistence 0.436, no more than the wage channel); 0.45 (just under 1 − α = 0.49, above which inflation accelerates with no new money) |
| h0 (slack in normal years, log) | 0 in every sector | Sourced, each at or past its no-pressure level, floored at 0: CBO output gap 2025 +1.4% (above potential); food manufacturing utilisation 2025 84.9% against its 1972-2025 mean 82.2%; rental vacancy 2025 7.1% against its 1956-2025 mean 7.3%; medical care: no capacity series opened (the general reading) | general basket only: 0.0445 = ln(79.41/75.95), total-industry utilisation 2025 against its 1972-2025 mean (goods-producing slack the CBO gap does not show) |
| ū (most output can stretch above its no-pressure level, log) | 0.0593 = ln(1.0611) | The largest positive CBO output gap since 1949 (1966 Q1, +6.1%) | none (reporting only) |
| λ | 1 | today's `lamG` | the old 0.25-1 sweep stays a reading under `'qt'` |

The derived κ and ρ come from one regression of the rule's own form on opened data; they are estimates of parameters, not tuned to any result. Values printed by the source script are rounded to the digits shown; the engine stores the script's output.

## 3. The conversion tax (S39 open item b)
Claude's reading, from the code and the earlier reading of the Hub papers (`dev/reports/03a-financing-reading.md`, Oct 1: the BLEI paper, 6.3 and 9, makes the conversion tax the system's revenue for the BU allocation; rule S4 there: "It is withheld from each payout, so it lowers the new money directly"): every conversion the engine pays is recorded net of the tax (project, holder and ESP conversions as gross × (1 − tax); the business premium as gross − tax − face value), so the tax never enters anyone's cash and is already outside U. Netting it from U again would count it twice. The Source spends none of it in the release and C2.2 rows (S54's levers keep project proceeds, not the tax, and those are already in U through `lvStep`). If the pilot's money-flow table confirms this, S39's sentence "the conversion tax the Source keeps does not reduce U" gets a dated correction note (U already excludes it), the rule needs no change, and no design question goes to Duke.

The money-flow table (study option `mf`, reporting only; year-0 dollars per adult-year, means over the run): BU issued; BU spent at face value; conversion gross; conversion tax withheld; conversion paid net; the Source's payout (BU at face plus net conversion); matched output; price cuts paid (PTF and PTH; outside U under Source financing, as today); PTH appreciation credited; U; cash income Y; U/Y; the tax as a share of gross conversion; and the identity check |U − (payout − matched)|. The tax "re-spent" line is 0 by construction in these rows and is printed as such. Balances held: the engine has no money stock apart from households' wealth; BU are not carried between years, so no BU balance is held (stated, not a line).

## 4. Unit tests (each mechanism alone)
1. Off: `pr` absent or `'qt'`: every output identical (the guard test; and a unit test on seed 1).
2. No new money: a no-programme row under `'capacity'` gives every output of the `'qt'` row exactly.
3. Nesting: κ = 1, α = ρ = 0, h = 0 gives today's price path to 1e-9 relative.
4. Slack: a year of new money no larger than its slack moves no price (output takes it).
5. At capacity: with h = 0, new money raises prices; with κ = 1 by the full gap.
6. More capacity, less pressure: a larger h0 gives a lower price level for the same money.
7. Supply shock, no new money: a capacity loss raises prices with U = 0.
8. Tax-financed differs from money-financed: the same programme with the flat contribution (`fin: 'tax'`) moves the general level less than with Source financing.
9. Expectations: with ρ > 0, prices keep rising after the money stops, so pass-through exceeds 1; with ρ = 0 and α = 0 they stop.
10. `mf` is reporting only: no output moves with it on; its identity holds on the release row.
The eight-draws-per-agent-year guarantee is untouched (the rule draws nothing).

## 5. Pilot (mechanism check, not a result)
- **Yardstick (every row):** as S57: the frozen engine (`frozenRow`), CPS earnings (`lt: {s: 'all', m: 'all'}`), today's safety net (`sn: {abawd: true, slope: true}`), the manifest's common settings (`fin: 'tax'` study default, NR6 profile, `TB_PROFILE_G`, `REL_V52_STUDY`), and `mf: true` on every row.
- **Rows:** no programme under `'qt'` (np) and `'capacity'` (np-cap, the identity check); the release row under `'qt'` (rel), `'capacity'` at the main values (rel-cap) and with κ = 0.25 (rel-k25); the C2.2 design (`c22Design`) under `'qt'` (c22), `'capacity'` main (c22-cap), κ = 0.25, κ = 1, ρ = 0, ρ = 0.45, α = 0, h0 general 0.0445, and the nesting point κ = 1, α = ρ = h = 0 (c22-nest). Every programme row is paired with np.
- **Environments:** Reference, Adverse, Stress. **Seeds 1-100**, paired (common random numbers); 500 adults; 20 years. Round 2 runs nothing at 500 seeds before S63's freeze.
- **Where:** the session machine (free). Command `node dev/tools/s58_price.js ENV 100 20` for ENV in ref, adv, st; tables by `python3 dev/tools/s58_table.py DIR`; outputs in compassionism-simulation `dev/runs/s58-price/` and compassionism-sim-results `s58-price-<engine commit, 7 chars>` with run.txt and SHA256SUMS.

## Outcomes
- **Primary (the rule's behaviour):** for each programme row, the programme's inflation (`endoAnn`, points a year), the end price level (`endoIdx`), general pass-through at years 3 and 19, and the difference between `'capacity'` and `'qt'` on each.
- **Secondary:** the programme's paired effect on basket poverty (`fgt0PY`), wealth poverty (`pov`), the cost of living (`hhCostPY`) and median real wealth (`medWealthReal`); the shadow readings (median real wealth and wealth poverty at shadow prices); the rationed share, the output response and the output loss; the money-flow table for rel and c22 under both rules.
- **Checks:** np-cap identical to np (every key outside `pr*`); c22-nest equal to c22 within 1e-9 relative on the end price level; the money-flow identity.
- **Family:** every table is exploratory (pilot) with unadjusted 95% intervals (2.5th-97.5th percentile of 2,000 paired bootstrap replicates over seeds); beside each, the count of estimates whose interval excludes zero and the count surviving Holm at 5% (the p-value from the normal tail of the mean over its bootstrap standard error, as S57 Amendment 1).

## Decision rules
1. The rule is ready for S63 if every unit test passes, the guard test is identical, np-cap equals np and c22-nest equals c22 within 1e-9. Otherwise the defect is fixed and the pilot rerun before any report.
2. Claude's recommendation for S63's ledger decision is fixed now, whatever the pilot shows: `'capacity'` at the main values above as the main-row candidate, `'qt'` beside it (the published placeholder), and the sweep above as readings. Reason: every parameter of `'capacity'` is sourced or derived, against today's single placeholder; the results do not enter the choice.
3. The conversion tax is settled by the money-flow table as section 3 says; only if the table shows the tax inside U (contrary to the reading) does the rule change, by a dated amendment here before any report.
4. Any choice made while building that this text does not fix is a dated amendment below, before the pilot runs.

## Reporting
Every cell is published in compassionism-simulation `dev/reports/s58-price-rule.md` (plain words; Claude's reading; sources opened; the labelled and derived parameters with their ranges; what the rule cannot do) and in compassionism-sim-results.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
