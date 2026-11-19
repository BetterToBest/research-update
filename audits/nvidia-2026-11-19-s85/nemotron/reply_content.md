# Independent Review of the Compassionism Simulation Preregistration (S85)

---

## 1. Economics of the new mechanism

### Output kept while paid hours fall
**Preregistration §B–C:** "The automated work is still done (output kept), and its output plus the part of the gain not paid as wages goes to owners."  
**Modeller's reading R4:** "The automated work is still done, by machines and software, so output does not fall when paid hours do."

**Problem:** This assumes **perfect substitution** of capital for labour with no adjustment costs, no complementary inputs, and no demand constraint. If 50% of paid hours are displaced but output is held constant, output per remaining hour must double (over 20 years: 3.5%/yr above trend). The sources (Acemoglu 0.1 pp/yr; Goldman Sachs 1.5 pp/yr for a decade) do not support this magnitude. The preregistration itself acknowledges (§Limits): "Lower prices from automation (real gains for every buyer) enter only through the pass-through to wages. In the main reading the rest goes to owners." But if output is *kept* while hours fall, the "dividend" `Div_t` is **pure rent to owners**—it is not produced by any additional input; it is an accounting identity: `Div_t = Σ E⁰_i,t × [(1−h)G + h(1−pw)(G−1)]`. This **double-counts** the gain: the same output appears once as wages (for remaining hours) and again as capital income to owners. In a closed economy, the sum of factor payments cannot exceed total output. The model has no aggregate output `Y` to enforce this adding-up constraint (MODEL_SPEC 6.12: "there is no aggregate output"). The price rule `P_G,t+1 = P_G,t × (1 + λ_G × U_t / Y_t)` uses `Y_t` = "aggregate cash income", not real output. So the dividend can grow without bound relative to the real resource base.

### Dividend of automated work going to owners
**Preregistration §D:** "A share `own` of Div_t is credited as capital income to adults in proportion to their business and stock holdings (`rt` classes, under the weights of `wt`). The rest goes to owners outside the model's households. `own` is 1, swept at 0.5, until Amendment 1 sets the sourced value."

**Problem:** `own = 1` means **all** of the dividend goes to model households (who hold 100% of US business equity). The source (Federal Reserve Financial Accounts B.101/L.223 or Rosenthal & Burke 2020) will show a lower share—likely 60–75% after foreign and institutional holdings. Using `own = 1` **biases in favour of the programme** because it recycles the entire automation dividend back into household income (and thus into BU spending capacity), inflating the programme's apparent fiscal space. The sweep at 0.5 is arbitrary and not sourced.

### Pass-through of the gain to wages
**Preregistration §C:** "Those still in paid work receive 0.7 of the gain in their pay; 0 and 1 are swept."  
**Modeller's reading R4:** "Those still in paid work receive 0.7 of the gain in their pay... from Stansbury and Summers."

**Source check:** Stansbury & Summers (2017) abstract: "One point more productivity growth goes with 0.7 to 1 percentage points higher median and average compensation growth and 0.4 to 0.7 percentage points higher production/nonsupervisory compensation growth." The preregistration picks 0.7 (where the two ranges meet). This is **reasonable as a central estimate** but the sweep at 1.0 (full pass-through) is inconsistent with the same source's upper bound for production workers (0.7). Using `pw = 1` in a sweep **overstates wage growth** for the bottom half.

### Programme's own work valued at pay over the labour share
**Preregistration §F (backing produced):**  
`M_t = m × (H^P_t + H^C_t) × (pay_t / s_L) × G_t + Σ_s K_s × (1−δ)^(t−s−1) × y_K × G_t`

**Modeller's reading R7:** "An hour of programme work produces what an hour produces in the economy: its pay over labour's share of output (from the national accounts), times the forecast gain."

**Problem 1 (double count):** `pay_t / s_L` is **output per hour in the nonfarm business sector** (since `s_L` = labour share = compensation / output). But `pay_t` is the *contract pay* (living wage ≈ $49,370/2080 = $23.74/hr), not the economy-wide average wage (~$35/hr in 2024). Using the lower contract pay **understates** the output attributed to programme work. However, the programme's project work is *not* representative of the nonfarm business sector—it is heavily weighted toward care, community, and creative work (Creative Collectives, PTF). The labour share `s_L` for those sectors is higher (lower capital intensity), so `pay/s_L` would be *lower* than the economy average. The model uses the **aggregate** `s_L`, which **overstates** output per programme hour.

**Problem 2 (leak):** The term `m × (H^P_t + H^C_t) × (pay_t / s_L) × G_t` counts **all** programme hours as producing market output scaled by `m` (share sold in shops). But `H^C_t` = "hours behind other conversions: their BU at face value over the contract pay". Conversions are **BU spent at face value**—they are not hours worked. The modeller's reading R7 says: "The hours behind a conversion are its BU at face value over the contract pay, as the model already counts project hours." This **conflates a financial flow (BU spending) with labour input**. A conversion dollar does not imply an hour of work; it implies a dollar of demand. Counting it as `H^C_t` hours at `pay_t/s_L` output per hour **invents output** that does not exist. This is a **leak** that biases the backing produced **upward**.

**Problem 3 (contradicts price rule):** The price rule (MODEL_SPEC 6.12) says matched output = "ESP reinvestment at face value and the project payout (`PROD.match 'market'`)". The backing-produced row **replaces** the project payout's market valuation with `M_t`. But `M_t` includes `G_t` (the automation gain), which is **not** produced by the programme—it is an exogenous multiplier applied to programme hours. The price rule's `U = (1−a)×(BU spent + conversions − matched output)` treats matched output as *real resources* absorbing money. If `M_t` includes `G_t > 1`, the model claims the programme produces *more* output per hour than the economy average *because of automation*—but the programme's work is not automated. This **contradicts the price rule's logic**: matched output should be the programme's *own* production, not the economy's automation dividend.

---

## 2. Displacement levels and consistency check

### Are 10%, 30%, 50%, 70% fair to sources?
**Preregistration:** "Duke added... three displacement levels: 30%, 50% and 70%."  
**Modeller's reading:** "I read each figure as the share of today's paid hours no longer done by people at the horizon, net of the new work that appears."

**Source check:**
- IMF (Cazzaniga et al.): "about 60 percent of jobs are exposed [in advanced economies], of which about half may be negatively affected" → **~30% of jobs harmed**. This matches the 30% reading *if* "harmed" = "displaced net of new work". But the IMF says "half could benefit"—new work creation is *already* in their 30% net figure. The preregistration treats 30% as *net* displacement, which is consistent.
- Frey & Osborne: 47% of employment in occupations with probability > 0.7. This is **exposure**, not displacement. The modeller notes: "Exposure is not loss." Using 47% as a displacement anchor **overstates** loss.
- Eloundou et al.: 19% of workers have ≥50% tasks exposed; 47–56% of *tasks* could be sped up with software. Task exposure ≠ hour displacement.
- Acemoglu & Restrepo: "automation always reduces the labor share... slower growth of employment... reflects stronger displacement and weaker reinstatement." But no magnitude for 20-year net displacement.

**Verdict:** 30% is **at the edge** of sourced net-displacement estimates (IMF harmed share). 50% and 70% **exceed** all sourced net-displacement figures. The preregistration correctly labels them "stress readings, beyond the forecasts" (§Checks 4). The 10% reading is added for "the case where new work replaces most of what is automated, as it has in the past" (modeller's reading). This is **fair** as a sensitivity range, but the preregistration should not present 50%/70% as "Duke's view" without clarifying they are stress tests.

### Consistency check: implied output per remaining hour
**Preregistration §G:** "Reported: the implied output per remaining hour (G_t / (1 − D_t))."  
**Modeller's reading:** "If output is kept while paid hours fall by these shares, output per remaining hour must rise. Over 20 years that is 1.8%, 3.5% and 6.2% a year above the usual growth. Over 40 years it is 0.9%, 1.75% and 3.1%. The highest forecast I opened is 1.5 points a year for a decade. So at 20 years, 30% is at the edge of the forecasts, and 50% and 70% are beyond them."

**Check:**  
- `G_t = (1 + u/100)^(T × S(t/T))` with `u = 0.1` (0.1%/yr gain) or `u = 1.5` (1.5%/yr gain).  
- At `D = 0.3`, `T = 20`: output per remaining hour = `G_20 / 0.7`. If `u = 0.1`, `G_20 ≈ 1.02`, ratio ≈ 1.46 → 1.9%/yr above trend. If `u = 1.5`, `G_20 ≈ 1.35`, ratio ≈ 1.93 → 3.3%/yr.  
- The modeller's 1.8%/3.5%/6.2% assumes `u = 0` (no exogenous gain, all from displacement). But the preregistration runs `u = 0.1` and `u = 1.5` *on top of* displacement. The consistency check should use the **same `u` as the row**. The reported "implied output per remaining hour" must be computed per row, not as a single number per `D`. The preregistration says "Reported: the implied output per remaining hour (G_t / (1 − D_t))"—this is correct *if* `G_t` includes the row's `u`. But the modeller's text computes it at `u = 0`. **Inconsistency:** the modeller's reading uses a different `u` than the rows will. The check must be row-specific.

---

## 3. Backing produced computation (M_t)

### Formula (Preregistration §F):
```
M_t = m × (H^P_t + H^C_t) × (pay_t / s_L) × G_t
    + Σ_s K_s × (1−δ)^(t−s−1) × y_K × G_t
```
- `H^P_t` = project hours (engine's)
- `H^C_t` = BU at face value / contract pay (modelling assumption R7)
- `pay_t` = contract pay (living wage / 2080, indexed)
- `s_L` = labour share (BLS, nonfarm business)
- `m` = share of programme work sold in shops (0.25, 0.5, 1)
- `K_s` = ESP reinvestment year `s` (year-0 $)
- `y_K` = output/$ fixed capital in essentials (BEA, capped 0.32)
- `δ` = 5%/yr
- `G_t` = automation gain multiplier

### Is it a fair test of whether programme work backs its payout?
**No.** Three biases:

**Bias FOR the programme (upward):**
1. **`H^C_t` invention:** Conversions are BU spending, not hours worked. Counting `BU_face / pay_t` as "hours" and multiplying by `pay_t/s_L` = `BU_face / s_L` imputes output = `m × BU_face / s_L × G_t`. Since `s_L ≈ 0.6`, this says **every dollar of BU spent at face value produces $1.67 of output** (times `m` and `G_t`). But BU spent at face value is *matched* by ESP output (ESP reinvestment at face value is already counted in matched output). This **double-counts** the ESP channel: once as `K_s` yield, again as `H^C_t` output.
2. **`G_t` multiplier on programme work:** The automation gain `G_t` applies to *economy-wide* output per hour. Programme work (care, community, creative) is **not automated** in the model. Applying `G_t` to it assumes the programme's productivity rises *as fast as* the automated sector's—a **spillover assumption with no source**.
3. **`m = 1` sweep:** The design does not state `m`. Sweeping to 1 assumes *all* programme work is market goods/services. The modeller's reading R7: "How much of that work is goods and services sold in shops is not in the writing. It is a design parameter, swept at a quarter, a half and all of it." Using `m = 1` as a main reading **overstates** backing.

**Bias AGAINST the programme (downward):**
1. **`pay_t` = living wage, not market wage:** Contract pay ≈ $23.74/hr vs. economy avg ~$35/hr. `pay_t / s_L` understates output per hour by ~30%.
2. **No output from BU spending on essentials:** BU spent at face value at ESPs buys real goods (food, housing, care). The model counts ESP *reinvestment* (`K_s`) as matched output, but not the *current-year* essentials output purchased by BU. The price rule (6.12) says `P_E,k = 1 + θ_k × (D−S)/S`—essentials prices rise if demand exceeds capacity. But the *output* of that capacity is not counted as matched output. This **understates** backing.
3. **Lag and wear on `K_s`:** `K_s` yields from next year at `y_K` and wears at 5%/yr. But ESP reinvestment builds *capacity* that produces output *every year*. The perpetuity formula `Σ K_s (1−δ)^(t−s−1) y_K` is correct for a decaying capital stock, but `y_K` is capped at 0.32 (economy-wide). Essentials industries (grocers, utilities) have **higher** output/capital (lower capital intensity). Capping at 0.32 **understates** their yield.

### What would make it biased?
| Direction | Mechanism |
|-----------|-----------|
| **For** | `H^C_t` double-counts BU spending; `G_t` on programme work; `m = 1` |
| **Against** | `pay_t` too low; essentials output from BU spending not counted; `y_K` cap too low for essentials |

---

## 4. Outcomes, offset categories, decision rules

### Are outcomes fixed before the run?
**Preregistration §Outcomes:** Lists 4 primary outcomes (basket poverty, wealth poverty avg & last year, savings ≥3 months), displacement cost/offset definitions, and 15+ secondary outcomes. **Yes, fixed.**

### Offset categories and decision rules
**Preregistration §Decision rules 2:** Four categories per primary outcome: *offsets fully*, *offsets in part*, *does not offset*, *worsens*. Based on paired-bootstrap intervals (10k replicates), Holm-corrected across 4 primary outcomes per question/environment/horizon/reading. **Sound and fixed.**

### Anything that could let a result be chosen after seeing it?
**Potential issues:**
1. **Holm correction scope:** "Holm across the four primary outcomes within each question, environment, horizon and reading, for any statement that the programme 'offsets' a cost or that a reading 'changes' an effect." This is **per-reading**, not across all readings. A reading with a favourable offset can be highlighted without correcting for the 124 rows × 3 environments × 2 horizons = 744 tests. The preregistration says: "Advocacy material may lead with the strongest robust findings; nothing is dropped from the record." This **allows cherry-picking** for advocacy, though the full record is kept.
2. **Offset share reported "only where cost_N's interval excludes zero"**: If displacement cost is not significant, offset share is not reported. This **hides** cases where the programme appears to help but the baseline cost is noisy.
3. **Q4 (backing produced) has no decision rule:** "The produced backed share against the published break-even shares... Each produced-backing row's own inflation is read directly. No new backing grid." No category for "backing sufficient/insufficient". This leaves interpretation open post-hoc.
4. **Stress readings label (§Decision rules 4):** "Wherever they are shown, they are labelled 'stress readings, beyond the forecasts'. No headline rests on them alone." But nothing prevents a headline from resting on *non-stress* readings that are still favourable only under specific `m`, `u`, `pw` combos.
5. **Amendment 1 fixes sourced values *before dry run*:** "The sourced values are fixed in Amendment 1 from opened sources only, before the dry run. A change after the dry run is a dated amendment with its reason and a full rerun." This is good, but the dry run itself could inform *which* sourced values to pick (e.g., choosing a higher `own` share if the dry run shows low backing). The preregistration says Amendment 1 fixes "the sourced values listed under 'To open before the dry run'"—but the *choice* of which source to use (e.g., Fed Financial Accounts vs. Rosenthal & Burke) is not pre-specified.

---

## 5. Missing elements a sceptical labour/macro economist would expect

| Omission | Bias direction | Reason |
|----------|----------------|--------|
| **Demand shortfall from automation** | **For programme** (cautious) | Preregistration §Limits: "Owners' lower spending out of the dividend is not modelled. This is the cautious side for the design, since the programme's spending would fill such slack." Correct: if owners save more of the dividend, aggregate demand falls, lowering output and wages. The programme's BU spending offsets this. Omitting it **biases against finding a shortfall** in the no-programme run, making the programme look *more* necessary but also *more* effective (since it fills a gap that isn't modelled). |
| **Prices falling with automation (real gains to buyers)** | **Against programme** | §Limits: "Lower prices from automation enter only through the pass-through to wages. In the main reading the rest goes to owners." If automation lowers prices, real wages rise even without nominal wage gains. The model only passes 70% of productivity gain to wages; the rest goes to owners as *nominal* capital income. But if prices fall, the *real* value of that capital income is higher. The model's price rule (6.12) ties `P_G` to unmatched money `U`, not to productivity. So automation gains **do not lower prices**—they only raise nominal incomes (wages + dividends). This **biases against the programme** because the BU's real value erodes if `P_G` rises with `U`, but automation's real gains are not captured. |
| **Reallocation into new work** | **For programme** (if new work is low-pay) / **Against** (if new work is high-pay) | §Limits: "New occupations that automation creates enter only through the net displacement readings." The model has **no occupational mobility** except job loss → re-employment at 0–20% lower pay (12.1). In reality, displaced workers move to new occupations (Autor et al.: most employment is post-1940 new work). If new work pays less, the model's "permanent job loss at lower pay" captures it. If new work pays more, the model misses it. **Direction ambiguous**, but likely **biases against programme** because the BU makes low-pay new work more viable (reservation wage effect), which the model's labour response (6.11) partially captures via `ρ = 0.16` on unconditional dollars. |
| **Hours tied to occupation** | **For programme** (concentrates loss) | Preregistration §B: "Hours are not tied to occupation in the engine, so this counts adults, not hours (a limit)." The `f: 'jobs'` form displaces *adults* (entire hours), `f: 'hours'` cuts hours proportionally to risk. Real automation cuts hours *within* occupations (e.g., radiologists read fewer scans). The model's binary job loss **overstates** the concentration of loss (all-or-nothing), making the programme's floor **more critical**—biases *for* finding large offset. |
| **Capital deepening / investment response** | **Against programme** | The dividend `Div_t` goes to owners as capital income. In a standard model, this raises savings → investment → capital stock → future output. The model has **no investment function**; `K_s` is only ESP reinvestment (fixed 20% of BU accepted). The automation dividend does not raise `K_s`. This **understates long-run output** in both runs, but more so in no-programme (where dividend is larger if `own=1`). Biases **against programme** in 40-year horizon. |
| **Fiscal / financing feedback** | **For programme** | §Limits: "The corporate revenue tax (financing; a separate study)". The BU is financed by "The Source issues the BU, pays conversions and keeps the conversion tax" (6.12). No tax distortion, no debt, no crowding out. This **biases for programme** by ignoring financing costs. |
| **Heterogeneous pass-through by wage level** | **Against programme** (for low-wage) | Stansbury & Summers: pass-through 0.4–0.7 for production workers, 0.7–1.0 for average. Model uses single `pw = 0.7`. Low-wage workers (more likely displaced) get **less** pass-through than average. Model overstates their wage gain → **biases for programme**. |
| **BU interaction with automation displacement** | **For programme** | Displaced adults get BU (if in programme run). But BU is **unconditional**—it does not require job search. Labour response (6.11): `ρ = 0.16` on unconditional dollars. This reduces labour supply. In no-programme run, displaced adults get UI (32% of pay for 26 weeks) then nothing. The BU **cushions** displacement but also **reduces re-employment**. The model captures this via `ρ`, but the net effect on poverty/wealth is ambiguous. Not a clear bias, but a key mechanism. |

---

## 6. Sources used correctly?

| Source | Claim in preregistration / reading | Actual source support | Verdict |
|--------|-----------------------------------|----------------------|---------|
| **Pencavel (2015)** | "Below 49 weekly hours, variations in output are proportional to variations in hours" → shorter weeks bring no gain per hour. | Correct quote. But Pencavel studies **munition workers in WWI** (mostly women, 12-hr shifts). Generalising to 2025 US service/knowledge work is **extrapolation beyond support**. | **Misused** (external validity) |
| **IMF (Cazzaniga et al.)** | "About 30% of jobs in advanced economies at risk of being harmed: the 30% reading's anchor." | IMF: "about 60% of jobs exposed... about half may be negatively affected" → 30% of *jobs*. But "negatively affected" ≠ "displaced net of new work". Could mean wage cut, hour cut, or job loss. | **Stretched** (negatively affected ≠ net displacement) |
| **Frey & Osborne (2013)** | "47% of US employment in occupations with probability > 0.7" → used as engine's automation risk. | Correct. But F&O is **computerisation probability**, not AI displacement. Many high-prob occupations (e.g., telemarketers) already declined. | **Dated but acceptable as risk proxy** |
| **Acemoglu (2024)** | "TFP no more than 0.66% over 10 years... GDP around 1.1% over 10 years" → low reading 0.1 pp/yr. | Acemoglu: "GDP around 1.1% over the next 10 years" = 0.11%/yr. TFP 0.66% over 10 years = 0.066%/yr. Preregistration uses 0.1 pp/yr for *output per hour* gain. **Consistent**. | **Correct** |
| **Goldman Sachs (2023) as quoted in Acemoglu** | "1.5% per annum increase in US productivity growth over a 10-year period" → high reading 1.5 pp/yr. | Acemoglu quotes GS: "a 1.5% per annum increase in US productivity growth over a 10-year period". But GS's own report (Briggs & Kodnani 2023) says "1.5% *average annual* productivity growth *boost*"—i.e., 1.5 pp/yr *for a decade*, not forever. Preregistration uses it as a *permanent* gain rate `u = 1.5` along S-path to year 20/40. **Extrapolates a decade-long boost to 20/40 years**. | **Misused** (horizon mismatch) |
| **Stansbury & Summers (2017)** | "One point more productivity growth goes with 0.7 to 1 pp higher median/average compensation... 0.4 to 0.7 for production workers" → `pw = 0.7` (where ranges meet). | Correct. But the sample is 1973–2016, pre-AI. AI may have different pass-through (Acemoglu expects widening capital-labour gap). | **Dated but best available** |
| **Autor et al. (2024)** | "Majority of current employment is in new work introduced after 1940" → why displacement readings are net of new work, and why low reading kept. | Correct. But "new work" includes high-skill (software) and low-skill (personal care). Net displacement depends on *which* new work appears. | **Correctly cited** |
| **BLS labour share (to open)** | `s_L` for `pay_t / s_L` in backing formula. | Nonfarm business labour share ≈ 0.58–0.62 (2020s). But programme work is not nonfarm business. | **Misapplied** (sector mismatch) |
| **BEA `y_K` (to open)** | Output/$ fixed capital in essentials, capped at 0.32. | Economy-wide `y_K` ≈ 0.32. Essentials (grocers, utilities) have **higher** output/capital (lower capital intensity). Capping at 0.32 **understates** ESP yield. | **Biased down** |

---

## 7. Three most important changes before the build

### 1. Fix the `H^C_t` double-count and `G_t` misapplication in backing produced
**Quote (Preregistration §F):**  
`M_t = m × (H^P_t + H^C_t) × (pay_t / s_L) × G_t + Σ_s K_s × (1−δ)^(t−s−1) × y_K × G_t`  
where `H^C_t` = "hours behind other conversions: their BU at face value over the contract pay (the reading's R7, a modelling assumption)"

**Change:**  
- **Remove `H^C_t` entirely.** Conversions are BU spending, not labour input. The output they elicit is already captured by ESP reinvestment (`K_s`) and the price rule's capacity response.  
- **Remove `G_t` from the programme-work term.** Programme work is not automated. Replace `× G_t` with `× 1` (or a separate, sourced programme-productivity parameter).  
- **Use sector-appropriate `s_L` and `y_K`.** For ESPs, use BEA industry-level labour share and output/capital (not economy-wide caps).

**Why:** This is the **core measurement** of Q4 (backing produced). As written, it invents output from BU spending and imports the economy's automation gain into the programme's work, biasing the backing share upward by a factor of 2–3×.

---

### 2. Enforce adding-up: dividend + wages ≤ real output
**Quote (Preregistration §D):**  
`Div_t = Σ_i E⁰_i,t × [(1−h_i,t) G_t + h_i,t (1−pw)(G_t−1)]`  
"A share `own` of Div_t is credited as capital income... The rest goes to owners outside the model's households."

**Change:**  
- Introduce an **aggregate real output** `Y_t^real` that grows at baseline productivity + automation gain `u` on *remaining hours*.  
- Constrain: `Σ wages_t + Div_t ≤ Y_t^real`.  
- If `Div_t` + wages exceed `Y_t^real`, scale down `Div_t` (or `pw`) proportionally.  
- Feed `Y_t^real` into the price rule: `P_G,t+1 = P_G,t × (1 + λ_G × U_t / Y_t^real)` (replace cash income `Y_t` with real output).

**Why:** Without this, the model creates **nominal income from nowhere**. The dividend is an accounting residual that can exceed the real resource base, making the programme look more fiscally sustainable than it is. The price rule currently uses cash income `Y_t` (which includes the dividend), creating a **feedback loop**: higher dividend → higher `Y_t` → lower inflation → higher real BU → higher spending → higher `U_t`... but no real output constraint.

---

### 3. Pre-specify the `own` share and `m` parameter with sourced values, not sweeps
**Quote (Preregistration §To open before dry run):**  
"1. The share of US business and corporate equity held by US households... `own`."  
"Amendment 1 fixes the sourced values... before the dry run."

**Quote (Modeller's reading R7):**  
"How much of that work is goods and services sold in shops is not in the writing. It is a design parameter, swept at a quarter, a half and all of it."

**Change:**  
- **`own`:** Use Federal Reserve Financial Accounts (B.101 + L.223) to compute US household direct + indirect (via funds) share of US corporate equity. **Fix this single number in Amendment 1.** No sweep.  
- **`m`:** Derive from the design's own documents. The "corporate transformation paper" and "implementation roadmap" describe Creative Collectives, PTF, projects. Estimate the share of programme work that is *market goods/services* (e.g., PTF grocery/housing/healthcare are market; Creative Collectives' art/care/community are not). **Fix a single sourced/derived value in Amendment 1.** No sweep.  
- If the design truly has no basis for `m`, **state `m` as an unknown** and report backing produced as a function `M_t(m)`, not as a sweep of three arbitrary points.

**Why:** `own = 1` (current main) recycles 100% of the automation dividend to households—**implausible** (foreign/institutional holdings ≈ 30–40%). `m = 1` assumes all programme work is sold in shops—**contradicted** by the design's emphasis on care, community, creative work. Sweeps let the analyst pick the favourable value post-hoc. Fixing them *before* the dry run from sources closes this degree of freedom.

---

### Summary of biases
| Mechanism | Bias | Magnitude |
|-----------|------|-----------|
| `H^C_t` double-count | **For programme** (backing ↑) | Large (×1.5–2) |
| `G_t` on programme work | **For programme** (backing ↑) | Large (×1.3–1.9 at 20yr) |
| `own = 1` | **For programme** (dividend recycled) | Medium (×1.3–1.5) |
| `m = 1` sweep | **For programme** (backing ↑) | Medium (×2–4 vs `m=0.25`) |
| No adding-up constraint | **For programme** (fiscal space ↑) | Large (unbounded) |
| `pay_t` = living wage | **Against programme** (backing ↓) | Medium (×0.7) |
| `y_K` cap at 0.32 | **Against programme** (ESP yield ↓) | Small–Medium (×0.8) |
| No price fall from automation | **Against programme** (real BU ↓) | Medium |
| No occupational mobility | **For programme** (offset ↑) | Medium |

**Net bias:** **Strongly for the programme** on the backing-produced measure (Q4) and displacement offset (Q1/Q5), because the upward biases are larger and compound (double-count + `G_t` + `own=1` + `m=1`), while downward biases are partial offsets. The three changes above would remove the largest upward biases.