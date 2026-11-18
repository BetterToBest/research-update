The user wants a critical reading of a preregistration for an agent-based microsimulation study (Compassionism Simulation) with three amendments and the engine code implementing the supply limit and reporting keys. I need to evaluate under seven specific headings.

Let me first understand the structure:
- Preregistration with Amendments 1-3 (dated Nov 17-18, 2026)
- Engine code (index.html v5.9.18) for supply limit (sl) and study reporting keys (s82)

I need to be critical, specific, cite sections/functions, and write in plain words. No praise, no summary.

Let me go through each heading systematically.

## 1. Amendments 1-3 as a whole: fitting design to result? Justified and dated before results?

Amendment 1 (Nov 17): Build decisions, naming, "essD with cut added back" clarification, cut total allocation method, fs dropped, sourced values placeholder. Dated before any run for results. The 2-seed smoke test was run but "nothing in the design, readings, grids or rules was changed after seeing them." The outside reading (Mistral) was partial. This seems justified as build-time decisions.

Amendment 2 (Nov 17, after sources opened, before dry run): Sourced values for v, m, η, λ from opened sources. fs dropped. Smaller readings as built. Job with checks. Dated before dry run. The sourced values are fixed from opened sources only. No outcome seen beyond 2 seeds. This seems justified.

Amendment 3 (Nov 18, before dry run): Strict-bound sweep (λ sweep for medical/food), Sgrid (strict bound on finer grid), section D reporting keys as built, Question 7 screen details. Dated before dry run. The sweep was requested by Duke, motivated by research rule 3 (design parameters swept). The grid values (0, 0.1, 0.25, 0.5, 1) seem reasonable. The decision rule "slowest building speed at which a result holds" is added.

Potential concern: Amendment 3 adds rows (Slam, Sgrid) and analysis after seeing Amendment 2's sourced values (which showed v=0, m=0 for medical/food). But the amendment says "the sweep's grid was fixed before any of it was printed" and "no outcome read for a decision." The 200-adult 1-seed smoke test printed some keys but "nothing in the design, grids or rules was changed after seeing them." This seems okay - the sweep is a response to the sourced values showing medical/food depend entirely on λ, so sweeping λ is appropriate. It's dated before dry run.

Overall: All amendments dated before any results run. Changes seem justified by design logic (sweeping design parameters, fixing sourced values, build clarifications). No obvious fitting to results.

## 2. Sourced values in Amendment 2: conversions to shares of needs consumption sound? Mistakes in units, coverage, interpretation?

Let me check each sector:

**Housing:**
- v (idle capacity): rental vacancy 7.10% vs 1956-2025 mean 7.27%; homeowner vacancy 1.15% vs 1.52%. Both below long-run means → v=0. This measures vacancy *beyond normal use*. Seems correct per Amendment 1 item 1: "idle capacity over needs consumption". But wait - vacancy rates are shares of *stock*, not shares of *needs consumption*. The prereg says "every value is a share of the sector's no-programme needs consumption". So vacancy rate (share of stock) needs to be converted to share of needs consumption. How? If needs consumption is 60% of output (as example in Amendment 1), and vacancy is 7.1% of stock, then idle capacity as share of needs consumption = (vacancy rate * stock) / (needs consumption). But stock ≈ output (housing services). So if needs are 60% of output, vacancy 7.1% of output → idle capacity share of needs = 7.1% / 60% ≈ 11.8%. But they set v=0 because vacancy is *below* long-run mean. The "idle capacity beyond normal use" is max(0, current vacancy - normal vacancy). Since current < normal, v=0. That seems consistent: they're measuring *excess* vacancy above normal as idle capacity. But is "normal" the long-run mean? And is the conversion to share of needs consumption done? The table shows v=0 directly. The text says "idle capacity is measured beyond normal use... so nothing is met 'at once' from idle capacity". So they're not converting the absolute vacancy to share of needs; they're saying the *excess* vacancy is zero. That seems fine for v=0.

- m (above-needs share): BEA housing services $3,814B / 134.8M households = $28,296/household vs model needs $15,796 → ratio 1.79. So above-needs = (28,296 - 15,796)/15,796 = 0.7914. This is "above-needs consumption over needs consumption". The prereg says "m is, if anything, understated" because BEA covers all US households while model population is working-age with more children/higher needs. Seems reasonable.

- η (elasticity): Albouy et al. 2016 preferred column 0.697 (range 0.49-0.83). This is price elasticity of housing demand. Used in m * η * θ * e. θ_housing = 0.6 (unsourced placeholder). So the price response of above-needs demand is η * θ. But η is elasticity of *total* housing demand, not just above-needs. The model assumes above-needs demand has same elasticity. Could be a limitation but not a mistake per se.

- λ (building speed): Wheaton et al. 2014: housing markets close ~20% a year of gap to long-run price-stock relation. They note "correction runs mainly through prices, not stock, so this is the generous side for building". λ=0.2. This is an error-correction speed, not exactly "new construction as share of stock". But used as building speed. The prereg acknowledges it's the generous side.

**Medical care:**
- v: hospital occupancy 75.3% (May 2023-Apr 2024) vs 63.9% (2009-2019). Current > normal → no idle capacity beyond normal → v=0. But occupancy is not the same as capacity. Hospitals can operate above 63.9% occupancy. The "normal" is pre-pandemic average. Current 75.3% suggests strain, not idle capacity. v=0 seems correct for "idle capacity beyond normal use".

- m: CE household health spending $6,470 vs MIT medical line $6,544. Both "household's own payments". Ratio ~0.99 → m=0 (no above-needs use). But CE is consumer expenditure survey (out-of-pocket + insurance payments?), MIT needs is a budget standard. The prereg says "both the household's own payments". If CE includes insurance payments, it's not directly comparable to a needs budget. But they're using it as a proxy. The near-equality suggests little above-needs consumption in the needs basket sense. m=0.

- η: RAND HIE (Keeler & Rolph 1988) via Aron-Dine et al. 2013: 0.2. This is price elasticity of medical care demand. Low, plausible.

- λ: 0.25 design parameter, no source opened. Acknowledged.

**Food:**
- v: food manufacturing utilization 84.9% vs 1972-2025 mean 82.2%. Current > mean → v=0. Utilization above normal → no idle capacity. Seems correct.

- m: CE food at home $6,491 vs MIT food plan $7,508. CE < MIT → m=0 (but actually negative, clipped to 0). The prereg says "not used: θ food is 0". So m doesn't matter.

- η: 0.5 design parameter, not used (θ=0).

- λ: 0.25 design parameter, no source opened.

**Key issues:**
1. **Units/conversion**: The prereg says "every value is a share of the sector's no-programme needs consumption". For v (idle capacity), they use vacancy rates (share of stock) and compare to long-run mean. But they don't convert to share of needs consumption - they just say excess vacancy is zero so v=0. If excess vacancy were positive, they'd need to convert. Since it's zero, it's fine for now but the method is implicit.

2. **Housing m**: BEA housing services includes owners' imputed rent. The model's needs basket housing component is $15,796. BEA gives $28,296. The ratio 1.79 seems high but plausible (owners' imputed rent is large). The prereg acknowledges CE outlays give 0.43 (lower). The choice of BEA over CE is a judgment call.

3. **Medical m**: CE health spending $6,470 vs MIT $6,544. CE includes out-of-pocket + insurance premiums? MIT is a budget standard for medical care. If CE is total household health spending (including employer-paid premiums?), it's not "household's own payments". The prereg says "both the household's own payments" - this might be inaccurate. CE health spending includes insurance premiums paid by household, but not employer-paid. Still, it's a measure of total health spending per household. The near-equality is suspicious - MIT living wage medical component might be calibrated to similar data. Could be circular.

4. **λ for medical/food**: Design parameters, no sources. Acknowledged.

5. **θ values**: Unsourced placeholders (housing 0.6, medical 0.5, food 0). The prereg says "the essentials price response θ is unchanged and unsourced." This is a known limitation.

Overall: Conversions are mostly sound given the "share of needs consumption" framing, but some comparisons (medical m) are questionable. The v=0 for all three sectors is a strong result of the "beyond normal use" definition.

## 3. Strict-bound sweep in Amendment 3: grid sensible? "Slowest building speed at which a result holds" fair? Missing sweeps?

**Grid**: λ = 0, 0.1, 0.25, 0.5, 1 for medical and food (housing λ fixed at sourced 0.2). The sourced λ for medical/food is 0.25 (design parameter). Grid includes 0 (strict bound), 0.1, 0.25 (sourced), 0.5, 1. This seems sensible - covers from strict to very fast building.

**"Slowest building speed at which a result holds"**: Defined as smallest λ on grid where decision rule 2 passes (effect keeps sign, 95% interval excludes zero under all three sharing rules). Read on grid, never interpolated. This is a clear, pre-specified decision rule. Fair summary? It's a threshold summary. Could be misleading if effect holds at λ=0.1 and 0.5 but not 0.25 (non-monotonic), but unlikely. The grid is coarse (5 points). "Slowest" implies monotonicity - if higher λ always makes it easier to hold, then yes. But if non-monotonic, "slowest" is ambiguous. The prereg doesn't assume monotonicity but the summary phrase does. Should note this.

**Missing sweeps**:
- Housing's values: v=0, m=0.7914, η=0.697, λ=0.2 are all sourced (except λ=0.2 from Wheaton which is "generous side"). The prereg sweeps λ for medical/food because they're design parameters. Housing λ is sourced (though with caveats). But housing m and η are also sourced. Should they be swept? Research rule 3: "design parameters be swept". Housing λ is sourced, not a design parameter. But the Wheaton estimate is noted as "generous side for building" - so it's uncertain. The restricted reading halves all sourced values. That's a form of sensitivity. But a sweep of housing λ (e.g., 0.1, 0.2, 0.3) might be warranted given the "generous side" comment.

- Price response θ: Unsourced placeholders (housing 0.6, medical 0.5, food 0). The prereg says "the essentials price response θ is unchanged and unsourced. With A on, prices and quantities are not derived from one elasticity." This is a major uncertainty. θ determines how much above-needs demand gives up (m * η * θ * e). For housing, θ=0.6, η=0.697 → effective elasticity of above-needs demand = 0.418. If θ is wrong, the headroom from above-needs demand is wrong. A sweep of θ (e.g., 0.3, 0.6, 0.9 for housing) would be important. The prereg doesn't sweep θ. This is a missing sweep.

- Also, the "restricted" reading halves all sourced values. That's a coarse sweep. But for key parameters like housing m (0.7914) and η (0.697), a finer sweep might be better.

The prereg acknowledges θ is unsourced and a limitation. But not sweeping it is a gap.

## 4. Engine code: bugs in slStep, slCut, slNew (including lam), s82Year, s82Res?

Let me examine the code carefully.

**slNew(o, a, theta)**:
- Creates S object with V (values per sector), c (capacity built), R (cut share), etc.
- Handles `lam` override: if `O.lam` provided, validates and overrides `V[k].lam`. Throws if `rd === 'full'`. Good.
- `nP` initialized to `{food:1, housing:1, medical:1}` - used in 'pay' rule normalization. Seems okay.
- `qN`, `qP` for ranking. `xk`, `pE`, `pC` for tracking.
- `sE`, `sC`, `sW` for accumulating E, cash, E*2*(1-F) for normalization.

**slCut(S, a, inc, mlc, costUSD)**:
- Called from `tbPov` for each adult.
- `B = a._slB > 0 ? a._slB : mlc` - uses `_slB` (basket cost before cut?) or `mlc` (current cost). `_slB` set in `runYear` as `mainLoopCostUSD*cfPreCCO` (cost before CCO relief). This is the basket cost at year's prices before supply cut? Actually `cfPreCCO` is cost factor before CCO relief. The supply cut is applied after CCO relief? Let's see: in `runYear`, `cf` is final cost factor, `cfPreCCO` is before CCO relief. The supply cut `slCut` is called in `tbPov` with `mlc` (mainLoopCostUSD*cf) and `costUSD` (same). But `B` uses `_slB` which is `mainLoopCostUSD*cfPreCCO`. So `B` is cost before CCO relief, while `mlc` is cost after CCO relief. This seems inconsistent. The cut should be based on the same cost basis. The prereg says "E its spending on k = basket x (1 - its unpaid share) x k's share at the year's prices". The unpaid share `u` is `a._slU` (from price module's `pmU`). `pmU` is based on `pmB` (basketOwn) which is `mainLoopCostUSD*cfPreCCO`. So `pmU` uses pre-CCO cost. Then `E = B*(1-u)*sh/bI` where `bI` is sum of `CFG.BASKET[k]*comp[k]` (total basket at current prices). `B` is `_slB` (pre-CCO cost). But the adult's actual spending on essentials is at post-CCO prices? This is messy.

- `bu = Math.min(E, (a._slBU || 0)*sh/ess)` - `_slBU` set in `runYear` as `buR` (BU spent at face value). `ess` is sum of essentials shares at current prices. This allocates BU spending across essentials proportionally to price shares. Seems okay.

- `cash = E - bu`

- `R = S.R[k]` - the sector's cut share for next year (set in `slStep` at end of previous year). But `slCut` is called during the year for poverty accounting. `S.R[k]` is from *last* year's `slStep`. The prereg says "next year's share of demand cut is R_k = r_k / (1 + e)". So the cut applied this year is based on last year's excess. That matches the timing: "At the end of each year t-1... next year's share of demand cut is R_k". So `slCut` uses `R` from previous year. Good.

- For 'pay' rule: `xk = R*E*2*(1-F)*S.nP[k]`. `S.nP[k] = S.sE[k]/S.sW[k]` where `sE` accumulates `E`, `sW` accumulates `E*2*(1-F)`. So `nP` normalizes so that sum of `xk` ≈ `R * sum E`. But `S.nP[k]` is updated at end of year in `slStep`. During the year, it's from previous year. At start of year, `nP` initialized to 1. So first year, no normalization. This is a timing issue: the normalization uses last year's distribution. The prereg says "N last year's sum E / sum E 2(1-F)". So using last year's `nP` is correct. But `S.nP[k]` is set in `slStep` at end of year. So for year t, `slCut` uses `nP` from year t-1. Good.

- However, `S.nP[k]` is computed as `S.sE[k]/S.sW[k]` where `sE` and `sW` are accumulated *during* the year in `slCut` (before reset). At the end of `slStep`, `S.nP[k] = S.sE[k]/S.sW[k]`. Then `sE`, `sW` reset to 0. So for next year, `nP` is correct. But during the year, `slCut` uses `nP` from previous year. This is correct.

- For 'bu' rule: `need = R*S.pE[k]`. `S.pE[k]` is set in `slStep` as `S.sE[k]` (total E for sector last year). `S.pC[k] = S.sC[k]` (total cash spending last year). Then `xk = need <= S.pC[k] ? cash*need/S.pC[k] : cash + (E - cash)*(need - S.pC[k])/(S.pE[k] - S.pC[k])`. This implements: cut cash spending first (proportionally), then if more needed, cut BU spending proportionally. But `cash` is this year's cash spending, `E` is this year's total spending. `need` is last year's target cut. This mixes years. The prereg says: "the part bought with cash... is cut first, at last year's totals; if that is too little, the rest ∝ E". The code uses `need = R * S.pE[k]` (last year's target cut in dollars? `R` is share, `pE` is last year's total E). Then compares to `S.pC[k]` (last year's total cash). If `need <= pC`, cut `cash * need/pC` (proportional to this year's cash). Else cut all cash plus `(E-cash)*(need-pC)/(pE-pC)`. This seems to implement the rule but with a mix of last year's totals and this year's composition. The prereg says "at last year's totals" for the cash-first part. The code uses last year's `need` and `pC` but this year's `cash` and `E`. This could cause the realized cut to deviate. The prereg acknowledges "the realised cut is close to the sector's share, not equal to it. It is reported (`slCutSh`) beside the target." So this is known.

- `xk = Math.min(E, Math.max(0, xk))` - caps at E.

- Accumulates `S.xk[k]`, `S.xs`, `S.xq` by fifth (using `F` from last year's ranks via `slRank`). `slRank` uses `S.qP` (sorted last year's `q` = inc/mlc). `S.qP` set in `slStep` at end of year. So ranking uses last year's income/cost. Prereg says "F its rank in cash income over its cost of living among last year's adults". Correct.

- `S.f0p` increments if `costUSD - inc > 0` (paid-for basket poverty). But `costUSD` is post-cut cost? Actually `costUSD = mainLoopCostUSD*cf` (final cost). The cut `x` is not subtracted from cost in main reading (money spent on other goods). So `costUSD - inc` is the gap without considering the cut. But `slF0p` is "paid-for basket poverty share". The prereg says "basket poverty on what was received: the gap is max(0, cost - income + x)/basket". But here `f0p` uses `costUSD - inc > 0` without `+x`. This seems wrong. `slF0p` should be the poverty rate *after* accounting for the cut (i.e., money that cannot buy needs doesn't count). But the code does `costUSD - inc > 0`. However, in `tbPov`, the actual poverty gap `g` is computed as `Math.max(0, costUSD - inc + slX)/mlc` where `slX` is the cut returned by `slCut`. So `tbPov` uses the correct formula. `slF0p` in `slCut` is just a separate accounting of "paid-for" poverty (without the cut adjustment). The prereg says "slF0p, the paid-for basket poverty share (adult-years), beside fgt0PY (received)". So `slF0p` is the poverty rate *ignoring* the cut (i.e., as if the cut money could buy needs). That's what the code does. Okay.

**slStep(S, d, s)**:
- Called at end of year. `d` = demand share (engine's `essD`), `s` = supply path (no-programme `essD`).
- `e = max(0, d/s - 1)`, `eu = (1 - S.a)*e`.
- For each sector: `th = +S.th[k] || 0` (θ_k), `c = S.c[k]`.
- `r = max(0, eu - c - V.v - V.m*V.eta*th*e)`.
- `S.R[k] = r/(1+e)` (next year's cut share).
- `S.c[k] = c + V.lam*max(0, eu - c - V.v)` (capacity built).
- `S.nP[k] = S.sW[k] > 0 ? S.sE[k]/S.sW[k] : 1` (normalization for 'pay' rule).
- `S.pE[k] = S.sE[k]`, `S.pC[k] = S.sC[k]` (store totals for 'bu' rule).
- Resets `sE`, `sC`, `sW`, `xk` to 0.
- `rec.cut = tE > 0 ? tX/tE : 0` (realized cut share).
- `S.qP = S.qN.sort(...)` (update ranks for next year).
- `S.qN = []`.

**Potential bugs:**
1. **`th = +S.th[k] || 0`**: `S.th` is passed as `theta` in `slNew` (from `c.o.th`?). In `runYear`, `slStep` is called with `S.th` being `PRICE.comp`? Let's check: In `runYear`, `slStep(SLS, PRICE.acc.essD, PRICE.acc.essS)`? Actually, `slStep` is called in `tbRunCore`? The prereg says "At the end of each year t-1 (the essentials prices' timing)...". In code, `slStep` is called from `tbRunCore`? I don't see `slStep` called in the provided code snippet. The provided code has `slStep` function but not its call site. However, `S.th` is initialized in `slNew` as `th:theta || {}`. `theta` likely comes from `PRICE.theta` or similar. In `slStep`, `th = +S.th[k] || 0`. If `S.th` is an object with keys 'food', 'housing', 'medical', this works. But `S.th` is passed as `theta` in `slNew`. In `runYear`, when is `slStep` called? Not in the provided snippet. But assuming it's called correctly.

2. **`V.m*V.eta*th*e`**: This is `m * η * θ * e`. But `e` is the *overall* excess demand share (same for all sectors?). The prereg says "for each sector k... e = max(0, D/S - 1) the excess". But `D` and `S` are for the *overall* essentials? Or per sector? The prereg: "for each sector k (food, housing, medical), in shares of the supply path S: D = the year's demand before any cut... e = max(0, D/S - 1)". This implies `D` and `S` are sector-specific. But in `slStep`, `d` and `s` are scalars (overall `essD` and `essS`). Then `e` is scalar. Then for each sector, `r = max(0, eu - c - V.v - V.m*V.eta*th*e)`. This uses the *same* `e` for all sectors. But the prereg says "for each sector k... e = max(0, D/S - 1)". If `D` and `S` are overall, then `e` is overall excess. But the headroom terms `v_k`, `m_k η_k θ_k e` are sector-specific. The prereg might mean `D` and `S` are vectors. But the engine's `essD` is a scalar (mean share of needs basket paid for). The supply path `S` is the no-programme run's `essD`. So `e` is overall essentials excess. Then the sectoral allocation of the cut uses the same `e`. This assumes the excess demand is distributed across sectors in proportion to basket shares. The prereg says "The extra need is one share of the basket, spread over the three sectors in the basket's proportions." So using overall `e` and applying sectoral headroom is consistent. But then `eu = (1-a)e` is overall unbacked excess. Then `r_k = max(0, eu - c_k - v_k - m_k η_k θ_k e)`. This subtracts sectoral headroom from *overall* unbacked excess. That doesn't make dimensional sense: `eu` is overall share, `c_k`, `v_k` are sectoral shares of *sectoral* supply? The prereg says "in shares of S". But `S` is overall supply path. The sectoral values `v_k`, `m_k`, `c_k` are defined as shares of *sectoral* needs consumption (Amendment 1). There's a units mismatch.

Let's check Amendment 1 item 1: "`e` is measured on the needs baskets (the engine's `essD`, the share of needs paid for), and `S` is the no-programme run's same share. It is not total sector output. So `v` and `m` are shares of the no-programme **needs consumption**: idle capacity over needs consumption, and above-needs consumption over needs consumption."

So `v_k` = idle capacity in sector k / needs consumption in sector k.
`m_k` = above-needs consumption in sector k / needs consumption in sector k.
`c_k` = capacity built in sector k / needs consumption in sector k.
`e` = overall excess demand (overall needs consumption / overall needs supply - 1).
`eu` = overall unbacked excess.

But then `r_k = max(0, eu - c_k - v_k - m_k η_k θ_k e)`. `eu` is overall, `c_k` is sectoral. You can't subtract sectoral from overall. Unless `eu` is also sectoral? The prereg says "eu = (1-a)e the part not met by the programme's own output". If `e` is overall, `eu` is overall. But the cut `r_k` is sectoral. The prereg might mean that the overall unbacked excess `eu` is allocated to sectors in proportion to basket shares, then each sector's cut is computed. But the formula doesn't show that.

Looking at the code: `eu = (1 - S.a)*e` (scalar). Then for each sector, `r = max(0, eu - c - V.v - V.m*V.eta*th*e)`. This subtracts sectoral headroom from overall `eu`. This is dimensionally inconsistent unless `eu`, `c`, `v`, `m` are all in the same units (shares of overall needs consumption). But `v_k` is defined as share of *sectoral* needs consumption. If sectoral needs consumption is, say, 30% of overall, then `v_k` (as share of sectoral) needs to be multiplied by sector share to be share of overall. The code doesn't do this. `V.v` is directly from `SL_SRC` which is "share of the sector's no-programme needs consumption". So `V.v` is sectoral. `eu` is overall. This is a bug.

Similarly, `c_k` is built as `c + V.lam*max(0, eu - c - V.v)`. `c` is sectoral (initialized to 0). `eu` is overall. So `c_k` becomes a mix.

This is a major bug: mixing overall and sectoral shares.

The prereg says "in shares of S". If `S` is overall supply path, then all should be shares of overall needs consumption. But the sourced values are shares of sectoral needs consumption. The conversion is missing.

Amendment 1 item 1: "A sourced share of output is divided by needs' share of output before use (for example, needs 60% of output and above-needs use 40% give m = 0.67)." This converts output shares to needs-consumption shares. But it's still *sectoral* needs consumption. To get overall needs consumption shares, multiply by sector's share of overall needs consumption.

The code does not do this. `SL_SRC` values are used directly as `V.v`, `V.m`, etc. `eu` is overall. So the subtraction is wrong.

**s82Year(S, agents, p, yr, T, SP, Sin)**:
- `lf = agents[0].yrBasketUSD/CFG.LIVING_WAGE_ANNUAL/(agents[0]._hhF || 1)` - price level for this adult? Uses first adult's household factor. If households differ, this is approximate.
- `L30 = CFG.BLEI_PRECARIOUS_MAX` - threshold for below 30 days.
- `w = agents.map(a => a._w || 1)` - weights.
- `C = S.cur` - array of [q, u, x, inCCO] from `s82Acc`.
- Sorts by `q` (inc/mlc) to compute fifths.
- `S.n++`, `S.u += x[1]` (unpaid share), `S.uq[q] += x[1]`, `S.xq[q] += x[2]` (cut share), `S.nq[q]++`.
- `S.uP`, `S.nP` for participants; `S.uN`, `S.nN` for non-participants.
- Then loops agents again for `wg`, `kc`, `mi`, `bn` (BLEI), `b` (below 30 days), `bw` (weighted).
- `S.pW += wg/lf`, `S.pF += (wg+kc)/lf`, `S.pY += mi/lf`.
- `G = PRICE ? lf/(PRICE.bIdx || 1)*(PRICE.comp.other || 1) : lf` - general price level? `lf` is basket price level. `PRICE.bIdx` is endogenous basket index. `PRICE.comp.other` is price of 'other' goods. So `G` = basket price level / (endogenous index * other price)? This seems to compute a general price level for wage deflation.
- `bu = p.ccoOn && p.bu > 0 && PRICE && PRICE.buY ? PRICE.buY/lf : 0` - BU in year-0 dollars.
- `wr = nw ? sw/nw/G : 0` - mean real wage.
- Stores `bu20`, `wg20` at year 19; `buE`, `wgE`, `wf`, `ls` at last year.
- `v = agents.map(a => a.wealth/lf)` - real wealth.
- If `SP` (supply-path run), stores its median real wealth in `SP.mwY[yr]`, `SP.mwYw[yr]`.
- If `Sin` (supply-path run for this run?), computes wealth poverty against `Sin`'s median.

**Potential issues:**
- `lf` uses first adult's `_hhF`. If households have different sizes, the price level per adult differs. Using first adult's is arbitrary. Should use each adult's own `mlc` (which is `mainLoopCostUSD*cf` for that adult). But `s82Year` is called once per year, not per adult. It loops agents. It could compute `lf` per adult. But it uses a single `lf` for all. This introduces error if household sizes vary.
- `G` calculation: `lf/(PRICE.bIdx || 1)*(PRICE.comp.other || 1)`. `lf` = `yrBasketUSD / LIVING_WAGE_ANNUAL / _hhF`. `yrBasketUSD` = `CFG.LIVING_WAGE_ANNUAL * oIdx * PRICE.bIdx * _hhF` (from `runYear`). So `lf` = `oIdx * PRICE.bIdx`. Then `G` = `oIdx * PRICE.bIdx / PRICE.bIdx * PRICE.comp.other` = `oIdx * PRICE.comp.other`. `oIdx` is outside price index (fixed inflation compounded). `PRICE.comp.other` is price of 'other' goods relative to base. So `G` is the price level of 'other' goods in year-0 dollars. But wages are in current dollars. `wr = sw/nw/G` = mean nominal wage / price of other goods. The prereg says "mean wage over the general price level (the outside index times the engine's general component, which every good but the essentials follows)". The engine's general component is `PRICE.bIdx`? But `PRICE.bIdx` is the endogenous basket index. The "general price level" for non-essentials is `oIdx * PRICE.bIdx`? Actually, `mainLoopCostUSD = CFG.LIVING_WAGE_ANNUAL * oIdx * PRICE.bIdx`. So the general price level is `oIdx * PRICE.bIdx`. But `G` = `oIdx * PRICE.comp.other`. `PRICE.comp.other` is the price of 'other' category relative to base. If 'other' follows general inflation, `PRICE.comp.other` ≈ `PRICE.bIdx`? Not necessarily. The price module has `PRICE.comp` for each category. The general inflation `piG` is based on `PRICE.bIdx`. The prereg says "general price level (the outside index times the engine's general component)". The engine's general component is `PRICE.bIdx`. So general price level = `oIdx * PRICE.bIdx`. But the code uses `G = oIdx * PRICE.comp.other`. This is different. `PRICE.comp.other` is the price index for 'other' goods. If 'other' goods have same inflation as general, then `PRICE.comp.other` = `PRICE.bIdx`. But they might differ. The code should use `oIdx * PRICE.bIdx` for general price level. Using `PRICE.comp.other` is wrong unless 'other' is the numeraire. This is a bug.

- `bu = PRICE.buY / lf`. `PRICE.buY` is `buEff` (effective BU per month in current dollars). `lf` = `oIdx * PRICE.bIdx`. So `bu` = BU in year-0 dollars. Correct.

- Wealth poverty: `v = a.wealth/lf`. `lf` is same for all adults (first adult's). Should be per adult's price level. But wealth is in current dollars, `lf` converts to year-0. If `lf` is wrong for some adults, real wealth is wrong.

- `SP` and `Sin`: `SP` is the supply-path run (no-programme). `Sin` is the same? The code: `if (SP) { (SP.mwY || (SP.mwY = []))[yr] = medianOf(v); ... }` - this stores the *current run's* median real wealth into `SP.mwY`. But `SP` is supposed to be the no-programme run. This is called for *both* runs? In `runYear`, `s82Year` is called with `SP` and `Sin`. Looking at `tbRunCore` (not provided), likely `SP` is the no-programme run's `S82S` object, and `Sin` is the same for the programme run? The code stores current run's median into `SP.mwY`. If called for no-programme run, `SP` is its own `S82S`, so it stores its own median. If called for programme run, `SP` is the no-programme run's `S82S` (passed as `tbBaseS`?), so it stores programme run's median into no-programme's array? That would be wrong. The prereg says: "The median is read from the supply-path run, which is that same no-programme run with the row's other options. In the no-programme run it is the run's own median (a check)." So for programme run, `Sin` should be the no-programme run's `S82S` (with its medians). The code: `if (Sin && Sin.mwY && Sin.mwY.length > yr) { var h = 0.5*Sin.mwY[yr], ... S.ok = 1; S.wp[yr] = c/n*100; ... if (yr === T - 1){ S.mw = Sin.mwY[yr]; S.mww = Sin.mwYw[yr]; } }`. So `Sin` provides the median to compare against. `SP` is used to *store* the current run's median? But `SP` is passed as the same object for both runs? This is confusing. Likely a bug: `SP` should be the no-programme run's `S82S` for the programme run, but the code writes to it. The check in job: "every run reads the no-programme median, and the no-programme run reads its own." The code writes to `SP.mwY` for both runs. If `SP` is shared, the programme run overwrites the no-programme median. But `SP` might be different objects. In `tbRunCore`, they probably create separate `S82S` for each run, but pass the no-programme's as `Sin` for the programme run. The `SP` parameter might be the current run's `S82S` (so it stores its own median for reporting). The code uses `SP` to store, `Sin` to read. For no-programme run, `SP` and `Sin` are the same. For programme run, `SP` is its own, `Sin` is no-programme's. That works if `SP` is the current run's `S82S`. But the variable name `SP` suggests "supply path". In the call `s82Year(S, agents, p, yr, T, SP, Sin)`, `S` is current run's `S82S`. `SP` might be a separate object for storing medians? Actually, the code does `(SP.mwY || (SP.mwY = []))[yr] = medianOf(v)`. If `SP` is `S` (current run), then it stores its own median in its own `mwY`. Then `Sin` is the no-programme run's `S82S` (which has its own `mwY` from its own run). That makes sense. But the parameter is named `SP` (supply path). In the prereg, "the supply-path run" is the no-programme run. So `Sin` is the supply-path run. `SP` might be a typo for `S`? But `S` is already the first argument. Looking at `s82New`, it doesn't have `mwY`. `s82Year` adds `mwY` to `SP`. So `SP` must be an object that persists. Likely `SP` is the `S82S` of the supply-path run (no-programme). But then the programme run would write to it. The job check 9: "every run reads the no-programme median, and the no-programme run reads its own." This suggests the no-programme median is stored in the no-programme run's `S82S` and read by the programme run. So `Sin` is the no-programme `S82S`. `SP` might be unused or same as `S`. The code uses `SP` to store median. If `SP` is `S` (current run), then `S.mwY` gets the median. But `S` is the current run's `S82S`. Then `Sin` is the no-programme's `S82S`. The code reads `Sin.mwY[yr]`. That works. But why pass `SP` separately? Maybe `SP` is `S` (aliased). In the call, it might be `s82Year(S82S, agents, p, yr, T, S82S, baseS82S)`. Then `SP` is `S82S` (current), `Sin` is `baseS82S`. The code writes to `SP.mwY` (current run's median) and reads from `Sin.mwY` (no-programme median). For no-programme run, `SP` and `Sin` are the same. This works. The parameter naming is confusing but logic holds.

**s82Res(r, S, T)**:
- Computes averages.
- `r.s82U = m(S.u, S.n)` - mean unpaid share.
- `r.s82Uq1-5 = m(S.uq[q], S.nq[q])` - by fifth.
- `r.s82Xq1-5 = m(S.xq[q], S.nq[q])` - cut by fifth (same fifths as unpaid).
- `r.s82UP`, `s82UN` - participant/non-participant unpaid.
- `r.s82B30 = m(S.b, S.py)`, `s82B30w = m(S.bw, S.pyw)` - below 30 days.
- `r.s82BuR20 = S.bu20`, `s82BuRE = S.buE`.
- `r.s82WgG20 = S.wg20`, `s82WgGE = S.wgE`.
- `r.s82WF = S.wf` (wages/(wages+capital) last year), `s82WFPY = S.pW/S.pF*100` (ratio of real sums over all years).
- `r.s82LS = S.ls` (wages/money income last year), `s82LSPY = S.pW/S.pY*100` (ratio of real sums).
- If `S.ok` and `S.wp.length === T`: sets `s82Ok=1`, `s82Mw0=S.mw`, `s82Mw0w=S.mww`, `s82Wp50=S.wp[T-1]`, `s82Wp50w=S.wpw[T-1]`, `s82Wp50A=avg(S.wp)`, `s82Wp50Aw=avg(S.wpw)`.

**Potential issues:**
- `S.wp` and `S.wpw` are set in `s82Year` only if `Sin` exists. For no-programme run, `Sin` is itself, so `S.ok=1`, `S.wp[yr]` set. For programme run, `Sin` is no-programme, so `S.ok=1`, `S.wp[yr]` set. Good.
- `avg(S.wp)` averages over years 1 to T-1 (since `for (var y = 1; y < T; y++)`). `ppovA` years. Good.
- `S.mw` and `S.mww` set at last year from `Sin.mwY[yr]`. So `s82Mw0` is no-programme median at last year. Correct.
- `s82Wp50` uses `S.wp[T-1]` which is wealth poverty at last year against no-programme median. Correct.
- `s82Wp50A` averages `S.wp[y]` for y=1..T-1. Correct.

**Other bugs in sl functions:**
- `slRank(S, q)`: binary search on `S.qP` (sorted last year's q). Returns rank. If `S.qP` empty, returns 0.5. Good.
- `slNew` validation: `if (O.lam !== undefined && O.lam !== null)` - but `O.lam` could be 0. `!== null` catches null, but `0` is allowed. Good.
- `prSec(O.lam, k, V[k].lam)` - `prSec` not defined in snippet. Probably a helper to get sector value from number or object. Assuming it works.

**Major bug**: The units mismatch in `slStep` between overall `eu` and sectoral `V.v`, `V.m`, `c`. This will cause incorrect cuts. The sectoral headroom should be scaled by sector's share of overall needs consumption.

Let `share_k` = basket share of sector k (at base prices? or current?). The overall needs consumption is sum_k `need_k`. `eu` is overall excess share. The sectoral excess is `eu * share_k` (approximately). Then sectoral cut `r_k = max(0, eu*share_k - c_k - v_k - m_k η_k θ_k e_k)`. But `e_k` is sectoral excess. If overall `e` is used, `e_k ≈ e`. The code uses `eu` (overall) directly. This overstates the headroom subtraction by factor 1/share_k. Since share_k < 1, `eu` > `eu*share_k`, so the cut `r_k` will be smaller than it should be (more headroom subtracted). This biases against finding cuts.

For example, housing share ~0.3. `eu` = 0.15 (overall). Sectoral `eu_h` ≈ 0.045. `V.v` = 0, `V.m` = 0.79, `η`=0.697, `θ`=0.6, `e`=0.15. `m η θ e` = 0.79*0.697*0.6*0.15 ≈ 0.05. Code computes `r = max(0, 0.15 - 0 - 0 - 0.05) = 0.10`. But should be `max(0, 0.045 - 0 - 0 - 0.05) = 0` (since 0.045 < 0.05). So code finds a cut of 10% of overall supply, but correct is 0. This is a huge error.

The prereg says "in shares of S". If S is overall, then all variables must be in shares of overall. The sourced values are in shares of sectoral needs consumption. They must be multiplied by sectoral share of overall needs consumption. The code does not do this.

This is a critical bug.

## 5. Question 7 (the screen): holding contribution's base at wages in tail block, reading other two bases in no-tail block, fair answer?

Amendment 3: Block FT (financed rows with weighted tail on) in Reference, Adverse, Stress. "The contribution's base held at wages: 43 inputs, 528 points × 3 rows, its own trajectories (seed 70003). In place of the two bases not read with the tail: block F (no tail) in Stress. S70 ran it in Reference and Adverse. Why: S72's Amendment 2 found that the tail's 18 adults, counted as ordinary adults in every decision, distort the bases 'wages plus capital income' and 'all money income': hours +143% with the tail against +21% without. That is a property of the engine's unweighted decisions, not of the contribution. On the wages base the tail changes nothing material."

So for the screen (sensitivity analysis), they run the financed block with weighted tail on, but only for the "wages" base. For the other two bases ("wages plus capital income" and "all money income"), they don't run with tail on because the tail distorts them. Instead, they run block F (no tail) in Stress as a substitute.

The question: "is holding the contribution's base at wages in the tail block, and reading the other two bases in the no-tail block, a fair answer to the stated problem?"

The stated problem: "The assumptions screen in Stress, and on the financed rows with the weighted tail on." (from prereg Q7). The screen is to test assumptions. The weighted tail is a new feature (S72). The screen should run the financed rows with the weighted tail on, in all environments including Stress.

But the tail distorts two of the three contribution bases. So they only run the wages base with tail on. For the other bases, they run without tail (block F) in Stress.

Is this fair? The screen is supposed to show how results change under different assumptions (including the weighted tail). By not running the other bases with tail on, they are not fully screening the tail's effect on those bases. They argue the distortion is an artifact of unweighted decisions, not the contribution. But the screen is about the *engine's* behavior with the tail. If the tail causes distortion, that's a finding of the screen. Avoiding it by switching bases means the screen doesn't reveal the tail's effect on those bases. The prereg says "the screen job gains the Stress environment and a block FT, run with the frozen design's inputs... block FT... the contribution's base held at wages... In place of the two bases not read with the tail: block F (no tail) in Stress."

This seems like a compromise. But is it a "fair answer"? The problem asks for the screen in Stress with weighted tail on. They partially do it (only wages base). For other bases, they fall back to no-tail. This doesn't answer how the tail affects those bases. It avoids the issue. A fair answer would be to run all bases with tail on, note the distortion, and interpret accordingly. Or run with tail on but with weighted decisions (if that's the fix). But they don't. So it's not a full answer to the stated problem. It's a partial answer with a workaround.

## 6. Checks and decision rules: any check that wouldn't catch a likely bug; any decision rule unclear or gameable?

**Checks (prereg):**
1. Off = identical: guard test, full-output diffs. Good.
2. Nesting: A 'full' at share 0 equals base programme row. Good.
3. Inactive at full backing: A 'strict' at share 1 equals main row. Good.
4. No-programme run unchanged by A, C, and B (π=0). Good.
5. B with wIdx=1 identical whatever wc; C with L=0 identical. Good.
6. Money accounts close; cut's dollars appear once. Good.
7. Eight random draws per adult-year unchanged; A draws nothing. Good.
8. Release start's baseline check passes. Good.
9. (Amendment 3) Building speed at sourced values equals sourced row; at 0 moves limit; s82 moves no other key; every run reads no-programme median, no-programme run reads own. Good.

**Likely bugs not caught:**
- The units mismatch in `slStep` (overall vs sectoral) would not be caught by these checks. Check 2: 'full' reading uses `v=Infinity`, so `r=0` always. The bug is in sectoral headroom calculation, but 'full' bypasses it. Check 3: 'strict' at share 1 has `eu=0`, so `r=0`. The bug only appears when `eu>0` and `rd` is 'sourced' or 'restricted'. The checks don't run a case with `eu>0` and sourced values. The dry run at 2 seeds might catch it if they inspect values, but the check is only equality tests. The selftest runs "equality tests only; no outcome value was printed". So the bug would not be caught.

- The `s82Year` `lf` and `G` issues: not caught by equality checks.

- The `slCut` 'bu' rule mixing years: not caught.

**Decision rules:**
1. Failed check → fix, rerun, only rerun reported. Clear.
2. "Holds under supply limit": effect keeps sign, 95% interval excludes zero under sourced reading with all three sharing rules. Per backed share, per primary outcome, never pooled. Clear.
3. Depends on rule: if holds with design's rule but not market's, report rests on sharing rule. Clear.
4. Strict bound in every table, labelled, no headline from it alone, no statement leaves it out. Clear.
5. Findings page: main row headlines cannot change; dated note replaced by curve. Clear.
6. Indexing: monthly/quarterly first, then yearly, then two-year. Sentence names delay. Clear.
7. Q4: if interaction interval excludes zero, separate effects not summed; joint row reported. Clear.
8. No tuning: sourced values fixed in Amendment 1; change after dry run = dated amendment with reason and full rerun. Clear.

**Unclear/gameable:**
- Decision rule 2: "under the sourced reading with all three sharing rules". What if it holds for 2 of 3? Then it doesn't hold. Strict.
- "The slowest building speed at which a result holds" (Amendment 3): per primary outcome and share, smallest λ where rule 2 passes. If λ=0 passes, "holds at strict bound". If λ=1 fails, "does not hold at any building speed on grid". Read on grid, never interpolated. This is clear but "slowest" assumes monotonicity. If non-monotonic, ambiguous. Not gameable but potentially misleading.
- Decision rule 4: "no headline is taken from it alone, and no statement about supply limits leaves it out." This is a reporting rule, not a decision rule per se. Could be gamed by not making statements about supply limits? But the rule says "no statement about supply limits leaves it out", so any statement must include it. Hard to game.
- "No tuning" rule: "nothing here is changed to reach a figure." But the amendments themselves change the design (e.g., Amendment 3 adds sweep). The rule says "A change after the dry run is a dated amendment with its reason and a full rerun." This is good.

## 7. Five most important changes before dry run, ranked.

1. **Fix the units mismatch in `slStep` (critical bug)**: The overall `eu` and sectoral `V.v`, `V.m`, `c` are in different units (overall vs sectoral needs consumption shares). This will produce wildly incorrect cuts. Must convert sectoral headroom to overall shares by multiplying by sector's share of overall needs consumption (basket share at current prices). This is the most important fix.

2. **Fix `s82Year` price level calculations**: `lf` should be per-adult (using each adult's `mlc` or `yrBasketUSD`), not first adult's. `G` (general price level) should be `oIdx * PRICE.bIdx` (outside index * endogenous basket index), not `oIdx * PRICE.comp.other`. This affects real wage, real BU, real wealth, wealth poverty.

3. **Sweep θ (price response) for housing and medical**: The unsourced θ placeholders (0.6, 0.5) are critical for above-needs demand response. A sweep (e.g., 0.3, 0.6, 0.9) should be added before dry run, as a sensitivity. The prereg acknowledges θ is unsourced and a limitation. Not sweeping it leaves a major uncertainty unquantified.

4. **Clarify/correct `slCut` 'bu' rule timing**: The rule mixes last year's totals (`need`, `pC`, `pE`) with this year's `cash` and `E`. The prereg says "at last year's totals". The code should use last year's `cash` and `E` composition, or clearly document the approximation. The realized cut deviation is reported, but the rule should be implemented as specified.

5. **Run the screen (Q7) with tail on for all bases, or document distortion**: The current plan avoids the tail for two bases. The screen should either run all bases with tail on (accepting distortion as a finding) or implement weighted decisions for the screen. The workaround of using no-tail block for Stress is not a full screen.

Other notable: The `slNew` `lam` override for 'full' reading throws error, but 'full' uses `v=Infinity` so `lam` irrelevant. Fine. The `slCut` `f0p` (paid-for poverty) doesn't include cut adjustment, but that's by design (it's "paid-for" not "received"). The `s82Year` double loop over agents (once for `cur`, once for wages/wealth) is inefficient but not wrong.

Ranking: 1 (critical bug), 2 (affects all s82 keys), 3 (major uncertainty), 4 (implementation fidelity), 5 (screen completeness).

Now write the answer.