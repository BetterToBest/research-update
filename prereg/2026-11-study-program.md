# Preregistration: the study programme (scale, synergy, horizon, participation, octave raise, yardstick)

Committed Oct 30, 2026 by S32, before any run of S35-S38. Engine: BetterToBest/compassionism-simulation at commit `d33de07ee7b489b1c6f24d8d941272386d7c980b` (main, after S34: release v5.6.0 plus the CPS earnings reading `CFG.CPS_EARN`, off by default). The engine changes listed under "Before the first run" land behind switches (off = bit-identical, guard test) and are recorded below as dated amendments naming the new commit; the S47 design freeze pins the commit the full batch runs on.

## Why
The Research Hub v2 will state what the simulation finds about Compassionism. Each finding must come from a study whose questions, rows, outcomes and decision rules were fixed before any result was seen (research rule 1). This file fixes them for the whole programme: the pilots (S35), the full batch (S48) and the reports that read it (S36 synergy, S5 participation, S38 community layer, S7 release).

## Plain-words summary
- Six questions: does population size change the results (Q1)? Do the five parts of the design (CCO, PTF, PTH, SZH, CIP) do more together than apart (Q2)? What changes between 20 and 40 years, and by the age at which people join (Q3)? How do results change with participation from 10% to 90% (Q4)? What does the octave wage raise do (Q5)? How do results change when the simulated people earn what working US adults earn (Q6)?
- **Headline yardstick, fixed now:** the main results use the no-programme run with the earnings of US adults aged 25-64 with earnings (CPS ASEC 2026; the engine's wage reading `lt: {s: 'all', m: 'all'}`). The released wage scale is run beside it everywhere and shown on every page. Reason below (Q6).
- **Headline setting, fixed now:** the octave wage raise off (the design's main reading since d46), with every result also shown with it on.
- Five primary outcomes: share below 30 days of basic living (BLEI), share below the cost of living, share with too little wealth, programme cost per adult, cumulative inflation. Every gain must also show on the cost-of-living and wealth measures (guardrail 6).
- Every row runs in the three environments (Reference, Adverse, Stress) on seeds 1-500, paired. All of it fits on GitHub Actions (about 460 core-hours; about 6 hours on 20 free runners).
- Every cell is published, including null and unfavourable results.

## Checks made before writing this (no outcome value was looked at)
`prereg/checks/s32_feasibility.js` (run in an engine checkout at d33de07; 60 adults, seeds 1-2) prints only whether a setting runs and which settings give bit-identical results. Its output, which this design rests on:
1. All 32 combinations of the five parts run in all three environments and give 32 distinct results; all five on is exactly the release row.
2. **All five off equals the no-programme run** on every outcome (only two to six diagnostic keys that are not outcomes differ: `pjRc`, `spSw`, `pdC5`, `pdC10`, `pdC19`, `pdMem19`). So the empty cell of the factorial is the no-programme run, and every cell's effect is measured from it.
3. PTF, PTH and CIP change people's money without CCO. **SZH alone changes only the design's own BLEI reading** (and measures built from it), not anyone's income, costs or wealth: the design's BLEI formula has an SZH term. So BLEI claims about the parts are made on the design-neutral BLEI (below).
4. Without CCO the octave wage raise still acts, because every adult receives a starting octave from the preset. Octaves are part of the CCO, so in the cells without CCO the raise is always off; with it off, starting octaves change nothing in those cells (checked).
5. Participation at 10% runs; it changes the no-programme run only in its participant / non-participant group reporting (the group is defined by the same participation draw), not in any all-adult outcome.
6. 40 years with ageing and the CPS earnings reading run for both rows.

## Questions
- **Q1 Scale.** Do the headline results (each primary outcome of the release row against no programme, and the no-programme levels) change with population size: 500, 2,000, 10,000 and 50,000 adults? Answer: for each size, the difference from 500 adults, and whether it passes the scale rule (Decision rules). Also: is the synergy table (Q2) at 10,000 adults the same as at 500, and the participation curve (Q4)?
- **Q2 Synergy.** For each primary outcome, how much of the full design's effect does each part contribute (Shapley shares), and do the parts interact (interaction contrasts)? Answer: the Shapley table and the interaction table with 95% intervals, and which interactions pass the synergy rule.
- **Q3 Horizon.** How do the effects at year 40 compare with year 20, and how do outcomes differ by the age at which an adult joins? Answer: year-20 and year-40 effects and their difference; outcomes by age group at joining.
- **Q4 Participation.** How do the effects change as participation goes from 10% to 90%? Answer: the curve with intervals (this feeds S5's one participation figure), and whether it departs from a straight line.
- **Q5 Octave raise.** For every row with CCO, what changes when the octave wage raise is on? Answer: every result in both settings, and the difference (ledger watch rule: the raise is the model's stand-in, not the design).
- **Q6 Yardstick.** How do the effects change between the two no-programme yardsticks? Answer: every result under both, and a statement wherever a decision differs.

## Design

### Rows
Every row is built as the study runner's reference job builds the release pair (`runner/jobs/release-pair.js` in compassionism-sim-results): `relMainCfgs(tbPresets(P))` with `sc: SPEND_SOURCED` and today's safety net with SNAP's work rule and the slope reading (`sn: {abawd: true, slope: true}`), run with `applyNR6()`, `tbSetG(TB_PROFILE_G)` and study options `{fin: 'tax', aT: 0, a: 0, X: 0, sc: SPEND_SOURCED}` plus `REL_V52_STUDY`. `P` is the environment's preset with `nAgents` and `years` set. Element 0 is the no-programme row (**none**), element 1 the release row (**main**). Each switch below changes only what it names:

| Switch | Setting | How it is set |
|---|---|---|
| Architecture cell | any of CCO, PTF, PTH, SZH, CIP on or off | on the main row: `c.p.ccoOn`, `c.p.ptf`, `c.p.pth`, `c.p.szh`, `c.p.cip`. The empty cell is the none row (check 2). Shares, coherence and demand settings stay at the environment's values. |
| Yardstick | released wages / **CPS earnings (headline)** | CPS: `c.lt = {s: 'all', m: 'all'}` on every row of the run, the none row included. Released: no `lt`. |
| Octave raise | **off (headline)** / on | off: `c.pw = {octaveWage: true}` (as released). On: `c.pw` removed (n1Row's `raise: true`). Cells without CCO: always off (check 4). |
| Participation | 10%, 20%, ..., 90% | `P.partRate` set before `tbPresets(P)`, so both rows are built from it. It is the share in the programme at the start; open enrolment (`jn`, as released) then lets adults join and leave, and the realised shares (`jnP5`, `jnP10`, `jnP19`) are reported beside each result. |
| Ageing | off (as released) / on | on: `c.ag = {}` (AGE_DEFAULTS: retired participants keep the BU, the average Social Security benefit, flat earnings by age) on both rows. |
| Debt reading | off (as released) / on | a new switch (Before the first run, item 3). |
| Population | 500 (release), 2,000, 10,000, 50,000 adults | `P.nAgents`. |
| Horizon | 20 (release), 40 years | `P.years`. |

### Studies
Seeds 1-500 in every study, paired across rows (common random numbers). All three environments: Reference (`FULL_INTEGRATION`), Adverse (`ADVERSE_REFERENCE`) and Stress (`STRESS_TEST`; it keeps its own weaker settings, including its 40% participation, except where Q4 sets participation). Rows are counted per environment.

| Study | Questions | Rows | Adults | Years | Ageing | Rows per environment | Core-hours |
|---|---|---|---|---|---|---|---|
| A scale | Q1, Q5, Q6 | main and none; both yardsticks; main with the raise off and on | 500, 2,000, 10,000, 50,000 | 20 and 40 | off | 6 | 323 |
| B synergy | Q2, Q5, Q6 | all 31 non-empty cells and none; both yardsticks; the 16 cells with CCO with the raise off and on | 500 | 20 and 40 | off | 96 | 39 |
| B10 synergy at scale | Q1, Q2 | all 31 non-empty cells and none; CPS yardstick; raise off | 10,000 | 20 | off | 32 | 61 |
| C ageing | Q3, Q5, Q6 | main and none; both yardsticks; raise off and on | 500 | 20 and 40 | on | 6 | 2.5 |
| D participation | Q4, Q5, Q6 | main at 10%, 20%, ..., 90%, and none; both yardsticks; raise off and on | 500 | 20 and 40 | off | 38 | 16 |
| D10 participation at scale | Q1, Q4 | main at 10%, ..., 90%, and none; CPS yardstick; raise off | 10,000 | 20 | off | 10 | 19 |
| F debt reading | I15, Q6, Q5 | main and none with the debt reading on; both yardsticks; raise off and on | 500 | 20 and 40 | off | 6 | 2.5 |

Core-hours from the S33 benchmarks (`prereg/RUNNING.md` section 5: a row costs half the main-plus-none pair; 40 years 1.9 times 20 years at 500 adults, 2.45 at 10,000, 2.5 assumed at 2,000 and 50,000). Total about 463 core-hours, about 6 hours on 20 runners: no study needs Runpod (RUNNING.md's threshold is about 1,000). S35 times a real row of each kind before S47 fixes the dispatch.

Why 500 seeds at every size (Q1): the Monte Carlo error of a mean over seeds falls as the population grows, so 500 seeds at every size gives every size an error no larger than the 500-adult one. Fewer seeds at the larger sizes would save little (the whole of study A costs about 4 hours on Actions), and part of the between-seed variation (recession and automation paths in Adverse and Stress) does not shrink with population.

Why ageing is a separate study (Q3): the release runs without ageing (nobody ages; children never grow up), and its 40-year panel does too. Studies A, B and D keep that for continuity with the release. Study C turns ageing on so that 40 years means 40 years of lives, and so that age at joining exists.

### Where it runs
GitHub Actions, the `run-study` workflow of compassionism-sim-results, as `prereg/RUNNING.md` describes. The job script `runner/jobs/program.js` (written before the first pilot, Before the first run, item 1) takes `--study=A|B|B10|C|D|D10|F` plus the runner's `--env`, `--seeds`, `--out` and `--procs`, and builds exactly the rows of the table above. Results folders: pilots `pilot-<study>-<engine, 7 characters>` (S35), the full batch `prog-<study>-<engine, 7 characters>` (S48), each with `run.txt`, `SHA256SUMS` and `DONE`. Shards are sized so no shard runs over 6 hours (one 50,000-adult, 40-year row takes about 80 seconds a seed).

### Before the first run (S35 does these first; each lands by pull request)
1. `runner/jobs/program.js` in compassionism-sim-results, with a check that its row lists have the counts in the Studies table (96 for B, 38 for D, and so on) and that its main and none rows equal `release-pair.js`'s byte for byte.
2. Reporting only (no random draw, no state the model reads; guard test identical): (a) the price level at each year to year 40 (the existing `pLev10` and `pLev20` give year 10 and the last year only), so that cumulative inflation at year 20 can be read from a 40-year run; (b) outcomes by age at joining (Outcomes, secondary); (c) the share of families (households) with net worth below zero at year 20 and year 40, as a per-seed measure (today only `dev/tools/baseline_realism.js` computes it, from the household trace).
3. The debt reading (study F), behind a switch, off = bit-identical: in a year when the graded spending rule (`budget × (income / budget)^0.557`, S34 report section 5) would have a household spend more than its cash income, the excess is paid only from positive savings; once savings are used up, the household spends its income and does not borrow for ordinary spending. Its one parameter, the borrowing limit for ordinary spending, is 0. The engine's existing debt floor still applies to everything else (job loss, shocks). This is the S34 report's first option with a limit of zero, chosen because it adds no free constant. It is a sensitivity reading: it does not replace the released spending rule in any headline (it was chosen after seeing the drift). If building it needs a choice not written here, that choice is a dated amendment before any run of study F.

## Outcomes
All figures are means over the 500 seeds of each seed's figure, with the 2.5th-97.5th percentile range over seeds. Dollars are year-0 dollars (the model's 2025 dollars), deflated by the model's own price level as released. Shares are % of adult-years over the run, or % of adults in a stated year. "Year 20" is the run's year index 19, "year 40" index 39.

**Primary (the headline can only come from these):**
1. **Below 30 days of basic living.** Share of adult-years whose BLEI is below 30 days, over the run. Read on two definitions, both reported: the design's own BLEI (`bOAPy`, the released headline) and the design-neutral BLEI (`bNAPy`: Baseline rules plus one month of the design's regular support). Claims are made on the design-neutral reading (check 3: the design's own formula credits SZH with days no one can spend); the design's own reading is shown beside it. Also the year-20 and year-40 shares (path keys `pbO_19`, `pbO_39`; design-neutral `bNA20` at the last year).
2. **Below the cost of living.** Share of adult-years with income below the MIT living-wage budget for their household (`fgt0PY`), over the run; and the year-20 and year-40 shares (`pf0_19`, `pf0_39`).
3. **Too little wealth.** Share of adults with wealth below $25,000 in year-0 prices at year 20 and at year 40 (`ppov_19`, `ppov_39`; `pov` at the last year).
4. **Programme cost per adult.** Year-0 dollars per adult-year (`cost`), with what the Source pays out (`srcPay`) and keeps in conversion tax (`srcTax`) beside it. 0 for the none row.
5. **Cumulative inflation.** The model's price level at year 20 and year 40 over year 0, minus 1, in % (`pLev20` at the last year; the year-20 value of a 40-year run from item 2a above); the yearly rate (`endoAnn`) beside it.

**Secondary (published, never the headline):** Gini of disposable income (`giniD`) and of wealth with debts kept (`eGiniW`); children below the cost of living (`hhCostKidPY`); hours of work relative to each adult's own hours with no programme, in % (`hrs × 100`); people below the official poverty line (`hhFplPY`); poverty severity (FGT2 × 100, `fgt2PY`); families in debt at years 20 and 40 (item 2c); participants' and non-participants' outcomes (the `gPart*`, `gNon*` groups); realised participation (`jnP5`, `jnP10`, `jnP19`); in study C, the primary outcomes 1-3 by age at joining, in four groups (joined at 25-34, 35-49, 50-66, never joined), each over the adult's years from joining (from year 0 for those never joining), against the same adults in the paired no-programme run; in study F, families in debt at years 20 and 40 beside the SCF 2025 figure (9.3%), as a check of the yardstick, not a target.

Effects are always the row minus the none row of the same environment, size, horizon, ageing, yardstick and seed. For outcomes 1-3, a reduction is written as a positive number of percentage points.

## Analysis
- **Estimates and intervals.** Per-seed paired differences, averaged over seeds. 95% intervals by paired bootstrap over seeds: 10,000 replicates, percentile intervals, one resample of seed indices shared by every row of a study (so differences between rows are paired too), bootstrap random seed 20261101. Comparisons between population sizes (Q1) are between independent runs: each size is resampled separately and the difference's interval is taken from the two bootstraps.
- **Shapley shares (Q2).** The players are the five parts: CCO, PTF, PTH, SZH, CIP. For a set S of parts, v(S) is the mean effect of the cell with exactly the parts in S on, against none (v of the empty set is 0, check 2). Each part's Shapley value is φᵢ = Σ over S not containing i of |S|! (4 − |S|)! / 5! × [v(S ∪ {i}) − v(S)]; the five values add up to v(all five). Its share is φᵢ / v(all five), reported only where v(all five)'s interval excludes zero (otherwise the values alone). Computed separately for each outcome, environment, horizon, yardstick and raise setting (the raise is a setting of the CCO, not a sixth part).
- **Interaction contrasts (Q2).** (a) *Whole-design synergy:* v(all five) − Σᵢ v({i}). (b) *Pair synergy within the design*, for each of the 10 pairs i, j: v(all) − v(all without i) − v(all without j) + v(all without i and j), that is, how much more i adds when j is there, with the other three on. (c) *All interaction terms* (secondary): the 26 Harsanyi dividends d(T) = Σ over S ⊆ T of (−1)^(|T|−|S|) v(S), for every T of two or more parts, and the two-way contrasts averaged over the other three parts' settings. Sign convention: for outcomes 1-3, a positive contrast means the parts together reduce the share by more than their separate effects add up to (synergy); negative means less (the parts overlap or work against each other).
- **Scale (Q1).** For each size N and each primary outcome: Δ = (effect at N) − (effect at 500 adults), and the same for the none row's level.
- **Horizon (Q3).** The year-40 effect minus the year-20 effect from the same 40-year run (paired), for outcomes 1-3 and 5.
- **Participation (Q4).** The effect at each level. Departure from a straight line: at each level q, the effect minus q/90% times the effect at 90%, with its interval.
- **Multiple comparisons.** Every interval is published unadjusted at 95%. Where a statement rests on a family of tests, it also says whether it survives Holm's correction within that family: the five primary outcomes for the main effect; the 11 contrasts (a) and (b) for each outcome's synergy; the three larger sizes for each outcome's scale effect.
- **Which cell heads the report.** Reference, 500 adults, 20 years, no ageing, CPS yardstick, raise off, the release row against none. Every other cell is reported in the same tables (research rule 2).

## Decision rules
1. **A programme effect** on an outcome is stated ("reduces", "raises") only where its 95% interval excludes zero. A gain in basic living is stated as a gain only if the same row also shows a gain, with intervals excluding zero, on the cost-of-living measure and on the wealth measure (guardrail 6); otherwise the statement names which measures move and which do not.
2. **A synergy** is claimed only where the interaction's 95% interval excludes zero (research rule 4). It is called *material* only if it is also at least 1 percentage point (outcomes 1-3), 5% of the full design's cost (outcome 4), or 1 percentage point of cumulative inflation (outcome 5). Whether it survives Holm is stated beside it. BLEI synergies are claimed on the design-neutral reading only. The Hub's "0.42 / 0.28 / 0.18 / 0.12" decomposition (no stated method, audit A08) is replaced by the Shapley table, whatever it shows.
3. **A scale effect** is claimed only where |Δ| exceeds both its Monte Carlo error (the half-width of Δ's 95% interval) and 1 percentage point (outcomes 1-3 and 5), or 5% of the 500-adult value (outcome 4). If a scale effect is found on a primary outcome, that outcome's headline figure comes from the largest population at which the row was run (50,000 adults for the release row) and the 500-adult figure is labelled a small-population result. If no scale effect is found anywhere, the report says plainly that, in this engine, a larger population narrows the intervals and changes no conclusion (S35's plain statement). The synergy table at 10,000 adults (B10) and the participation curve at 10,000 (D10) are compared with 500 adults by the same rule, contrast by contrast and level by level.
4. **Horizon.** An effect is said to grow or shrink between year 20 and year 40 only where the paired difference's interval excludes zero and it is at least 1 percentage point. A 40-year statement is made only if it holds both without ageing (study A or B) and with ageing (study C); if not, it is reported as depending on whether people age.
5. **Participation (for S5).** S5's one participation figure is the lowest level in the grid at which the release row's effect on all three of outcomes 1-3 has an interval that excludes zero in the favourable direction, in the Reference environment with the CPS yardstick and the raise off; the same figure is reported for every other cell beside it. It is a detection level, not a viability threshold: the engine has no network effect and no collapse below a minimum share (its own warning says so). So the Hub's "75% minimum viable participation" (no run or source behind it: `audits/early-figures.md`, S30 and S31) can be neither confirmed nor refuted by this engine, and S5 says so. A curve is called non-linear only where the departure from the straight line has an interval excluding zero and is at least 1 percentage point.
6. **Octave raise (Q5).** Headline results are with the raise off. Every result with CCO is shown in both settings; where a decision under rules 1-5 differs between them, the headline sentence says so.
7. **Yardstick (Q6).** Headline results use the CPS earnings yardstick. Every page names the yardstick its figures use. Wherever a decision under rules 1-5 differs between the two yardsticks, the headline sentence says so. The reason for the choice, fixed before any programme row has been run with the CPS reading: the simulated people are working adults aged 25-64 and their children (no one is outside the labour force), and the released wage scale was set from the median personal income of everyone aged 15 and over, earners or not (S34 report, section 4). The earnings of US adults aged 25-64 with earnings are the cited figure for the people the model simulates. The full-time year-round reading (`'ft'`) is not run: it is the upper end, and the model has no part-time work (S34 recommendation).
8. **Debt reading (study F).** It is reported beside the main rows as a sensitivity reading. If it changes a decision under rules 1-5 for the main row, the headline sentence says the result depends on how households below their budget borrow. Its families-in-debt figure is compared with the SCF's 9.3% to describe the yardstick; no constant is changed to approach it.
9. **No target results.** No constant is tuned during or after the programme to reach any figure, earlier Hub figures included (research rule 3). A change of design after a result is a dated amendment, and S47 re-freezes.

## Reporting
Every cell of every study above is published, including null and unfavourable results and the Adverse and Stress environments, in compassionism-sim-results (per-seed values of every measure, `run.txt`, `SHA256SUMS`) and on the findings page. Pilot results (S35) are labelled pilot throughout and are not headline figures. Advocacy material may lead with the strongest findings that pass the rules above; nothing is dropped from the record.

## Limits carried from S34 (stated on the findings page)
Everyone in the model works (no one outside the labour force; no part-time work, so EITC reach is low: 11.9% against 15.3%); the engine has no child and dependent care credit ($138 a year less refundable CTC for one of six PolicyEngine households); without ageing, nobody grows up, retires or dies.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
