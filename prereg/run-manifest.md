# Run manifest: the full study batch (S47 design freeze, for S48)

Written Nov 5, 2026 by S47, before any 500-seed run. This file lists every job the batch runs: its rows, environments, seeds, population, horizon, outputs, and which later step reads them. S48 runs it exactly. It is the record the study programme (`prereg/2026-11-study-program.md`, Amendment 9) and each addendum point to.

**Status: draft, not yet frozen.** The design choices below are made. The freeze is complete when the items in section 6 have landed, the engine commit is pinned in section 1, and every job has passed its 2-seed dry run (section 7). Until then no job here runs at 500 seeds.

## 1. The model being frozen
- **Engine:** BetterToBest/compassionism-simulation at commit `<pinned when section 6's engine items land>`. Every job runs in a clean checkout of that one commit.
- **The frozen engine** is the published engine (v5.6) with two sets of corrections switched on in every row of every job, the no-programme rows included:
  - the outside audit's three corrections (row option `au: true`: the BLEI test for the wage bonus and PTF adoption deflated by the price level; income-graded spending once the year's cash income is known; the financial-stability score deflated). Source: Simulation `dev/reports/s13-engine-audit.md` section 1.
  - the second implementation's four fixes (a new row option, `fx: true`, built in section 6): PTH's books opened after households are formed; the essentials' supply path from a run with job loss, the safety net and the labour response; PTH home prices at the basket's housing cost; `snAbN` counting no rounding remainders. Source: Simulation `dev/reports/s50-independent-implementation/GAPS.md`, phase 2, items 2, 6, 7 and 8.
  - the spending share re-derived by its own method on the frozen no-programme run: 0.877 of cash surplus consumed (`SPEND_FROZEN`), in place of 0.593 (Amendment 3). The published engine keeps 0.593.
  - All three are set by one helper, Simulation `harness.js` `frozenRow(c)` (`au: true, fx: true, sc: 0.877`), which every job script uses; the C2.2 design is `c22Design(c)`.
- **The headline design** is the C2.2 design (study programme Amendment 4, Duke's answer to ledger D8): the BU at the cost of food, housing with utilities, and medical care for one adult (`c22NeedsBU()`, $1,788.43 a month), indexed to those prices every year, paid automatically to every resident; child allowance a quarter of the adult BU.
- **Beside it, in every table where its question applies:** the release design ($1,200, opt-in, as published in v5.6), on the same frozen engine. Labelled "release design".
- **The published engine itself** (v5.6 exactly: no `au`, no `fx`) runs only in study R. R measures how far each set of corrections moves the release row and the C2.2 design, so every other study can be read against the published figures.
- **The cost-of-living line stays at $49,370** (MIT's unweighted mean), labelled as such. Study L's decision rule 3 adopts a weighted line only if its figure is MIT's own licensed data, or if the two weighted estimates agree within 1%. Neither holds: ext ($51,201.28) is MIT's own weighted mean taken from a published copy of its table, not licensed data, and ext and bea ($51,837.76) differ by 1.24%. Study L publishes both beside the headline. (Study L's Amendment 1 recommended ext; the rule as preregistered does not allow it, and S47 follows the rule.)
- **Common settings** (every row, as in the study programme's Rows): the runner's reference pair (`relMainCfgs(tbPresets(P))`, `sc: SPEND_SOURCED`, `sn: {abawd: true, slope: true}`, `applyNR6()`, `tbSetG(TB_PROFILE_G)`, study options `{fin: 'tax', aT: 0, a: 0, X: 0, sc: SPEND_SOURCED}` plus `REL_V52_STUDY`). Headline yardstick: CPS earnings (`lt: {s: 'all', m: 'all'}`). Octave raise off. No ageing. Environments: Reference, Adverse, Stress. Seeds 1-500, paired across every row of a job (common random numbers), except study N's stage 3 (seeds 501-1000).

## 2. Who reads what (consumers)

| Consumer | What it needs | From |
|---|---|---|
| S7 release panel and findings page | the headline pair and the release design, 20 and 40 years, both yardsticks, every primary outcome, per-seed values; the published-engine figures beside them | R, A (500 adults) |
| S11 BLEI visuals (ledger I1) | per-year series: BLEI tiers, median BLEI and its three parts, relative income poverty, extreme poverty | X |
| S5 participation figure (NEEC C5.3) | basket and wealth poverty against opt-in participation, 2% to 90% | D, D10 |
| S36 synergy tables | the 32-cell factorial, 20 and 40 years, both designs, raise on and off; at 10,000 adults | B, B10 |
| S38 community-layer report | the layer's rows | G, G10, H, I, J |
| S39 outside cross-check (BeforeIT.jl) | the price level by year at matched settings and population | A (`plv_0` to `plv_39`) |
| N-S70 NEEC readings (H-S5, H-S6) | C2.2 coverage and adequacy; the participation figure | K, D, R |
| S45 advocacy charts | the release panel and the robust findings | R, A, B, D |
| S19 public costs | the per-year poverty series (`S19_KEYS`) | R, P, N, O |
| S51 to S54 reports (full-study versions) | their addenda's rows | M, O, P, N |
| Study L (the line) | its 9 rows | L |

## 3. The jobs

Runner-hours are for 500 seeds at 2 processes per runner, from the pilots' measured cost (S35 report section 1; S51 to S54 timings), before the dry run re-times them. "Rows per environment" counts each yardstick and each horizon setting as its own row where the job runs both.

| Job | Script and arguments | Rows per environment | Adults | Years | Seeds | Runner-hours | Folder |
|---|---|---|---|---|---|---|---|
| R release panel and bridge | `program.js --study=R` | 21 rows x 2 yardsticks | 500 | 20, 40 | 1-500 | 6 | `prog-r-<engine>` |
| R-panel (page format) | `harness.js testbed 500 release ENV --v54 --snab --slope` (published engine) and the same with `--frozen` (section 6) | the testbed's | 500 | 20, 40 | 1-500 | 2 | `panel-<engine>` |
| A scale | `program.js --study=A` | 12 (500 to 10,000 adults); 6 (50,000) | 500, 2,000, 10,000, 50,000 | 20, 40 | 1-500 | 187 | `prog-a-<engine>` |
| B synergy | `program.js --study=B` | 192 | 500 | 20, 40 | 1-500 | 29 | `prog-b-<engine>` |
| B10 synergy at scale | `program.js --study=B10` | 64 | 10,000 | 20 | 1-500 | 66 | `prog-b10-<engine>` |
| C ageing | `program.js --study=C` | 12 | 500 | 20, 40 | 1-500 | 2 | `prog-c-<engine>` |
| D participation | `program.js --study=D` | 46 | 500 | 20, 40 | 1-500 | 10 | `prog-d-<engine>` |
| D10 participation at scale | `program.js --study=D10` | 12 | 10,000 | 20 | 1-500 | 19 | `prog-d10-<engine>` |
| F debt reading | `program.js --study=F` | 12 | 500 | 20, 40 | 1-500 | 2 | `prog-f-<engine>` |
| G, G10, H, I, J community layer | `program.js --study=G` (and G10, H, I, J) | 36, 32, 18, 12, 4 | as the addendum | as the addendum | 1-500 | 50 | `prog-g-<engine>` and so on |
| K coverage and adequacy | `c22.js --env=all` | 13 | 500 | 20, 40 | 1-500 | 6 | `k-<engine>` |
| L cost-of-living line | `lw.js --env=all` | 9 | 500 | 20, 40 | 1-500 | 4 | `l-<engine>` |
| M backing | `backing.js --env=all` | 466 | 500 | 20 | 1-500 | 29 | `m-<engine>` |
| N1, N2 levers, stages 1-2 | `levers.js --stage=1`, `--stage=2` | 520, 1,164 | 500 | 20 | 1-500 | 190 | `n1-<engine>`, `n2-<engine>` |
| N3 levers, stage 3 | `levers.js --stage=3 --list=FILE` (list derived from N1 and N2 by rule 4, in a dated amendment) | the front's size (250 in the pilot) | 500 | 20 | 501-1000 | 30 | `n3-<engine>` |
| N3x stage 3 on the shock path | `levers.js --stage=3 --list=FILE --sx=main` (section 6) | as N3 | 500 | 20 | 501-1000 | 30 | `n3x-<engine>` |
| O supply shock | `shock.js --env=all` | 70 | 500 | 20 | 1-500 | 5 | `o-<engine>` |
| P security | `security.js --env=all` | 12 | 500 | 20 | 1-500 | 1 | `p-<engine>` |
| X per-year series | `explore_export.js ENV YRS 500 1 --v54 --snab --slope` extended (section 6), headline pair and release design | 3 | 500 | 20, 40 | 1-500 | 2 | `x-<engine>` |
| **Total** | | | | | | **about 670** | |

About 670 runner-hours is about 34 hours on 20 runners at once. No job needs more than 6 hours in one shard if shards are sized as section 5 says.

## 4. Rows, job by job

**R, the release panel and the bridge** (new; programme study id R). Per yardstick and horizon, in all three environments:
- the published engine: none, the release row, the C2.2 design (3 rows);
- the audit's corrections only (`au: true`): the same 3 rows;
- the frozen engine (`au: true, fx: true`): the same 3 rows; the C2.2 row here is the headline;
- on the frozen engine, both designs: the middle backing reading (`aK: CFG.KENYA_ABSORB_ROLLOUT`) and the every-dollar-backed reading (`a: 1`) (Grok audit triage, item 6); the FBS50 reading (`fb: {dist: 'fbs50'}`, audit E7) (6 rows);
- on the frozen engine: wages that also follow outside inflation (`au: {gate: true, sg: true, fbs: true, wOut: true}`) for none and both designs (audit E5; identical to the frozen rows in Reference, which has no outside inflation, and kept as a check) (3 rows).
- on the frozen engine at the published spending share, 0.593: none and both designs (Amendment 3) (3 rows). R is then 21 rows per yardstick and horizon.
- Study options `sec: true` on every row (security addendum: the release panel's security outcomes and the S19 series).
- Checks: the published-engine none and release rows equal `release-pair.js`'s byte for byte; the published-engine panel reproduces the v5.6 panel fingerprints (REPRODUCE.md).
- The audit's `wIdx` sweep (E6) is study M's arm A at a backed share of 0 (four wage indexations on both designs); R adds no row for it.

**A, scale.** The preregistered 6 rows (none and the programme row, both yardsticks, raise off and on) built twice: on the C2.2 design (headline) and on the release design, with their own none rows: 12 rows at 500, 2,000 and 10,000 adults. At 50,000 adults, the C2.2 design only (6 rows): the scale question (Q1) asks whether outcomes change with population, which the other three sizes answer for the release design; this saves about 130 runner-hours.

**B and B10, synergy.** The preregistered factorial (31 cells and none; B: both yardsticks, the 16 cells with CCO raise off and on, 96 rows; B10: CPS, raise off, 32 rows) built on the C2.2 design (headline) and on the release design (its comparison, Amendment 4): 192 and 64 rows. A cell without CCO has no BU under either design, so the two builds of those cells are equal; they are kept as a check.

**C, ageing; F, debt reading.** Each preregistered row set on both designs: 12 rows each.

**D and D10, participation.** The release design only (Amendment 4: under automatic distribution everyone takes part). The grid gains 2% and 5% (S35 report section 9 item 7; Amendment 9): D is 11 levels x 2 yardsticks x raise off and on, plus none for each yardstick, 46 rows; D10 is 11 levels plus none, CPS, raise off, 12 rows.

**G to J, community layer.** The addendum's rows built on both designs (headline C2.2): G 36, G10 32, H 18, I 12, J 4 rows (J at 2,000 and 10,000 adults). Keys `clN`, `clZ`, `clSd`, `clHi`, `clTh`, `pfMem`, `pfCut` kept.

**K, L, M, N, O, P.** Their addenda's rows exactly (with the amendments already recorded: M 466 rows, P 12 rows, N's stage 3 by rule 4), on the frozen engine. Additions:
- **M:** the two sensitivities of Amendment 1 (`sv` arm A, 104 rows; the BU raised every year, 12 rows).
- **N:** `sec: true` on every row, both savings readings (already in the job); the money-income falls by cause (security addendum Amendment 1 item 3a) on every row, so the outside-finance rows' big income falls can be traced (S54 report, "What S47 carries" item 4). Stage 2 at 500 seeds, as preregistered. The three identical issuance-cap rows and the flat contribution's 90% wage row stay, as preregistered checks. Output trimmed to the keys the addendum's outcomes and `s54_levers.py` read, gzip-compressed (section 6).
- **N3x:** stage 3's list on S52's main shock path (supply-shock addendum; S54 report item 5), with the joining reading's participation reported under the shock.
- **O:** `sec: true`; the three descriptive outputs of the supply-shock addendum's Amendment 1 (essential costs by payer and category; the Source's backed and unbacked payout and the BU's cost by year; a dollar-based volatility).
- **P:** the two descriptive measures of the security addendum's Amendment 1 (money-income falls by cause; uncovered falls below own cost) under `sec`.

**X, per-year series** (S11, ledger I1). `explore_export.js` gains BLEI tiers, median BLEI and its three parts, relative income poverty and extreme poverty, by year; it runs for none, the C2.2 design and the release design on the frozen engine.

## 5. Measures kept, and how files are written
- Every job keeps the measures its preregistration names. The programme jobs keep the 46 measures of Amendment 1 plus: the design-neutral basic-living share at year 20 in 40-year runs (a new reporting key, section 6); the community keys under `cl`; `SEC_KEYS` and `S19_KEYS` to the run's horizon in R.
- Keys past a run's end (year-40 keys in 20-year rows), participation keys on no-programme rows and ageing keys without ageing are written as `null`, never 0 (S35 report section 9 item 2).
- Dispatch: `--procs=2` (S35 report section 1: a 4-vCPU runner does about two cores' work), shards sized to run under 2 hours, at most 20 runners at once. Every folder gets `run.txt`, `SHA256SUMS` and `DONE`; the workflow checks every shard (`check-shards.js`).

## 6. What must land before the dry run (S47, later sessions)
Engine (compassionism-simulation; guardrails 1-9; off = bit-identical, guard test, lineage):
1. Row option `fx` (the four S50 fixes), each part separately switchable, measured on 50 paired seeds before the freeze (a dated note in the engine's DECISIONS.md and in this file). **Done Nov 5** (Amendment 2).
2. Reporting keys: the design-neutral basic-living share at year 20 in 40-year runs; the security addendum's two descriptive measures under `sec`; the supply-shock addendum's three descriptive outputs. **Done Nov 6** (Simulation pull request 75): `bNAy20`, `bOAy20`; `secF25`, `secF25w`, `secF25c`, `secF25o`, `secU25b` per group; `sxE*`, `sxK*` per group and window, `sxQb_t`, `sxQu_t`, `sxQi_t`, `sxVd`.
3. `harness.js testbed ... --frozen` (the page-format panel on the frozen engine and the C2.2 design), and `explore_export.js`'s added series. **Done Nov 6** (pull request 75): the C2.2 design is the panel's row `c22`; `explore_export.js ... --suite --frozen --panel=FILE` writes the visual series (BLEI tiers, the median BLEI and its parts, relative income poverty, extreme poverty) for no programme, C2.2 and the release design, and checks its yearly means against the frozen panel.
4. The 0.593 spending share (`SPEND_SOURCED`) re-derived on the frozen engine's no-programme run (audit E17). If it differs, that is a dated amendment before the freeze, and the measured effect is recorded; no other constant moves. **Done Nov 6: it differs (0.877; Amendment 3).**
5. MODEL_SPEC.md and TESTBED_SPEC.md written for the frozen model (every switch its rows turn on; the S50 contradictions corrected and its 30 gaps closed).

Jobs (compassionism-sim-results `runner/jobs/`; each with `--check` of its row counts):
6. `program.js`: studies R, G, G10, H, I, J; both designs in A, B, B10, C, F; D and D10 at 2% and 5%; `au` and `fx` on every row; nulls for missing keys.
7. `--frozen` (the `au` and `fx` options on every row) in `c22.js`, `lw.js`, `backing.js`, `shock.js`, `security.js`, `levers.js`; backing's 116 added rows; levers' key trim, gzip and `--sx=main`.

## 7. Dry run
Every job at seeds 1-2 on Actions, one shard each (`run-study`, study id `dry-<job>`). For each: the folder is `DONE`, checksums pass, and the consumer's script loads it: `pilot_studies.py` (A to J), `c22_pilot.py` (K), `lw_pilot.py` (L), `s51_backing.py` (M), `s54_levers.py --check` (N), `s52_shock.py` (O), `s53_security.py --check` and `s19_series.py` (P, R), `merge_panel.py` (R-panel). Timings from the dry run replace section 3's estimates.

## 8. Where it runs, and the cost
- **Cheapest split, and the route Duke chose (Amendment 1): everything on GitHub Actions, at no cost.** No job exceeds the thresholds of `prereg/RUNNING.md` section 5 (about 1,000 core-hours in one study, or 6 hours in one process). The pilots of S35 and S51 to S54 ran there with no objection from GitHub.
- **Caution (ledger I16):** GitHub's terms describe Actions as being for building, testing and deploying a repository's own software. The batch is about 670 runner-hours, several times the pilots. If GitHub objects, the Runpod route (RUNNING.md section 6) takes the rest from the piece where it stopped.
- **Runpod, if used** (a 16-vCPU CPU pod at $0.48 an hour, the price paid on Oct 12, 2026; to be re-checked when the key is added; a vCPU counted as half a core, as on Actions): the two largest pieces (study A at 50,000 adults and study N, about 760 core-hours) take about 95 pod-hours, about $46; the whole batch (about 1,340 core-hours) about 170 pod-hours, about $80. The dry run's timings replace these figures.

## Amendments
Dated, with the reason, below this line.

### Amendment 1 (Nov 5, 2026, S47 part 2, before any 500-seed run): the batch runs on GitHub Actions
- **Duke's choice** (in the S47 part 2 session, Nov 5): the batch runs on GitHub Actions, as section 8's cheapest split proposed, not on Runpod. Step 5's ledger decision no longer asks for the Runpod key or a choice of route; it records that the design is frozen and that S48 runs on Actions.
- **What it changes:** S48 starts once the freeze is complete (section 6 landed, engine pinned, every job's 2-seed dry run passed); it no longer waits for a Runpod key. Nothing in the design changes. Dispatch stays as section 5 says (`--procs=2`, shards under 2 hours, at most 20 runners at once).
- **If GitHub objects or limits the runs** (ledger I16): S48 stops where it is (every piece is resumable), and moving the rest to Runpod becomes a new ledger decision with its cost; nothing that costs money runs before Duke answers it and adds the key.
- Why: the first estimate (section 8) puts every job under RUNNING.md's thresholds, at no cost; Duke prefers that route.

### Amendment 2 (Nov 5, 2026, S47 part 2, before any 500-seed run): the fourth fix built, and all of them measured
- **Built:** `fx` part `sp` (compassionism-simulation pull request 74). Each year's capacity for the essentials now comes from the study's own no-programme testbed run: the same seed, environment, population and economy-wide rules. Until now it came from a separate price-only run with no job loss, safety net or labour response, always at 500 adults. With `sp`, a no-programme row's essentials prices stay exactly still. `fx: true` is all four parts.
- **Measured** (Simulation `dev/reports/s47-fx.md`; seeds 1-50, all three environments, none, the release design and the C2.2 design, published vs `au` vs each part vs frozen). `sp` removes the no-programme drift (0.7% by year 20 in Reference), lowers basket poverty without a programme by 0.3 to 0.4 points, and lowers programme inflation by 0.24 to 0.59 points a year. `pthb`, `hb` and `ab` move no outcome beyond its interval (`ab` only the work-rule count). The audit's corrections stay the larger change. No programme effect changes direction.
- **Decision:** the freeze keeps every part on (section 1 unchanged). Section 1's engine commit is pinned when the rest of section 6 has landed.
- **For the job scripts (item 6-7):** `fx: true` on a row now includes `sp`, so no job needs a separate option. Study R's "audit's corrections only" rows stay `au: true` with no `fx`.

### Amendment 3 (Nov 6, 2026, S47 part 3, before any 500-seed run): the spending share, re-derived
- **What was asked** (section 6 item 4; outside audit E17): repeat the derivation of the 0.593 spending share by its own method on the frozen model's no-programme run. The method: the share of cash surplus consumed at which that run saves 5.4% of income, the US personal saving rate in 2025 (BEA NIPA Table 2.1, line 35), in Reference over seeds 1-100.
- **Found** (Simulation `dev/reports/s47-spend.md`, `dev/tools/s47_spend.js`, `dev/runs/s47-spend/rederive.json`):
  - At 0.593 the frozen no-programme run saves 19.5% of disposable income. Re-derived: **0.877** on saving over disposable income, 0.862 on the method's own formula over wages.
  - The original derivation's ledger also counted the supply-path run and a repeated year 0. Counted as it was then, the published run reproduces 5.40% at 0.593, so the new tool counts as the old one did before the faults are removed.
- **Decision:** every frozen row uses 0.877 (`SPEND_FROZEN`, set by `frozenRow`). Saving over disposable income is the reading because the 5.4% target is a share of disposable income, and the frozen run has income besides wages: Social Security, unemployment insurance, the safety net's cash net of tax, and income-graded spending. The published engine and study R's published rows keep 0.593. This re-derives a constant by its own method. No programme figure was used to choose it.
- **Measured effect** (50 paired seeds, all three environments, no programme and both designs on the frozen engine at 0.593, 0.779 and 0.877; `dev/tools/s47_spend_effect.js`, tables `dev/reports/s47-spend-tables.md`):
  - Basket poverty and programme inflation do not move (at most 0.1 point).
  - Median real wealth with no programme falls by about half (Reference: $409,000 to $212,000).
  - The programme's effect on year-20 wealth poverty rises: C2.2 from −17.4 to +0.5 points in Reference, −17.4 to +30.1 in Adverse, −7.8 to +41.7 in Stress; the release design from −3.5 to +21.4 in Reference. These are far outside their intervals.
  - The design-neutral BLEI effect moves by under a point.
- **Added rows:** study R runs the frozen engine at 0.593 for none and both designs (3 rows per yardstick and horizon; section 4), so the release panel shows how much of the frozen model's wealth result comes from the share.
- **Nothing else moves:** no other constant, row, outcome or decision rule. The fix measurements of Amendment 2 were made at 0.593; they measure the fixes, and stay as they are.
