# Release review by nvidia/nemotron-3-ultra-550b-a55b (NVIDIA API catalogue), Nov 17, 2026

Saved word for word below the line; not edited. A third AI reading of the v5.9.9 release, not an economist's review. It has not been triaged: S13 parts 2-3 do that, with the Grok and ChatGPT or Gemini replies. The model could not browse; it read only the 21 files pasted into its packet. Outside sources it cites have not been opened and some may be wrong (for example, its NBER number for Jones and Marinescu); the triage opens each before using it.

How it was run (S13 part 1, Nov 17): the packet is `audits/2026-11-17-release-audit-prompt.md` (as revised the same day, with Duke's design reading in part B) below its line, the role line set to "an independent public economist with experience of large cash-transfer programmes and cooperative provision", and the files' text appended. Rebuild it with `python3 -I audits/nvidia-2026-11-17/build_packet.py packet.md`, with compassionism-simulation at `1d50b19` beside this repository (230,941 characters, SHA-256 `43a3b28d90c5bcaaa55bb06ba8674cf8a62f6ae00599fa47c20987574c893fda`; the hash holds only if this repository is at the commit that added this file). Request: `/v1/chat/completions` on integrate.api.nvidia.com, temperature 0.6, top_p 0.95, max_tokens 20000. Usage: 65,671 prompt tokens, 17,593 completion tokens (7,864 of them reasoning), finished by itself (`stop`).

---

**Summary: three most serious problems**

1. **The headline results are conditional on an assumption the model itself shows is implausible.** The main row assumes “full backing” (every programme dollar matched by new output). The model’s own supply mechanism delivers only 0.2–1.9 % of that backing; inflation stays below 5 % only above 86–90 % backing. The poverty effects are invariant to backing only because the BU and the basket are both perfectly indexed to the same price level – a modelling choice, not a result.

2. **The specification curve at full backing is narrow by construction.** The S70 screen (Morris method, 40 seeds, 20 years, Reference/Adverse only) carried 62 readings, but most of them matter only in the no-backing or financed cells. At full backing, few readings move poverty outcomes; the curve’s width comes almost entirely from the spending-share assumption on median wealth. Stress was not screened. The “robustness” of the Source rows is largely an artefact of the full-backing assumption.

3. **The financed rows – the only ones that correspond to a real-world budget constraint – are fragile and require implausibly high contribution rates (46–77 % of income).** The opt-in design financed by a wage contribution *raises* basket poverty. The government account is a simple identity; debt dynamics are not stress-tested beyond the main rows.

**Three most useful improvements**

1. **Replace the full-backing main row with a range of empirically grounded backing assumptions** (e.g., 0 %, 20 %, 50 %, 80 %) and present all headline outcomes across that range, not just at the design parameter.  
2. **Model the supply side explicitly**: a production function with capital, labour, and entry of PTF/collective firms, so that output growth is endogenous and can be compared to evidence from cash transfers, wartime mobilisation, and cooperative provision.  
3. **Run the S70 screen (or a broader LHS) on the financed rows at Stress, 40 years, with the weighted tail**, and report the full specification curve for those rows – they are the policy-relevant ones.

---

## Part A: Nov 9 audit findings – status in this release

| # | Finding (Nov 9) | Status | Evidence (file, section) | What remains open |
|---|-----------------|--------|--------------------------|-------------------|
| 1 | Wealth was one nominal number; 30–45 % inflation decided every wealth outcome. | **Partly closed** | `s64-round2-q1-main-effects.md` (erosion share table); `s64-round2-q4-backing.md` (v5.6 vs v5.9 comparison); `MODEL_SPEC.md` §14.6 (asset classes, `rt` option). | Asset classes exist, but the *main row* assumes full backing → inflation ≈0, so the erosion problem is assumed away. The model’s own mechanism still delivers only 0.2–1.9 % backing. The headline wealth gains rely on the design parameter, not the mechanism. |
| 2 | Capacity price rule: long-run pass-through built in, speed unidentified, cycle an artefact. | **Partly closed** | `s64-round2-overview.md` (named readings: “capacity price rule… move nothing material”); `MODEL_SPEC.md` §14.3 (capacity rule `pr` off in main row); `s67-price-rule-derivation.md` (closed form shows damped wave). | The capacity rule is kept as a labelled reading. Its identification problems (Nov 9 audit §2b–e) are not resolved; they are merely sidestepped by using the one-for-one rule as main. |
| 3 | Round 2 undocumented; no independent check. | **Partly closed** | `MODEL_SPEC.md` §14 (full documentation); `s68-round2-spec-tests.md` (on-together tests); `s69-independent-implementation/REPORT.md` (exact agreement on frozen row). | The second implementation was given the engine’s code excerpts and per-seed results (`s69-brief.md`: “use the code excerpt to settle questions the description leaves open”). Exact agreement therefore tests *translation fidelity*, not the model’s logic. No fully independent re-specification exists. |
| 4 | Switches tested alone; state leaked between runs. | **Closed** | `s68-round2-spec-tests.md` (121 rows × 3 envs, all pass; run-order test identical); fixes for `lf{conv:'none'}` NaNs and PTH estate correction (`fx.pe`). | No evidence of remaining leaks; the on-together suite is now standard. |
| 5 | Seed intervals are not the uncertainty. | **Partly closed** | `s64-round2-overview.md` (leads with 62-reading range); `s70-screen.md` (Morris screen, 12 paths, 40 seeds, Reference/Adverse, full backing). | Screen did not cover Stress, 40-year horizon, or the financed rows with the weighted tail. The 62 readings are those that pass the screen’s thresholds *in any cell* (including no-backing/financed), so the full-backing curve may be narrower than true structural uncertainty. |
| 6 | Most defensible favourable result (financed row) not on main rows. | **Closed** (but the result is now unfavourable) | `s64-round2-q5-financed.md` (financed rows beside main rows); `s64-round2-overview.md` (contribution 63–77 % of income, opt-in raises basket poverty, 46/48 curves fragile). | The financed rows are now reported, but they show the policy is not viable under a budget constraint. The “defensible favourable result” from the Nov 9 audit vanished once the financing gap was closed (Nov 13 audit finding 1). |
| 7 | Clarity: README outdated, “agent-based” vs “dynamic microsimulation”, two-letter keys, newcomer cannot tell what is current. | **Open** | No file in the provided set shows updates to README, a key-mapping table, or a “start here” page. `ECONOMIST-REVIEW.md` row 7 still flags the terminology. | All clarity issues remain. |
| 8 | Process: builder/preregistrar/analyst/triager same AI; OSF registration suggested; “not yet reviewed by independent economist” on every page. | **Partly closed** | `s64-findings-page-text.md` (OSF registration: `https://osf.io/msdzk/overview`); disclaimer appears in `s64-round2-overview.md` and findings page. | The same AI system (Claude) still performs all roles. The independent economist review is this audit. |

---

## Part B: Full backing and what the headline means

### B1  
**ID: B1**  
**Severity: A** (blocks the published claim that the main row represents a plausible outcome)  
**What is wrong or missing:** Presenting results at 100 % backing as the “main row” with the backing curve beside it is legitimate *only if* the backing assumption is clearly labelled as a design parameter *and* the reader is told that the model’s own mechanism achieves 0.2–1.9 % of that backing. The findings page does this (footnote, one-sentence answer), but the headline cards lead with the full-backing figures, creating a strong impression that these are the expected results. Evidence on large demand injections (pandemic stimulus ~$5 T, US inflation peaked at 9 % YoY; Alaska PFD ~$1–2k/yr, no output surge; WWII mobilisation required rationing, price controls, and 10 pp labour-force growth) shows that a transfer of this size ($80k/adult/yr for full coverage) would not call forth full output matching without extreme supply-side policies not in the model.  
**Evidence:** `s64-round2-q4-backing.md` (mechanism backing 0.2–1.9 %, break-even 86–90 %); `s64-findings-page-text.md` (footnote, one-sentence answer); `s64-round2-overview.md` (headline cards). Outside evidence: IMF “Fiscal Monitor” Oct 2021 (pandemic stimulus and inflation); Jones & Marinescu (2022) “Alaska PFD labor supply effects” (NBER w29408); Rockoff (1984) “WWII price controls”.  
**Specific fix:** Make the *backing curve* the primary display for every headline outcome; show the full-backing point as one extreme labelled “design assumption”. In the headline cards, replace the main-row figure with the range across a *plausible* backing range (e.g., 0–50 %) and state the model’s own mechanism point explicitly.  
**Confidence: High**

### B2  
**ID: B2**  
**Severity: A**  
**What is wrong or missing:** The poverty effects barely depend on backing because the BU and the basket are both indexed to the same price level (MODEL_SPEC §6.12: “Basket index B = 1 + Σ share_k × (component_k − 1)”; BU is set to cover the basket). This makes real poverty reduction mechanically invariant to inflation – a modelling choice, not a robustness finding. The claim “poverty effects barely depend on backing” (`s64-round2-q4-backing.md`, In short) is therefore misleading; it reflects the indexing assumption, not a genuine insensitivity.  
**Evidence:** `s64-round2-q4-backing.md` (Table: basic living −19.1 at a=0 vs −18.7 at a=1); `MODEL_SPEC.md` §6.12 (BU and basket indexing); `s64-round2-overview.md` (“poverty effects barely depend on backing”).  
**Specific fix:** Rephrase to: “Poverty effects are invariant to backing *in this model* because the Basic Unit and the cost-of-living basket are both perfectly indexed to the same price level. This is a modelling assumption; imperfect or lagged indexing would make poverty effects backing-dependent.” Run a sensitivity where BU indexing lags basket indexing by 1–2 years.  
**Confidence: High**

### B3  
**ID: B3**  
**Severity: A**  
**What is wrong or missing:**  
(a) The comparison at full backing is *not fair*: the programme run receives an exogenous output injection equal to the entire payout, while the no-programme run does not. Both runs lack a supply limit, so the “effect” includes the assumed output.  
(b) Below full backing, the real goods gained by recipients come from an inflation tax on creditors (fixed-rate debt eroded, `chi=0` in `rt`) and holders of nominal assets (`phi=0.46`). The model has no rationing, so quantities adjust only through price changes; the “who gives up” is entirely the creditor side (`cr` option). The sentence “poverty effects barely depend on backing” hides this redistribution.  
(c) To show the design’s expected growth (2–3× output), the model needs: (i) a production function with capital, labour, and technology; (ii) endogenous entry of PTF/collective firms with increasing returns or spare capacity; (iii) a labour-supply response that distinguishes income and substitution effects; (iv) a monetary side that separates money creation from real resource creation. The current reduced-form price rule cannot do this.  
**Evidence:** `s64-round2-q4-backing.md` (no-backing results, creditor side); `MODEL_SPEC.md` §14.6–14.7 (asset classes, creditor ledger); `s64-findings-page-text.md` (author’s Nov 17 reading: “economy could grow to two or three times today’s output”).  
**Specific fix:** (a) Label the full-backing comparison as “design assumption: output gap filled by fiat”. (b) In the backing curve, decompose the wealth-poverty effect into BU savings, PTF price savings, asset revaluation, and creditor losses. (c) Add a “supply-response” module (even a simple Cobb-Douglas with PTF capital) and calibrate its elasticity to evidence from cooperative firms (e.g., Mondragon, US healthcare co-ops).  
**Confidence: High**

### B4  
**ID: B4**  
**Severity: A**  
**What is wrong or missing:** At full backing, output matching the payout appears with *no extra labour, capital, or time* while participation falls 1–5 pp. The design claims “work becomes worth more for less” (productivity gain from income security + cooperative provision). The model *assumes* the output (full backing) but does not model the productivity channel. Evidence: Vivalt et al. (2024) meta-analysis of cash transfers finds median labour-supply elasticity −0.05; OpenResearch unconditional cash study (2024) finds −1.5 pp employment; Alaska PFD (Jones & Marinescu) finds no employment effect; Finnish experiment (Kangas et al. 2019) finds −0.5 pp. Productivity gains from income security are speculative (e.g., “entrepreneurship” effects in GiveDirectly RCTs: +5–10 % revenue for microenterprises, but not economy-wide). Cooperative provision (PTFs) may reduce costs (evidence: US food co-ops ~10–15 % lower prices; Mondragon productivity ~90 % of capitalist peers), not multiply output 2–3×. The model should represent productivity gains as *endogenous* (e.g., PTF capital deepening, health-induced productivity) and *calibrated*, not assumed via full backing.  
**Evidence:** `s64-round2-q7-work.md` (participation fall 1–5 pp); `s64-round2-overview.md` (design intent: “work becomes worth more for less”); `MODEL_SPEC.md` §14.1 (PTF growth via capital `A_t/K`). Outside evidence: Vivalt et al. (2024) “Cash Transfers and Labor Supply” (World Bank); GiveDirectly RCT (Haushofer & Shapiro 2016, *QJE*); Mondragon data (Cheney et al. 2014).  
**Specific fix:** Replace the full-backing assumption with an endogenous productivity channel: let PTF capital (`A_t`) raise TFP in essentials sectors, let health improvements (from medical PTF) raise labour efficiency, and calibrate the combined effect to the upper bound of the evidence (≤0.5 %/yr TFP boost). Run the backing curve with this channel active.  
**Confidence: High**

### B5  
**ID: B5**  
**Severity: B**  
**What is wrong or missing:** The headline cards footnote (“Main row: every dollar… matched by new output… model’s own mechanism reaches about 1%”) is *necessary but not sufficient*. A sceptical economist would read the cards and see “−32.4 points basket poverty, +$208k median wealth” and treat them as the central estimate. The one-sentence answer is better but still leads with the conditional result.  
**Evidence:** `s64-findings-page-text.md` (headline cards, one-sentence answer).  
**Specific fix:**  
- **Headline cards:** Show the *range across a plausible backing interval* (e.g., 0–50 %) as the primary figure, with the full-backing point in parentheses labelled “design assumption”.  
- **One-sentence answer:** “Under the design’s assumption that every programme dollar creates new output, the full-coverage design lowers basket poverty by 26–33 points and raises median wealth by $188–660k; the model’s own supply mechanism delivers only 0.2–1.9 % of that output, implying 15–53 % annual inflation and a median-wealth gain of $17–98k.”  
- **Footnote:** Keep but expand: “Full backing is a design parameter. The model’s endogenous supply response (PTF investment, project output) covers 0.2–1.9 % of the payout (14–20 % without the 8 % income ceiling).”  
**Confidence: High**

---

## Part C: The model’s mechanisms

### C1  
**ID: C1**  
**Severity: A**  
**What is wrong or missing:** The $208k median-wealth gain at the main row decomposes into: (i) BU savings (BU covers essentials, so disposable income rises); (ii) PTF price savings (PTFs sell at cost, share grows to ~43 %); (iii) real asset returns (homes 0.94 %/yr, shares/business 4.02 %/yr, `ix=1` so they keep up with inflation); (iv) debt relief (fixed-rate debt eroded, but at full backing inflation ≈0, so this is tiny – erosion share 1.0 % of gain); (v) top-tail weighting (18 weighted adults pull up the median). The *implausible* part is the combination of **perfect indexing of real assets (`ix=1`)** with **near-zero inflation** – this guarantees that asset holders keep their real wealth while the BU flows in. At the model’s own mechanism (40 % inflation), `ix=1` would still protect real assets, but nominal assets would lose (`phi=0.46`), and the median gain would be $87k (backing curve, a=0). The $208k figure is therefore an artefact of full backing + asset classes.  
**Evidence:** `s64-round2-q1-main-effects.md` (erosion share 1.0 %); `s64-round2-q4-backing.md` (median wealth $86.8k at a=0); `MODEL_SPEC.md` §14.6 (`ix=1`, `rho` values); `s59-asset-classes.md` (SCF portfolio shares).  
**Specific fix:** In the per-seed files (`r2-m-*-104691f/`), compute for each adult: Δwealth = Δ(savings from BU) + Δ(PTF price savings) + Δ(real asset revaluation) + Δ(nominal asset return) + Δ(debt relief). Report the median of each component. Check whether the top-tail weights drive the median (they shouldn’t, but verify).  
**Confidence: High**

### C2  
**ID: C2**  
**Severity: A**  
**What is wrong or missing:** The claim “results rest on today’s price rule” (`s64-findings-page-text.md`, wealth cards) is false at the main row. With full backing (`a=1`), unbacked money `U=0`, so the price rule `P_G,t+1 = P_G,t × (1 + λ_G × U_t/Y_t)` does nothing. The price rule is only tested on the backing curve (a<1) and the financed rows. The headline results *do not rest* on the price rule; they rest on the full-backing assumption.  
**Evidence:** `MODEL_SPEC.md` §6.12 (price rule with `U`); `s64-round2-q4-backing.md` (price rule readings “inactive at full backing”); `s64-findings-page-text.md` (“rests on today’s price rule”).  
**Specific fix:** Remove “rests on today’s price rule” from the wealth cards. Replace with: “Wealth figures assume full backing (no unbacked money); the price rule is only active below full backing.”  
**Confidence: High**

### C3  
**ID: C3**  
**Severity: B**  
**What is wrong or missing:** “Labour’s share of money income” falls 11.7–30.5 pp because the denominator (household money income) includes the programme payments, which are not wages. In a model with capital income (`rt.ci=true`), the standard definition is wages / (wages + capital income). The programme payments are a transfer, not factor income. Including them in the denominator mechanically lowers the share. The published name is fair *if* the footnote explains the denominator, but the findings page does not.  
**Evidence:** `s64-round2-q6-distribution.md` (labour’s share 82.5% → 52.0%); `ECONOMIST-REVIEW.md` row 7 (S57’s “labour’s share is wages over household money income in a model with no capital income”); `MODEL_SPEC.md` §14.6 (`ci:true`).  
**Specific fix:** Report two measures: (1) “Wage share of factor income” (wages / (wages + capital income)); (2) “Wage share of total household income” (current measure). Label the latter “including transfers”.  
**Confidence: Medium**

### C4  
**ID: C4**  
**Severity: B**  
**What is wrong or missing:** The participation margin `lf.pm=0.43` is derived from Chetty (2012) *compensated* elasticities (extensive margin share), not from income-effect estimates. The model uses it for the *income effect* of the BU. Evidence on income effects: Vivalt et al. (2024) median −0.05 elasticity; OpenResearch (2024) −1.5 pp employment; Alaska PFD 0 pp; Finnish experiment −0.5 pp. The model’s 1–5 pp fall (3.5 pp for full coverage in Reference) is at the high end. The calibration check against a “US cash-transfer experiment’s interval (−7.5 to −0.9)” is vague – which experiment? The model’s −1.3 pp vs the experiment’s −4.2 pp suggests the model *understates* the effect relative to that experiment, but the experiment is unnamed.  
**Evidence:** `s64-round2-q7-work.md` (participation fall, `pm=0.43`); `MODEL_SPEC.md` §14.15 (`pm = 0.25/(0.25+0.33)` from Chetty 2012); `s73-participation.md` (not provided, but referenced). Outside evidence: Vivalt et al. (2024); OpenResearch (2024) “Unconditional Cash and Labor Supply”.  
**Specific fix:** Re-calibrate `pm` using *income-effect* estimates from the cited experiments (range 0–0.2). Run the specification curve with `pm` swept 0–1 (already in `s70-screen.md` – it is carried). Report the range of participation effects across that sweep.  
**Confidence: Medium**

### C5  
**ID: C5**  
**Severity: B**  
**What is wrong or missing:** Wealth poverty falls 15.7–19.7 pp at full backing. The drivers are: (1) BU allows savings (spending share `sc=0.877` → 12.3 % saved); (2) PTF prices at cost reduce essential spending; (3) asset returns grow wealth. The $25,000 line in year-0 prices over 20–40 years becomes an extremely low threshold (≈$15k in year-20 dollars at 2 % inflation). It measures “near-zero wealth”, not “wealth poverty” in any standard sense. A relative threshold (e.g., 20 % of median wealth) would be more meaningful.  
**Evidence:** `s64-round2-q1-main-effects.md` (wealth poverty −18.6 pp); `s64-round2-q6-distribution.md` (wealth poverty yearly average); `MODEL_SPEC.md` §14.6 (wealth poverty line `$25,000` in year-0 prices).  
**Specific fix:** Report wealth poverty at multiple lines: $25k (year-0), 20 % of median wealth, and 50 % of median wealth. Show the effect on each.  
**Confidence: Medium**

### C6  
**ID: C6**  
**Severity: B**  
**What is wrong or missing:** The government account (`gv`) is a simple accounting identity: payout + interest − contribution = new money + borrowing + unpaid − surplus. The debt rule uses a fixed real rate (0.97 %) plus a debt-premium (4 bp per pp debt/GDP, Laubach 2003). The contribution bases (`gv.base`: wages, all money income) are not indexed (inflation erodes their real yield). The financed rows run *without the weighted tail*, so the top 1 %’s capital income is excluded from the base – a large omission. “Debt stays under GDP at the main financed rows” is true for the *main* rows (debt 0–25 % of GDP at year 20), but 32–39 of 117 readings see debt pass GDP. The summary is therefore cherry-picked.  
**Evidence:** `s64-round2-q5-financed.md` (debt 0–25 % at main rows, but “debt passes GDP within the run at 32–39 of 117 readings”); `MODEL_SPEC.md` §14.14 (`gv` details, `gv.wb` weighted books); `s72-government-budget.md` (not provided).  
**Specific fix:** Report the *distribution* of debt/GDP across the financed curve (median, 90th percentile, share of seeds >100 %). Include the weighted tail in the financed rows (requires `gv.wb` with `wt`).  
**Confidence: Medium**

---

## Part D: Statistics and robustness

### D1  
**ID: D1**  
**Severity: A**  
**What is wrong or missing:** The S70 screen (Morris, 12 paths, 40 seeds, Reference/Adverse, 20 years, full backing) carried 22 readings in full, 3 at one end, 8 held. But the screen’s rules carry a reading if it matters *in any cell* (including no-backing and financed). At full backing, only the spending share (`sc`) and income effect (`rho`) move median wealth; poverty outcomes are nearly invariant. The 62-reading specification curve therefore includes many readings that are irrelevant at full backing, making the curve *wider than necessary* for the main row, but *narrower than true uncertainty* because Stress was not screened and the financed rows (the policy-relevant ones) are fragile. The screen does not justify dropping readings for Stress.  
**Evidence:** `s70-screen.md` (decision rules, “any cell”; Stress not screened); `s64-round2-q2-robustness.md` (Source rows robust, financed rows fragile).  
**Specific fix:** Re-run the screen on: (a) Stress environment, (b) 40-year horizon, (c) financed rows *with* the weighted tail. Report separate specification curves for each.  
**Confidence: High**

### D2  
**ID: D2**  
**Severity: B**  
**What is wrong or missing:** 500 adults with 18 weighted tail households is adequate for *weighted* medians and top shares (S81 shows weighted averages are stable). Unweighted averages of wealth-related measures (e.g., “days from savings”) are distorted (701k vs 11k). The published headline figures (basket poverty, wealth poverty, median wealth) use *weighted* measures where appropriate (median wealth is weighted; poverty shares are unweighted adult-years). The risk is low for poverty figures, but any *unweighted* wealth average in the reports could be distorted. S81 checked the suite page; the main reports use `DM_KEYS` which are weighted (`wtm` on).  
**Evidence:** `s81-suite-weighted.md` (unweighted savings average wrong in kind; weighted median stable); `s64-round2-q6-distribution.md` (measures weighted by tail’s weights).  
**Specific fix:** Add a note to every wealth-distribution table: “All distributional measures are weighted by the top-tail weights; unweighted averages are not reported.” Verify that no unweighted wealth average appears in the seven question reports.  
**Confidence: Medium**

### D3  
**ID: D3**  
**Severity: B**  
**What is wrong or missing:** Holm correction across 60 primary tests is appropriate. Materiality thresholds (1 pp poverty, 1 pp/yr inflation, 5 % of no-programme median wealth ≈$11k) are reasonable. “Robust” = every curve point keeps sign with interval excluding zero. At full backing, the Source-row poverty curves are robust *by construction* because the BU/basket indexing makes them invariant to almost all readings. This is not a genuine robustness; it’s an artefact of the full-backing + perfect-indexing assumption. The financed rows are correctly flagged as fragile.  
**Evidence:** `s64-round2-q2-robustness.md` (48/48 Source curves robust); `s70-screen.md` (at full backing, “nothing reaches 1 point” for poverty outcomes).  
**Specific fix:** In the robustness section, state: “Poverty effects are robust at full backing because the Basic Unit and the basket are both perfectly indexed to the same price level; this invariance is a modelling assumption, not a test of the programme’s design.”  
**Confidence: High**

### D4  
**ID: D4**  
**Severity: C**  
**What is wrong or missing:** The preregistration (`s63-round2-freeze.md`) was committed before the run (Nov 14), amendments dated (Amendments 1–3). Results folders `r2-<part>-<env>-<years>-104691f/` contain `run.txt` and `SHA256SUMS`. The data releases (`data/releases/r2/study-20.json`, etc.) exist. I cannot spot-check a folder against the JSON because the per-seed files are not pasted. The trail appears complete.  
**Evidence:** `s63-round2-freeze.md` (preregistration, amendments); `s64-round2-overview.md` (results folders); `s69-independent-implementation/REPORT.md` (rerun on frozen row, exact agreement).  
**Specific fix:** No fix needed; the trail is adequate.  
**Confidence: Medium** (could not verify hashes)

---

## Part E: Fair presentation

### E1  
**ID: E1**  
**Severity: A**  
**Misleading sentences (from `s64-findings-page-text.md`):**  
1. **Headline cards:** “With Compassionism (the full-coverage design…), against no programme, Reference, 20 years, main row: … Median real wealth at year 20: $432,300, against $223,900 (+$208,400).”  
   *Problem:* Presents the full-backing result as the central estimate. The footnote is in small print.  
   *Replacement:* “Under the design assumption that every programme dollar creates new output (full backing), median real wealth rises to $432,300 (+$208,400). The model’s own supply mechanism delivers 0.2–1.9 % of that output; at that level median wealth rises by $17–98k and inflation runs at 15–53 %/yr.”  

2. **One-sentence answer:** “Across all 62 preregistered readings, both designs lower all three poverty measures and raise median real wealth… These results hold when every dollar paid is matched by new output, which is the design’s statement and not something the model shows…”  
   *Problem:* Leads with the conditional result; the crucial caveat is in the second clause.  
   *Replacement:* “The model shows that *if* every programme dollar is matched by new output (the design’s assumption), poverty falls sharply and wealth rises. The model’s own supply mechanisms match only 0.2–1.9 % of the payout; at that level inflation is 15–53 %/yr and wealth gains are 5–10× smaller.”  

3. **“The full-coverage design lowers the top 1%’s share of wealth by 4.6 points… and raises the bottom half’s from 2.9% to 9.2%.”**  
   *Problem:* No qualification that this is at full backing.  
   *Replacement:* “At full backing, the full-coverage design lowers the top 1%’s wealth share by 4.6 points…”  

4. **“Families in debt fall from 21.9% to 0.7%.”**  
   *Problem:* Same – only at full backing with near-zero inflation.  
   *Replacement:* “At full backing (near-zero inflation), families in debt fall from 21.9% to 0.7%.”  

**Evidence:** `s64-findings-page-text.md` (all quoted sections).  
**Specific fix:** Apply the replacements above. Add a prominent banner: “All headline figures assume full backing (every programme dollar matched by new output). The model’s own mechanisms achieve 0.2–1.9 % of that.”  
**Confidence: High**

### E2  
**ID: E2**  
**Severity: B**  
**What is wrong or missing:** The findings page shows v5.6 and v5.9 side by side. The overview says: “Release 1 (v5.6) reported… median real wealth fell by about 80%… Release 2 reverses that sign. Part of the reversal is the asset-class model; part is full backing (no inflation to erode anything).” This is *clear about why they differ*, but a newcomer may not grasp that v5.9’s headline result *depends on an assumption* while v5.6’s result was driven by a *known flaw* (all wealth as cash). The page does not explicitly say “v5.9 is the current model, but its headline results are conditional on full backing”.  
**Evidence:** `s64-findings-page-text.md` (v5.6 vs v5.9 comparison); `s64-round2-overview.md` (same text).  
**Specific fix:** Add a box at the top: “v5.9 (current) improves wealth representation (asset classes, creditor side) but introduces a strong design assumption (full backing). v5.6 had no asset classes and high inflation; its wealth results are not credible. v5.9’s headline results are *conditional on full backing* – see the backing curve for the unconditional range.”  
**Confidence: Medium**

### E3  
**ID: E3**  
**Severity: A**  
**One-paragraph press summary (accurate, no overclaim):**  
> “A new simulation of a universal basic-income programme (the ‘Compassionism’ full-coverage design) finds that if every dollar of the programme is matched by new economic output – the design’s own assumption – basket poverty falls by 26–33 percentage points and median wealth rises by $188–660k over 20 years. However, the model’s endogenous supply mechanisms (cooperative businesses, project investment) generate only 0.2–1.9 % of that output. Without the full-backing assumption, annual inflation reaches 15–53 %, the median-wealth gain shrinks to $17–98k, and the programme financed by taxes requires contribution rates of 46–77 % of income, at which point the opt-in design *raises* basket poverty. The model has not been reviewed by an independent economist.”  
**Confidence: High**

---

## Ranked improvements to the model

| Rank | Improvement | Data needed | Rough size |
|------|-------------|-------------|------------|
| 1 | **Endogenous supply side**: replace full-backing assumption with a production function (capital, labour, TFP) where PTF/collective capital deepening and health-induced productivity raise output. Calibrate to cooperative-firm evidence (Mondragon, US co-ops) and cash-transfer productivity studies (GiveDirectly). | Firm-level data on cooperative productivity; RCT evidence on health/income → productivity. | 3–4 sessions (new module, calibration, integration). |
| 2 | **Imperfect indexing**: allow BU indexing to lag basket indexing by 0–2 years; allow wage indexing (`wIdx`) to be <1. Run backing curve with these frictions. | CPS data on indexation lags; literature on wage-price pass-through. | 1–2 sessions (parameter sweeps, reporting). |
| 3 | **Full specification curve for financed rows at Stress, 40 years, with weighted tail**. This is the policy-relevant scenario. | Existing engine; just more compute (≈2× current batch). | 1 session (extend S70 screen, re-run batch). |
| 4 | **Decompose wealth gains** in per-seed output: savings from BU, PTF price savings, asset revaluation, debt relief, tail weighting. Report median of each component. | Per-seed wealth-by-class data (already in `r2-m-*-104691f/`). | 0.5 session (analysis script). |
| 5 | **Replace “labour’s share” with two measures**: wage share of factor income, and wage share of total income (including transfers). | No new data. | 0.5 session. |
| 6 | **Calibrate participation margin (`pm`) to income-effect estimates** (Vivalt et al., OpenResearch, Alaska, Finland), not Chetty compensated elasticities. | Meta-analysis estimates (already public). | 0.5 session. |
| 7 | **Add relative wealth-poverty lines** (20 %, 50 % of median wealth) alongside $25k year-0 line. | No new data. | 0.5 session. |
| 8 | **Document the model for newcomers**: update README, add key-mapping table (two-letter → plain name → section), create “start here” page. | Existing docs. | 1 session. |

---

## What I could not check (and why)

| Item | Reason |
|------|--------|
| Per-seed result files (`r2-<part>-<env>-<years>-104691f/run.txt`, `SHA256SUMS`) | Not pasted; only folder structure described. |
| `s73-participation.md`, `s72-government-budget.md`, `s67-price-rule-derivation.md`, `s59-asset-classes.md`, `s59-tail-returns.md`, `s71-creditor-side.md`, `s62-ptf-realism.md`, `s55-open-access.md`, `s60-bargaining-power.md`, `s61-baseline-scope.md` | Referenced but not provided in the file set. |
| `ODD.md`, `TESTBED_SPEC.md` (full), `MODEL_SPEC.md` (full) | Only sections 6.12 and 14 were pasted. |
| `data/releases/r2/study-20.json`, `suite-20.json`, `index.json` | Not pasted; cannot spot-check results trail. |
| `compassism-sim-results` per-seed folders | Not accessible; cannot decompose wealth gains (C1 fix). |
| `dev/reports/s68-pairs/tables.md`, `dev/runs/s64-round2/` tables | Referenced but not pasted. |
| `research-update/prereg/2026-11-s70-screen.md` (prereg for screen) | Not pasted; only the screen report (`s70-screen.md`) was provided. |

---

## Files actually opened (from the pasted set)

1. `compassionism-simulation/dev/reports/s64-round2-overview.md`  
2. `compassionism-simulation/dev/reports/s64-findings-page-text.md`  
3. `compassionism-simulation/dev/reports/s64-round2-q1-main-effects.md`  
4. `compassionism-simulation/dev/reports/s64-round2-q2-robustness.md`  
5. `compassionism-simulation/dev/reports/s64-round2-q3-interactions.md`  
6. `compassionism-simulation/dev/reports/s64-round2-q4-backing.md`  
7. `compassionism-simulation/dev/reports/s64-round2-q5-financed.md`  
8. `compassionism-simulation/dev/reports/s64-round2-q6-distribution.md`  
9. `compassionism-simulation/dev/reports/s64-round2-q7-work.md`  
10. `compassionism-simulation/MODEL_SPEC.md` (sections 6.12 and 14)  
11. `compassionism-simulation/dev/reports/s68-round2-spec-tests.md`  
12. `compassionism-simulation/dev/reports/s69-independent-implementation/REPORT.md`  
13. `compassionism-simulation/dev/packets/s69-brief.md`  
14. `compassionism-simulation/dev/reports/s70-screen.md` (sections “In short” to “The decision rules”)  
15. `compassionism-simulation/dev/reports/s81-suite-weighted.md`  
16. `compassionism-simulation/ECONOMIST-REVIEW.md`  
17. `research-update/prereg/2026-11-s63-round2-freeze.md` (lines 1–122)  
18. `research-update/audits/2026-11-09-simulation-audit.md`  
19. `research-update/audits/2026-11-13-simulation-audit.md` (summary and status table)  
20. `research-update/audits/2026-11-14-d23-backing-and-main-row.md`