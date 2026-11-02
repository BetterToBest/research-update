# Preregistration addendum: an outside supply shock, and whether PTF and PTH protect the basics (S52, study O, for S47)

Committed Nov 2, 2026 by S52, before any run of these rows. One disclosure: before this file was committed, the engine switch, the job and the analysis script were tested on seeds 1-2 on the session machine (Reference), to check that they run, that a shock of size 0 changes nothing, that the no-programme run passes the whole shock on, and that the tables form. Those numbers are not results and are not used. The tests changed three things in this file, none of them a constant or a row of the grid: the BU absorbs much of the shock for participants (their money costs exclude BU spent on essentials), so the group "everyone else" was split into CCO participants in neither PTF nor PTH (P) and adults in none of the three (N), to keep the BU's protection apart from PTF's; PTH's comparison group became P rather than N for the same reason; and the unshocked rows run with a shock of size 0, which changes no figure but records the measures the pairing needs.

## Why
The Hub says PTF and PTH give stable, affordable access to the basics, and that PTF communities resist shocks, "energy price manipulation" included. The model has had recessions and steady outside inflation, but never a sudden outside jump in the price of the basics. S52 adds one: an energy price spike that reaches food, transport, utilities and heating, whatever its cause. It separates the markup part of the rise, which PTF can remove, from the real-cost part, which it can remove only by sourcing locally.

## Plain-words summary
- **Q14 (primary).** In an energy price shock, what share of the rise in the basics reaches the money costs of PTF members, PTH members, other participants, and adults outside the programme? How does it compare with no programme?
- **Q15.** How much does it depend on how much of the market's rise is markup (none, a quarter, a half), and on PTF's local sourcing (none to all)?
- **Q16.** Does the shock raise basket poverty, during and after it, and for whom? Does it make essential costs jump more from year to year?
- Two designs: the release row as released, and the C2.2 design (study programme Amendment 4).
- **Pilot now:** seeds 1-50 on GitHub Actions, labelled pilot throughout. **Full:** seeds 1-500 in the S48 batch, after the S47 freeze.

## Design
**The environment** (preset key `sx`; engine reading `dev/reports/s52-supply-shock-reading.md`, readings X1-X9). The real price of energy rises by E over two years from year 5 (half in the first year), then falls back over two years to a share `keep` of the rise, which stays. Each category's price is multiplied by (1 + e)^beta: food 0.101, transport 0.390, housing by its utilities' share (12.8%) of household energy's 0.488; other categories, rents and medical care 0. The shock is layered on each of the three environments (Reference, Adverse, Stress) and is the environment's, so the no-programme run faces it too.

**PTF and PTH** (design parameters): a PTF member pays PTF's price before the shock plus (1 − m)(1 − s(1 − kap)) of the market's dollar rise in food and utilities; with pooling, that rise is the average over the last `pool` years. PTH's housing cut is on housing before the shock, so a PTH household pays its utilities' rise unless it is also a PTF member. Transport is outside PTF in the model and reaches members in full.

**Constants** (none is fitted to any result):

| Parameter | Values | Basis |
|---|---|---|
| E, rise in the real energy price at the peak | 0.328 (main); 0.246, 0.373; 0.655 | US CPI energy over core, 1967-2024 (BLS via FRED, opened Nov 2, 2026; `sources/s52_energy_shock.py`): the median of the three largest episodes (1972-74, 1978-80, 2020-22), the other two, and twice the median (beyond history, labelled so) |
| keep, share of the rise still there two years after the peak, and after | 0.88 (main); 0.51, 1 | the same episodes: median, 2020-22, 1972-74 |
| t0, ramp, fall | year 5; 2 years; 2 years | t0: design parameter (the programme has matured); ramp and fall: the episodes |
| beta: food, transport, household energy | 0.101, 0.390, 0.488 | the same data: two-year changes relative to core, OLS, 1969-2024 |
| m, markup share of the market's rise | 0.25 (main); 0, 0.5 | design parameter; sourced range: Kansas City Fed Economic Review 108(1), 2023 (markups 3.4% against 5.8% inflation in 2021, then falling in the second half); IMF WP/23/131, 2023 (no widespread rise in markups) |
| s, PTF's local-sourcing share | 0 (main); 0.25, 0.5, 1 | design parameter (the Hub gives no share) |
| kap, the shock's reach into local supply | 0.5 (main); 0 | design parameter |
| pool, years PTF spreads a cost rise over | 1 (main); 3 | design parameter |

**Rows** (job `runner/jobs/shock.js` in compassionism-sim-results; `--check` confirms 70 rows per environment). Every row is the runner's reference job (release-pair.js settings) with only the named change. Per design (rel, the release row; c22, the C2.2 design, CPS yardstick), 35 rows:

| Shock path | Rows | Count |
|---|---|---|
| off (no shock: a shock of size 0, which changes no figure (unit test) and records the measures) | none; the programme | 2 |
| main | none; the programme at m {0, 25, 50}% x s {0, 25, 50, 100}% (kap 50%, pool 1) | 1 + 12 |
| main | kap 0 at s {25, 50, 100}% (m 25%); pool 3 at s {0, 50}% (m 25%) | 5 |
| e246, e373, e655, k51, k100 | none; the programme at the main reading and at s 50% | 5 x 3 |

- Environments: Reference, Adverse, Stress, each with the shock layered on.
- Seeds: pilot 1-50; full 1-500. Paired across all rows (common random numbers).
- 500 adults, 20 years.
- Engine: compassionism-simulation commit `98b61000697078619b496b1cca0f3bf495de73b2` (pull request 64; the merge commit).
- Where: GitHub Actions, workflow `run-study`, study `s52-shock`, job `shock.js`, `job_args` `--env=all --procs=4`, 10 shards; folder `s52-shock-98b6100/` in compassionism-sim-results. Seeds 1-500 join the S48 batch.

## Outcomes
Groups (each year): F, PTF members; H, PTH members not in PTF; P, CCO participants in neither; N, adults in none of the three; X, adults who chose not to take part (the same adults in every design and in the no-programme run); A, all. Windows: B, before the shock (years 0-4); D, during it (years 5-8); After (years 9-19). For each group and window: own money cost (`sxC`), the same basket at market prices (`sxM`), basket poverty (`sxP`); and the volatility of the group's costs (`sxV`).
- **Primary (Q14): the share of the shock reaching a group** during the shock, R_g = [sxC_Dg(shocked) − sxC_Dg(off)] / [sxM_Dg(shocked) − sxM_Dg(off)], each against the same design's off row on the same seed. For the no-programme row, R is 1 by construction (unit test); for groups X, its R is the comparison.
- **Confirmations:** the same share after the shock (window After); basket poverty during and after the shock (`sxP`, and `fgt0PY` over the run), as differences shocked minus off; wealth poverty at year 20 (`pov`) (guardrail 6).
- **Secondary:** volatility `sxV` (shocked minus off); programme cost (`cost`, `cBU`, `srcPay`, `srcM`); programme inflation (`endoAnn`, `pLev20`, `plv_0`..`plv_19`); participants' and non-participants' basket and wealth poverty over the run (`gPartF0`, `gNonF0`, `gPartW`, `gNonW`); PTF membership and its cut (`pfMem`, `pfCut`); participation in year 19 (`jnP19`); Gini (`giniD`); median real wealth (`medWealthReal`).

## Analysis
- **R_g:** the ratio of the seed-mean differences (numerator and denominator each averaged over seeds, then divided). 95% interval: paired bootstrap over seeds, 2,000 replicates, seed 52 for the resampler, the same resample for every row.
- **Protection by a part of the design:** PTF's protection is 1 − R_F at the PTF reading against 1 − R_F at m 0, s 0 (no markup, no local sourcing: what remains is the BU's and the household mix's); the BU's is set beside it as R_N less R_P (other CCO participants hold BU; adults in none of the three do not). PTH's is R_P less R_H (both groups mostly hold BU; PTH members differ by PTH), with the caveat that the groups differ in who they are. Each difference with its paired bootstrap interval.
- **No harm:** R_N and R_X (programme) against R for all adults in the no-programme row; basket poverty of X, shocked minus off, programme against no programme (a difference in differences, with its interval).
- **By construction, said so:** R_N = 1 and the no-programme row's R = 1 follow from the rules; so does the order R_F(m 50) ≤ R_F(m 25) ≤ R_F(m 0) at the same s. What emerges: the BU's share, the poverty effects, participation, programme inflation and costs.
- **Multiple comparisons:** intervals unadjusted at 95%; every row published. No single favourable setting is reported alone.

## Decision rules
1. **PTF protects** in this shock if 1 − R_F at the main reading exceeds 1 − R_F at (m 0, s 0) with the difference's 95% interval above zero. The report gives the size in plain words (for example, "PTF members pay x% of the rise; without PTF's markup removal they would pay y%"). If not, it says PTF does not measurably protect members from this shock and why (transport is outside PTF; the rise is mostly real cost).
2. **Local sourcing** is credited only as an upper bound (no normal-times price premium is modelled), and only from the rows with kap 50%; kap 0 is labelled optimistic.
3. **PTH protects** in this shock only if R_H is below R_P with the interval of the difference above zero. The reading (X7) predicts it does not, except through PTF membership; the report says which.
4. **Harm:** if basket poverty of X rises more under the programme than under no programme (interval above zero), the report says the shock harms non-participants more with the programme, and names the channel.
5. The headline uses the main path and main reading in each environment; every other row is labelled a sensitivity. Pilot results are labelled pilot and never quoted as figures of the model. They decide only what S47 carries into the batch.
6. The policy comparison stays frozen (ledger d94): no comparator rows are run with the shock.

## Reporting
Every cell above is published, including null and unfavourable results and the Adverse and Stress environments: per-seed values in compassionism-sim-results (`s52-shock-<engine>/`, with run.txt and SHA256SUMS), the pilot report `dev/reports/s52-supply-shock.md` in the engine repository, and the findings page after S48.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
