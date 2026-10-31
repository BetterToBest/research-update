# Preregistration: the cost-of-living line, weighted by where people live (S14, study L)

Committed Oct 31, 2026 by S14, before any run of these rows. It stands beside the study programme (`prereg/2026-11-study-program.md`, whose Amendment 4 points here) and changes nothing fixed there. Engine: BetterToBest/compassionism-simulation at commit `f66dc67b06126a2b88f772c32f4a99dd0be4a9ee` (pull request 56: the switch `LW`, row option `lw`, off by default; guard test identical). Job script: BetterToBest/compassionism-sim-results `runner/jobs/lw.js`. The derivation, the audit of every dollar path, and every modelling choice: compassionism-simulation `dev/reports/lw-weighted-line.md` and `dev/DECISIONS.md` (S14).

## Why
The model's cost of living for one adult, $49,370 a year, is the plain average of MIT's 51 state living wages. Weighted by population it is higher, because the most populous states cost more. The model's wages come from a national survey, which reflects where people live, so the weighted line is the consistent comparison. This study asks whether the findings depend on which line is used.

## Plain-words summary
- MIT's terms allow web use of at most ten locations, so MIT's own weighted figure cannot be computed here (a licence is Duke's decision). Two estimates run beside the current line: **ext** $51,201 (+3.7%; a weighted mean of MIT's 51 figures computed outside the project, partly checked) and **bea** $51,838 (+5.0%; the current line × the weighting ratio estimated from BEA's state price levels). At each line, the budget shares, household budgets and childcare are refitted by the model's own method.
- Three rows at each line: no programme, the release row, and the C2.2 design (Duke's answer to decision D8: automatic, every resident, BU at the cost of food, housing and medical care at that line, indexed to those prices).
- **Headline cell, fixed now:** Reference, 500 adults, 20 years, CPS earnings yardstick, octave raise off (the study programme's headline settings).
- **Pilot:** seeds 1-100 on GitHub Actions now, labelled pilot. **Full:** seeds 1-500 in the S48 batch, after the S47 freeze.
- Every cell is published, including null and unfavourable results.

## Checks made before writing this (no outcome value was looked at)
- `sources/lw_line.py` at $49,369.82 reproduces the engine's basket shares, household ratios and childcare exactly.
- Engine unit test (`v54UnitSuite`, S14): a row at another line moves that row only. Rows run after it equal rows run alone, the four refitted sets come back exactly, every set's shares sum to 1, and the needs level follows the line. Guard test: every figure identical with the switch off.
- `runner/jobs/lw.js --check` (seeds 1-2, 500 adults, 20 years, every environment): 9 rows. The base rows equal the plain release pair on every kept measure, even after a row at another line. The C2.2 rows carry the needs level of their own line. The weighted main row differs from the base main row.

## Questions
- **Q14a Level.** How much do the no-programme world's poverty and wealth measures move when the line moves (none at ext and at bea, against none at base)?
- **Q14b Effect.** Does the programme's effect against no programme depend on the line? For the release row and for the C2.2 design: the effect at ext and at bea, against the effect at base (a difference in differences).
- **Q14c Cost.** How do programme cost and inflation move with the line, above all for the C2.2 design, whose BU level is set by the line?

## Design

### Rows
| Row | What it is | Setting |
|---|---|---|
| base.none, base.main, base.c22 | no programme; the release row ($1,200, opt-in); the C2.2 design | no `lw`; `c22: {}`; C2.2: `c22: {auto: true, idx: 'needs'}`, `p.bu` = needs level $1,788.43 |
| ext.none, ext.main, ext.c22 | the same at $51,201.28 | `lw: 'ext'`; C2.2 needs level $1,885.06 |
| bea.none, bea.main, bea.c22 | the same at $51,837.76 | `lw: 'bea'`; C2.2 needs level $1,918.43 |

Every row starts from the study programme's reference pair, as study K's do. `c22: {}` on the none and main rows only reports coverage: S6 showed it changes no output. The child allowance stays a quarter of the adult BU in every row, as released.

### Studies
| Study | Rows | Adults | Years | Yardstick | Environments | Seeds |
|---|---|---|---|---|---|---|
| L pilot (now, Actions) | 9 | 500 | 20 and 40 | CPS | all three | 1-100 |
| L (S48 batch) | 9 | 500 | 20 and 40 | CPS | all three | 1-500 |

Command per shard (in a clean checkout of the engine commit): `node runner/jobs/lw.js --env=all --procs=2 --seeds=A-B --out=FILE`, through the `run-study` workflow (study id `pilot-l` for the pilot, `l` for the batch).

## Outcomes
- **Primary (as the study programme's):** below 30 days of basic living, design-neutral (`bNAPy`), with the design's own reading beside it (`bOAPy`); below the cost of living (`fgt0PY`); too little wealth (`pov`, `ppov_19`, `ppov_39`); programme cost per adult (`cost`); cumulative inflation (`pLev20`, `plv_19`, `plv_39`).
- **This study's own:** too little wealth, household reading (`hhWlthPY`, `hhWlthEnd`: net wealth below six months of the household's own cost of living, which follows the line, while `pov`'s $25,000 does not); households below their cost of living (`hhCostPY`); BU receipt and coverage of the C2.2 needs (`buPY`, `c22PY`, `c22R`).
- **Secondary:** children below the cost of living (`hhCostKidPY`), poverty severity (`fgt2PY`), official poverty (`hhFplPY`), non-participants' outcomes (`gNonF0`, `gNonW`), participation (`jnP5`, `jnP10`, `jnP19`), hours (`hrs`), Ginis.

## Analysis
As the study programme's Analysis: per-seed paired differences, averaged over seeds; 95% intervals by paired bootstrap over seeds (10,000 replicates, percentile intervals, one shared resample, bootstrap seed 20261101). Contrasts: (a) none at ext and at bea, against none at base; (b) main and c22 against none, at each line; (c) the difference in differences: (row − none) at ext or bea, minus (row − none) at base, for main and c22. Cost and inflation are also given as a percentage of the base row's.

## Decision rules
1. **Line-sensitive or not**, for each primary outcome and row, in the headline cell and then in every cell. In percentage points, from contrast (c):
   - *Not changed by the line:* the 95% interval of the difference in differences lies inside ±1 point.
   - *Changed by the line:* the interval excludes zero and the estimate is at least 1 point in size.
   - *Small change:* the interval excludes zero and the estimate is under 1 point.
   - Otherwise *unclear* (the interval is wider than ±1 point and includes zero).
   For cost, the change is stated as a percentage of the base row's cost, with its interval.
2. **What the findings say.** Every headline figure that rests on the line is stated with its range across the three lines. A finding is called robust to the line only if it is "not changed by the line" at both ext and bea in the headline cell.
3. **The released line.** This study does not choose the line. S47 decides which line the batch uses and records why. A weighted line is adopted only if its figure is MIT's own (licensed data), or if ext and bea agree within 1%. Until then the release keeps $49,370, labelled the unweighted mean, and these rows are published beside it. No constant is chosen to reach a result.
4. **Pilot and batch.** Pilot figures are labelled pilot. The S48 batch reruns every row at 500 seeds; if a label under rule 1 differs, the report says so.

## Reporting
Every cell goes to compassionism-sim-results (`pilot-l-<engine>`, later `l-<engine>`, with `run.txt` and `SHA256SUMS`), to `dev/reports/lw-weighted-line.md`, and to the findings page with the release, in every environment, including the Adverse and Stress Test.

## Limits (stated with every figure)
Neither weighted figure is MIT's own. The shares are fitted on eight state pages. There is one national line, because the model has no regions. MIT's prices are for 2026, BEA's for 2024 and the populations for July 2025.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
