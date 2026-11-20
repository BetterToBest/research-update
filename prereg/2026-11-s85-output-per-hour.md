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

### Amendment 1 (Nov 19, 2026, after the outside reading, before any build or run)

Reason: the outside reading (`audits/2026-11-19-s85-prereg-reading-nemotron.md`; Nemotron 3 Ultra on the file as committed, `bd7905f`) found three choices that favour the programme without a source, one source used beyond its horizon, and two gaps in the rules. Nothing has been built or run. The sourced values, names, engine commit and job that the text above assigns to Amendment 1 now go in **Amendment 2** (after the build, before the dry run).

1. **The backing produced (section F), main reading.** M_t = m × H^P_t × (pay_t / s_L) + Σ_s K_s × (1 − δ)^(t − s − 1) × y_K.
   - Only project hours count. They are the engine's only observed hours of programme work.
   - There is no forecast gain on programme output (G_t = 1 in M_t). The gains in the sources are economy-wide or for one task.
   - y_K is capital's share of output per dollar of net capital in the essentials industries: (1 − s_L,ess) × value added / net capital stock, BEA by industry, weighted by the basket's shares. The full output per dollar would count the labour the capital needs, which no programme hour supplies.
   - **Labelled readings:** `conv` adds H^C_t, the hours behind participants' own conversions of their expired BU, at face value over the contract pay. It never includes ESP conversions or payroll BU. `gain` multiplies both terms by G_t. `vk` uses the full value added per dollar of capital (capped at 0.32).
   - Block E becomes: D ∈ {0, 0.3, 0.5, 0.7} jobs × gain ∈ {low, high} × m ∈ {0.25, 0.5, 1} (48 rows, main reading). Then `acct: 'growth'` at m 1 × gain ∈ {low, high} × D ∈ {0, 0.5} (8). The floor, a = 0 with nothing produced, at D ∈ {0, 0.5} (4). Then at m ∈ {0.5, 1} × D ∈ {0, 0.5} with the high gain: `conv` (8), `gain` (8), `conv` and `gain` together (8), and `vk` at m 1 only (4). That is 88 rows, so the study has 152 rows per environment and horizon. Block F uses the main reading.
2. **The gain's path (sections A and C).** Goldman Sachs' 1.5 points a year is a boost over ten years, so it is not run for 20 or 40.
   - *Low:* Penn Wharton's published levels. G is 1 at year 0, 1.015 at year 10, 1.03 at year 30 ("nearly 3%") and 1.037 at year 50, linear between. That gives 1.0225 at year 20 and 1.0335 at year 40. Acemoglu's 1.1% at ten years agrees.
   - *High:* a decade of 1.5 points, a level of 1.015^10 = 1.161. It is reached along the S-path at T and held.
   - The rows' "u 0.1" and "u 1.5" read *low* and *high*; "u 0" is no gain.
3. **Multiple comparisons for the headlines.** Statements that the programme offsets displacement's cost use Holm across the four primary outcomes × the eight block-A cells (D 0.1-0.7 × two forms), within each environment and horizon (32 tests). Other blocks keep Holm within each reading. Findings-page headlines come only from block A (displacement) and block F (together). Every other block is reported in full as a reading.
4. **The backing produced: categories.** Each produced-backing row is put in one of three categories by its yearly programme inflation, using the 95% interval:
   - *backs enough:* the interval's upper end is at most 5 points a year;
   - *uncertain:* the interval straddles 5;
   - *does not back enough:* the lower end is above 5.
   M_t is linear in m in the main reading. So the report also gives the m at which the produced share would reach the inflation break-even (linear between the grid's m, never extrapolated): the share of programme work that would have to be goods and services people would otherwise buy (item 8). Every Q4 sentence names m.
5. **The sources, named now.**
   - `own`: the share of US corporate equity held by US households, directly or through funds and retirement accounts, from Rosenthal and Burke (2020). If that cannot be opened, the Federal Reserve's Financial Accounts, L.223, with fund and pension holdings attributed to households. The sourced value is the main reading; 0.5 and 1 are its bounds.
   - s_L: BLS, the labour share of the nonfarm business sector (level, latest full year). s_L,ess and y_K: BEA, compensation and value added by industry, and the net stock of fixed assets by industry, for food services and grocers (retail food), utilities, housing and health care, weighted by the basket's shares.
   - If a source cannot be opened, the value stays a labelled design parameter at the bounds above, and the report says so.
6. **Clarifications.**
   - The reading note's 1.8%, 3.5% and 6.2% a year are the floor with no added gain. Each row reports its own implied output per remaining hour, with its gain.
   - The IMF's "negatively affected" covers lower pay and fewer hours as well as lost jobs, so it anchors the 30% reading only loosely.
   - New diagnostic, reported per row: aggregate cash income in the price rule, with and without displacement, and the part of it that is the dividend paid to the model's households (the part kept outside them is not in it).
7. **Further limits stated in advance.**
   - Pencavel's sample (British munitions workers in the First World War) limits how far "no per-hour gain below 49 hours" carries. The design's maintained take-home reading is the counterpoint.
   - The dividend raises no investment, so there is no capital deepening in either run (against both runs, most at 40 years).
   - One pass-through for every wage level. Production workers' 0.4-0.7 suggests less for the low-paid, so the main reading may overstate their gain.
   - Contract pay values a project hour below many workers' own wage, the cautious side for the backing.
8. **What m counts** (Nov 19, 2026, Duke's question "What about services?"; a clarification before any build). "Goods and services sold in shops" in section F was too narrow a phrase. m is the share of programme work whose output people or businesses would otherwise **buy**, from a shop or from a service provider. That covers goods and **services alike**: food, housing and repairs, health and personal care, childcare and elder care, transport, utilities, education and training, and the services of the essential providers (ESPs and PTFs). It also counts work that **replaces** a purchase: a collective's free childcare counts if a household no longer pays for childcare, because that lowers the money chasing paid childcare. It does not count output that replaces no purchase, such as unsold art or a community event, however valuable. The quantity-theory price rule absorbs new money only with output that buyers would otherwise pay for. The value of the rest is real, but it is reported apart (the design's cultural value), not as backing. The grid's values (0.25, 0.5, 1) are unchanged. The report names the categories wherever it gives m.

### Amendment 2 (Nov 19, 2026, after the build, before the dry run)

Reason: the build (compassionism-simulation v5.9.21, branch `claude/s85-oh-build`) and the sources Amendment 1 names. Nothing has been run beyond unit tests and a one-seed smoke test of 200 adults (which reads no outcome against any target; its figures are not results). Decisions in compassionism-simulation `dev/DECISIONS.md`, "S85 part 2"; specification MODEL_SPEC section 17.

1. **Sourced values** (`sources/s85_values.py`; extracts in `sources/s85_values/`; full downloads' checksums in the script):
   - `own` = **0.541**: Rosenthal and Burke (2020), appendix Table 4, 2019 (PDF supplied by Duke): life insurance separate accounts 1,065 + defined-benefit plans 3,102 + defined-contribution plans 3,220 + IRAs 4,690 + taxable accounts 9,498 = 21,575 of 39,886 ($ billions). Not households: foreigners 15,988, government 368, nonprofits 1,955. The model's adults are 25 to 64, so part of this share belongs to older households outside the model (a limit; it leans toward the model's households in both runs). Bounds 0.5 and 1 are both run (block D gains `own` 1; Amendment 1 item 5 named both bounds).
   - s_L = **0.542**: BLS, labour productivity and related measures for major sectors (released Nov 5, 2026), nonfarm business, all workers, labour share, 2025 (54.5 in 2024; the quarterly release's 53.0 for 2026 Q3 is not a full year). BLS refuses direct requests; the file came through the fetch tool.
   - yK = **0.164**: BEA, value added and compensation by industry (TVA113-A) and net capital stock (Fixed Assets 3.1ESI; Table 1.1 for housing's residential stock), 2024. Food (food and beverage stores, food services): capital income per dollar of capital 0.409; housing with utilities 0.083; medical (ambulatory, hospitals, nursing) 0.165; weighted by the basket (0.207, 0.634, 0.159). The 0.32 cap applies to the result and does not bind (capping each sector first would give 0.145; not the preregistered rule). `vk` = 0.421, capped at **0.32**.
2. **The forecasts opened in the original**, not as quoted: McKinsey (2023), Exhibit 15, United States, 2022-40 a year: early adoption 3.8 (generative AI 0.7), late 1.0 (0.3), assuming automated hours re-employed at today's output per hour; Goldman Sachs (2023), the article Duke pasted: 1.5 points a year over ten years; McKinsey's summary of the report: 7% of US employment substituted, scenarios 0.3 to 3.0. Neither changes a reading: the high reading stays a decade of 1.5 points, the low Penn Wharton's levels. The four-day week pilot (Autonomy 2023: hours 38 to 34 a week, revenue +1.4%, self-selected companies, no comparison group) is context for the maintained take-home reading only.
3. **Names.** Row option `oh: {D, T, f, ord, g, pw, own, kp, bk}`: `g` is the gain, `'none'`, `'low'` or `'high'` (the text's u 0, 0.1 and 1.5); `bk: {m, acct, conv, gain, vk, y0}`, where `y0` drops the capital term. The floor rows are `bk {m: 0, y0: true}`. New stream: seed + 850085, one draw per adult at the start. Reporting keys `OH_KEYS` (MODEL_SPEC 17).
4. **Exact places** (section B's "Amendment 1"): wage earnings are scaled right after the labour response (and the participation margin), before project hours; adults outside the labour force that year are skipped (they earn no wage). The adults in paid work at the start are those not outside the labour force after the start's labour-force stock is drawn, the same in both runs.
5. **A displaced adult (lost jobs).** E0 is what they would have earned that year: their job-loss spells and labour response still run, so the main and job-loss streams draw as before. Their wages are 0. Unemployment insurance is paid once, in the year of displacement, if the year's job-loss draw for recipiency is below the rate (26 weeks at the replacement rate), and not from later spells. Employer health cover is lost.
6. **The dividend's payment.** Paid the next year, as the income wealth pays (so the spending rule and the money accounts treat it as other capital income), to adults in proportion to their share and business holdings (classes eq and bus) at the end of the year, weighted by the tail's weights, deflated to the year's price level and paid at the next year's. The last year's dividend falls after the run and is not paid; `ohPaid` reports the share paid.
7. **Check 6 corrected.** "bk with m 0 and y_K 0 equals the a = 0 row in every key" cannot hold: the a = 0 row counts the project payout at its market valuation as matched output, and bk replaces that valuation. Check 6 is now: the floor (`bk {m: 0, y0: true}`) produces nothing (`ohA` 0) and its programme inflation is at least the a = 0 row's (unit test). The one-seed unit test gives, at D 0.5 with the low gain: inflation 42% a year at a = 0, 62% at the floor, 53% at m 1.
8. **The produced share's denominator.** `ohA` = 1 − Σ U / Σ base over the run, where base is the payout less the engine's other matched output (the reinvestment at face value and capital charges). The published backing grid's `a` is defined on the payout less all matched output, project payout included, so the two are not the same scale; Q4 reads each row's own inflation, as preregistered.
9. **`conv` is empty in this row.** Every expired BU goes to the project pool in the main row (`PROJ.share` 1), so there are no participants' own conversions outside projects: `conv` rows equal their counterparts (checked on two seeds: no key differs). They are run as preregistered and reported as such.
10. **The price rule's income** (aggregate cash income: wages, conversions, Social Security) does not include capital income, so the dividend paid to households is not in it (`ohYdv` reports what share it would add). Displacement lowers this income in both runs. This is the engine's existing rule, stated here because it bears on inflation per unmatched dollar.
11. **The supply path** for the essentials prices (the no-programme run, `fx.sp`) runs with `oh`'s both-run parts, as the preregistration's "all of B-D act in both runs" requires.
12. **Rows.** Job `runner/jobs/s85.js` in compassionism-sim-results: 77 programme rows per design (A 10, B 5, C 3, D 6, E 44, F 8, G 1) and 25 no-programme runs shared by the rows with the same both-run settings: **179 rows per environment and horizon**. Block D has one row more than Amendment 1's count (`own` 1). Block F's wages read `wIdx` 0.75 with `wc` 1 and the BU's delay `bl` 0.125 (a month), as S82's central readings; the supply limit `sl {rd: 'sourced', sh: 'bu'}`.
13. **The dry run** (Nov 19, 2026; Reference, seeds 1-2, both horizons, `--procs=4`, the build's head `82f2391` in a clean worktree): check 2 holds (the zero rows equal the main row in every key, both designs, and their no-programme run equals the plain one); checks 3 and 4 pass in every row (displacement as set; wages plus the dividend equal every E0 times G within 1e-6); no non-finite value; the `conv` rows equal their counterparts (8 of 8). Checks 1 and 5-8 passed in the build (guard test identical; unit tests for pairing, the floor, the money accounts and the draws). Timing: 49.5 s (20 years) and 87.2 s (40 years) for two seeds of all 179 rows on four processes, about 86 and 156 row-seconds a seed; the whole study is about 100 core-hours on Actions (free), under `prereg/RUNNING.md`'s 1,000 core-hour mark. No outcome was read against any target; the dry run's figures are not results.
14. **Engine commit:** compassionism-simulation `503fa483f9711900054842e75fc0edc01eba8dc9` (v5.9.21, the merge of PR 167; its tree equals the dry run's `82f2391`). **Job:** compassionism-sim-results `runner/jobs/s85.js` (PR 61, merged `0a7c264`). **Dispatch** (Nov 19, 2026), the `run-study` workflow, six runs, each 20 shards of 25 seeds, seeds 1-500: study `s85-<env>-<years>`, engine as above, job `s85.js`, job_args `--env=<env> --years=<years> --procs=4`, for env ref, adv, str and years 20, 40. Results land in `s85-<env>-<years>-503fa48/` with `run.txt`, `SHA256SUMS` and `DONE`.

### Amendment 3 (Nov 20, 2026, after the batch finished, before any table is read)

Reason: the six result folders are complete (runs 155-160, every shard `DONE`). Writing the analysis found one outcome the batch does not hold and several choices the text leaves open. Each is fixed here before any outcome is read; where the text is silent the cautious reading is taken. No figure of the batch has been looked at beyond the folders' file lists and key names.

1. **Primary outcome 4 (savings).** The text names "the share of adults with at least three months of their cost of living in liquid savings (the security measures)" and leaves its key to Amendment 1, which did not fix it. That measure is the security study's `secM3A` (adult-years whose liquid savings, 20% of positive savings, cover under three months of need; the security addendum's Q17), which the engine adds only with the row option `o.sec` (reporting only, no draw). The job did not switch it on, so the batch does not hold it.
   - **Supplementary run:** blocks A and F (the only blocks headlines may come from, Amendment 1 item 3) and the no-programme runs they pair with, rerun with `o.sec` on and nothing else changed, same engine commit, seeds 1-500, all six environments and horizons (folders `s85sec-<env>-<years>-503fa48`). Job: `runner/jobs/s85.js --sec` (the flag adds `o.sec` and keeps only those rows; without it the job is unchanged). **Check 10:** every key the batch holds is identical in the supplement, row by row and seed by seed (the measure is reporting only). Primary 4 is read on `secM3A` (lower is favourable) from the supplement once check 10 passes.
   - Until then, and for blocks B-E (not rerun), the fourth slot is read on the batch's nearest stored measure, adult-years below 30 days of basic living (`bNAPy`, design-neutral; liquid savings at the same 20% share plus a month's wage share), the measure the supply and private-price studies read as primary. Every statement says which of the two it uses.
2. **Holm for the block-A headlines.** The four primary outcomes are read on six measures (wealth poverty yearly and at the last year; median real wealth weighted and unweighted). Holm runs over the six × the eight block-A cells = **48 tests** within each environment, horizon and design (the two designs are separate rows; Amendment 1's 32 is per design). This is the cautious side of 32, as the supply study's tables did. Where the savings measure is `secM3A`, it takes `bNAPy`'s place in the 48. Significance for Holm: two-sided paired t over the 500 seeds. Unadjusted 95% intervals are printed beside.
3. **Signs.** A cost is signed so that positive is harm: for the poverty measures, the run at D minus the run at D 0; for median wealth, the run at D 0 minus the run at D. The offset = cost_N − cost_P, positive when the programme takes away part of the harm. Decision rule 2's categories read the offset's Holm-adjusted significance and its sign, and cost_P's unadjusted 95% interval. The offset share = 1 − mean cost_P / mean cost_N, with the bootstrap interval of that ratio; it is given only where cost_N's interval lies wholly on the harmful side (where displacement significantly improves an outcome with no programme, no share is given and the table says so).
4. **The D 0 reference of each row.** Block A: `A.<design>.gain.D0` (D 0, low gain, same design). Block C (T 40): the same row, since the low gain's path does not depend on T (MODEL_SPEC 17) and with D 0 nothing is displaced. Block D's even order: the same row (order acts only on whom displacement reaches). Block B's no-gain row: block G's zero row (D 0, no gain); its high-gain row: `B.<design>.ghigh.D0`. Block B's pass-through rows and block D's owner-share rows have no D 0 row at their own setting, so only their effects and the change against `A.<design>.jobs.D0.5` are read (no cost or offset). Block D's take-home rows: the change against the shorter-hours row at the same D (the same no-programme run).
5. **Intervals.** Paired bootstrap, 10,000 replicates, seeds resampled, one resample shared by every table (generator `numpy.random.default_rng(20261120)`), percentile intervals.
6. **The backing produced (Q4).** Programme inflation is the programme run's `endoAnn` in points a year; the category (Amendment 1 item 4) reads its 95% interval. The break-even m: the mean inflation at m 0.25, 0.5 and 1, interpolated linearly to 5 points a year, with the bootstrap interval of the crossing; "at or below 0.25" or "above 1" where the grid does not reach it (never extrapolated). The produced share is `ohA` over the run (Amendment 2 item 8's denominator), with `ohA5`, `ohA10`, `ohA19` and `ohA39`.
7. **Who gains (Q3).** By fifth of starting wealth: mean real wealth at the last year, weighted (`rtE` + `rtV` + `rtS` for fifths 1-5). The top 1% share of wealth: `wtT1E`. The labour share: `ohLab`. The dividend against wages: `ohDiv`; the share paid to the model's households: `ohPaid`.
8. **Displaced adults (Q5).** At the last year, the displaced (lost jobs: no paid work; shorter hours: half or more of their hours cut) and the rest, in each run: basket poverty (`ohDB`, `ohNB`), wealth poverty (`ohDW`, `ohNW`), median months of cover on all wealth (`ohDM`, `ohNM`). These are not stored by fifth, so Q5's "by fifth" is reported for all adults only (a limit).
9. **The checks as rebuilt** (the dry run's scripts were not kept): check 9 (SHA256SUMS, 20 shards covering seeds 1-500 once, the pinned engine and a clean checkout in every shard's manifest, the baseline check); check 1 (the main rows with `oh` off, `A.<design>.off` and their no-programme run, equal the published main rows with the private price at the sale, `s90-sale-<env>-<years>-b8ccd8d`, in every key and seed, if the engine's changes between the two commits leave the main row as it was; otherwise the keys that moved are printed and the guard test of the build stands as check 1); check 2 (`G.<design>.zero` equals `A.<design>.off` in every key but `oh`'s own, and its no-programme run equals the plain one); check 3 (`ohChk` 0 for lost jobs and at most 1e-9 for shorter hours, every row and seed); check 4 (`ohId` at most 1e-6); check 5 (the job's pairing check, `s85.js --check`, at the job's commit); check 6 (the floor rows produce nothing, `ohA` 0); check 7 (the money accounts' residual `mfChk` as the engine reports it); check 8 (the build's unit test; nothing in the batch measures draws); the `conv` rows equal their counterparts in every key and seed; every stored value is finite.
10. **The supplement's job and dispatch** (Nov 20, 2026). compassionism-sim-results PR 62 (merged `f260054`): `s85.js --sec` keeps the 36 programme rows of blocks A and F and the 12 no-programme runs they pair with (48 rows) and sets `o.sec` on each; without the flag the job is unchanged (`--check` passes with and without it, 179 and 48 rows). Smoke test on the pinned engine: seed 1 of all 48 rows at Reference, 20 years, equals the batch's shard in every key the batch holds (0 values differ) and adds the 420 security keys; the one value printed to confirm the key exists (seed 1, the main row) was not read against anything. Dispatched: `run-study`, engine `503fa48…`, job `s85.js`, job_args `--env=<env> --years=<years> --procs=4 --sec`, seeds 1-500 in 20 shards, study `s85sec-<env>-<years>`, runs 161-166 in the order ref-20, adv-20, str-20, ref-40, adv-40, str-40.
11. **Check 7 as read** (Nov 20, 2026, from the checks, before any outcome table). `mfChk` is the Source-financing identity |U − (payout − matched)|, which is 0 only on a Source-financed row. The main rows are financed by the flat contribution, so it is not 0 there, in this batch or in the published main rows the batch's main rows equal in every key (check 1). Item 9's reading of check 7 on `mfChk` is therefore withdrawn: check 7 rests on the build's unit test for the money accounts, and `mfChk` is printed as an inspection. Every other check passed in all six folders.

### Amendment 4 (Nov 20, 2026, after the supplement was read, before the trace is computed)

Reason: the report's explanation of why the opt-in design, with lost jobs, makes displacement's rise in basket poverty larger than the no-programme run does rests on an inspection of one environment (Adverse, seeds 1-100) that was not preregistered, and the full trace was left for part 4. The trace is fixed here before any of its figures is computed. **What was looked at before this amendment:** (a) the report's inspection just named; (b) seeds 1-25 of Adverse at 20 years: the means of the group keys, the contribution rate and the participation keys at D 0 and D 0.5 for the two designs' lost-jobs rows and their no-programme partners, to learn what the keys hold; and a check, on the same 25 seeds, that the stored group figures add up to the totals exactly (largest difference 0.0) and that the groups' sizes are the same in every run. No interval, no other cell and no 500-seed figure of the trace was read.

1. **Question.** Why does the opt-in programme, with lost jobs, raise basket poverty more under displacement than the no-programme run does (decision rule 2's "worsens": 15 to 17 cells at 20 years)? Which adults carry the difference; is it more adults below the line or adults further below it; and what do the contribution rate and the share enrolled do?
2. **Data: keys the batch already stores; no new run.** `fgt0PY` and `fgt2PY` (all adults; basket poverty and its severity, adult-years); `gPartF0`, `gNonF0`, `gPartF2`, `gNonF2`, `gPartK`, `gNonK` (the two groups of latent adults, the same adults in every design and in the no-programme run: those who would take part, "take-part type", and those who would not); `tauMean`, `tauLast` (the flat contribution rate, run mean and last year); `jnP5`, `jnP10`, `jnP19`, `jnJoin`, `jnLeave` (adults enrolled in years 5, 10 and 19; joins and leaves over the run); `ohDN`, `ohNN`, `ohDB`, `ohNB` (the last year's displaced adults and the rest of those in paid work at the start: counts and share below the basket).
3. **Cells.** Block A, both designs, lost jobs and shorter hours, D 0.1 to 0.7, the three environments, 20 and 40 years. The question's cells are the opt-in design with lost jobs; the other three combinations are contrasts. D 0 references as in Amendment 3 item 4.
4. **Decomposition.** With s_g = k_g/(k_Part + k_Non) (the same in every run of a seed), the all-adult figure is the s-weighted sum of the two groups' figures, exactly. For each of `fgt0PY` and `fgt2PY`: the harm-signed change in group g's level from D 0 to D in the programme run (Δ^P_g) and in the no-programme run (Δ^N_g); the worsening W = cost_P − cost_N (= minus the offset, Amendment 3 item 3); and W = W_Part + W_Non with W_g = s_g (Δ^P_g − Δ^N_g). Means over the 500 seeds with the paired bootstrap of Amendment 3 item 5 (10,000 replicates, one resample shared by every table, generator `numpy.random.default_rng(20261120)`); no p-values and no Holm correction, since this splits a difference already tested and is read with its interval. A group's share of W (W_g / W) is given only where W's interval lies wholly above zero.
5. **Readings fixed in advance, per cell** (each reads the 95% interval):
   - *More adults below the line, not further below:* W_Part (headcount) wholly above zero and W2_Part (severity) not wholly above zero. *Further below as well:* both wholly above zero.
   - *A burden on those who would not take part:* W_Non wholly above zero. The stored keys do not separate the contribution from programme inflation; the report says so.
   - *The contribution rate:* `tauLast` and `tauMean` at D minus at D 0, programme run.
   - *Enrolment:* `jnP19` at D minus at D 0, and `jnJoin`, `jnLeave`, programme run: whether the enrolled share falls under displacement.
   - *The displaced adults:* `ohDB` and `ohNB` in each run and the programme's effect on each (programme minus no programme).
   - Where a cell's readings do not point to one channel, the report says so.
6. **What the trace does not do.** It is a decomposition, not a test by intervention: nothing is switched off (a run with the contribution held at its D 0 rate needs an engine option that does not exist, and is listed as an open follow-up, not built). The two groups are latent adults, not those enrolled in a given year (`jnP19` gives the enrolled share). It reads the headline block only.
7. **Output.** compassionism-sim-results `s85-trace-503fa48` (tables, summary JSON, `analysis.txt`, `SHA256SUMS`), made by `dev/tools/s85_trace.py` in compassionism-simulation; a short subsection of the report's section 4. No figure of the earlier tables changes.
