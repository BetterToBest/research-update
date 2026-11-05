# Preregistration addendum: the policy levers (S54, study N, for S47)

Committed Nov 5, 2026 by S54, before any run of these rows on Actions. Engine: compassionism-simulation commit `e6da0506188d67fc542f1bd2c430e733a44bd921` (pull request 68; the merge commit). One disclosure: before this file was committed, the engine switch and the job script were tested on the session machine on seed 1 (stage 1 in Reference: 520 rows; stage 2 in Reference: a timing run), to check that the switch moves nothing when set to the design's own values, that duplicate rows (for example the 12% tax and the base row) agree exactly, that every lever moves what it should, and how long a seed takes. Those numbers are not results and are not used. They changed one thing in the design, before this file: the inflation-protected account paid for with new money fed its own inflation on that seed (about 1,200% a year), so a capped account (the first $10,000 a person) was added beside the uncapped one.

## Why
The backing study (S51) found that the release row pays out about 60% of a year's earned income in new money every year, and no plausible amount of new output backs it. Duke's answer to ledger decision D12 (Nov 1) is to test every lever a government running the programme could set before choosing one; his answer to D13 (confirmed Nov 2) is the rule that picks the best setting. Finding that a lever does not work is a result, and is published as one. Claude's reading of the levers, written before any run: `dev/reports/s54-levers-reading.md` in compassionism-simulation.

## Plain-words summary
- **Q20 (stage 1, primary).** Each lever on its own, around each design: what does it do to basket poverty, wealth poverty, non-participants' basket poverty, participation and programme inflation? Which levers work, which do nothing, which harm?
- **Q21.** For the conversion tax, three break-even rates with intervals: where the Source's net new money reaches zero (self-funding), where basket poverty is lowest, and where participation falls 5 points below its level at the released rate (deterrence).
- **Q22 (stage 2).** With all levers set together: which matter most (Morris screening), and what is the trade-off front between basket poverty, wealth poverty, participation and inflation (Latin hypercube)?
- **Q23 (stage 3).** The best settings by D13's rule, and every point on the front, rerun on seeds never used to choose them. Only confirmed settings are reported as findings.
- Two designs: the release row as released, and the C2.2 design (study programme Amendment 4). Wages keeping up with the programme's prices 100% and 90%.
- **Pilot now:** stages 1 and 2 on seeds 1-50 on GitHub Actions; stage 3 on seeds 51-100 after them. Labelled pilot throughout. **Full:** S47 carries stages 1-3 (choose on seeds 1-500, confirm on 501-1000).

## Design
**The levers** (row option `lv` and existing row settings; the reading note gives each one's source, institution and range). Every programme row carries `lv: {jn: 'conv', tref: <the design's own base tax>}` (joining that sees what joining pays, the **test reading**), wage indexation `wIdx`, and the study option `sec` (S53's measures, reporting only).

**Stage 1 rows** (job `runner/jobs/levers.js --stage=1` in compassionism-sim-results; `--check` confirms 520 rows per environment). For each design (rel, c22) and wage indexation (100, 90):

| Row | What it sets |
|---|---|
| `none`, `none.sv` | the no-programme run; with savings that keep up with prices |
| `asis` | the design with today's joining rule |
| `base` | the design with the test reading (every lever at the design's value) |
| `t0` ... `t40` | conversion tax base rate 0, 4, 8, 12, 16, 20, 25, 30, 40% (test reading) |
| `asis.t0` ... `asis.t40` | the same under today's joining rule |
| `pr0c75`, `pr8c75`, `pr0c50`, `pr4c50`, `pr8c50` | progression 0, 4, 8 points per rate point above 3x; cap 75 or 50% |
| `bt0`, `bt25`, `bt50`, `bt75` | a separate base rate on business conversions |
| `kp10`, `kp25`, `kp50` | the Source keeps 10, 25, 50% of the projects' sales and retires it |
| `ex50`, `ex0` | 50% or none of expired BU recycled to projects (the rest retired) |
| `fprog`, `fland`, `fflat` | outside finance: a progressive income tax, a land-value tax, a flat contribution on wages |
| `br1`, `br15`, `br2` | business conversion rate 1x, 1.5x, 2x |
| `bu60`, `bu80` | 60, 80% of the design's BU |
| `mm3`, `mm6`, `mm9` | top multiplier |
| `oc25`, `oc50`, `oc100` | octave capacity enforced at 25, 50, 100% |
| `no2`, `no4`, `no6` | number of octaves |
| `phi0` | the Phi tier off |
| `ph5`, `ph10` | conversions phased in over 5 or 10 years |
| `cap2`, `cap4`, `cap8` | the Source's net new money capped at 2, 4, 8% of earned income a year |
| `ixs`, `ixy`, `ixn` | BU indexation: the surge protocol (5%), every year to the price level, every year to the price of basic needs |
| `sva`, `svc` | the inflation-protected account paid for by the Source: all savings; the first $10,000 a person |
| `rcap`, `hc`, `hcrc` | the rent cap for BU tenants; the rent risk ($1.41 of higher rent per BU dollar, every renter outside PTH; Susin 2002); both |

Every programme row except `sva` and `svc` also has a `.sv` twin: the same row with savings that keep up with prices, compared with `none.sv` (the second savings reading). Rows that repeat the design's own value (for example `t12` and `mm9` in Reference) are kept, as a built-in check, so every environment has the same rows.

**Stage 2 rows** (`--stage=2`; 1,164 rows per environment). Seventeen factors, each over stage 1's range: base tax, progression, its cap, business tax, project sales kept, expired BU recycled, business rate, BU amount, top multiplier, octave capacity (none enforced, 100, 50, 25%), number of octaves (2-6), Phi tier, phase-in years, issuance cap (none, 8, 4, 2%), indexation (surge, every year, basic needs), protected account (none, capped, all), rent cap. Test reading, ordinary savings. The design is fixed by the job script (generator seed 54) and written into every output file:
- **Morris screening:** 10 trajectories of 18 points on a 4-level grid (step 2/3), for each design at wages 100% (360 rows).
- **Latin hypercube:** 200 points, for each design at wages 100% and 90% (800 rows).
- The no-programme row of each design and wage (4 rows).

**Stage 3** (after stages 1 and 2; its rows are derived mechanically by the rule below and listed in a dated amendment before they run): the chosen setting and every Pareto point for each design and wage, each with its no-programme row; the chosen setting also with the `.sv` twin and under today's joining rule.

- Environments: Reference, Adverse, Stress.
- Seeds: pilot stages 1-2 on 1-50, stage 3 on 51-100; full study: stages 1-2 on 1-500, stage 3 on 501-1000. Paired across all rows (common random numbers).
- 500 adults, 20 years.
- Engine: compassionism-simulation commit `e6da0506188d67fc542f1bd2c430e733a44bd921` (pull request 68).
- Where: GitHub Actions, workflow `run-study`, job `levers.js`; study `s54-levers1` (`job_args` `--stage=1 --env=all --procs=4`, 25 shards) and `s54-levers2` (`--stage=2 --env=all --procs=4`, 50 shards); folders `s54-levers1-<engine, 7 characters>/` and `s54-levers2-<engine>/` in compassionism-sim-results.

## Outcomes
Every outcome is a row's seed mean minus its own no-programme row on the same seeds (programme effect), and a lever row minus its design's `base` row (lever effect).
- **Primary (Q20):** basket poverty (`fgt0PY`, person-years); wealth poverty at year 20 (`pov`) on ordinary savings (the preregistered reading; the `.sv` twins give the other); non-participants' basket poverty (`gNonF0`, the no-harm test); programme inflation (`endoAnn`, a year); participation (`lvJm`, mean over years 1-19; and `lvJ1`, `lvJ7`, `lvJ19`).
- **Confirmations and secondary:** below 30 days of basic living (`bOAPy`, design-neutral `bNAPy`); non-participants' wealth poverty (`gNonW`); participants' basket and wealth poverty; the Source's net new money and payout as % of earned income (`lvU`, `lvP`); share of the payout backed or retired (`lvBk`); cost per adult (`cost`); income Gini (`giniD`); S53's security outcomes `secU25` and `secM3` for all adults, participants and non-participants (and on both savings readings, through the twins); median real wealth; employment and hours; FGT2 (never alone); the premium factor (`lvQ`), cap met (`lvCap`), project sales kept (`lvKp`), account interest (`lvSv`).
- **Q21, the three break-even tax rates** (each design, wage and environment, under both joining readings; the test reading is `jn: 'conv'`):
  1. *Self-funding:* the lowest rate at which the Source's net new money (`lvU`) is zero or below.
  2. *Lowest basket poverty:* the grid rate with the lowest mean basket poverty.
  3. *Deterrence:* the lowest rate above the released rate (12%; 18% in Stress) at which mean participation (`lvJm`) is 5 points or more below its level at the released rate.
- **Q22:** Morris elementary effects (mean absolute effect and its spread) of each factor on the four objectives; the Pareto front of the four objectives: basket poverty (lower), wealth poverty (lower), participation (higher), programme inflation (lower).

## Analysis
- **Estimates:** seed means of paired differences. 95% interval: paired bootstrap over seeds, 2,000 replicates, resampler seed 54, the same resample for every cell (analysis script `dev/tools/s54_levers.py` in compassionism-simulation, written before the results are read).
- **Break-evens:** linear interpolation between grid rates of the seed-mean curve (1 and 3), or the grid argmin (2); the interval is the 2.5th-97.5th percentile of the same statistic over the bootstrap replicates, with the share of replicates in which the break-even is reached. If it is not reached in the swept range, the result is "not reached by 40%", with the value at 40%.
- **Morris:** descriptive screening only (no claim rests on it): elementary effects on the [0, 1] factor scale, per design and environment.
- **Pareto front:** per design and wage indexation, on each objective's mean over the three environments (equal weights), among the candidates: every stage-1 programme row under the test reading on ordinary savings (not the `asis` or `.sv` rows) and every stage-2 row. Fronts per environment are published beside it.
- **Multiple comparisons:** intervals unadjusted at 95%; every cell published. Selection is protected by stage 3's fresh seeds, not by adjustment.

## Decision rules
1. **What a lever does.** Against its design's `base` row, a lever *works* on an outcome where the interval of the change excludes zero in the favourable direction in all three environments at that wage; it *harms* where it excludes zero in the unfavourable direction in any environment; otherwise it *does not move* that outcome. Each lever is reported in these words, with its size, including the levers that do nothing and why.
2. **Self-funding.** The reading note shows, before any run, that the face value of BU spent is new money that no conversion tax below 100% removes. If self-funding is not reached by 40%, the report says so and gives the net new money at 40%.
3. **Joining readings.** The test reading's break-evens are the results; today's rule is published beside them. If the two readings put deterrence at different rates, both are stated.
4. **The best setting (stage 3, Duke's rule D13).** For each design and wage indexation, on the choosing seeds and in every environment: (a) **no harm first:** non-participants no worse off (`gNonF0`, `gNonW`, `secU25X`, `secM3X`: mean change against no programme at or below zero) and wealth poverty no worse than with no programme (`pov` at or below zero, ordinary savings); (b) among those, programme inflation under 5% a year (`endoAnn` < 0.05); (c) among those, the lowest basket poverty (mean over the three environments). If no candidate passes (a) and (b), the report says plainly that no setting tested meets the rule, and names the candidates that come closest and what fails; none is reported as a finding.
5. **Confirmation.** On the fresh seeds, a setting is confirmed if, in every environment: basket poverty falls (the interval of the change lies below zero); each no-harm measure's interval has its upper end at or below +0.5 points (a stated non-inferiority margin); and the upper end of programme inflation's interval is under 5% a year. Pareto points are confirmed on the same tests, except that the inflation test is reported, not required. Only confirmed settings are reported as findings; the others are published as "not confirmed".
6. **Design changes are Duke's.** Any change to the design the results suggest is a ledger decision, a new row and a dated amendment before S47. The release row stays as released either way; the policy comparison stays frozen (ledger d94) unless Duke lifts it.
7. Pilot results are labelled pilot and never quoted as figures of the model. They decide only what S47 carries into the batch.
8. Results that run away (for example the uncapped protected account) are reported as they are, with the mechanism, not dropped.

## Reporting
Every cell above is published, including null and unfavourable results and the Adverse and Stress environments: per-seed values in compassionism-sim-results (`s54-levers1-<engine>/`, `s54-levers2-<engine>/`, stage 3's folder, each with run.txt and SHA256SUMS), the pilot report `dev/reports/s54-levers.md` in the engine repository, and the findings page after S48.

## For S47
- Stages 1-3 at seeds 1-500 (choose) and 501-1000 (confirm). Size at 50 seeds: about 12 processor-hours for stage 1 and 26 for stage 2 (local timing, 280 seconds per seed per environment for stage 1's 520 rows), so at 500 seeds about 380 processor-hours; S47 may run stage 2 at fewer seeds (at least 100) by amendment before the freeze, since stage 3 confirms. Output size: about 120 MB at 50 seeds, so S47 should trim the keys or compress the files.
- The confirmed settings also run on S52's main shock path, with both joining readings (S52 addendum, for S54).
- `secU25` and `secM3` on both savings readings for every lever row and in the no-harm test (S53 addendum Amendment 1): carried here.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.

### Amendment 1 (Nov 5, 2026): stage 3's rows, and how the analysis reads what this file leaves open
**Reason.** Stages 1 and 2 finished on seeds 1-50 (runs 42099920669 and 42099926032; folders `s54-levers1-e6da050/`, `s54-levers2-e6da050/`, checksums verified, every row and key present). This file says stage 3's rows are derived by decision rule 4 and listed in a dated amendment before they run. Nothing above this heading changes.

**The analysis script.** `dev/tools/s54_levers.py` in compassionism-simulation, committed (commit 5b22d9f, pull request 70) before any result was read and tested only on made-up numbers. Where this file is silent it reads (compassionism-simulation `dev/DECISIONS.md`, S54):
1. Each row is compared with the row it differs from in one thing only. Today's rule's tax sweep (`asis.tNN`) is compared with `asis`. `asis` is compared with `base`, so that row measures the joining reading. The `.sv` twins are compared with `base.sv` and `none.sv`. The protected accounts (`sva`, `svc`) are compared with `base` and `none`: the account belongs to the programme, and the world without the programme has none.
2. Programme inflation is the change in `endoAnn` against the no-programme row, as the Outcomes section defines every outcome.
3. A bootstrap replicate that never reaches a break-even counts as beyond 40%.
4. Candidates with identical objectives are one point on the front. Ties in rule 4 go to the first candidate listed.
5. If no candidate passes rule 4, the five closest are ranked by the summed excess of what fails, in points (inflation counts its excess over 5 points a year).

**Rule 4 on seeds 1-50: no setting tested meets the rule, in any design or wage.** Of 435 candidates per design at wages 100% and 255 at 90%:
- Release row: none passes the no-harm test, at either wage.
- C2.2 design, wages 100%: 175 pass the no-harm test, but none of them keeps programme inflation under 5% a year in every environment.
- C2.2 design, wages 90%: none passes the no-harm test.

So there is no chosen setting. Stage 3 therefore has no `.sv` twin and no run under today's rule. The closest candidates are named in the tables (`dev/reports/s54-levers-tables.md`) and the pilot report. Rule 4 says none of them is reported as a finding.

**Stage 3's rows.** Each design and wage gets its no-programme row and every point of the front on the three-environment means. That is 246 settings and 4 no-programme rows: 250 rows per environment.
- Release row, wages 100% (162 points): `t0`, `bt0`, `t4`, `ixn`, `t8`, `rcap`, `pr0c75`, `kp50`, `mm9`, `kp25`, `kp10`, `phi0`, `mm6`, `mm3`, `ex0`, `ph5`, `svc`, `bt25`, `t25`, `ph10`, `h100`, `bu80`, `h10`, `h192`, `br2`, `h23`, `bt50`, `h119`, `h4`, `h141`, `h126`, `bu60`, `m9.6`, `br1`, `h50`, `h89`, `h132`, `h41`, `m3.4`, `h154`, `m0.0`, `h138`, `h130`, `h164`, `h46`, `h20`, `h61`, `m7.12`, `m1.4`, `h178`, `m1.7`, `m7.11`, `h32`, `h131`, `h166`, `h66`, `h102`, `h153`, `h146`, `h105`, `fland`, `h21`, `h168`, `m3.9`, `h47`, `m3.5`, `h108`, `h86`, `m9.5`, `m9.1`, `h71`, `m4.16`, `m9.0`, `h162`, `h40`, `h30`, `h176`, `m9.2`, `h193`, `m9.3`, `h113`, `h14`, `h129`, `h182`, `h25`, `h26`, `m3.2`, `h123`, `m3.3`, `m3.0`, `m1.1`, `m1.2`, `h53`, `h34`, `m1.0`, `h8`, `m1.3`, `h74`, `h114`, `m7.5`, `h167`, `sva`, `m2.0`, `m2.1`, `m2.4`, `m2.5`, `h177`, `h83`, `m7.6`, `m7.9`, `m7.8`, `m7.10`, `h142`, `h101`, `m8.0`, `h122`, `h67`, `h92`, `h137`, `h98`, `h28`, `h160`, `m4.2`, `m4.4`, `h147`, `h81`, `m9.12`, `m5.6`, `m5.7`, `m5.4`, `m5.3`, `m4.6`, `m4.5`, `m5.2`, `h158`, `m4.12`, `m5.0`, `h170`, `h55`, `h77`, `h93`, `m6.0`, `h184`, `m6.1`, `m6.4`, `h197`, `h189`, `h62`, `m9.9`, `h13`, `h112`, `h37`, `h90`, `h143`, `h64`, `h87`, `h103`, `h36`, `m5.8`, `m5.11`, `m6.12`, `fflat`.
- Release row, wages 90% (74 points): `t0`, `bt0`, `t4`, `t8`, `fland`, `kp50`, `ixn`, `pr0c75`, `kp25`, `kp10`, `no6`, `phi0`, `ph5`, `ph10`, `bt25`, `bu80`, `h10`, `svc`, `bu60`, `h119`, `h100`, `h50`, `h192`, `h89`, `h61`, `h154`, `h23`, `h126`, `h32`, `h174`, `h86`, `h141`, `h132`, `h138`, `h182`, `h53`, `h74`, `h28`, `h101`, `h164`, `h102`, `h144`, `h26`, `h147`, `h81`, `h146`, `h162`, `h153`, `h108`, `h21`, `h105`, `fflat`, `sva`, `h170`, `h197`, `h189`, `h118`, `h62`, `h190`, `h42`, `h159`, `h13`, `h165`, `h171`, `h112`, `h181`, `h116`, `h48`, `h187`, `h24`, `h90`, `h143`, `h64`, `h87`.
- C2.2 design, wages 100% (5 points): `t0`, `kp50`, `svc`, `fflat`, `fland`.
- C2.2 design, wages 90% (5 points): `t0`, `kp50`, `svc`, `fflat`, `fland`.

`hI` is point I of the Latin hypercube. `mT.S` is step S of Morris trajectory T. Both are rebuilt from the job's seed-54 design. The other names are stage 1's rows.

The list is compassionism-sim-results `runner/jobs/levers-stage3.json` (SHA-256 `6b906101993040b344ae601a3d0c07c4693a8c6869ab7bfccb7e58238b68e782`), written by `s54_levers.py --select`. The job is `runner/jobs/levers.js --stage=3 --env=all --procs=4`. Its `--check` passes with 250 rows per environment. Stages 1 and 2 build exactly the same rows as before: their configurations hash identically.

A seed-1 run of stage 3 in Reference reproduced all 4,634 values of the same rows in stages 1 and 2 exactly. That run is a check of the job, not a result.

**Run.** Study `s54-levers3`, seeds 51-100 (never used to choose), all three environments, engine `e6da0506188d67fc542f1bd2c430e733a44bd921`, 25 shards on GitHub Actions. Folder `s54-levers3-e6da050/`.

**Analysis.** `s54_levers.py --s3 FOLDER --list runner/jobs/levers-stage3.json` applies decision rule 5 to every point. Pareto points are tested on basket poverty and the no-harm margin; the inflation test is reported. Rule 4 chose no setting, so stage 3 cannot produce a confirmed best setting. Any Pareto point it confirms is reported as a confirmed point of the trade-off front, with its inflation, and not as the best setting.

**Diagnostic, not preregistered.** In stage 2's Morris screening, the share of expired BU recycled to projects changed nothing in any release-row trajectory. Seed-1 runs on the session machine showed why. The share acts only on BU that expire unspent. Fewer BU expire as the BU gets smaller (548 at the full BU, 109 at 87%), so in most combinations nothing is left for the share to act on. This explains a null result; it is not a result.

### Amendment 2 (Nov 5, 2026, S47, before any 500-seed run): the frozen engine, seeds and output
Every row of this study in the S48 batch, the no-programme rows included, runs on the frozen engine: the outside audit's corrections (`au: true`) and the second implementation's four fixes (`fx: true`), as the study programme's Amendment 9 sets out. Rows, outcomes, analysis and decision rules are otherwise unchanged. The pilot ran on the published engine, so a pilot-to-batch difference combines new seeds and the corrections; the report says so, and study R measures the corrections. Jobs, folders and outputs: `prereg/run-manifest.md`. Stages 1 and 2 run at seeds 1-500 as preregistered (the reduction to 100 seeds this file allows is not taken; the batch fits on Actions). Stage 3's list is derived from them by rule 4 and recorded in a dated amendment before it runs on seeds 501-1000; it also runs on S52's main shock path (folder `n3x-<engine>`). The issuance-cap rows and the flat contribution's 90% wage row stay as checks. Each shard keeps only the keys this file's outcomes and `s54_levers.py` read, gzip-compressed (about 1.1 GB uncompressed at 500 seeds otherwise). Every row also records the security addendum's money-income falls by cause.
