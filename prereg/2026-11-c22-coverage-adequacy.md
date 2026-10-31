# Preregistration: who receives the Basic Units, and do they cover basic needs (S6, C2.2)

Committed Oct 31, 2026 by S6, before any run of these rows. It stands beside the study programme (`prereg/2026-11-study-program.md`, whose Amendment 3 points here) and changes nothing fixed there. Engine: BetterToBest/compassionism-simulation at commit `3e79adb45493972225ea3ec115bf5b379682555b` (pull request 53: the switch `C22`, row option `c22`, off by default; guard test identical). Job script: BetterToBest/compassionism-sim-results `runner/jobs/c22.js`. Claude's reading of the design, and every modelling choice: compassionism-simulation `dev/reports/c22-coverage-adequacy.md` and `dev/DECISIONS.md` (S6).

## Why
NEEC's criterion C2.2 passes a system that gives "unconditional provision covering 100% of basic needs (housing, food, healthcare, utilities) for all residents". NEEC's adjudication reads Compassionism at 0.5 on it (NEEC decision 83.8, ledger D65). The draft Act pays only "every citizen and legal resident 18 years or older", and the published model leaves adults below their cost of living. Whether to change the design (who receives the BU, and how much) is Duke's decision. These rows give the modelled figures he needs beside each option.

## Plain-words summary
- Three questions. How many people does the design reach, and what happens to those it leaves out (Q11)? How much of basic needs does the BU cover, at today's level and at a level set to cover them (Q12)? What does each option cost, in programme dollars and in inflation, and what does it do for poverty and wealth (Q13)?
- **Headline cell, fixed now:** Reference, 500 adults, 20 years, CPS earnings yardstick, octave raise off (the study programme's headline settings).
- Thirteen rows, two yardsticks, two horizons, three environments. **Pilot:** seeds 1-100 on GitHub Actions now, labelled pilot, for the ledger decision. **Full:** seeds 1-500 in the S48 batch, after the S47 freeze (about 6 runner-hours on Actions with 2 processes per runner).
- Every cell is published, including null and unfavourable results.

## Checks made before writing this (no outcome value was looked at)
- Engine unit test (`v54UnitSuite`, S6). With the switch on and nothing set, the run equals the switch off on every output. The status rule on the no-programme row changes no output. With u = 1, nobody receives the BU. With automatic distribution, every eligible adult receives it in every year.
- `runner/jobs/c22.js --check` (seeds 1-2, 500 adults, 20 years, every environment): 13 rows per yardstick. The none rows with the status rule (4.1%, 5.6%) equal the plain none row on all 40 kept measures, and the main row with the switch on equals the plain main row. The rows at the needs level carry `c22NeedsBU()`.
- A smoke run of seeds 1-2 (counts only, no values printed): all 156 rows run, 47 measures each, clean engine.

## Questions
- **Q11 Coverage.** For each coverage option: the share of adult-years receiving the BU (`buPY`); the share of adults left out by status (`elN`); the outcomes of the adults left out, against the same adults with no programme (`elF0`, `elW`, `elRes`); and non-participants' outcomes (`gNonF0`, `gNonW`).
- **Q12 Adequacy.** For each row: the share of adult-years in which the BU received covers the C2.2 needs at market prices (`c22PY`), and the mean share covered, capped at 100% (`c22R`).
- **Q13 Effects and cost.** For each row, the study programme's five primary outcomes against none, and each option against the release row (main), paired.

## Design

### Rows
Built as in the study programme (Rows): the main row is the release row; none is the no-programme row. Each row changes only what it names (`c22.js`, `ROWS`):

| Row | What it is | Setting |
|---|---|---|
| none | no programme (status drawn at 4.1%, to find the same adults) | `c22: {u: 0.041}` (identical to none, check) |
| none.el56 | the same, status drawn at 5.6% | `c22: {u: 0.056}` |
| main | the release row: opt-in, everyone eligible, $1,200 | `c22: {}` (identical to main, check) |
| el | the Act's status rule, opt-in | `u: 0.041` |
| el56 | the same at the workforce share | `u: 0.056` |
| auto | automatic distribution, everyone eligible | `auto: true` |
| act | **the Act as written**: automatic, citizens and legal residents only | `auto: true, u: 0.041` |
| bu1500 | BU $1,500 (design parameter between the two levels) | `p.bu = 1500` |
| needs.fixed | BU at the C2.2 needs level, indexed as released (only above 5% inflation) | `p.bu = c22NeedsBU()` ($1,788.43) |
| needs | BU at the needs level, indexed to the needs every year | `p.bu = c22NeedsBU(), idx: 'needs'` |
| c22 | **the C2.2 design**: automatic, everyone eligible, needs level, needs-indexed | `auto, idx: 'needs'`, needs level |
| c22.act | the same with the Act's status rule | plus `u: 0.041` |
| c22.cb50 | the C2.2 design with a child allowance of half the adult BU | plus `hh.childBU: 0.5` |

The status shares come from Pew Research Center (Aug 21, 2025; opened): unauthorized immigrants were 4.1% of the US population and 5.6% of its workforce in 2023. The adult share lies between the two. The needs level is a derived calculation: MIT's 2026 single-adult budget ($49,370) × the shares of food, housing with utilities, and medical care (0.4347) / 12.

### Studies
| Study | Rows | Adults | Years | Yardsticks | Environments | Seeds |
|---|---|---|---|---|---|---|
| K pilot (now, Actions) | 13 | 500 | 20 and 40 | CPS (headline) and released | all three | 1-100 |
| K (S48 batch) | 13 | 500 | 20 and 40 | both | all three | 1-500 |

Command per shard (in a clean checkout of the engine commit): `node runner/jobs/c22.js --env=all --procs=2 --seeds=A-B --out=FILE`, through the `run-study` workflow (study id `pilot-k` for the pilot, `k` for the batch).

## Outcomes
- **Primary (as the study programme's):** below 30 days of basic living, design-neutral (`bNAPy`) with the design's own reading beside it (`bOAPy`); below the cost of living (`fgt0PY`); too little wealth (`pov`, and `ppov_19`, `ppov_39`); programme cost per adult (`cost`); cumulative inflation (`pLev20`, `plv_19`, `plv_39`).
- **C2.2 outcomes (this study's own):** `buPY`, `c22PY`, `c22R`; for the adults left out by status, `elF0`, `elW` and `elRes` in each row and in the paired none row.
- **Secondary:** children below the cost of living (`hhCostKidPY`), poverty severity (`fgt2PY`), official poverty (`hhFplPY`), non-participants' outcomes (`gNonF0`, `gNonW`), realised participation (`jnP5`, `jnP10`, `jnP19`), hours (`hrs`), Ginis.

## Analysis
As the study programme's Analysis: per-seed paired differences, averaged over seeds; 95% intervals by paired bootstrap over seeds (10,000 replicates, percentile intervals, one shared resample, bootstrap seed 20261101). Two sets of contrasts: (a) each row against none, and (b) each option row against main. For the adults left out (status rows), contrast (c): their outcome in the row against the same adults' outcome in the none row with the same draw (none for 4.1%, none.el56 for 5.6%). `c22PY`, `c22R` and `buPY` are reported as levels, with intervals over seeds.

## Decision rules
1. **Coverage closed (in the model)** for a row: `buPY` = 100% in every environment, at both horizons.
2. **Adequacy closed (in the model)** for a row: `c22PY` = 100% in every environment, at both horizons. Otherwise the row is described by `c22R` and `c22PY`, never called adequate.
3. **Left out and harmed.** Under a status row, the adults left out are said to be made worse off by the programme if their below-cost-of-living share or their too-little-wealth share is higher than the same adults' with no programme, with the interval excluding zero (contrast c). Any such finding is stated in the decision put to Duke.
4. **Better or worse for people.** An option is called better than the release row only if, against main, it reduces both the below-cost-of-living share and the too-little-wealth share, with both intervals excluding zero (guardrail 6). It is called worse if either rises with the interval excluding zero. Otherwise it is mixed, and the statement names what moves. Cost and inflation are stated beside every comparison, whatever their direction.
5. **Pilot and batch.** Pilot figures are labelled pilot and go to Duke's decision as such. The S48 batch reruns every row at 500 seeds; if a label under rules 1-4 differs, the report says so.
6. **No target results.** No constant is chosen to reach a C2.2 score. The needs level comes from MIT's budget shares; the status shares come from Pew. A design chosen by Duke after seeing these figures is a design decision, recorded in the ledger, and S47 freezes it.

## Reporting
Every cell goes to compassionism-sim-results (`pilot-k-<engine>`, later `k-<engine>`, with `run.txt` and `SHA256SUMS`), to `dev/reports/c22-coverage-adequacy.md`, and to the findings page with the release. The adults left out by status, and the non-participants, are reported in every environment, including the Adverse and Stress Test.

## Limits (stated with every figure)
One US-average cost-of-living line (S14 builds a population-weighted one). MIT's medical budget assumes employer coverage. Status is drawn by household, so mixed-status families are not modelled. Temporary visa holders are not modelled separately. "Automatic" also opens conversion to everyone. Everyone in the model works (S34).

## Amendments

### Amendment 1 (Oct 31, 2026, S6, after the first pilot run): a rounding error in the coverage measure
- **What was wrong.** In the rows where the BU is set to the C2.2 needs and indexed to them, a single adult's BU equals their needs exactly. In about 1 adult-year in 10, floating-point rounding made the BU a few billionths of a dollar short of the needs, so the test "BU at least the needs" failed. This understated `c22PY` in the rows `needs`, `c22`, `c22.act` and `c22.cb50`. It was found by checking each adult's ratio by household type on one seed (singles: exactly 1.000000; 90.5% counted as covered).
- **Change.** An adult-year counts as covered when the BU is at least the needs within a relative 1e-9 (engine pull request 54). Nothing else changes: the measure, the rows and every other output are unchanged (guard test identical, release panels identical).
- **Runs.** The first pilot (`pilot-k-3e79adb`) stays published. The pilot is rerun on the fixed engine (`pilot-k-<new commit>`), and the report takes `c22PY` from the rerun. The report also checks that every other kept measure is identical between the two runs, seed by seed.
- **Engine:** compassionism-simulation at commit `395dd5bd0475a03467e816d08534705bd0e1f9c8` (pull request 54). S47 pins the batch's commit.

### Amendment 2 (Oct 31, 2026, S14, before any 500-seed run): Duke's design answer (ledger D8)
- **Answer:** the BU should cover the basics and depend on the cost of living, and for testing no one is left out (quoted in the study programme's Amendment 4).
- **Reading:** the row `c22` (automatic, every resident, BU at the C2.2 needs level, indexed to the needs; child allowance a quarter, as released) is the design Duke chose. Study K's rows, outcomes and rules do not change. Its report and the findings page name `c22` as the chosen design, and every other row as an option Duke did not choose. The decision put to Duke under rule 3 is answered: no status rule.
- **Batch:** study K runs as preregistered in S48. The study programme's Amendment 4 says how the other studies are built on the chosen design.
