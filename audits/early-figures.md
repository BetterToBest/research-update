# Where the early figures came from (S30)

Oct 29, 2026. Research-hub at `7e3b829`, compassionism-simulation at `6f4c6e7`. Scripts and outputs are in `audits/early/`.

## In plain words

The Hub's early headline figures came from no code that exists. These are 85% and 98% poverty reduction, median wealth of $37,000 and $82,000 with a 95% interval, "65% lower inflation", "10,000 iterations", the elasticity table, a Gini of 0.28, participation thresholds of 30%, 55% and 75%, 94% stability and 88% work participation. All of them were on the Hub between August 27 and September 18, 2025. The simulation's first engine was committed on May 21, 2026, eight months later, so no version of it can have produced them. The papers point to a Python package (`bettertobest/cco-ptf-simulation`, "10,000+ Monte Carlo iterations"), but that repository does not exist in the account and was never in the Hub repository. The code the modelling paper prints in its Appendix A cannot produce them either. It is a skeleton that calls functions it never defines, and it fails as printed. The few blocks that do run either return hard-coded numbers (the "92% of scenarios stable" is a constant in the code) or give something other than the paper's figure (the carbon block gives 20%, the paper says 35-45% and 45%).

The first engines (May-June 2026) took several of these figures as **inputs and targets**. They drew "$82K target" and "Nordic benchmark 0.28" as reference lines, and copied the parameter file's values into their Full Integration preset. They warned when participation fell "below 55%". Their "System Stability" was a random number between 88% and 96% whenever poverty fell in the last quarter of the run. They also cut the no-program run's wealth by an undocumented factor of 0.85, fixed in v4.4. Run as published on 100 seeds each, the 38 engines before v4.20 never reproduce the Hub's $82,000 median wealth or Gini 0.28; their results by version are in the table below.

So every early headline figure is classed "not produced by any code found". The one partial exception is a coincidence of wording. The first engine's comparison table printed "poverty elimination" as 100 minus its own poverty rate, which came to about 98%. That was in May 2026, about a different quantity, and with errors fixed since.

## What was checked

1. **Dates.** For each figure, the first research-hub commit that added it (`first_dates.py`; output in `early/first-dates.md`), against the simulation's first engine commit (May 21, 2026).
2. **Code the papers print.** `run_printed_code.py` runs every code block in the modelling paper (HTML and PDF), first exactly as printed, then with only the imports it plainly assumes (output in `early/printed-code.md`). The transfer-design paper prints no code, only parameter distributions (its Appendix A), so there is nothing of it to run.
3. **Every engine before v4.20.** `run_engines.js` loads the page at each commit in headless Chromium, applies the Full Integration preset, runs it and reads the figures as the page showed them. It covers 38 engines: 11 distinct unversioned engines from May 21 to June 10, then the last commit of each version from v3.3 to v4.19, on seeds 1-100 each. Engines before v3.3 cannot be seeded, so the script replaces their `Math.random` with a seeded generator, which gives the same draws, reproducibly. The run was checked against the record: v4.19 at seed 42 gives 16.6% poverty, $559K median wealth and Gini 0.534, exactly the seed-42 regression figures in the simulation's CHANGELOG. One commit (May 23, `f46d5fa`, "Integrated Economic System ABM Simulator") is a truncated upload whose script ends mid-statement; it cannot run in any browser and was replaced the same day. Output: `early/runs/*.jsonl`, summarised in `early/engine-results.md`.
4. **`data/optimal-parameters.json`.** Each value was checked against the printed code, the first engine's preset and the papers (table below).
5. **Other places code could be.** The Hub repository has never held code or results (its history has no `.py`, notebook, data or zip file). The download page (`assets/downloads/README.md`) lists zips that were never committed. The README promising `bettertobest/cco-ptf-simulation` dates from Sep 18, 2025, and that repository is not among the account's repositories. Chat histories are S31's to check.

## Figure by figure

ENGINE_TABLE_PLACEHOLDER

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
