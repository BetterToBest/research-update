# Audit prompt: the Compassionism Simulation's S39 and S55 studies, and how it measures inequality

Paste everything below the line into an AI system that can read web pages. Use it with two different systems and bring both replies back. It needs no code to run; the reports and code are public. Expected time to answer: 30 to 60 minutes. Then paste each full reply back into Claude (Chat in the Better To Best Research Project, or a Claude Code session started with `/start-session S56`) and say which system wrote it.


**Correction notes (Nov 9, 2026, S56, after the two reviews came back; the prompt below is kept as sent).** (1) "The check bounds the pass-through between 0 and 1" (S39 results) overstates it: 0 and 1 are the two engines' assumptions, not bounds on the real value, which could lie outside them (S39 report, correction note under section 6). (2) The inequality table is the frozen headline (CPS wages, spending share 0.877, 10,000 adults). Its 21.9% of families in debt at year 20 is not comparable with S34's 33.4%, which is the released v5.6 engine with released wages and spending share 0.593 (with US wages S34 gives 21.4%). (3) "Wealth Gini" in the table counts debts as zero. Triage: `audits/2026-11-s39-s55-review-triage.md`.

---

You are auditing two completed studies of an open agent-based simulation, and the way the simulation measures inequality. Please be direct: say what is wrong or unsupported, not only what is good. Where you are unsure, say so. Do not assume the results favour the policy; the author wants the work to stand up to critical economists.

## What the model is

The Compassionism Simulation is an open, in-browser agent-based model of an economic design called Compassionism (author: Duke Johnson). It follows 500 to 50,000 simulated US working-age adults (25 to 64) and their children for 20 or 40 years, in three environments (Reference, Adverse, Stress), once with no programme and once with the programme, using the **same simulated people and random draws** in both runs. Results are means over 500 paired seeds, with 95% paired-bootstrap intervals. Today's US safety net (SNAP, the earned income tax credit, the refundable child tax credit) is in both runs.

The design has five parts: **CCO** (a monthly Basic Unit, BU, paid by a "Source"), **PTF** (Public Trust Foundations: not-for-profit essentials businesses, such as grocers and utilities, that accept BU and sell below market price), **PTH** (housing PTFs), **SZH** (zones) and **CIP** (community investment). Two designs are studied: **C2.2** (BU automatic, at the cost of food, housing and medical care) and the **release design** ($1,200 a month, opt-in).

The engine passes new money into prices with a fixed rule: each year, the Source's payout not matched by new output is divided by the year's cash income, and the general price level rises by that share (a quantity-theory rule with a pass-through of 1, which the engine's own notes call a placeholder). Savings earn no return in the main reading.

Main sources (please read the reports, not only this summary):
- Code and reports: https://github.com/BetterToBest/compassionism-simulation
- S55 report: https://raw.githubusercontent.com/BetterToBest/compassionism-simulation/main/dev/reports/s55-open-access.md
- S55 design reading: https://raw.githubusercontent.com/BetterToBest/compassionism-simulation/main/dev/reports/s55-ptf-access-reading.md and https://raw.githubusercontent.com/BetterToBest/compassionism-simulation/main/dev/reports/s55-ptf-growth.md
- S39 report: https://raw.githubusercontent.com/BetterToBest/compassionism-simulation/main/dev/reports/s39-outside-crosscheck.md
- Baseline against US data (S34): https://raw.githubusercontent.com/BetterToBest/compassionism-simulation/main/dev/reports/baseline-realism.md
- Model description: https://raw.githubusercontent.com/BetterToBest/compassionism-simulation/main/MODEL_SPEC.md and https://raw.githubusercontent.com/BetterToBest/compassionism-simulation/main/ODD.md
- Preregistrations: https://github.com/BetterToBest/research-update/tree/main/prereg
- Per-seed results: https://github.com/BetterToBest/compassionism-sim-results

## Study S55: open PTF access

**Question.** The design lets anyone shop at a PTF, in dollars or BU, at one posted price. The earlier model let only PTF members pay PTF prices. S55 builds open access: every adult in a zone buys the zone's PTF share of essential sales at PTF prices, and two density tests from the design's papers read that share (the PTF price cut is smaller below a 40% share; a "synergy coefficient" θ is zero below 55%). The share starts at 18% (8% in Stress) and grows each year until one of three limits binds: capacity (PTF capital per adult), operations (sales must cover running costs) or demand (a ceiling of 49%, taken from S Group's share of Finland's grocery sales and labelled a design parameter, swept at 25%, 75% and 100%).

**Results (headline cell: C2.2, Reference, 10,000 adults, 20 years).**
- Basic living (share of adult-years under 30 days of basic living): open minus members +0.03 points. Cost of living (share under the MIT living-wage budget): +0.14 points. Neither is material (the preregistered threshold is 1 point).
- Low wealth (share of adults with wealth under $25,000 in year-0 prices): 2.42 points fewer [2.40, 2.44], material. With members only, the programme left 0.19 points *more* low-wealth adults than no programme; with open access, 2.23 points fewer.
- Cost +$1,398 per adult-year (2.3%); inflation −0.64 points a year (the programme's inflation is about 35% a year in this cell).
- Under the release design, nothing is material; wealth gets slightly worse in 8 of 12 settings.
- The wealth gain disappears with a 25% demand ceiling, with outside running costs, or with growth off; it rises to +5.2 and +7.6 points with 75% and 100% ceilings.
- Capacity binds first, then demand; operations never binds in the main reading, because the design prices at cost. At outside sector margins, PTF sales cover only 35-59% of running costs and the network never grows.
- At the 49% ceiling the 55% test is never passed, so θ never activates.
- A fixed-share sweep (10% to 100%, growth off) rises smoothly, with one small step at 40% and none at 55%. Wealth is better at a 10% share than at 20-30%; the cause is not traced.
- The report's reading: open access lets PTF price damping cover about 43% of sales instead of the member share (about 20%); since the engine's inflation erodes savings, slower inflation leaves more adults above $25,000. This was not tested by a separate run.

## Study S39: an outside model of prices

**Question.** Does a published whole-economy model reproduce the engine's inflation when given the same new money? BeforeIT.jl (the Bank of Italy's implementation of Poledna, Miess, Hommes and Rabitsch 2023, calibrated to Austria) received the same yearly new money as a share of household income (31-46% a year under C2.2), at full scale (8.9 million agents, 5 seeds) and at 1:1000 (100 seeds), with readings for tax financing, a domestic central bank, gross money and doses of 1% to 30%.

**Results.**
- The engine's price level after 19 years: about 408 times its start (C2.2, Reference); pass-through 1 by construction.
- BeforeIT's consumer prices after 20 years: −0.4% against its own no-payout run [−7.1%, +6.8%]; pass-through 0.00 [−0.012, 0.010].
- Reading BeforeIT's source after the runs showed why: with its packaged uniform starting prices, every firm's cost-push term is zero, and prices grow each quarter by expected inflation alone (a forecast from past inflation plus a random draw). Demand, wages and the payout never enter. This was confirmed in all 1,365 runs to machine precision. So BeforeIT's zero is also an assumption, not a measurement.
- In BeforeIT the money raises real output (+15.5% after 3 years, unemployment to zero, output per worker stretched up to 1.5 times) and government debt (9.8 years of output after 20 years, against 1.1 without the payout). Financed by income tax instead (the rate rises from 21% to about 60%), almost all of the output gain disappears.
- The report's conclusion: the check bounds the pass-through between 0 and 1 but does not narrow it. Open engine questions: an outside source for the pass-through of large money-financed transfers, and a conversion tax the Source keeps but does not net from the new money.

## Inequality measures, computed from the per-seed results

10,000 adults, 20 years, Reference, mean over 500 seeds:

| | No programme | C2.2, members only | C2.2, open access | Release, open access |
|---|---|---|---|---|
| Wealth Gini, end of run | 0.728 | 0.353 | 0.346 | 0.479 |
| Income Gini (disposable) | 0.337 | 0.294 | 0.288 | 0.351 |
| Median wealth, year-0 dollars | $212,351 | $41,043 | $42,888 | $29,199 |
| Families in debt, year 20 | 21.9% | 0.8% | 0.6% | 9.2% |
| Adults with wealth under $25,000 | 22.0% | 22.2% | 19.8% | 43.6% |
| Poverty severity (FGT2 × 100) | 4.13 | 0.06 | 0.06 | 0.70 |

The wealth Gini halves while median real wealth falls by about 80%: the gap narrows from both ends (debt nearly disappears, while savings lose their value to modelled inflation).

**The baseline against the US** (S34 and computed): earnings Gini 0.41 in the model's CPS reading against 0.45 in the US; household income Gini 0.40 against 0.467; every simulated adult works (80.9% of US adults 25-64 have earnings); with no programme, 21.9% of families are in debt after 20 years (US 9.3%), because the spending rule lets households below their budget spend more than their income every year. Starting wealth is drawn from SCF percentiles and the engine's single-adult table gives a wealth Gini near 0.82 and a top 1% share near 27% (US: about 0.83 and 35% in the SCF 2022; 32.5% in the Fed's Distributional Financial Accounts, Q2 2026). The table stops at the SCF's 99.5th percentile (about $10.8 million): there are no larger fortunes, savings earn no return, and there is no business or property income.

## What to review

Please answer each part. Cite sources with links where you rely on outside evidence.

**A. S55's design and statistics**
1. Is reading both density tests as the PTFs' share of a zone's essential *sales* a defensible translation of "merchant participation"? What else could it mean, and would it change the results?
2. Is a 49% demand ceiling from one Finnish cooperative a reasonable anchor? What other evidence on cooperative or public-option market shares exists (consumer co-ops, public utilities, municipal grocers, public options in insurance)?
3. The operations limit cannot bind because the design prices at cost. Is that assumption reasonable for not-for-profit grocers, utilities and childcare? What cost and margin data would test it?
4. Are 500 paired seeds, the bootstrap, the materiality thresholds (1 point; 5% of cost) and the Holm correction appropriate? Does reporting about 26,000 estimates invite false findings?
5. What could explain wealth being better at a 10% fixed share than at 20-30%?

**B. S39 and the price rule**
1. Was BeforeIT a meaningful cross-check, given what its price rule turned out to be? Name better outside models or calibrations, and say what each would add.
2. What empirical evidence bears on the pass-through of large cash transfers or money-financed spending into prices (for example local price effects of large cash-transfer programmes, pandemic stimulus, historical monetary financing)? Give the range it supports for an injection of 30-50% of household income a year, or say that no evidence covers that size.
3. Propose a price rule for the engine that responds to demand relative to capacity, with sourced parameters, that a small team could build and test.
4. Should the conversion tax the Source keeps be netted from the new money?

**C. Measuring inequality, concentration and power**
1. The wealth Gini falls sharply while median wealth falls. What measures should be reported beside the Gini so readers are not misled in either direction (for example top 1% and top 10% shares, the Palma ratio, wealth and income percentiles in real terms, growth incidence curves, mobility between quintiles, debt)?
2. The model cannot hold large fortunes (its table stops at the 99.5th percentile and 10,000 adults are too few to sample the top). How should a top tail be added (for example a Pareto tail fitted to the SCF and the Forbes 400, with population weights) so concentration can be measured without breaking the paired design?
3. Savings earn no return and there is no capital or business income, so wealth cannot compound at the top. What is the simplest sourced way to add returns on capital that differ by wealth, and ownership of businesses?
4. The author's concern is that concentrated wealth gives leverage over wages, prices and politics. Which measurable quantities could a model like this report as proxies (for example the share of wealth or business ownership held by the top 1%, labour's share of income, wage markdowns under monopsony, workers' reservation wages)? A basic income may raise workers' bargaining power through a better outside option; the model's only labour response is an hours response. What evidence and mechanism could be added, and how should it be validated?

**D. The baseline**
1. Which baseline gaps matter most for the programme's measured effects: everyone working, the debt drift (a spending rule that lets households below their budget spend more than their income every year), the missing top tail, or the missing returns on capital?
2. What would you fix first, and with which data?

**E. Help with the planned improvements**

The author has planned six engine changes in response to these studies (plan: https://raw.githubusercontent.com/BetterToBest/research-update/main/audits/2026-11-engine-round-2.md). Each will sit behind a switch with today's behaviour as the default, use only cited sources or labelled and swept design parameters, and be preregistered before any full run. For each one, please give: the best published evidence and data (with links), the parameter values or ranges they support, a design you would recommend (and simpler or more ambitious alternatives), how to test that it works, and the mistakes to avoid. Say plainly if you think one should not be built, or should be built differently.

1. **Distribution measures** (reporting only): top 1% and top 10% shares, the Palma ratio, real percentiles up to P99.9, a growth-incidence curve, mobility between wealth fifths, labour's share of income, families in debt. Which of these, or others, best show whether a policy helps people and reduces concentration, without misleading in either direction? How should intervals be computed for top shares in a model with few agents at the top?
2. **A price rule that answers demand and capacity**, replacing the fixed pass-through of 1: what evidence exists on how much large cash transfers or money-financed spending raise prices, and at what scale? Which rule (for example a Phillips-curve form, markup over costs with a capacity term, or a sector-level rule for essentials) fits an agent-based model of households with a simple production side? Should a conversion tax the Source keeps be netted from the new money?
3. **A weighted top tail and returns on capital**: how to fit a Pareto tail to the SCF and the Forbes 400 and carry it with population weights while keeping each simulated person paired with their no-programme twin; what returns on wealth by wealth level (and business ownership) the evidence supports for the US.
4. **Bargaining power**: how to model a worker's outside option and an employer's markdown (monopsony) so that a Basic Unit can raise reservation wages; US markdown estimates; what unconditional cash and basic-income studies found on wages, hours and job search; how to keep one consistent wage elasticity.
5. **Baseline scope**: adding adults outside the labour force (caregivers, disability, students, early retirees) at US shares; a spending rule that stops households below their budget from spending more than their income every year, chosen from evidence on consumption and borrowing at low incomes.
6. **PTF realism**: running costs and margins of not-for-profit grocers, utilities and childcare (cooperative and public-utility financial data); how to model PTF jobs and wages.

**F. Fair presentation**
1. The author advocates for the policy and publishes the results on a research hub. Which of the findings above can be stated as results, which only as model outputs under named assumptions, and which should not be claimed? Suggest wording for the headline wealth finding and for the inflation figures.
2. Is anything reported here that you think is misleading, in either direction?

## How to answer

- Start with a short summary: the three most important problems and the three most useful improvements.
- Answer part E as its own section, one heading per planned improvement, so each can be handed to the step that builds it.
- Then numbered findings, each with: **severity** (blocks a published claim / should fix before release / worth doing later), **what is wrong or missing**, **evidence** (a source link, or a quote from the reports with its section), and **a specific fix**.
- Then a ranked list of improvements to the simulation, each with the data it needs and a rough size of the work.
- End with what you could not check, and why.
