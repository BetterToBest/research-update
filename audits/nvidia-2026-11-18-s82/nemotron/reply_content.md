1. Amendments 1-3 as a whole  
All three amendments are dated before any results run (Nov 17–18, 2026). Amendment 1 records build-time decisions (naming, cut allocation method, dropping `fs`, placeholder sourced values) after a 2-seed smoke test that only verified guard-test equalities; no design parameter was changed after seeing outcomes. Amendment 2 fixes the sourced values from opened sources only, drops `fs` formally, and locks the smaller readings; the 2-seed probe printed only accounting identities. Amendment 3 adds the λ-sweep and finer strict grid because the Amendment 2 sourced values showed medical and food have v=m=0, making them depend entirely on the unsourced λ=0.25; the sweep grid (0, 0.1, 0.25, 0.5, 1) was fixed before any output was inspected. No amendment changes a question, outcome, or decision rule after seeing a result. The changes are justified and properly dated.

2. Sourced values in Amendment 2  
The conversions to shares of *needs consumption* are mostly sound but have three material issues:  
- **Housing m**: BEA housing services ($28,296/hh) vs. model needs ($15,796) gives m=0.7914. The prereg notes CE outlays give 0.43 (low end) and that the BEA figure covers all US households while the model population is working-age with more children. Using the BEA aggregate without adjusting for population mismatch likely overstates m.  
- **Medical m**: CE health spending $6,470 vs. MIT $6,544 → m≈0. The prereg calls both “the household’s own payments”, but CE health spending includes employer-paid premiums; MIT is a budget standard. The near-equality is suspicious and may reflect common calibration sources rather than independent measurement.  
- **Units of v, m, λ**: All sourced values are shares of *sectoral* needs consumption (Amendment 1, item 1). The engine code (slStep) treats `eu` as an *overall* excess share but subtracts sectoral `V.v`, `V.m`, `c` directly (see §4). This unit mismatch is not caught by the sourced-value table; it is an engine bug.  
- **Housing λ**: Wheaton et al. 2014 estimate a 20%/year error correction toward long-run price-stock relation, but note correction runs mainly through prices, not stock. Using 0.2 as a building speed is the “generous side for building” as stated, but it is an error-correction parameter, not a construction-speed parameter.  
- **θ values**: Remain unsourced placeholders (housing 0.6, medical 0.5, food 0); the prereg acknowledges this as a stated limit.

3. Strict-bound sweep in Amendment 3  
- **Grid**: λ = 0, 0.1, 0.25, 0.5, 1 for medical/food (housing λ fixed at 0.2) is sensible; it brackets the sourced 0.25 and reaches the strict bound (0) and a very fast build (1).  
- **“Slowest building speed at which a result holds”**: Defined as the smallest λ on the grid where decision rule 2 passes (effect keeps sign, 95% CI excludes zero under all three sharing rules). This assumes monotonicity in λ; if the effect is non-monotonic (e.g., holds at 0.1 and 0.5 but not 0.25), the phrase “slowest” is ambiguous. The rule says “read on the grid, never interpolated”, which avoids interpolation but not non-monotonicity.  
- **Missing sweeps**:  
  - **θ (price response)**: Unsourced for housing (0.6) and medical (0.5); it directly scales the above-needs demand response `m·η·θ·e`. No sweep is planned. This is a major omitted sensitivity.  
  - **Housing λ**: Though sourced, the Wheaton estimate is explicitly “generous side for building”. A sweep (e.g., 0.1, 0.2, 0.3) would be warranted.  
  - **Housing m and η**: Sourced but with acknowledged coverage issues (BEA population mismatch, elasticity from a single study). The “restricted” reading halves them, but a finer grid would be more informative.

4. Engine code bugs  
**slStep (critical unit mismatch)**:  
`eu = (1 - S.a)*e` is an *overall* excess share (scalar). The loop subtracts sectoral `V.v`, `V.m`, `c` which are shares of *sectoral* needs consumption (per Amendment 1 and SL_SRC). Example: housing share ≈0.3 of basket; overall `eu=0.15`; sectoral `eu_h ≈0.045`. Code computes `r = max(0, 0.15 - 0 - 0 - 0.79*0.697*0.6*0.15) ≈ 0.10` but correct sectoral cut is `max(0, 0.045 - 0.05) = 0`. The cut is overstated by ~10×. All sectoral headroom terms must be multiplied by the sector’s share of overall needs consumption (basket share at current prices) before subtracting from `eu`.

**slCut ‘bu’ rule timing**:  
Uses last year’s `need = R*S.pE[k]` and `S.pC[k]` but this year’s `cash` and `E`. The prereg says “at last year’s totals”. The mix causes the realised cut to deviate from the target (acknowledged in Amendment 1, item 3), but the rule should either use last year’s composition or document the approximation explicitly.

**s82Year price levels**:  
- `lf = agents[0].yrBasketUSD/CFG.LIVING_WAGE_ANNUAL/(agents[0]._hhF || 1)` uses the first adult’s household factor for all adults. Real wealth, real wage, and BU purchasing power should use each adult’s own `mlc` (or `yrBasketUSD`).  
- `G = lf/(PRICE.bIdx || 1)*(PRICE.comp.other || 1)` computes `oIdx * PRICE.comp.other` as the general price level. The prereg defines it as “outside index times the engine’s general component” (`oIdx * PRICE.bIdx`). Using `PRICE.comp.other` (price of ‘other’ goods) is wrong unless ‘other’ is the numeraire; it biases `s82WgG20`, `s82WgGE`, and wealth poverty keys.

**s82Res wealth poverty**:  
`S.wp[yr]` is computed against `Sin.mwY[yr]` (no-programme median). For the no-programme run, `Sin` is itself, so `S.ok=1` and `S.wp` is set. For the programme run, `Sin` is the no-programme run’s `S82S`. This works if `SP` (the first median-storage argument) is the current run’s `S82S` and `Sin` is the no-programme’s. The parameter naming is confusing but the logic holds if called correctly.

**slNew lam override**:  
Throws if `rd === 'full'`; correct because ‘full’ uses `v=Infinity` and builds nothing.

5. Question 7 (the screen)  
The screen is required to run “in Stress, and on the financed rows with the weighted tail on”. Amendment 3 runs block FT (financed, tail on) only for the *wages* base in all three environments. For the other two bases (“wages plus capital income”, “all money income”) it substitutes block F (no tail) in Stress, because S72 Amendment 2 found the tail distorts those bases (+143% hours vs. +21%). This does not answer the stated problem for those bases; it avoids the distortion rather than measuring it. A fair screen would run all bases with the tail on, report the distortion, and interpret it (or use weighted decisions for the screen). The current design gives a partial answer only.

6. Checks and decision rules  
- **Check 9 (Amendment 3)** verifies `lam` at sourced values equals the sourced row and at 0 moves the limit, but does not run a sourced-row with `eu>0`; the critical unit bug in slStep would not be caught because the dry-run selftest runs “equality tests only; no outcome value was printed”.  
- **Check 6** (money accounts close) would not catch the slStep unit error because the cut’s dollars are still accounted once (spent on other goods).  
- **Decision rule 2** (“holds under supply limit”) requires all three sharing rules to pass. This is strict and clear.  
- **Decision rule “slowest building speed”** assumes monotonicity; if non-monotonic, the summary is misleading.  
- **No-tuning rule** is clear: any post-dry-run change requires a dated amendment and full rerun.

7. Five most important changes before dry run (ranked)  
1. **Fix the unit mismatch in slStep** (§4): multiply each sector’s `V.v`, `V.m`, `c`, `V.m*V.eta*th*e` by the sector’s current share of overall needs consumption before subtracting from overall `eu`. Without this, cuts are wrong by an order of magnitude.  
2. **Correct s82Year price levels** (§4): compute `lf` per adult (using each adult’s `mlc` or `yrBasketUSD`); set general price level `G = oIdx * PRICE.bIdx` (not `PRICE.comp.other`). This affects every s82 key (real wage, real BU, real wealth, wealth poverty).  
3. **Add a θ sweep for housing and medical** (§3): the unsourced θ (0.6, 0.5) drives the above-needs demand response. A sweep (e.g., 0.3, 0.6, 0.9) must be added before the dry run; otherwise a major uncertainty is unquantified.  
4. **Align slCut ‘bu’ rule with prereg timing** (§4): either use last year’s `cash` and `E` composition (stored in `slStep`) or explicitly document the approximation and its effect on `slCutSh`.  
5. **Run the Q7 screen with tail on for all three bases** (§5): either accept the distortion as a finding or implement weighted decisions for the screen; substituting no-tail rows does not satisfy the preregistered screen requirement.