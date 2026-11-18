### 1. Amendments 1–3 as a whole: fitting design to result? Justified and dated before results?

No amendment changes the study in a way that could be read as fitting the design to a result. All three are dated before any run for results (the dry run or the batch), and each change is justified by a design commitment or an external input.

- **Amendment 1** (Nov 17, after build, before any run) documents build-time decisions: naming conventions, that `essD` already measures pre-cut demand, that the cut’s realised share is approximate (reported as `slCutSh`), that `fs` is dropped pending money-account work, and that sourced values remain at design middles until sources are opened. A 2-seed smoke test checked only identity guards (`full` = base, `strict`@1 = main, `wIdx=1` identical); no outcome values were inspected and no design element was changed afterward.
- **Amendment 2** (Nov 17, after sources opened, before dry run) fixes `v, m, η, λ` from opened sources (Census, BEA, RAND, Wheaton et al., USDA). The key consequence—that medical and food have `v=m=0` and are met only by new capacity—is stated before any run: “Nothing here was chosen to move a figure. No outcome of any S82 reading has been seen at more than two seeds.” The job’s `--selftest` passed on v5.9.17 (equality tests only, no outcome values printed).
- **Amendment 3** (Nov 18, before dry run) adds the strict-bound sweep (λ = 0, 0.1, 0.25, 0.5, 1 for medical/food) because those sectors’ sourced reading differs from the strict bound only by the unsourced design parameter λ = 0.25. Duke requested the sweep; research rule 3 requires sweeping design parameters. The sweep grid and the finer strict-bound grid (0.125, 0.375, 0.625, 0.875) are fixed before any output is seen. A 200-adult, 1-seed smoke test printed some `s82` keys but “nothing in the design, the grids or the rules was changed after seeing them.”

No 500-seed or 100-seed run has been made at any stage.

---

### 2. Sourced values in Amendment 2: conversions sound? Mistakes in units, coverage, interpretation?

**Housing** – conversions are sound.  
- `v = 0`: rental vacancy 7.10% and homeowner vacancy 1.15% are *below* their 1956–2025 means (7.27%, 1.52%), so no idle capacity beyond normal use. Correct.  
- `m = 0.7914`: BEA housing services $28,296/household ÷ model needs $15,796 = 1.7914; above-needs share = (1.7914 − 1) = 0.7914. Amendment 1 item 1 confirms the conversion (output share ÷ needs share). Correct.  
- `η = 0.697`: Albouy, Ehrlich & Liu (2016) preferred column. This is the *overall* housing demand elasticity; the engine applies it to above-needs demand. A mismatch if above-needs elasticity differs, but no better source is available. Noted as a limit.  
- `λ = 0.2`: Wheaton, Chervachidze & Nechayev (2014) error-correction speed (20%/year toward long-run price–stock relation). The prereg acknowledges this is the “generous side for building” because the correction runs mainly through prices. Acceptable as a sourced design parameter.

**Medical care** – `m = 0` is questionable.  
- `v = 0`: hospital occupancy 75.3% (2023–24) vs. 63.9% (2009–19 mean) → no idle capacity. Correct.  
- `m = 0`: CE household health spending $6,470/unit vs. MIT medical line $6,544. The prereg says “both the household’s own payments.” CE “healthcare” includes *employer-paid* premiums; MIT needs is household’s own payments (premiums + OOP). If CE includes employer share, CE > household own payments → `m > 0`. The prereg does not show the adjustment that makes them match. This is a potential coverage/interpretation error that could understate medical headroom.  
- `η = 0.2`: RAND HIE elasticity for *total* medical demand; applied to above-needs demand. Same limitation as housing.  
- `λ = 0.25`: design parameter, no source. Acknowledged.

**Food** – conversions are sound but `m = 0` is moot because `θ_food = 0`.  
- `v = 0`: food-manufacturing utilisation 84.9% > 1972–2025 mean 82.2%. Correct.  
- `m = 0`: CE food at home $6,491 < MIT food plan $7,508. The prereg says “not used: θ food is 0.” Since `θ_food = 0`, `m` does not enter the price-response term; it only affects capacity building via `max(0, eu − c − v)`. With `v = 0`, building responds to `eu` directly. Acceptable.  
- `η = 0.5`, `λ = 0.25`: design parameters, unused or acknowledged.

**General** – all values are correctly expressed as shares of *no-programme needs consumption* (Amendment 1 item 1). The Wheaton λ and RAND η are applied to above-needs demand without sector-specific evidence; this is a stated limit, not a mistake.

---

### 3. Strict-bound sweep in Amendment 3: grid sensible? “Slowest building speed” fair? Missing sweeps?

**Grid** – λ = 0, 0.1, 0.25, 0.5, 1 for medical/food (housing fixed at sourced λ = 0.2) is sensible: it brackets the sourced value (0.25), includes the strict bound (0), a slower build (0.1), and faster builds (0.5, 1). The strict-bound grid (0, 0.125, 0.375, 0.625, 0.875, 1) is twice as fine as the 5-point backing grid. Good.

**“Slowest building speed at which a result holds”** – defined as the smallest λ on the grid where decision rule 2 passes (effect keeps sign, 95% interval excludes zero under all three sharing rules), read on the grid, never interpolated. This is a fair, discrete-grid summary.

**Missing sweeps** – two important design parameters are not swept:
1. **Housing’s λ, m, η**: housing has `m = 0.7914`, `η = 0.697`, `λ = 0.2` (sourced). The sweep only varies medical/food λ. Housing’s headroom comes largely from above-needs give-up (`m·η·θ·e`); its λ is sourced but could be swept (Wheaton et al. is one estimate). Research rule 3 asks that design parameters be swept; housing’s sourced values are still parameters in the model.
2. **Price response θ**: `θ_housing = 0.6`, `θ_medical = 0.5` are “unsourced placeholders” (prereg, Limits). They directly scale the above-needs give-up (`m·η·θ·e`). Not sweeping θ leaves a key unsourced parameter fixed at a single value. The prereg acknowledges θ is unsourced but does not sweep it.

---

### 4. Engine code: bugs in `slStep`, `slCut`, `slNew` (including `lam`), `s82Year`, `s82Res`?

**`slNew`** – correct. Validates `rd`, `sh`, rejects `fs`, applies `lam` override per sector (refused for `full`), initializes all accumulators.

**`slCut`** – allocation logic matches the prereg, but two issues:
- **`a._slBU` allocation to essentials**: `buR = mlc*(cfPreCCO − cf) − tbG − spCut` is the *total* BU relief on the whole basket. The code spreads it over essentials in proportion to their price shares (`sh/ess`). The prereg says “the adult’s BU relief spread over the three essentials in their price shares.” This assumes BU relief reduces essentials spending proportionally, but BU relief reduces the *whole* basket cost. The approximation is reasonable but undocumented as an assumption.
- **Normalisation uses last year’s totals**: `S.nP[k]` (for `pay` rule) and `S.pE[k]`, `S.pC[k]` (for `bu` rule) are from the previous year (set at end of `slStep`). Amendment 1 item 3 accepts the realised cut will be “within about 5% of the target” and reports `slCutSh`. No check enforces the tolerance.

**`slStep`** – correct implementation of the prereg formulas:
- `r = max(0, eu − c − V.v − V.m·V.eta·th·e)` (cut share of supply path).
- `S.c[k] += V.lam·max(0, eu − c − V.v)` (building responds to lasting excess above idle capacity, *including* the part met by squeezing above-needs use). Matches “both the part cut and the part met by squeezing above-needs use.”
- `th = +S.th[k] || 0` picks up `θ_k` from `slNew`’s `theta` argument. In the main run this comes from `PM_DEFAULTS.theta` (0, 0.6, 0.5). No division-by-zero risk (`s > 0` guard).

**`s82Year` / `s82Res`** – one clear bug:
- **`s82BuR20` / `s82BuRE` use the wrong price index**. The prereg (Section D) says: