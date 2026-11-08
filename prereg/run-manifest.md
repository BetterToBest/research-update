# Run manifest: the full study batch (S47 design freeze, for S48)

Written Nov 5, 2026 by S47, before any 500-seed run. This file lists every job the batch runs: its rows, environments, seeds, population, horizon, outputs, and which later step reads them. S48 runs it exactly. It is the record the study programme (`prereg/2026-11-study-program.md`, Amendment 9) and each addendum point to.

**Status: frozen (Nov 6, 2026, S47 part 5).** Every section 6 item has landed, the engine commit is pinned (section 1), and every job passed its 2-seed dry run and loads in its consumer (section 7). S48 runs this file exactly, on GitHub Actions (Amendment 1), with the dispatch of section 3. A change after this point is a dated amendment to the preregistration it touches and a new S47 pass; a job that fails is rerun from its shard, never redesigned.

## 1. The model being frozen
- **Engine:** BetterToBest/compassionism-simulation at commit `ce8d030b8d16a752706c4ea2db71196e11e73831` (pinned Nov 6, 2026, S47 part 4: pull request 76's merge, after every section 6 item landed). Every job runs in a clean checkout of that one commit, with the job scripts of BetterToBest/compassionism-sim-results at `031861a` (pull request 16) or later.
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

Runner-hours are for 500 seeds, measured by the 2-seed dry run on GitHub-hosted runners (section 7; Nov 6, 2026): each job's wall-clock seconds for seeds 1-2 (seeds 501-502 for N3 and N3x) times 250. They include each process's start-up, so they are upper bounds. Before the dry run they were estimated from the pilots (the previous estimate is in brackets). "Rows per environment" counts each yardstick as its own row and, where a job runs both horizons, counts the 20- and 40-year runs once (the folders hold both). "Shards" is the dispatch: seeds per shard sized so no shard runs over 2 hours at the measured rate (the workflow stops a shard at 350 minutes).

| Job | Script and arguments | Rows per environment | Adults | Years | Seeds | Runner-hours (estimate) | Shards (seeds each) | Folder |
|---|---|---|---|---|---|---|---|---|
| R release panel and bridge | `program.js --study=R --env=all --procs=2` | 21 rows x 2 yardsticks | 500 | 20, 40 | 1-500 | 8.6 (6) | 5 (100) | `prog-r-<engine>` |
| R-panel (page format) | `panel.js --n=500 --parts=5` (published engine) and `panel.js --n=500 --parts=5 --frozen`: each shard runs one environment, horizon and fifth of the rows of `harness.js testbed 500 release ENV --v54 --snab --slope [--years=40] [--frozen] --part=I/5` on all 500 seeds | the testbed's (51; 52 frozen) | 500 | 20, 40 | 1-500 | 27.5 + 30.1 (2) | 30 + 30 (workflow seeds 1-30: environment, horizon and piece) | `panel-<engine>`, `panel-frz-<engine>` |
| A scale, 500 to 10,000 adults | `program.js --study=A --env=all --procs=2 --sizes=500,2000,10000` | 12 per size | 500, 2,000, 10,000 | 20, 40 | 1-500 | 40.1 (187 with A50) | 25 (20) | `prog-a-<engine>` |
| A50 scale, 50,000 adults | `program.js --study=A --env=all --procs=2 --sizes=50000` | 6 | 50,000 | 20, 40 | 1-500 | 130.3 | 100 (5) | `prog-a50-<engine>` |
| B synergy | `program.js --study=B --env=all --procs=2` | 192 | 500 | 20, 40 | 1-500 | 25.8 (29) | 20 (25) | `prog-b-<engine>` |
| B10 synergy at scale | `program.js --study=B10 --env=all --procs=2` | 64 | 10,000 | 20 | 1-500 | 54.5 (66) | 50 (10) | `prog-b10-<engine>` |
| C ageing | `program.js --study=C --env=all --procs=2` | 12 | 500 | 20, 40 | 1-500 | 3.5 (2) | 2 (250) | `prog-c-<engine>` |
| D participation | `program.js --study=D --env=all --procs=2` | 46 | 500 | 20, 40 | 1-500 | 6.2 (10) | 4 (125) | `prog-d-<engine>` |
| D10 participation at scale | `program.js --study=D10 --env=all --procs=2` | 12 | 10,000 | 20 | 1-500 | 18.7 (19) | 10 (50) | `prog-d10-<engine>` |
| F debt reading | `program.js --study=F --env=all --procs=2` | 12 | 500 | 20, 40 | 1-500 | 2.2 (2) | 2 (250) | `prog-f-<engine>` |
| G layer synergy | `program.js --study=G --env=all --procs=2` | 36 | 500 | 20, 40 | 1-500 | 6.9 | 4 (125) | `prog-g-<engine>` |
| G10 layer synergy at scale | `program.js --study=G10 --env=all --procs=2` | 32 | 10,000 | 20 | 1-500 | 31.1 | 20 (25) | `prog-g10-<engine>` |
| H layer design parameters | `program.js --study=H --env=all --procs=2` | 18 | 500 | 20, 40 | 1-500 | 4.3 | 4 (125) | `prog-h-<engine>` |
| I PTF starting size | `program.js --study=I --env=all --procs=2` | 12 | 500 | 20, 40 | 1-500 | 3.2 | 2 (250) | `prog-i-<engine>` |
| J layer at scale | `program.js --study=J --env=all --procs=2` | 4 | 2,000, 10,000 | 20, 40 | 1-500 | 13.2 (G to J: 50) | 10 (50) | `prog-j-<engine>` |
| K coverage and adequacy | `c22.js --env=all --procs=2 --frozen` | 13 | 500 | 20, 40 | 1-500 | 6.1 (6) | 4 (125) | `k-<engine>` |
| L cost-of-living line | `lw.js --env=all --procs=2 --frozen` | 9 | 500 | 20, 40 | 1-500 | 1.2 (4) | 1 (500) | `l-<engine>` |
| M backing | `backing.js --env=all --procs=2 --frozen` | 466 | 500 | 20 | 1-500 | 32.1 (29) | 20 (25) | `m-<engine>` |
| N1 levers, stage 1 | `levers.js --stage=1 --env=all --procs=2 --frozen --gzip` | 520 | 500 | 20 | 1-500 | 47.0 (190 with N2) | 25 (20) | `n1-<engine>` |
| N2 levers, stage 2 | `levers.js --stage=2 --env=all --procs=2 --frozen --gzip` | 1,164 | 500 | 20 | 1-500 | 105.0 | 100 (5) | `n2-<engine>` |
| N3 levers, stage 3 | `levers.js --stage=3 --list=FILE --env=all --procs=2 --frozen --gzip` (list derived from N1 and N2 by rule 4, in a dated amendment) | the front's size (250 in the pilot and the dry run) | 500 | 20 | 501-1000 | 17.4 at 250 rows (30) | 10 (50) | `n3-<engine>` |
| N3x stage 3 on the shock path | as N3, with `--sx=main` | as N3 | 500 | 20 | 501-1000 | 24.4 at 250 rows (30) | 20 (25) | `n3x-<engine>` |
| O supply shock | `shock.js --env=all --procs=2 --frozen` | 70 | 500 | 20 | 1-500 | 6.2 (5) | 4 (125) | `o-<engine>` |
| P security | `security.js --env=all --procs=2 --frozen` | 12 | 500 | 20 | 1-500 | 0.9 (1) | 1 (500) | `p-<engine>` |
| X per-year series | `series.js --n=500 --frozen`: each of 6 shards runs `explore_export.js ENV YRS 500 1 --v54 --snab --slope --suite --frozen` for one environment and horizon (no programme, the C2.2 design, the release design); checked against the merged frozen panel afterwards (`--panel=FILE`) | 3 | 500 | 20, 40 | 1-500 | 1.8 (2) | 6 (workflow seeds 1-6) | `x-<engine>` |
| **Total** | | | | | | **648 (about 670)** | **about 510** | |

About 650 runner-hours is about 33 hours on 20 runners at once, plus queueing. N3's and N3x's hours scale with the size of the front rule 4 picks (here the pilot's 250 rows). With `--env=all`, the levers job runs one process per environment (3 processes on the runner; `levers.js` gives each environment at least one), the setting the dry run timed. Peak memory: 1.8 GB (N2), 1.3 GB (A50); a runner has 16 GB.

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
5. MODEL_SPEC.md and TESTBED_SPEC.md written for the frozen model (every switch its rows turn on; the S50 contradictions corrected and its 30 gaps closed). **Done Nov 6** (Simulation pull request 76): MODEL_SPEC.md section 13 (the frozen model and the C2.2 design), the eight contradictions corrected where they occur, Appendix C (the 30 gaps); TESTBED_SPEC.md section 6 (what each job switches beyond the frozen engine).

Jobs (compassionism-sim-results `runner/jobs/`; each with `--check` of its row counts):
6. `program.js`: studies R, G, G10, H, I, J; both designs in A, B, B10, C, F; D and D10 at 2% and 5%; `au` and `fx` on every row; nulls for missing keys. **Done Nov 6** (results pull request 16). Rows are named `ENV.nN.yY.DESIGN.ROW` (`c22` or `rls`); R's `ENV.n500.yY.YARD.ENGINE.DESIGN[.READING]`. `null` also for the mean octave (`octMean`) on rows without CCO, where the C2.2 design's automatic receipt would count adults who receive no BU, and for keys a row's switches do not report. `--check` passes: every row count; R's published rows equal `release-pair.js`; B's none row and cells without CCO equal on the two designs; R's `wout` rows equal its frozen rows in Reference.
7. `--frozen` (the `au` and `fx` options on every row) in `c22.js`, `lw.js`, `backing.js`, `shock.js`, `security.js`, `levers.js`; backing's 116 added rows; levers' key trim, gzip and `--sx=main`. **Done Nov 6** (results pull request 16): `--frozen` is each job's batch version (shock's adds `sec`, the security outputs and the S19 series; levers' adds the money-income falls by cause); backing 466 rows; security 12 (the C2.2 design's savings rows); levers `--sx=main` and `--gzip` (the run-study workflow compresses the checked shards; `s54_levers.py` reads them). The R-panel and X jobs run through two wrappers, `panel.js` and `series.js` (section 3), because their engine commands average over all seeds in one process.

## 7. Dry run
Every job at seeds 1-2 on Actions, one shard each (`run-study`, study id `dry-<job>`).

**Dispatched Nov 6, 2026 (S47 part 4), engine `ce8d030`, 26 runs** (folders `dry-<id>-ce8d030` in compassionism-sim-results, each with `DONE` when finished):
- `program.js --env=all --procs=2`, seeds 1-2: `dry-r` (R), `dry-a` (A at 500, 2,000 and 10,000 adults), `dry-a50` (A at 50,000: memory at 2 processes), `dry-b`, `dry-b10`, `dry-c`, `dry-d`, `dry-d10`, `dry-f`, `dry-g`, `dry-g10`, `dry-h`, `dry-i`, `dry-j`.
- `--env=all --procs=2 --frozen`, seeds 1-2: `dry-k` (`c22.js`), `dry-l` (`lw.js`), `dry-m` (`backing.js`), `dry-o` (`shock.js`), `dry-p` (`security.js`).
- `levers.js --env=all --procs=2 --frozen --gzip`: `dry-n1` (`--stage=1`) and `dry-n2` (`--stage=2`) at seeds 1-2; `dry-n3` (`--stage=3`) and `dry-n3x` (`--stage=3 --sx=main`) at seeds 501-502, on the pilot's stage-3 list (`levers-stage3.json`; the batch's list comes from N1 and N2 by rule 4).
- `panel.js --n=2 --parts=1` (`dry-panel`, the published engine) and the same with `--frozen` (`dry-panel-frz`), seeds 1-6 in 6 shards; `series.js --n=2 --frozen` (`dry-x`), 6 shards. For each: the folder is `DONE`, checksums pass, and the consumer's script loads it: `pilot_studies.py` (A to J), `c22_pilot.py` (K), `lw_pilot.py` (L), `s51_backing.py` (M), `s54_levers.py --check` (N), `s52_shock.py` (O), `s53_security.py --check` and `s19_series.py` (P, R), `merge_panel.py` (R-panel). Timings from the dry run replace section 3's estimates.

**Result (Nov 6, 2026, S47 part 5): every job passed.** All 26 folders arrived with `DONE`, and every file matches its `SHA256SUMS`. The consumers read them as follows:
- **A to J and R** (`program.js`): `dev/tools/batch_load.py --check` (Simulation pull request 77) passes on all 14 folders. It checks contiguous seeds, one engine commit, the same rows in every environment, the primary outcomes finite in every row, and keys past a row's horizon null. Row counts per environment, with both horizons where the job runs them: R 84, A 72, A50 12, B 384, B10 64, C 24, D 92, D10 12, F 24, G 72, G10 32, H 36, I 24, J 8. `pilot_studies.py` hard-codes the pilot folders and 50 seeds. Its readers get the batch through `batch_load.by_design()`, which gives one design's rows under the pilots' names. Every pilot row name and key of A, B and D is present, so S36 changes only the folder and the seed count.
- **K** `c22_pilot.py` and **L** `lw_pilot.py`: both write their tables (2,412 and 2,100 estimates). **M** `s51_backing.py` and **O** `s52_shock.py`: both write their tables.
- **N** `s54_levers.py --check`: PASS. Stage 1 has 1,560 rows and stage 2 has 3,492 (520 and 1,164 per environment). Stages 3 and 3x have 750 rows each. Every key is present. Stage 1's keys include `secU25` and `secM3` and the money-income falls by cause (`secF25*`).
- **P and R** `s53_security.py --check`: PASS (P 30 rows, R 252 rows). `s19_series.py`: PASS on P, R (20 and 40 years) and O. Yearly basket poverty and FGT1, weighted by adults, equal the person-year figures within 1.4e-14. R's 40-year rows failed at first because both readers assumed one horizon per file. Both now read each row to its own horizon (Simulation pull request 77). The job output was complete.
- **R-panel**: both panels (published and frozen) merge through `merge_parts.py` and `merge_panel.py`. `merge_parts.py` now reads `panel.js`'s pieces (pull request 77). Each environment holds 51 rows (52 frozen, with the `c22` row).
- **X**: `explore_export.js ... --suite --frozen --panel=FILE` passes its self-check against the merged frozen dry-run panel (Reference 20 years, Stress 40 years). The Actions shard for Reference, 20 years matches a run on the session machine byte for byte.
- **Timings** are in section 3. Two changes to the dispatch, neither to any row (Amendment 4): A runs as two dispatches by size, and the R-panel in 5 pieces per environment and horizon. The R-panel's cost was under-estimated (58 runner-hours, not 2). The total is about 650 runner-hours.

## 8. Where it runs, and the cost
- **Cheapest split, and the route Duke chose (Amendment 1): everything on GitHub Actions, at no cost.** No shard runs over 2 hours at the dry run's measured rate (section 3). No study exceeds the thresholds of `prereg/RUNNING.md` section 5 (about 1,000 core-hours in one study, or 6 hours in one process). The largest are A50 (about 260 core-hours) and N2 (about 210). The pilots of S35 and S51 to S54 ran there with no objection from GitHub, and so did the dry run (26 runs, 38 shards).
- **Caution (ledger I16):** GitHub's terms describe Actions as being for building, testing and deploying a repository's own software. The batch is about 650 runner-hours in about 510 shards, several times the pilots. If GitHub objects, the Runpod route (RUNNING.md section 6) takes the rest from the shard where it stopped, after a new ledger decision and Duke's key.
- **Runpod, if used.** Prices: a 16-vCPU CPU pod at $0.48 an hour (the price paid on Oct 12, 2026; to be re-checked when the key is added). A vCPU counts as half a core, as on Actions, so a 4-vCPU runner-hour is 2 core-hours and a pod-hour is 8. On the dry run's timings, the batch is about 1,300 core-hours, about 162 pod-hours, about $78. The two largest pieces (A50 and study N, about 323 runner-hours or 650 core-hours) take about 81 pod-hours, about $39.

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

### Amendment 4 (Nov 6, 2026, S47 part 5, before any 500-seed run): the dry run's timings and the dispatch
- **What changed:** section 3's runner-hours are now the dry run's measurements, and each job has a shard plan. Two dispatch changes: study A runs as two dispatches, `--sizes=500,2000,10000` (`prog-a-<engine>`) and `--sizes=50000` (`prog-a50-<engine>`). The R-panel runs in 5 pieces of rows per environment and horizon (`--parts=5`, 30 shards per panel).
- **Why:** a 50,000-adult seed takes about 15.6 minutes on a runner, against about 4.8 minutes for all of the smaller sizes together. With all sizes in one shard, a 2-hour shard would hold 5 seeds of everything, or the small sizes would take 100 shards. The R-panel's testbed runs every seed in one process (it is cut by rows, not seeds). At 500 seeds its slowest environment and horizon takes about 8.3 hours whole. Five pieces keep each under 2 hours. The pre-dry-run estimate of 2 runner-hours came from the pilots' per-row cost and missed the testbed's 51 rows.
- **What it does not change:** no row, seed, setting or output. Rows are separate runs on the same seeds (common random numbers), so how they are split into processes or shards changes no figure. `merge_parts.py` checks this: a row in two pieces must be identical. The folders' consumers join the shards as they did in the dry run. `program.js`'s `--sizes` was written for pilots, and here it is the batch's dispatch of A. The two A folders together hold exactly the rows of `program.js --study=A`, which `--check` counts.
- **Consumers fixed, not jobs:** three readers did not load the dry run. `s19_series.py` and `s53_security.py --check` read R's 40-year rows as 20-year rows, and `merge_parts.py` did not accept `panel.js`'s pieces. `pilot_studies.py` cannot read batch folders. The readers were fixed and a batch loader added (Simulation pull request 77, tools only). The job outputs were complete.


### Amendment 5 (Nov 8, 2026, S48 part 3, after the batch ran): how R and O are stored, and how X was checked
- **What happened:** study R (`prog-r`, run 59) and study O (`o`, run 64) computed every shard, but the workflow's last job could not commit them, twice. The cause was not the push race noted on Nov 7. Each shard file was over GitHub's 100 MB file limit (R about 125 MB, O about 207 MB), and neither job ran with `--gzip`. The dry run, at 2 seeds, could not show it.
- **What was done:** the shard artifacts were downloaded before they expired (each zip's SHA-256 equal to GitHub's recorded digest) and checked with `runner/check-shards.js`, exactly as the last job does (passed). They were then compressed with `gzip -n -9`, as the workflow does for `--gzip` jobs. Gunzip gives back the run's bytes, checked file by file. The folders carry run.txt (with a line saying so), SHA256SUMS and DONE (results pull request 19). Four readers (`batch_load.py`, `s53_security.py`, `s19_series.py`, `s52_shock.py`) now read `.json.gz` (Simulation pull request 78, tools only).
- **X's check:** `explore_export.js ... --panel=FILE` compares the series' yearly means, rounded as the panel rounds them, with the merged frozen panel. The X shards store exactly those means. So the comparison was made on the stored means (`dev/tools/x_panel_check.js`), without rerunning X: all 2,160 equal the panel. The merged panels (published and frozen, 20 and 40 years) are kept in `panel-merged-<engine>` (results pull request 20).
- **What it does not change:** no row, seed, setting, output or figure. No shard was rerun.

### Amendment 6 (Nov 8, 2026, S55 part 2, before any run of these jobs): the open-access jobs
- **What is added:** the jobs of `prereg/2026-11-ptf-access-addendum.md`. They are not part of the frozen batch; they pair with it. Engine: BetterToBest/compassionism-simulation at `0c93593e1ea502555387e42215b79f290a60f127` (pull request 82). With `PTF_ACCESS` off it reproduces the frozen engine `ce8d030` figure for figure (guard test; engine lineage link 8bb948abed0e → 68b5d6170719). Job script: compassionism-sim-results `runner/jobs/program.js` (pull request 21), whose `--check` confirms each open row is a frozen row with `pa` added.

| Job | Script and arguments | Rows per environment | Adults | Years | Seeds | Runner-hours (estimate) | Shards (seeds each) | Folder |
|---|---|---|---|---|---|---|---|---|
| T open access | `program.js --study=T --env=all --procs=2` | 2 | 500, 10,000 | 20, 40 | 1-500 | 6 | 10 (50) | `prog-t-<engine>` |
| U open factorial | `program.js --study=U --env=all --procs=2` | 32 | 500 | 20, 40 | 1-500 | 4 | 4 (125) | `prog-u-<engine>` |
| U10 at scale | `program.js --study=U10 --env=all --procs=2` | 32 | 10,000 | 20 | 1-500 | 27 | 20 (25) | `prog-u10-<engine>` |
| V open layer | `program.js --study=V --env=all --procs=2` | 62 | 500 | 20, 40 | 1-500 | 12 | 10 (50) | `prog-v-<engine>` |
| V10 open layer at scale | `program.js --study=V10 --env=all --procs=2` | 32 | 10,000 | 20 | 1-500 | 31 | 20 (25) | `prog-v10-<engine>` |
| VJ open layer, other sizes | `program.js --study=VJ --env=all --procs=2` | 2 | 2,000, 10,000 | 20, 40 | 1-500 | 7 | 5 (100) | `prog-vj-<engine>` |
| W fixed-share sweep | `program.js --study=W --env=all --procs=2` | 20 | 500 | 20, 40 | 1-500 | 3 | 2 (250) | `prog-w-<engine>` |
| W10 sweep at scale | `program.js --study=W10 --env=all --procs=2` | 20 | 10,000 | 20 | 1-500 | 17 | 10 (50) | `prog-w10-<engine>` |
| Y growth settings | `program.js --study=Y --env=all --procs=2` | 12 | 500 | 20, 40 | 1-500 | 2 | 2 (250) | `prog-y-<engine>` |
| **Total** | | | | | | **about 108** | **83** | |

- **Pilot first** (addendum, Pilot first): seeds 1-50, `--sizes=500 --years=20`, one dispatch each for T (with `--members`), U, V, W and Y, one shard each, folders `pilot55-<study>-<engine>`. T's members-only rows must equal `prog-a-ce8d030`'s values for seeds 1-50 on every kept measure. Shards are sized from the pilot's timings before the 500-seed dispatch; a change of shards changes no figure (seeds are paired and independent).
- **Who reads them:** S55 part 3's report (open against members on every preregistered outcome, the fixed-share curve, which limit binds), with the frozen batch's A, B, B10, G, G10, H, I and J folders as the members-only side. S7's release carries both readings behind the switch.
- **What it does not change:** no job, row, seed, setting or output of the frozen batch.

### Amendment 7 (Nov 8, 2026, S55 part 3): pilot checked, shards sized, the nine jobs dispatched
- **Pilot result (seeds 1-50, 500 adults, 20 years):** T's members-only rows equal study A's (`prog-a-ce8d030`) for seeds 1-50 on all 55 kept measures in all six rows (3 environments × 2 designs); the 17 access keys (`pa*`, `pfMem`, `pfCut`) exist only in T. Row counts per environment match Amendment 6 (T 4 with members rows, U 32, V 62, W 20, Y 12); every seed array holds 50 values, none non-finite. Pilot timings (seconds per seed for three environments, 4 processes): T 1.33 (with members rows), U 5.2, V 22.9, W 5.0, Y 5.7.
- **Shards re-sized from the timings** (the frozen batch's own timings give the scale: 10,000 adults cost about 21 times 500 adults, 40 years about 1.8 times 20 years). Largest expected shard is V10 at about 1.7 hours, under the 6-hour job limit; a change of shards changes no figure. Runs use `--procs=4` (a runner has 4 vCPUs; processes never change bytes, S33). Expected total about 96 runner-hours, inside Amendment 6's 108.

| Job (study id) | Shards (seeds each) | Run |
|---|---|---|
| T `prog-t` | 10 (50) | [86](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472393103) |
| U `prog-u` | 4 (125) | [87](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472395687) |
| U10 `prog-u10` | 20 (25) | [88](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472398061) |
| V `prog-v` | 10 (50) | [89](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472400373) |
| V10 `prog-v10` | 20 (25) | [90](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472402724) |
| VJ `prog-vj` | 10 (50; was 5) | [91](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472404743) |
| W `prog-w` | 5 (100; was 2) | [92](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472407087) |
| W10 `prog-w10` | 20 (25; was 10) | [93](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472409538) |
| Y `prog-y` | 4 (125; was 2) | [94](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42472411721) |

- Total 103 shards (Amendment 6 said 83). Engine `0c93593e1ea502555387e42215b79f290a60f127`, seeds 1-500, `job=program.js`, `job_args=--study=<S> --env=all --procs=4`. Folders `prog-<study>-0c93593` with `DONE` when every shard is in. No row, outcome, seed or rule changed.
