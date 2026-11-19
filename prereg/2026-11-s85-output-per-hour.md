# Preregistration: output per hour and automation, with the backing produced (S85, the v6 engine)

Committed Nov 19, 2026 by S85 part 1, before any switch below is built and before any run. Engine: compassionism-simulation at commit `353662e0f89f16b3ac854a0f66c547ca9078d1be` (main, after PR 165). The build lands on a `claude/s85-*` branch from it, off by default (guard test identical). Option names below are provisional. Amendment 1 (after the build, before the dry run) fixes the names, the sourced values listed under "To open before the dry run", the engine commit and the job.

Claude's reading of the design: compassionism-simulation `dev/reports/s85-output-reading.md`. Sources opened Nov 19: `sources/s85_output.md`, `sources/s85_hours.py` (branch `claude/s85-output-reading`, commit `cf687db`).

## Why

The main row assumes full backing. The model's own mechanism for new output reaches 0.2-1.9% of the payout (S64, question 4). The release reviews asked for the design's growth to be modelled, not assumed (triage theme 2; in-house finding 2 and Duke's reply, "work is worth more for less"; Nemotron B4 and ranked improvement 1). Duke added, on Nov 17 and Nov 19, that AI and automation will raise output per hour and cut paid hours whatever policy does, and he named three displacement levels: 30%, 50% and 70%.

This study models output per hour and paid hours as two separate inputs. It runs automation on both sides of every pair. It measures what displacement does with and without the programme. It lets the programme's own work produce its backed share instead of assuming it.

**Duke's view, attributed and not an input.** "The goal of the program is more for less, not less for more"; free time "to pursue personal projects" is "part of the flourishing aspect that the program can offer"; implemented and maintained well, the programme "can prevent much of the distress" automation would otherwise cause. Whether it does is what the run measures. Every result below is reported whichever way it falls.

## What the engine does today (read in the code before this file; no run)

1. **Wages** (MODEL_SPEC 6.1): base real growth 1.0% a year, plus 0.8% gated on the BLEI, plus prices (`wIdx` 1). The automation pay drag has been off since v5.4.
2. **Automation** (MODEL_SPEC 12.1; `EMPL`, `CFG.EMPL_OCC`): each adult holds one of 700 occupations with Frey and Osborne's probability as their automation risk. In Adverse and Stress, an automation wave (`popAIDisp`: 1.2% a year from year 5, 2.2% from year 15, capped at 10%) times the adult's risk is an extra chance of a permanent job loss. The adult comes back at 0-20% lower pay, and their risk drops to 1/7. Reference has no wave. Hours lost net of returns are small, and there is no output side.
3. **Hours**: the engine models earnings. Hours enter only as each adult's change from their own start (`C.hrs`, wage plus project hours over starting earnings). Hours are not tied to occupation (a stated limit).
4. **Output and prices** (MODEL_SPEC 6.12, `prStep`): there is no aggregate output. The general level rises with λ × U / Y, where U is the year's unmatched new money and Y the year's aggregate cash income. Matched output is ESP reinvestment at face value and the project payout (`PROD.match 'market'`). U = (1 − a) × (BU spent at face value + conversions − matched output). The backed share `a` is an input, and the main row sets a = 1. A year's matched output offsets that year's new money ("matched output permanent").
5. **Project hours** (`PROJ`): project BU converted / the contract pay (the living wage over 2,080 hours, indexed). Hours are added beside wage work (`hours 'side'`).
6. **Backing as a mechanism** (`bkm`, S51): f, ρ, lag, wear, ceiling, and accounting `'growth'` or `'retire'`. At S64's points it reaches 0.2-1.9%.
7. **The v6 readings** (S82): supply limit `sl`, partial wage indexing `wc`, the BU's delay `bl`.
8. **Capital income** (`rt` with business owners and the income wealth pays; the weighted tail `wt`): in the main row.
9. **The private price at the sale** (`sp.vAt: 'sale'`, S90/S92): the corrected model, not yet the default (D34).

## Questions

- **Q1 (displacement).** At each displacement reading, what does displacement do to the four primary outcomes with no programme and with the programme? What share of displacement's cost does the programme offset?
- **Q2 (form and order).** Lost jobs against shorter hours. The most exposed first against evenly.
- **Q3 (output per hour and who gets it).** The forecast gain at 0, low and high. Its pass-through to wages. The share of the dividend the model's households keep. Who gains: by fifth of starting wealth, and the top 1% share of wealth.
- **Q4 (the backing produced).** The backed share the programme's own work produces under each reading. The programme's effects and inflation at that share, under the engine's accounting and the stricter one.
- **Q5 (where the programme falls short).** Displaced adults' outcomes in both runs, by fifth. Every cell where the offset is not significant or is negative.
- **Q6 (free time).** Paid hours per adult. Free time split into secure (household above the cost-of-living line that year) and insecure.
- **Q7 (the design's maintained take-home).** The shorter-hours form with the automated hours' output paid to the workers whose hours fell (programme run only).
- **Q8 (together).** The produced backing with S82's readings: the sourced supply limit with the design's sharing rule, wages at three quarters made up a year later, and the BU a month behind.

## What is built (one switch, row option `oh`; off = identical)

**A. The path.** With S(x) = 3x² − 2x³ for x = t/T in [0, 1] and 1 after: displacement D_t = D × S(t/T). The gain's level is G_t = (1 + u/100)^(T × S(t/T)), held after T. T is 20 or 40.

**B. Displacement (both runs).** Each adult has a needed share of their paid work, h_i,t in [0, 1]. Wage earnings (not project or conversion income) are multiplied by h_i,t after the job-loss and labour-response steps (exact place: Amendment 1).
- `f: 'jobs'` (main). Adults in paid work at the start are ranked once by the order key. `ord: 'risk'` (main) ranks by automation risk, highest first, with ties broken by a draw on a new stream. `ord: 'even'` ranks by the draw alone. The first round(D_t × N_w) adults in the ranking are displaced: h = 0 for the rest of the run. Each counts as a permanent automation job loss in the year it happens (unemployment insurance as the engine pays it), with no return to wage work. Later spells, flows into and out of the labour force, and the Adverse wave do not restore their wage earnings. Hours are not tied to occupation in the engine, so this counts adults, not hours (a limit).
- `f: 'hours'`. h_i,t = 1 − c_i,t, where c_i,t is proportional to the adult's risk (`'risk'`) or equal (`'even'`), capped at 1. The excess above the cap is spread over the others so that the mean cut over adults in paid work at the start equals D_t (water-filling; Amendment 1 gives the algorithm).
- An hour's pay is not changed by displacement itself. The Adverse and Stress wave stays as it is (churn with return), and this path is added on top.

**C. Output per hour (both runs).** The earnings of the hours still worked are multiplied by 1 + pw × (G_t − 1). The no-programme-raise wages the reports keep (`_wNB` and the like) are treated the same way.

**D. The dividend (both runs).** Div_t = Σ_i E⁰_i,t × [(1 − h_i,t) G_t + h_i,t (1 − pw)(G_t − 1)], where E⁰_i,t is the adult's wage earnings that year before B and C. The automated work is still done (output kept), and its output plus the part of the gain not paid as wages goes to owners. A share `own` of Div_t is credited as capital income to adults in proportion to their business and stock holdings (`rt` classes, under the weights of `wt`). The rest goes to owners outside the model's households. `own` is 1, swept at 0.5, until Amendment 1 sets the sourced value.

**E. The design's maintained take-home** (`kp: 'workers'`; programme run only; needs `f: 'hours'`). The part E⁰_i,t (1 − h_i,t) G_t is paid to adult i as wages, not to owners.

**F. The backing produced** (sub-option `bk`; programme run only). The row runs at a = 0, and the matched output is M_t + the ESP reinvestment at face value (the engine's capital goods), replacing the project payout's market valuation:
M_t = m × (H^P_t + H^C_t) × (pay_t / s_L) × G_t + Σ_s K_s × (1 − δ)^(t − s − 1) × y_K × G_t,
- where H^P_t is project hours (the engine's), and H^C_t the hours behind other conversions: their BU at face value over the contract pay (the reading's R7, a modelling assumption);
- pay_t is the contract pay at the year's price level, and s_L the labour share of the nonfarm business sector (BLS; Amendment 1);
- m is the share of programme work that is goods and services sold in shops: a design parameter, 0.25, 0.5 or 1;
- K_s is the ESP reinvestment of year s (year-0 dollars), yielding from the next year at y_K (BEA, essentials industries; Amendment 1; never above 0.32) and wearing at δ = 5% a year (the backing study's main).
- Work output counts in the year it is worked (lag 0, the engine's convention for project output).
- `acct: 'year'` (main) uses the engine's convention: U_t = max(0, payout_t − matched_t). `acct: 'growth'` is the backing study's stricter reading: only the year's added M absorbs new money, with the backing mechanism's carry.
- Reported: the produced backed share by year and over the run.

**G. Reporting** (study option; draws nothing, changes no adult): paid hours per adult over the start; free time per adult (hours a year no longer paid, at 2,080 hours a full year), split into secure and insecure by the household's basket position that year; the number displaced; displaced adults' basket poverty, wealth poverty and months of cover in each run; the dividend as a share of earned income; labour income over labour income plus the dividend; the top 1% share of wealth (weighted); the produced backed share in years 5, 10, 19 and 39; the implied output per remaining hour (G_t / (1 − D_t)).

**H. Draws.** One new stream, one draw per adult at the start (Amendment 1 names its offset). The main stream's eight draws per adult-year are untouched. Both runs read the same ranking (CRN).

**I. Refusals** (at the top of `tbStudy`, before any switch is set): `oh` with ageing (`ag`); `oh` without `rt`; `kp: 'workers'` with `f: 'jobs'`; `bk` outside a programme row.

## Design

Environments: Reference, Adverse and Stress. Horizons: 20 years (primary) and 40. Seeds 1-500, paired. 500 adults. Every row is the v5.9 main row (`r2MainRow`) with `sp.vAt: 'sale'`, the corrected model (S92), in two designs: full coverage (the C2.2 design) and opt-in (the release design). Every row has its own no-programme run. All of B-D act in both runs.

| Block | Rows (each in both designs) | Count |
|---|---|---|
| A. Displacement | D ∈ {0.1, 0.3, 0.5, 0.7} × f ∈ {jobs, hours}, at T 20, u 0.1, pw 0.7, ord risk, own 1; D 0 at u 0.1 (gain only); `oh` off (the main row) | 20 |
| B. Output per hour | at D 0.5 jobs: u 0 and u 1.5; pw 0 and pw 1 (one at a time); D 0 at u 1.5 | 10 |
| C. The slower path | T 40 at D ∈ {0.3, 0.5, 0.7}, jobs | 6 |
| D. Order, owners, take-home | ord even at D 0.5 jobs and hours; own 0.5 at D 0.5 jobs; kp workers at D 0.3 and 0.5 hours | 10 |
| E. Backing produced | D ∈ {0, 0.3, 0.5, 0.7} jobs × u ∈ {0.1, 1.5} × m ∈ {0.25, 0.5, 1}; acct growth at m 1 × u ∈ {0.1, 1.5} × D ∈ {0, 0.5}; a = 0 with no produced output at D ∈ {0, 0.5} (the floor) | 60 |
| F. Together | E at m ∈ {0.5, 1} × u ∈ {0.1, 1.5} × D ∈ {0, 0.5}, with `sl` sourced (the design's rule), `wc` three quarters made up a year later, `bl` one month | 16 |
| G. Check rows | `oh` {D 0, u 0} (must equal the main row) | 2 |

That is 124 rows per environment and horizon, run on GitHub Actions in 20 pieces of 25 seeds each.

## Outcomes

**Primary** (the headline can come only from these; each run's level and the paired programme − no-programme effect):
1. basket poverty (`fgt0PY`);
2. wealth poverty, the yearly average over years 1-19 (`ppovA`), and at the last year (`pov`);
3. median real wealth, weighted (`wtMedE`) and unweighted (`medWealthReal`);
4. savings: the share of adults with at least three months of their cost of living in liquid savings (the security measures; key fixed in Amendment 1).

**Displacement's cost** in a run is that run at D minus the same run at D 0 (same u, pw, own and design), paired by seed: cost_N with no programme, cost_P with the programme. **The offset** = cost_N − cost_P (the interaction). **The offset share** = 1 − cost_P / cost_N, reported only where cost_N's interval excludes zero.

**Secondary:** programme inflation (`endoAnn`); the produced backed share; displaced adults' outcomes; outcomes by fifth of starting wealth; the top 1% share of wealth; the labour share; paid hours and free time (secure and insecure); below 30 days of basic living (`bNAPy`); poverty severity (`fgt2PY`); the 40-year figures; the implied output per remaining hour.

Every gain is confirmed on basket poverty and wealth poverty, not on severity alone.

## Analysis

- Paired differences over seeds, with 95% paired-bootstrap intervals (10,000 replicates, seeds resampled).
- Offsets and interactions with intervals. An interaction or offset is claimed only where its 95% interval excludes zero (research rule 4).
- Holm across the four primary outcomes within each question, environment, horizon and reading, for any statement that the programme "offsets" a cost or that a reading "changes" an effect. Unadjusted intervals are published beside.
- Q4: the produced backed share against the published break-even shares (inflation 5 points a year at 0.86-0.90 of backing, S64; S82's under the v6 readings). Each produced-backing row's own inflation is read directly. No new backing grid.

## Checks (before any table is read; each must pass)

1. Off = identical: the guard test, and full-output diffs with `oh` absent and at its off values.
2. On at zero = identical: `oh` {D 0, u 0} equals the main row in every key, whatever f, ord, pw, own (block G and unit tests).
3. Displacement as set: in each run and year, the displaced count equals round(D_t × N_w) (jobs), and the mean cut equals D_t within 1e-9 (hours).
4. The dividend's identity, each year and in both runs: Σ wage earnings after B-C + Div_t = Σ E⁰ × G_t (with `kp: 'workers'`, the same total with the split moved), within 1e-6 relative.
5. Pairing: the no-programme run of each row is unchanged by E, F and `bk` (they act only in the programme run).
6. Nesting: `bk` with m 0 and y_K 0 equals the a = 0 row at the same D and u, in every key.
7. The money accounts (MODEL_SPEC 11) close with `oh` on, and the dividend enters capital income once.
8. Eight draws per adult-year, unchanged. The new stream takes one draw per adult.
9. Results files match their checksums. The pieces cover seeds 1-500 once, on the pinned engine with a clean checkout. The release start's baseline check passes in the job.

## Decision rules (fixed now)

1. **A failed check:** the defect is fixed and the whole batch is rerun on the new engine commit. Only the rerun is reported.
2. **Offset categories** (per primary outcome, D, form, environment and horizon; after Holm): *offsets fully* when the offset is significant and cost_P's interval includes zero or lies on the favourable side; *offsets in part* when the offset is significant and cost_P is significantly adverse; *does not offset* when the offset's interval includes zero; *worsens* when the offset is significantly negative.
3. **No category for Duke's words.** "Prevents much of the distress" is not a category. The report gives the offset share with its interval, and names every cell in "does not offset" or "worsens" (Q5) in the same section as any favourable statement.
4. **Stress readings:** D 0.5 and 0.7 at T 20 need output per hour to grow faster than any forecast opened (3.5% and 6.2% a year above trend). Wherever they are shown, they are labelled "stress readings, beyond the forecasts". No headline rests on them alone.
5. **The backing produced:** if programme inflation at the produced share exceeds 5 points a year, any headline at full backing carries, in the same paragraph, the produced share and that inflation.
6. **Free time** is always reported split. No sentence calls free time a gain without the insecure part beside it.
7. **Interactions** are claimed only where their intervals exclude zero; separate effects are not summed where they interact.
8. **No tuning:** nothing is changed to reach a figure. The sourced values are fixed in Amendment 1 from opened sources only, before the dry run. A change after the dry run is a dated amendment with its reason and a full rerun.

## Reporting

Every cell above is published, null and unfavourable results included, in compassionism-sim-results (folders `s85-<env>-<years>-<engine 7>`) and in a plain-words report (`dev/reports/s85-output-per-hour.md`), with the findings-page text. Advocacy material may lead with the strongest robust findings; nothing is dropped from the record. Duke's views are attributed to him and kept apart from the results.

## Limits stated in advance

- **No shortfall of spending.** Owners' lower spending out of the dividend is not modelled. This is the cautious side for the design, since the programme's spending would fill such slack.
- **Lower prices from automation** (real gains for every buyer) enter only through the pass-through to wages. In the main reading the rest goes to owners.
- **Lost jobs counts adults, not hours**, because hours are not tied to occupation in the engine. There is one ranking for the run, and new occupations enter only through the net D.
- **What is left out:** the corporate revenue tax (financing; a separate study), health and security raising output per hour (no opened source sizes it), and the Creative Collectives' lending to start-ups (Duke, Nov 17; a later step).
- **The backed share produced depends on m**, which the design does not state. Every Q4 statement names m.
- **No population change:** `oh` is refused with ageing in this study.

## To open before the dry run (Amendment 1)

1. The share of US business and corporate equity held by US households, directly and through funds (Federal Reserve Financial Accounts, B.101 and L.223, or Rosenthal and Burke 2020): `own`.
2. The labour share of the nonfarm business sector (BLS): s_L.
3. Output a year per dollar of fixed capital in the essentials industries (BEA fixed assets and value added by industry): y_K (capped at 0.32).
4. The option and key names, the stream offset, the engine commit, the job file and the dispatch lines.

The outside reading of this preregistration (NVIDIA catalogue) is saved in `audits/` and any change it prompts is an amendment below.

## Amendments
