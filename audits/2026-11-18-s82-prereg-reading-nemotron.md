# S82: an outside reading of the preregistration with Amendments 1-3, before the dry run (Nov 18, 2026)

**What was sent.** `audits/nvidia-2026-11-18-s82/build_packet.py` builds the packet (227,907 characters). It holds the reviewer's instructions (seven headings), the preregistration as committed with Amendments 1-3 (research-update `e11a717`), and the engine code of compassionism-simulation `ef15c3e` (v5.9.18 before the fix below), `index.html` lines 5568-6958. That range runs from the C2.2 needs block through `runYear`, the supply limit (`sl`) and the study's reporting keys (`s82`). The slice was meant to start at the supply limit and began at an earlier comment; the extra code is engine context, nothing else. The request (`packet.json`, `nemotron/packet.json`) used streaming, temperature 0.3.

**Models and attempts** (NVIDIA API catalogue; the model list read again on Nov 18: 32 models):
- Mistral Large 4 (`mistralai/mistral-large-4-1t-a52b`, max_tokens 16,000): slow (about 17,500 characters of reasoning in 17 minutes). The session's container restarted at 01:11 UTC and cut it before any answer (`mistral-reasoning-partial.md`, `mistral-stream-partial.txt`).
- Nemotron 3 Ultra (`nvidia/nemotron-3-ultra-550b-a55b`, max_tokens 32,000): the first attempt was cut by the same restart after 7,831 characters of answer (`nemotron/reply_content-partial-1.md`). The second attempt finished (`finish_reason` "stop"; 45,034 characters of reasoning, 8,661 of answer): `nemotron/reply_content.md`, `nemotron/reply_reasoning.md`, `nemotron/stream.txt`.

It is a reading, not a result. Every point below was checked against the code or an opened source before anything changed.

## Triage

| # | The reading's point | Checked against | Verdict | What changes |
|---|---|---|---|---|
| 1 | Amendments 1-3 are dated before any run and change nothing after seeing a result | the file | Agreed | none |
| 2 | (first attempt, §4) `s82BuR20`/`s82BuRE` use the wrong price index | `index.html` 6210-6216: the BU follows `colaF`, the C2.2 needs' price (outside index × `c22Share`); the key divided by the whole basket's price | **Confirmed** (a build error: the preregistration says "the BU over the needs' price") | Fixed in v5.9.18 (`3e345eb`), before any run; unit test added (a two-year delay lowers the real BU) |
| 3 | θ, the essentials price response (housing 0.6, medical 0.5), is unsourced and scales housing's above-needs give-up `m·η·θ·e`; not swept | the preregistration's limits; research rule 3 | **Confirmed** | Amendment 4: θ at half and double (34 rows) |
| 4 | "The slowest building speed at which a result holds" assumes the pattern is monotone | Amendment 3, analysis item 2 | **Confirmed** (wording) | Amendment 4 defines it for any pattern |
| 5 | `slStep` mixes units: `eu` is an overall share, the headroom terms are sectoral | Section A; Amendment 1, item 1; the stated limit that the extra need is spread over the sectors in the basket's proportions | Not confirmed. `e` is the same proportional excess in every sector, so `eu`, `v_k`, `m_k`, `c_k` and `r_k` are all shares of sector k's own needs consumption, and `R_k` is applied to each household's spending on k. The unit test `slStep` checks the formula with known values | A sentence in Amendment 4 states the units |
| 6 | `s82Year` reads the price level from the first adult | the engine's convention (`tbRepYear`, `dmYear`): the level is `oIdx × bIdx`, the household factor divided out, the same for every adult | Not confirmed | none |
| 7 | The general price level should be `oIdx × bIdx`, not `oIdx × comp.other` | `tbRunCore`: every basket component but the essentials is set to the general level `PG`; `bIdx` is the basket's index, essentials included | Not confirmed (`comp.other` is `PG`; the preregistration asks for the general level) | none |
| 8 | CE health spending includes employer-paid premiums, so medical `m` is understated | BLS Handbook of Methods, CE concepts (opened Nov 18): expenditures are "the actual financial obligation incurred ... by the CU"; "in-kind benefits" are "nonexpenditure consumption" | Not confirmed: CE health care is the household's own payments, as MIT's line is. Medical care's headroom is new capacity either way, which the building-speed sweep covers | none |
| 9 | Housing `m` (0.79) may be overstated by the population mismatch | Amendment 2, item 2 (argues the other direction) | Open (direction unclear) | none: the restricted reading (m 0.40) and the CE low end (0.43) bracket it, and both are reported |
| 10 | Housing λ (0.2) is an error-correction speed, not a building speed; sweep it | Amendment 2 says so ("the generous side for building") | Agreed as a limit | none: sourced; the restricted reading halves it to 0.1 |
| 11 | The `bu` rule mixes last year's totals with this year's spending | Amendment 1, item 3 (stated; `slCutSh` reports the realised cut) | Agreed as a stated approximation | none |
| 12 | Question 7: holding the base at wages in block FT avoids the tail's distortion instead of measuring it; run all bases with the tail | S72 Amendment 2; the Morris design | Not adopted. In a one-at-a-time screen, trajectories through points with the distorted bases would carry the distortion into every other input's elementary effects, and the screen ranks inputs. The distortion itself is measured and published by S72's frontier with and without the tail | none |
| 13 | Check 9 would not catch the unit error in item 5 | item 5 | Not applicable | none |

## The reply, word for word (second attempt)

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