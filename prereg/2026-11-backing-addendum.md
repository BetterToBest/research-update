# Preregistration addendum: backing as a mechanism, and the break-even backed share (S51, for S47)

Committed Nov 2, 2026 by S51, before any run of these rows. One disclosure: before this file was committed, the job and the analysis script were tested on seeds 1-2 on the session machine, to check that they run and that the tables form. Those numbers are not results and are not used. The test showed one thing that changed this file: at 90% wage indexation the release row can lower basket poverty while raising wealth poverty. Decision rule 2 therefore requires both to fall (guardrail 6, which already binds every claim). The change makes the test stricter, not easier to pass. It adds study M to the study programme (`prereg/2026-11-study-program.md`; its Amendment 5 points here). Nothing already fixed there changes. Engine: BetterToBest/compassionism-simulation at commit `6428b96f95e28bbbda5b0717e8915a09206310a0` (pull request 62: the row option `bkm`, off by default; guard test identical). S47's design freeze pins the commit the full batch runs on. Claude's reading of the design: `dev/reports/s51-backing-reading.md` in the engine repository. Ledger decision D11 (Duke, Nov 1): backing is the design's requirement; the model makes it a mechanism and reports the break-even backing share.

## Why
The release row treats almost all of what the Source pays at conversion as new money. Only matched project output (about 7.7%) backs it, and that is where its programme inflation of about 51% a year comes from. The audit (S13, E6) found that the fall in basket poverty holds only if wages keep up in full with that inflation. At 95% indexation the fall shrinks from 30 to 22 points in Reference; at 75% the programme raises basket poverty everywhere. The every-dollar-backed reading removes the inflation by assumption. This study asks how much backing the result needs, and whether a backing mechanism can supply it.

## Plain-words summary
- **Q11 (primary).** How much of the Source's net payout must be backed by output for basket poverty to fall when wages keep up with prices only in part (95%, 90%, 75%)? This is the **break-even backed share**, with its interval, for each environment.
- **Q12.** When conversion pay funds projects whose output enters supply (the mechanism), what share of the payout ends up backed? Does it reach the break-even share, and under which settings?
- **Q13.** How much do the answers depend on the mechanism's design parameters (share funded, productivity, ceiling, lag, wear) and on how output backs money (added output only, or proceeds retiring the money)?
- Two designs: the release row as released (the plan's subject), and the C2.2 design (the study programme's headline design from S47, Amendment 4).
- **Pilot now:** seeds 1-50 on GitHub Actions, labelled pilot throughout. **Full:** seeds 1-500 in the S48 batch, after the S47 freeze.

## Questions
- **Q11.** For each design, environment and wage indexation `wIdx` in {100%, 95%, 90%, 75%}: the smallest assumed backed share `a` at which the paired mean difference in basket poverty (programme minus no programme) is below zero. Answer: b* and its 95% interval, or "not reached" (no share up to 100% makes it fall).
- **Q12.** For each mechanism setting: the realised backed share (`bkA`, %) with its interval; whether it reaches b* at the same `wIdx` (Decision rules, 2); and the setting's own primary outcomes against no programme.
- **Q13.** The same answers across the mechanism's grid and its sensitivities.

## Design
**The mechanism** (row option `bkm`; Claude's reading B1-B5). Each year a share `f` of the Source's net payout funds work on supply-adding projects. A dollar funded (year-0 prices) adds `rho` dollars of output a year, starting `lag` years later and wearing away at `dep` a year. Total added output is at most `cap` of the year's earned income. Under the reading `g` (main: added output only), the year's increase in project output absorbs that year's new money; any excess carries forward, and a fall in output adds to the new money. Under the reading `r` (sensitivity: proceeds retire the money), each year's whole output retires that much new money, never more than the year's new money. Household pay, conversions and octaves are unchanged. Only the price path moves.

**Design parameters** (none is fitted to any result; every one is swept):

| Parameter | Values | Basis |
|---|---|---|
| f, share of the net payout funding supply-adding projects | 25%, 50%, 100% | design parameter (the design is silent) |
| rho, output a year per dollar funded | 0.05, 0.10, 0.20, 0.32 | design parameter; 0.32 is US GDP 2024 over the net stock of fixed assets at the end of 2024 (BEA via FRED GDPA, K1TTOTL1ES000; opened Nov 2, 2026), an upper end |
| cap, ceiling on added output, share of earned income | 8%, 16%, none (C2.2 design: 8%, none) | 8%: BLS U-6 2025 (CFG.US_UNDERUSE); 16%: Kenya's peak absorption (CFG.KENYA_ABSORB_PEAK, Egger et al. 2022); both already sourced in the engine |
| lag | 2 years (1 and 3: sensitivity) | design parameter |
| dep, wear a year | 5% (0: sensitivity) | design parameter |
| reading | g (main), r | modelling assumption (reading B5) |

**Rows** (job `runner/jobs/backing.js` in compassionism-sim-results; `--check` confirms 350 rows per environment). Every row is the runner's reference job (release-pair.js settings) with only the named change:

| Design | Rows | Count |
|---|---|---|
| rel (release row, released wages) | none at each wIdx | 4 |
| rel | arm A: assumed backed share a in {0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100}% x wIdx {100, 95, 90, 75}% | 48 |
| rel | arm B: mechanism, reading {g, r} x f x rho x cap {8, 16, none} x wIdx {100, 90}% | 144 |
| rel | sensitivities at f 100%, rho 0.20, no ceiling, wIdx 100%: lag 1, lag 3, wear 0, each reading | 6 |
| c22 (C2.2 design, CPS yardstick) | none at each wIdx | 4 |
| c22 | arm A, as for rel | 48 |
| c22 | arm B: reading x f x rho x cap {8, none} x wIdx {100, 90}% | 96 |

- Environments: Reference, Adverse, Stress.
- Seeds: pilot 1-50; full 1-500. Paired across all rows (common random numbers).
- 500 adults, 20 years.
- Where: GitHub Actions, workflow `run-study`, study `s51-backing`, job `backing.js`, `job_args` `--env=all --procs=4`, 25 shards; folder `s51-backing-6428b96/` in compassionism-sim-results. Seeds 1-500 join the S48 batch.

## Outcomes
- **Primary (Q11):** basket poverty, the share of adult-years with income below the cost of living for the household (`fgt0PY`, %), the measure of the audit's E6 table. b* is read from it.
- **Confirmations (guardrail 6), each with its own break-even read the same way:** below 30 days of basic living, design-neutral (`bNAPy`) and the design's own (`bOAPy`); too little wealth at year 20 (`pov`).
- **Secondary:** the realised backed share (`bkA`, and the mechanism's own `bkmA`, `bkm5`, `bkm10`, `bkm19`); the payout as a share of earned income (`bkPY`); project output in year 19 as a share of earned income (`bkmO19`); programme inflation a year (`endoAnn`) and the price level at year 20 (`pLev20`); programme cost (`cost`, `srcPay`, `srcTax`); hours (`hrs`); Gini (`giniD`, `eGiniW`); participants' and non-participants' basket poverty (`gPartF0`, `gNonF0`).

## Analysis
- **Paired differences** against the row's own no-programme run at the same wIdx: D(a) = mean over seeds of [`fgt0PY`(programme) − `fgt0PY`(none)]. Intervals: paired bootstrap over seeds, 2,000 replicates, seed 51 for the resampler, the same resample for every row.
- **b\*:** along arm A's grid, take the first a at which D(a) < 0. b* is found by linear interpolation between that grid point and the one before it. If D(0) < 0, b* = 0 ("falls with no backing"). If D(a) ≥ 0 up to a = 100%, b* is "not reached". The interval comes from recomputing b* on each bootstrap replicate (percentiles 2.5 and 97.5). Replicates that do not reach are counted, and the share of them is reported.
- **b\*\_clear (secondary):** the same, using the first a at which the upper end of D(a)'s 95% interval is below zero.
- **The mechanism's rows:** the realised backed share `bkA` (mean and interval) and D for the row itself, at wIdx 100% and 90%.
- **Multiple comparisons:** intervals are published unadjusted at 95%. The statement "the mechanism reaches break-even" is made per setting, and the report says how many of the grid's settings support it. No single favourable setting is reported alone.

## Decision rules
1. For each design, environment and wIdx < 100%: if b* is reached, the report states "basket poverty falls only if at least b* (interval) of the payout is backed by output". If it is not reached: "no backing share makes basket poverty fall at this indexation". The same statement is made for each confirmation measure; a gain is claimed only where basket and wealth poverty agree (guardrail 6).
2. A mechanism setting **reaches** break-even at wIdx 90% if its own D's 95% interval lies below zero **and** the interval of its difference in wealth poverty (`pov`) lies below zero too (guardrail 6). If basket poverty falls but wealth poverty does not, it is reported as **basket only**. It **does not reach** break-even if D's interval lies above zero. Otherwise it is **unclear**. The realised share `bkA` is set beside b* as a check, not the test: the mechanism's backing ramps up over time, while arm A's is the same every year.
3. The headline statement for Q12 comes from the main reading (g, cap 8%, lag 2, wear 5%) only. Every other setting is labelled a sensitivity. If only settings outside the main reading reach break-even, the report says which assumptions that needs (for example: no ceiling, or proceeds that retire the money).
4. If the mechanism reaches break-even nowhere in the main reading, the report says so plainly. It lists the design's other levers the model could test (the size or pace of the payout, the conversion tax, octave capacity) as questions for Duke. Changing them is a design change: a ledger decision, not a modelling one.
5. Pilot results are labelled pilot and never quoted as figures of the model. They decide only what S47 carries into the batch.

## Reporting
Every cell above is published, including null and unfavourable results and the Adverse and Stress environments: per-seed values in compassionism-sim-results (`s51-backing-<engine>/`, with run.txt and SHA256SUMS), the pilot report `dev/reports/s51-backing-mechanism.md` in the engine repository, and the findings page after S48.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.

### Amendment 1 (Nov 2, 2026, after the pilot; to be built and frozen at S47)
**Reason.** The pilot (seeds 1-50; report `dev/reports/s51-backing-mechanism.md` in the engine repository) showed two patterns. A 10-seed check on the session machine, not preregistered (`dev/tools/s51_diag.js`), traced each to a cause:
- Wealth poverty rises under the release row because money savings do not keep up with about 51% inflation a year. With savings that keep up with prices (row option `sv`), the rise becomes a fall.
- Arm A dips near full backing. In the release row the BU is raised to the price level only in years when inflation exceeds 5%, so at 2-5% inflation it wears down unprotected and participation falls.

**Change.** Two sensitivities are added, both labelled "added after the pilot". Nothing above changes: the primary measure, the confirmation measures, the decision rules and every preregistered row stay as they are.
1. **Savings that keep up with prices.** Arm A for both designs at all four wage indexations, the no-programme rows included, with `sv` on both sides of each pair (104 rows per environment). Wealth poverty is reported both ways, side by side. The preregistered measure stays the test.
2. **The BU raised every year (release row).** Arm A's 90%, 95% and 100% rows at all four wage indexations, with the BU raised to the price level every year (12 rows per environment).

S47 adds these rows to `runner/jobs/backing.js` (row count 350 → 466 per environment), dry-runs them, and pins them with the rest of the batch.
