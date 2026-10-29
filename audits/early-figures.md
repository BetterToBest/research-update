# Where the early figures came from (S30)

Oct 29, 2026. Research-hub at `7e3b829`, compassionism-simulation at `6f4c6e7`. Scripts and outputs are in `audits/early/`.

## In plain words

The Hub's early headline figures came from no code that exists. These are 85% and 98% poverty reduction, median wealth of $37,000 and $82,000 with a 95% interval, "65% lower inflation", "10,000 iterations", the elasticity table, a Gini of 0.28, participation thresholds of 30%, 55% and 75%, 94% stability and 88% work participation. All of them were on the Hub between August 27 and September 18, 2025. The simulation's first engine was committed on May 21, 2026, eight months later, so no version of it can have produced them. The papers point to a Python package (`bettertobest/cco-ptf-simulation`, "10,000+ Monte Carlo iterations"), but that repository does not exist in the account and was never in the Hub repository. The code the modelling paper prints in its Appendix A cannot produce them either. It is a skeleton that calls functions it never defines, and it fails as printed. The few blocks that do run either return hard-coded numbers (the "92% of scenarios stable" is a constant in the code) or give something other than the paper's figure (the carbon block gives 20%, the paper says 35-45% and 45%).

The first engines (May-June 2026) took several of these figures as **inputs and targets**. They drew "$82K target" and "Nordic benchmark 0.28" as reference lines, and copied the parameter file's values into their Full Integration preset. They warned when participation fell "below 55%". Their "System Stability" was a random number between 88% and 96% whenever poverty fell in the last quarter of the run. They also cut the no-program run's wealth by an undocumented factor of 0.85, fixed in v4.4. Run as published on 100 seeds each, the 38 engines before v4.20 never reach Gini 0.28 (their lowest mean is 0.357) or 98% poverty reduction. One figure does reappear: v4.0 to v4.2 (August 2026) give a median wealth of $81,000-$83,000. That is the Hub's $82,000, but it was produced a year after the figure was published, by engines that showed $82K as their target, and only while they added wages in model units to wealth in dollars. When v4.3 fixed that error, the same preset's median wealth rose to about $484,000. The one figure an engine version is cited for, the BLEI paper's Gini of 0.518 at v4.4, does reproduce: 0.518 on 100 seeds (no-program run 0.858).

So every early headline figure is classed "not produced by any code found", except $82,000, which is "produced only with an error since fixed" (and after the fact). A second near-match is a coincidence of wording. The first engine's comparison table printed "poverty elimination" as 100 minus its own poverty rate, which came to about 98%. That was in May 2026, about a different quantity, and with errors fixed since.

## What was checked

1. **Dates.** For each figure, the first research-hub commit that added it (`first_dates.py`; output in `early/first-dates.md`), against the simulation's first engine commit (May 21, 2026).
2. **Code the papers print.** `run_printed_code.py` runs every code block in the modelling paper (HTML and PDF), first exactly as printed, then with only the imports it plainly assumes (output in `early/printed-code.md`). The transfer-design paper prints no code, only parameter distributions (its Appendix A), so there is nothing of it to run.
3. **Every engine before v4.20.** `run_engines.js` loads the page at each commit in headless Chromium, applies the Full Integration preset, runs it and reads the figures as the page showed them. It covers 38 engines: 11 distinct unversioned engines from May 21 to June 10, then the last commit of each version from v3.3 to v4.19, on seeds 1-100 each. Engines before v3.3 cannot be seeded, so the script replaces their `Math.random` with a seeded generator, which gives the same draws, reproducibly. The run was checked against the record: v4.19 at seed 42 gives 16.6% poverty, $559K median wealth and Gini 0.534, exactly the seed-42 regression figures in the simulation's CHANGELOG. One commit (May 23, `f46d5fa`, "Integrated Economic System ABM Simulator") is a truncated upload whose script ends mid-statement; it cannot run in any browser and was replaced the same day. Output: `early/runs/*.jsonl`, summarised in `early/engine-results.md`.
4. **`data/optimal-parameters.json`.** Each value was checked against the printed code, the first engine's preset and the papers (table below).
5. **Other places code could be.** The Hub repository has never held code or results (its history has no `.py`, notebook, data or zip file). The download page (`assets/downloads/README.md`) lists zips that were never committed. The README promising `bettertobest/cco-ptf-simulation` dates from Sep 18, 2025, and that repository is not among the account's repositories. Chat histories are S31's to check.

## Figure by figure

Dates from `early/first-dates.md`; engine figures are the Full Integration means over seeds 1-100 (`early/engine-results.md`).

| Figure | First on the Hub | Code that prints or produces it | Engines before v4.20 (Full Integration, 100 seeds) | Provenance |
|---|---|---|---|---|
| 85% poverty reduction (CCO only) | Aug 27, 2025 (economic-modeling paper) | printed `MonteCarloAnalysis` fails as printed | not reported for CCO only by these runs | not produced by any code found |
| 98% poverty reduction / elimination (integrated) | Sep 16, 2025 | parameter file stores it as an outcome; printed code fails | first engine (May 2026) printed "poverty elimination" = 100 − its poverty rate (1.6%) ≈ 98%; its reduction against its own no-program run was 84% (1.6% vs 9.9%) | not produced by any code found (the May 2026 "98%" is a different quantity, eight months later) |
| $37,000 median wealth (CCO only) | Sep 16, 2025 | none | n/a | not produced by any code found |
| $82,000 median wealth, 95% interval $64,000-$103,000 | Sep 16, 2025 | parameter file lists it as an input ("expected wealth building") | v4.0-v4.2 (Aug 2026): $81K-$83K; every other engine $90K-$530K; no engine reports an interval | produced only with an error since fixed (wage-unit mismatch, v4.3), a year after publication, by engines that displayed $82K as their target |
| 65% lower inflation | Sep 2, 2025 (dual-currency paper) | none; the paper's own table gives 51-54% or 78-86% (S29 B033) | no inflation comparison in these engines | not produced by any code found |
| "10,000 iterations" / "10,000+ Monte Carlo simulations" | Aug 27, 2025 | printed `MonteCarloAnalysis(n_iterations=10000)` fails as printed | engines offered 3, 10 or 50 runs | no such run exists |
| Elasticity table (Basic Unit −0.71, ...) | Sep 16, 2025 | none; the table's own poverty values give −1.60 (S29 B002) | n/a | not produced by any code found |
| Gini 0.28 (integrated) | Sep 16, 2025 | none; the first engine drew 0.28 as "Nordic benchmark" | lowest engine mean 0.357 (May 27, 2026); v4.x 0.49-0.61 | not produced by any code found |
| 30% participation viability | Sep 16, 2025 (CCO-PTF paper) | none | n/a | not produced by any code found |
| 55% minimum viable participation | Sep 16, 2025 | none; the first engine used 55% as a warning threshold (an input) | n/a | not produced by any code found |
| 75% minimum viable participation | Sep 18, 2025 (replication page) | none | n/a | not produced by any code found |
| θ 0.15-0.25 "from Monte Carlo simulations ... confidence interval" | range Sep 18, 2025; the Monte Carlo sentence May 10, 2026 | none; the engines use θ as a design parameter (uniform 0.15-0.25, density-gated from v4.0) | n/a | design parameter; the calibration claim was written 11 days before the first engine existed |
| 94% system stability | Sep 16, 2025 | printed `SystemStability` returns a typed-in 0.92 | first engines: a random number 88-96% (mean 91.8%) | not produced by any code found |
| 92% of scenarios stable | Sep 16, 2025 (PDF) | typed into the printed code as `stress_test_pass_rate: 0.92` | n/a | a constant, not a result |
| 88% work participation | Sep 18, 2025 (simulation README) | none | n/a | not produced by any code found |
| 45% carbon reduction (35-45% in the PDF) | Sep 16, 2025 | printed `carbon_reduction_ptf()` returns 0.20 | n/a | not produced by the printed code (it gives 20%) |
| Gini 0.518 (EDC-adjusted, v4.4, BLEI paper) | 2026 | Compassionism Simulation v4.4 | v4.4: 0.518 (0.479-0.545); no-program run 0.858 | produced by v4.4 (`0beb185`), reproduced here on 100 seeds; the paper should cite the commit and command |

## Engines before v4.20, by version

| Engine | Runs ok | Poverty % | Baseline poverty % | Gini | Baseline Gini | Median wealth | Baseline median wealth | Stability % |
|---|---|---|---|---|---|---|---|---|
| `244075c` 2026-05-21 (unversioned) | 100/100 | 1.6 (0.6-2.6) | 9.9 (7.6-12.0) | 0.427 (0.404-0.448) | 0.529 (0.489-0.579) | $237K ($217K-$260K) | $40K ($37K-$45K) | 91.8 (88.0-96.0) |
| `9e499c0` 2026-05-21 (unversioned) | 100/100 | 1.6 (0.6-2.6) | 9.9 (7.6-12.0) | 0.427 (0.404-0.448) | 0.529 (0.489-0.579) | $237K ($217K-$260K) | $40K ($37K-$45K) | 91.8 (88.0-96.0) |
| `64c866a` 2026-05-22 (unversioned) | 100/100 | 29.2 (24.6-33.2) | 99.9 (99.8-100.0) | 0.601 (0.570-0.625) | 0.162 (0.000-0.858) | $143K ($117K-$171K) | $0K ($0K-$0K) | 78.4 (59.0-95.0) |
| `54f926a` 2026-05-22 (unversioned) | 100/100 | 29.4 (25.4-33.0) | 99.9 (99.8-100.0) | 0.601 (0.572-0.630) | 0.161 (0.000-0.857) | $143K ($115K-$165K) | $0K ($0K-$0K) | 80.6 (57.0-96.0) |
| `2a64b56` 2026-05-22 (unversioned) | 100/100 | 6.9 (4.6-8.6) | 36.2 (32.4-40.8) | 0.441 (0.417-0.466) | 0.671 (0.645-0.696) | $452K ($415K-$487K) | $130K ($99K-$163K) | 82.4 (57.0-96.0) |
| `2389c8d` 2026-05-27 (unversioned) | 100/100 | 1.5 (0.4-2.4) | 10.2 (8.2-13.2) | 0.357 (0.335-0.379) | 0.532 (0.495-0.580) | $231K ($220K-$242K) | $40K ($36K-$44K) | 97.7 (95.0-99.0) |
| `dcfdd0a` 2026-05-28 (unversioned) | 100/100 | 5.0 (3.0-6.6) | 28.8 (25.4-33.4) | 0.372 (0.336-0.406) | 0.532 (0.495-0.580) | $120K ($113K-$130K) | $40K ($36K-$44K) | 97.7 (95.0-99.0) |
| `46e6c11` 2026-06-02 (unversioned) | 100/100 | 5.0 (3.0-6.6) | 29.1 (25.6-34.0) | 0.372 (0.335-0.406) | 0.533 (0.496-0.581) | $120K ($113K-$129K) | $40K ($36K-$43K) | 97.8 (95.0-99.0) |
| `db1b618` 2026-06-03 (unversioned) | 100/100 | 11.2 (8.6-14.2) | 61.5 (57.8-66.0) | 0.437 (0.394-0.475) | 0.754 (0.717-0.794) | $91K ($86K-$97K) | $12K ($8K-$16K) | 79.7 (67.0-99.0) |
| `5f95861` 2026-06-04 (unversioned) | 100/100 | 11.8 (8.8-14.8) | 61.6 (57.0-66.0) | 0.440 (0.401-0.495) | 0.845 (0.790-0.897) | $92K ($87K-$98K) | $12K ($8K-$16K) | 78.1 (67.0-99.0) |
| `cb699cc` 2026-06-10 (unversioned) | 100/100 | 11.8 (8.8-15.0) | 61.7 (56.8-66.2) | 0.436 (0.398-0.493) | 0.756 (0.718-0.807) | $92K ($86K-$99K) | $12K ($8K-$16K) | 77.7 (67.0-99.0) |
| `844cddb` v3.3 2026-06-12 | 100/100 | 11.8 (8.6-15.0) | 61.6 (56.8-66.0) | 0.437 (0.398-0.493) | 0.755 (0.716-0.808) | $91K ($86K-$97K) | $12K ($8K-$16K) | 77.3 (67.0-99.0) |
| `f3963a9` v3.4 2026-06-14 | 100/100 | 11.8 (9.4-12.2) | 62.6 (59.0-63.0) | 0.460 (0.397-0.472) | 0.776 (0.736-0.787) | $93K ($90K-$94K) | $11K ($11K-$14K) | 74.2 (67.0-99.0) |
| `a2e3bdb` v3.5 2026-06-30 | 100/100 | 12.0 (9.4-12.4) | 62.5 (59.0-63.0) | 0.463 (0.397-0.472) | 0.777 (0.736-0.787) | $93K ($90K-$94K) | $11K ($11K-$14K) | 74.5 (67.0-98.0) |
| `0efeae2` v3.6 2026-07-21 | 100/100 | 12.0 (9.4-12.4) | 62.5 (59.0-63.0) | 0.464 (0.397-0.472) | 0.778 (0.736-0.787) | $93K ($90K-$94K) | $11K ($11K-$14K) | 73.4 (69.0-74.0) |
| `b6d4636` v3.7 2026-07-30 | 100/100 | 11.9 (9.4-12.6) | 62.5 (59.0-63.6) | 0.458 (0.397-0.472) | 0.774 (0.736-0.787) | $93K ($87K-$94K) | $11K ($10K-$14K) | 74.3 (68.0-98.0) |
| `37f86e1` v3.8 2026-07-30 | 100/100 | 9.8 (9.2-12.6) | 61.9 (59.0-62.8) | 0.438 (0.398-0.454) | 0.765 (0.736-0.774) | $90K ($89K-$93K) | $13K ($11K-$14K) | 91.5 (67.0-99.0) |
| `79a5d85` v3.9 2026-07-31 | 100/100 | 9.8 (9.2-12.4) | 62.0 (59.0-63.0) | 0.438 (0.398-0.452) | 0.765 (0.736-0.774) | $90K ($89K-$92K) | $13K ($11K-$14K) | 91.4 (68.0-99.0) |
| `ae31e52` v4.0 2026-08-15 | 100/100 | 16.9 (14.4-20.6) | 68.0 (64.6-72.0) | 0.583 (0.479-0.674) | 0.818 (0.791-0.849) | $81K ($74K-$85K) | $2K ($-3K-$6K) | 98.2 (95.0-99.0) |
| `710ce2e` v4.1 2026-08-16 | 100/100 | 16.0 (12.8-20.4) | 68.0 (64.6-72.0) | 0.608 (0.471-0.674) | 0.818 (0.791-0.849) | $83K ($76K-$85K) | $2K ($-3K-$6K) | 98.6 (95.0-99.0) |
| `970c11a` v4.2 2026-08-21 | 100/100 | 14.9 (12.0-18.0) | 67.8 (63.6-71.6) | 0.487 (0.449-0.544) | 0.820 (0.798-0.857) | $82K ($76K-$89K) | $2K ($-2K-$7K) | 94.7 (94.0-95.0) |
| `8a70325` v4.3 2026-08-29 | 100/100 | 20.4 (17.6-23.6) | 72.6 (69.0-76.8) | 0.542 (0.518-0.568) | 0.858 (0.830-0.883) | $484K ($415K-$567K) | $-10K ($-10K-$-10K) | 88.6 (88.0-89.0) |
| `0beb185` v4.4 2026-09-02 | 100/100 | 15.4 (12.2-18.4) | 71.4 (67.2-74.8) | 0.518 (0.479-0.545) | 0.858 (0.840-0.876) | $527K ($462K-$589K) | $-10K ($-10K-$-10K) | 88.7 (88.0-89.0) |
| `df48f72` v4.5 2026-09-04 | 100/100 | 15.4 (11.8-18.0) | 71.4 (67.2-74.8) | 0.516 (0.481-0.544) | 0.858 (0.840-0.876) | $529K ($466K-$599K) | $-10K ($-10K-$-10K) | 88.6 (88.0-89.0) |
| `27f971c` v4.6 2026-09-05 | 100/100 | 15.4 (12.0-17.8) | 71.4 (67.2-74.8) | 0.517 (0.480-0.548) | 0.858 (0.840-0.876) | $529K ($464K-$597K) | $-10K ($-10K-$-10K) | 88.7 (88.0-89.0) |
| `1e975b4` v4.7 2026-09-06 | 100/100 | 15.4 (11.8-18.4) | 71.4 (67.2-74.8) | 0.517 (0.481-0.548) | 0.858 (0.840-0.876) | $528K ($463K-$590K) | $-10K ($-10K-$-10K) | 88.7 (88.0-89.0) |
| `e0eb8ff` v4.8 2026-09-08 | 100/100 | 15.3 (11.6-18.4) | 71.4 (67.2-74.8) | 0.516 (0.478-0.549) | 0.858 (0.840-0.876) | $530K ($462K-$599K) | $-10K ($-10K-$-10K) | 88.7 (88.0-89.0) |
| `d7efd7b` v4.9 2026-09-09 | 100/100 | 15.4 (11.6-18.0) | 71.4 (67.2-74.8) | 0.516 (0.483-0.548) | 0.858 (0.840-0.876) | $529K ($462K-$588K) | $-10K ($-10K-$-10K) | 88.6 (88.0-89.0) |
| `e27a9e3` v4.10 2026-09-11 | 100/100 | 15.4 (12.2-18.4) | 71.4 (67.2-74.8) | 0.516 (0.484-0.547) | 0.858 (0.840-0.876) | $529K ($466K-$591K) | $-10K ($-10K-$-10K) | 88.6 (88.0-89.0) |
| `f93fa38` v4.11 2026-09-13 | 100/100 | 15.4 (12.2-18.0) | 71.4 (67.2-74.8) | 0.517 (0.478-0.544) | 0.858 (0.840-0.876) | $529K ($464K-$590K) | $-10K ($-10K-$-10K) | 88.6 (88.0-89.0) |
| `03e6919` v4.12 2026-09-14 | 100/100 | 15.4 (12.2-18.0) | 71.4 (67.2-74.8) | 0.517 (0.483-0.549) | 0.858 (0.840-0.876) | $529K ($465K-$591K) | $-10K ($-10K-$-10K) | 88.6 (88.0-90.0) |
| `ce539b2` v4.13 2026-09-14 | 100/100 | 15.4 (12.2-18.0) | 71.4 (67.2-74.8) | 0.516 (0.484-0.544) | 0.858 (0.840-0.876) | $529K ($461K-$590K) | $-10K ($-10K-$-10K) | 88.6 (88.0-89.0) |
| `21b603d` v4.14 2026-09-17 | 100/100 | 15.3 (12.0-18.4) | 71.4 (67.2-74.8) | 0.516 (0.480-0.544) | 0.858 (0.840-0.876) | $530K ($466K-$587K) | $-10K ($-10K-$-10K) | 88.7 (88.0-89.0) |
| `cd0ceec` v4.15 2026-09-21 | 100/100 | 15.3 (12.2-17.6) | 71.4 (67.2-74.8) | 0.516 (0.483-0.549) | 0.858 (0.840-0.876) | $529K ($459K-$591K) | $-10K ($-10K-$-10K) | 88.6 (88.0-89.0) |
| `7e5b256` v4.16 2026-09-24 | 100/100 | 15.3 (11.4-17.8) | 71.4 (67.2-74.8) | 0.516 (0.480-0.543) | 0.858 (0.840-0.876) | $530K ($461K-$599K) | $-10K ($-10K-$-10K) | 88.7 (88.0-89.0) |
| `19d098c` v4.17 2026-09-24 | 100/100 | 15.3 (11.4-17.8) | 71.4 (67.2-74.8) | 0.516 (0.480-0.543) | 0.858 (0.840-0.876) | $530K ($461K-$599K) | $-10K ($-10K-$-10K) | 88.7 (88.0-89.0) |
| `11f9299` v4.18 2026-09-24 | 100/100 | 15.3 (11.4-17.8) | 71.4 (67.2-74.8) | 0.516 (0.480-0.543) | 0.858 (0.840-0.876) | $530K ($461K-$599K) | $-10K ($-10K-$-10K) | 88.7 (88.0-89.0) |
| `33c7aef` v4.19 2026-09-25 | 100/100 | 15.3 (11.4-17.8) | 71.4 (67.2-74.8) | 0.516 (0.480-0.543) | 0.858 (0.840-0.876) | $530K ($461K-$599K) | $-10K ($-10K-$-10K) | 88.7 (88.0-89.0) |

Reading the table: the first engines (May 21-28, 2026) gave Full Integration poverty anywhere from 1.5% to 29% depending on the day's code. From June 3 to v3.9 it was 10-12%, and from v4.0 15-20%, against 62-73% in the no-program run. Median wealth moved most with the unit fixes: $120K-$452K in May, about $90K from June 3 to v3.9, $81K-$83K at v4.0-v4.2, about $484K at v4.3 and about $530K from v4.4. The first engines' stability was a random draw (88-96% when poverty fell). The v3.x heuristic (trend plus noise) gave 67-99%. The structural measure (v4.2 on) gives 88-95%. No engine's Gini fell below 0.357.

## The printed code (modelling paper, Appendix A and PDF sections)

| Block | As printed | With the imports it assumes | What the paper says it gives |
|---|---|---|---|
| `MonteCarloAnalysis` (HTML A.1; PDF section 10) | fails: `random` is not defined | fails: `generate_shock` / `calculate_outcome` are never defined | Poverty <2% at 95% confidence, 88% fiscal positive, Gini <0.30 at 92%, stability 94% |
| `CCOAgent` (HTML A.2) | defines a class; needs an environment and initial conditions the paper never defines | same | none |
| `AcreEquityModel` (PDF 2.2) | runs: 100 acres grow to 184 in 10 years, 308 in 20 (6.3% and 5.8% a year) | same | no dollar figure; nothing near $82,000 |
| `InflationModel` (PDF 5) | fails: `random` is not defined | runs (with `random` = numpy.random): mean 2.31%, mean peak 3.25% over 1,000 runs | "Peak inflation 3.5% (Year 1), long-term average 2.1%". These are the code's own hard-coded starting levels (3.5, 2.5, 2.0) before its 30% "dampening"; the dampened path does not reach them |
| `SystemStability` (PDF 7.1) | runs: returns constants, including `stress_test_pass_rate: 0.92` | same | "92% of scenarios stable". The figure is typed into the code, not computed |
| `carbon_reduction_ptf` (PDF 9) | runs: 0.20 | same | "35-45% by Year 10"; the HTML page says 45% |
| `ptf_job_creation`, `calculate_ptf_enhanced_conversion` (PDF) | define functions; need inputs the paper never gives | same | none |
| `optimal_parameters` (PDF 10.1) | a dictionary of inputs (BU $1,200, PTF share 18%, tax 12% ...) | same | inputs, not results |

## `data/optimal-parameters.json`

Created Sep 18, 2025 (`ce3a737`), titled "Optimal parameters ... achieving 98% poverty elimination". No optimisation, validation or Monte Carlo run behind it exists.

| Values | What they are | Verdict |
|---|---|---|
| `basic_unit_amount` 1200 [800, 1500]; `max_octave_level` 6 [4, 8]; `base_quality_multiplier` 1-9; `phi_enhancement_rate` 1.618; `acre_appreciation_rate` 0.04 | design choices; the ranges match the HTML code's `random.uniform` draws (BU 800-1500) | design parameters; the first engine copied them as its Full Integration preset |
| `participation_rate` 0.78 [0.6, 0.95]; `uptake_rate` 0.20 [0.1, 0.3]; `peer_review_accuracy` 0.82; `governance_efficiency` 0.85 | behavioural assumptions; the ranges match the printed code's draws (participation 0.6-0.95 in the PDF, uptake 0.10-0.30 in the HTML) | assumptions labelled "optimal": no optimisation exists (S29 B022) |
| `validation_confidence` 0.94 and 0.92; `confidence_level` 0.95; `validation_iterations` 10000; `validation_benchmarks` (10,000 iterations, 156 sensitivity tests, 10 folds, 24 scenarios, 8 stress conditions) | claims of validation work | no such runs exist |
| `median_wealth_accumulation` 82000 (10 years, "expected wealth building per household") | listed among the inputs, reported in the papers as a result with a 95% interval ($64,000-$103,000) | a target written into the parameter file; the first engine drew it as "$82K target" (S29 B093) |
| `system_outcomes`: poverty elimination 0.98 [0.96, 0.99], stability 0.94, work participation 0.88, median income ×2.3 | results stored as parameters | produced by no code found |
| `break_even_threshold` 35; `creative_collective_size` 42 [35, 50]; `pth_community_size` 150 | design choices stated as optima | design parameters; "optimal" unsupported |
| `gdp_growth` 0.025 ± 0.01; `inflation_target` 0.02; `interest_rates` 0.03 ± 0.01 | environment assumptions | assumptions, uncited |
| `international_adaptations` (×1.5 developed, ×0.4 developing) | design choices | design parameters |
| `technical_specifications` (Python 3.9+, numpy, pandas ...) | describes a package that does not exist | metadata for a missing package |

## Errors the early engines carried, fixed later

| Error | In | Fixed |
|---|---|---|
| Unseeded runs (`Math.random`); no two runs comparable | May 21 - June 10, 2026 | v3.3 (Mulberry32, seed box) |
| "System Stability" = random 88-96% if poverty fell in the last quarter, else 60-75%; "work incentive" = random 82-92% | first engines | v4.2 (structural stability measure) |
| Hub figures used as targets: "$82K target", "Nordic benchmark 0.28", Gini target ≤0.25; KPI colours set by distance from them | from May 21, 2026 | **not fixed**: labelled "pre-v4.3 calibration, not yet reconsidered" from v4.19, and the current page (v5.6.0) still holds `CFG.TARGET_WEALTH` 82000, `TARGET_GINI` 0.25, `TARGET_POVERTY` 0.05 and `TARGET_STABILITY` 0.90 and prints "Target $82K" on its median-wealth tile. Research rule 3 says earlier figures are not targets: remove them (S40) |
| Undocumented ×0.85 cut to the no-program run's starting wealth | from May 21, 2026 | v4.4 |
| Wage in model units (lognormal(3.5, 0.5), about 35 a month) added to dollar wealth | to v4.2 | v4.3 (`WAGE_TO_USD`), v4.4 (one scale everywhere) |
| Gamma sampler returned the constant 1 at a = 1 (automation risk draws) | to v4.3 | v4.4 |
| RNG draws depended on which branches ran, so paired scenarios drifted apart | to v4.2 | v4.2-v4.3 |

## What follows

- `data/claims.csv` (S23) already classes these figures "no basis found" (811 rows claimed as simulation results). This report confirms it: none was produced by code. S24 removes or relabels them per the claims ledger; S25 replaces them with results from the preregistered studies.
- S31 (chat-history provenance) looks for where the figures were written in August-September 2025.
- The simulation page still shows the Hub's $82K, Gini 0.25, 5% poverty and 90% stability as targets (`CFG.TARGET_*`). They should go (S40, or the next engine release).
- The papers' printed code should be removed or marked "illustrative pseudo-code, not run" (S24). The `SystemStability` block in particular presents a typed-in constant as a test result.
