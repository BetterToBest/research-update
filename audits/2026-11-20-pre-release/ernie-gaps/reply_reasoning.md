Let me work through this carefully. I'm asked to be an independent reviewer of an agent-based economic simulation and its findings page. I need to answer four numbered questions, be concrete and short, not praise, plain text.

Let me understand the materials:

1. **The release step (PLAN.md, S93)**: Makes the private price at sale the default. Steps:
   - `sp.vAt: 'sale'` becomes default at that version
   - Regenerate main rows' findings-page data from `s90-sale-*-b8ccd8d`, replace dated notes with figures
   - Hub corrections-log entry; root-site indexes
   - Late-price figures stay as v5.9 record (OSF)
   - Then a preregistered amendment deciding which reached studies are rerun on release engine

2. **The findings-page text**: The v5.9 release text. Key claims:
   - Headline cards: poverty measures, wealth, all with full backing
   - Full backing is a design parameter, not a model estimate
   - Model's own mechanism reaches ~1% of payout
   - 62 preregistered readings
   - Prices: 0.0-0.2 points above no programme at main row (with full backing)
   - Model's own mechanism: 0.2-1.9% of payout (14-20% if ceiling removed)
   - Inflation under 5% only above 86-90% backing
   - Financed rows: contribution-based, fragile
   - Who gains
   - Unfavourable results
   - What no figure covers
   - Basis class

3. **The automation study limits (s85, section 13)**: 
   - Full backing assumed, not produced
   - Produced backing 6-17% at 20 years
   - Prices rise 48-69% a year
   - Various limits

4. **The supply study limits (s82, section 11)**:
   - Poverty effects barely depend on backing
   - But depends on wage/BU catch-up
   - BU's two-year cycle from the late private price bug (now fixed behind option)
   - Various limits

5. **The inventory of open gaps (audits/2026-11-20-release-gaps.md)**:
   - A. What the headline rests on (items 1-3)
   - B. Engine and model gaps (items 4-15)
   - C. The Hub and its figures (items 16-21)
   - D. Process before a release (item 22)

Now let me answer the four questions.

**Question 1: Rank the inventory's items by how much each could change a headline claim or mislead a reader. For top ten, say fix in model / fix in text / state as limit, and how to verify.**

Let me think about which items could most change a headline claim or mislead a reader.

The headline claims are:
- Poverty reductions (0.9%, 3.7%, 6.0% vs baselines)
- Median wealth +$208,400
- All rest on full backing (design parameter)
- Model's own mechanism ~1%

Let me rank the inventory items:

**Item 1 (Full backing assumed in main row)**: This is THE biggest. Every headline rests on it. The model's own mechanism reaches ~1%, automation study says 6-17%. This directly affects how every headline reads. The findings page already carries a footnote and section. But the open decision is on the headline cards' headings. This is the top item. Fix: text (the headline cards should carry the full-backing condition prominently, not just a footnote). Actually the question is whether the headline cards' headings should state full backing. This could mislead if a reader sees "0.9% poverty" without knowing it rests on assumed full backing. Fix in text primarily. Verify: check that every headline card and the one-sentence answer states the full-backing condition inline, not just in a footnote.

**Item 2 (No limit on total supply below full backing)**: The dated note covers this. Below full backing only. The findings page has a Nov 17 note. This is important because it means the poverty results below full backing aren't evidence the design works. But it's below full backing only, and the main row is full backing. Still, the one-sentence answer says "with the model's own backing mechanism, prices rise 15 to 53 points a year" — and the poverty effects "barely depend on backing" which is misleading without the supply caveat. Fix: text (keep the dated note, ensure it's prominent). Actually the supply study (s82) shows poverty effects DO depend on backing when wages don't keep up. So there's tension. Let me note this.

**Item 3 (Opt-in does far less)**: Published, but release text should keep it beside full-coverage headline. This could mislead if full-coverage headline is shown without opt-in comparison. Fix: text. Verify: check opt-in figure appears beside every full-coverage headline.

**Item 5 (Late private price / BU two-year swing)**: This is the release's core change. The BU's relief runs a damped two-year cycle in EVERY programme row, main row included (supply study limit 5). This is a defect being fixed. The main rows were rerun. This affects the cost-of-living / basic-living figures potentially. This is high because it's a known defect affecting the main row that the release fixes. But wait — the release regenerates the main rows' data. So the question is whether the regenerated figures change. This is being fixed in the model (the release). Verify: compare regenerated main-row figures against v5.9; the BU cycle should be gone.

Actually, let me reconsider. The item says "fixed behind an option, and the main rows were rerun. The release makes it the default." So the fix is happening. The gap is item 5 of the release step (which studies to rerun) not preregistered. So this is more of a process gap. But the underlying defect (BU two-year cycle in main row) is a headline-affecting issue that's being fixed.

**Item 6 (Simulation page uses Hub's early figures as targets: TARGET_WEALTH 82000, etc.)**: Visible to readers. The "Target $82K" label. This could mislead readers about what the model targets/validates against. But it's on the interactive simulation page, not the findings page. Research rule 3. Visible to readers. Fix: model/config (update the targets or remove the label). Verify: grep for the four occurrences, confirm updated.

**Item 16 (Audit-flagged figures still live on Hub)**: $847B net savings, "65% lower inflation", "15 pp" (it's 13), 85%/98% poverty reduction, $82,000 median wealth with 95% interval, "10,000 iterations", elasticity −0.71 (it's −1.6), steady state 11.8%, "14% of GDP" (about 11%), Bristol Pound "£5 billion", 2.86 multiplier (it's 1.95). These are WRONG figures live on the Hub. This is very misleading — these are numerical errors that contradict the current findings. This is high priority for misleading readers. Fix: text (Hub corrections). Verify: check each figure against current results.

Hmm, but these are on the Hub, not the findings page. The question is about "change a headline claim or mislead a reader." These Hub figures directly mislead readers with wrong numbers. Very high.

**Item 7 (Written description doesn't describe validation presets; "Gini" is mislabeled)**: The validation presets' "Gini" is of wealth less one year of cost of living times annual wage, not a wealth Gini. This is a methodological mislabeling. Could mislead about validation. Medium.

**Item 9 (Tax credits: no child/dependent care credit; EITC reach low 11.9% vs 15.3%)**: This affects the poverty/redistribution results. EITC reach low because no part-time work. This could affect headline poverty figures. Medium-high. Fix: model (add part-time work) or state as limit.

**Item 12 (No private firms, banks, bond market; central-bank rule reduced form, no channel to essentials price; no expectations channel)**: This is a big structural limitation. Affects inflation and price results. The findings page mentions "no central bank" in "What no figure covers." State as limit mostly. But the inflation figures are central to the backing discussion. Medium.

**Item 10 (Who is simulated: working-age adults and families; Hub should say so)**: Scope. Could mislead about generalizability. The findings page mentions "500 adults" and "fixed population." State as limit / text. Medium.

**Item 13 (Capital income not in price rule's income; automation dividend raises no investment)**: Affects wealth and price results. State as limit. Medium.

**Item 17 (168 cited external figures not opened)**: Sourcing. Could mislead if citations are wrong. But these are external claims, not the model's own results. Medium-low for headline, but relevant for credibility.

**Item 18 (θ Monte Carlo calibration: no record it was run)**: If the findings claim calibration that didn't happen, that's a false basis claim. Medium. Need to check if findings page claims calibration. The findings page doesn't seem to claim θ calibration explicitly. But "the widest part of the range comes from how much of their spare cash adults spend" — that's a parameter. Hmm.

**Item 19 (BLEI page may state poverty line inverted)**: Could mislead. Status to confirm. Medium.

**Item 20 (Release data lacks series BLEI visuals and Five Measures chart need)**: The release regenerates data. If the regenerated data lacks series needed for charts, the charts break or mislead. This is directly relevant to the release. Medium-high for the release specifically.

**Item 21 (Hub's 32-item site audit: Gini comparability, terminology, sourcing, AI-authorship, transparency)**: Broad. Medium.

**Item 4 (Creative Collectives' lending to start-ups)**: Preregistered, build to follow. This is future work, not a current gap in the release. It's about producing backing. Low for this release (it's a known missing feature, stated as future). State as limit.

**Item 8 (MODEL_SPEC gaps and contradictions)**: Documentation. Four contradictions, ~30 gaps. Could mislead about model specification. Medium-low for headline.

**Item 11 (Capacity of community businesses for whole population, not by zone/sector; one utility share)**: Structural. State as limit. Low-medium.

**Item 14 (Displaced adults' outcomes by fifth of starting wealth not stored)**: Data gap. Affects distributional analysis of automation. Low-medium.

**Item 15 (Health, security, output per hour: no source)**: Left out of automation study. State as limit. Low.

**Item 22 (Outside readings not done for release's regenerated figures)**: Process. The automation study had two readers; the release's regenerated figures haven't. This is a process gap directly relevant to the release. Medium-high for the release.

Now let me pick the top ten and rank them.

Ranking by "could change a headline claim or mislead a reader":

1. **Item 1 (Full backing assumed)** — Every headline rests on it. Model produces ~1%, automation 6-17%. Top. Fix: text (headline cards must state full-backing condition inline). Verify: every headline card + one-sentence answer states it; cross-check produced-backing figures.

2. **Item 16 (Wrong figures live on Hub)** — Directly wrong numbers ($847B, 65%, 15pp vs 13, 85/98%, $82K with 95% CI, 10,000 iterations, −0.71 vs −1.6, 11.8%, 14% vs 11%, £5B, 2.86 vs 1.95). Misleads readers with contradictions. Fix: text (Hub corrections package). Verify: each figure checked against current results; corrections-log entry.

3. **Item 5 (Late private price / BU two-year cycle)** — Known defect in EVERY programme row including main row; the release fixes it and regenerates. Affects basic-living/cost-of-living headline figures. Fix: model (the release does this). Verify: BU cycle gone in regenerated main rows; compare v5.9 vs release figures; document delta.

4. **Item 2 (No supply limit below full backing)** — Poverty "barely depends on backing" is misleading; supply study shows it depends on wage/BU catch-up. Fix: text (dated note prominent; reconcile with s82). Verify: note present and reconciled with s82 break-even shares.

5. **Item 3 (Opt-in does far less)** — Full-coverage headline without opt-in beside it misleads. Fix: text. Verify: opt-in figure beside every full-coverage headline.

6. **Item 6 (Hub target figures: $82K etc.)** — Visible to readers, mislabels what model targets. Fix: model/config (update targets/label). Verify: grep four occurrences, confirm.

7. **Item 20 (Release data lacks series for BLEI/Five Measures charts)** — Release-specific; charts break or mislead. Fix: model/data (add series before release). Verify: charts render from release data.

8. **Item 9 (Tax credits / EITC reach low, no part-time work)** — Affects redistribution/poverty headline. Fix: model (part-time work) or state as limit. Verify: EITC reach vs target; poverty with/without.

9. **Item 22 (No outside reading of regenerated figures)** — Release-specific process gap. Fix: process (get readers). Verify: two readers sign off on regenerated figures.

10. **Item 7 (Validation preset "Gini" mislabeled)** — Misleads about validation. Fix: text (describe presets; relabel). Verify: MODEL_SPEC/ODD describe presets; label corrected.

Alternatively item 12 (no central bank, no expectations) could be top ten. And item 10 (who is simulated). Let me reconsider.

Actually, let me reconsider the ranking. The question asks to rank by "how much each could change a headline claim or mislead a reader."

Headline claims are the poverty/wealth/inflation figures. What could change them or mislead?

- Item 1: full backing — YES, biggest, affects interpretation of every headline.
- Item 5: BU cycle defect — changes the actual numbers (basic living, cost of living). Being fixed.
- Item 16: wrong Hub figures — misleads directly with wrong numbers.
- Item 2: supply limit — misleads about below-full-backing poverty.
- Item 3: opt-in — misleads by omission.
- Item 9: tax credits/EITC — could change poverty numbers.
- Item 6: Hub targets — misleads about validation.
- Item 20: release data series — release-specific.
- Item 22: outside reading — process.
- Item 7: Gini mislabel — validation.
- Item 12: no central bank/expectations — affects inflation interpretation.
- Item 10: who is simulated — scope/generalizability.

I think my top ten is reasonable. Let me also consider item 13 (capital income not in price rule) — affects wealth/inflation. And item 18 (θ calibration not run) — if findings imply calibration.

Let me finalize top ten:
1. Item 1
2. Item 16
3. Item 5
4. Item 2
5. Item 3
6. Item 6
7. Item 9
8. Item 20
9. Item 22
10. Item 7

Actually, I want to reconsider whether item 12 should be in over item 7 or item 22. Item 12 (no central bank, no expectations channel, reduced-form central bank rule with no channel to essentials price) is significant for the inflation claims, which are central to the backing discussion. The findings page says "no central bank" in "What no figure covers" — so it's partly stated. But the inflation figures (15-53 points, 48-69 points) are presented as if meaningful, when the automation study itself says "the inflation figures measure the size of the unbacked money, not a forecast of prices." So there's a risk of misleading on inflation. Item 12 supports this. But it's partly covered.

I'll keep my top ten but maybe mention item 12 as close. Actually, let me be disciplined and pick ten. I'll go with the ten above but I could swap item 7 for item 12. Let me think about which misleads more.

Item 7: The validation preset "Gini" is mislabeled — it's not a wealth Gini. This affects validation claims. If the findings or Hub claim the model matches a wealth Gini, that's misleading. But the findings page doesn't seem to make that claim prominently. It's more of a documentation issue.

Item 12: No central bank, no expectations, reduced-form rule with no channel to essentials prices. This affects the inflation figures which ARE in the findings (15-53 points, backing thresholds). The automation study explicitly warns these aren't forecasts. If the findings page presents inflation figures without that warning... let me check. The findings page says "programme inflation is 0.0 to 0.2 points a year above no programme" at main row, and "runs at 15 to 53 points a year at the mechanism's own point." It doesn't carry the "not a forecast of prices" warning prominently. So item 12 could mislead on inflation. I'll include item 12 over item 7.

Revised top ten:
1. Item 1
2. Item 16
3. Item 5
4. Item 2
5. Item 3
6. Item 6
7. Item 9
8. Item 20
9. Item 12
10. Item 22

Hmm, but item 22 (outside reading) is a process gap, not a "change a headline or mislead" item per se. It's about verification. But it's release-relevant. Let me keep it but rank it lower. Actually the question says "rank by how much each could change a headline claim or mislead a reader." Item 22 doesn't itself change or mislead — it's a safeguard. So maybe it shouldn't be in the top ten by that criterion. Let me reconsider.

By the strict criterion (change a headline or mislead), the process items (22) and documentation items (8, 21) rank lower. Let me re-rank purely by mislead/change potential:

1. Item 1 (full backing) — changes interpretation of every headline.
2. Item 16 (wrong Hub figures) — directly misleads with wrong numbers.
3. Item 5 (BU cycle defect) — changes actual headline numbers.
4. Item 2 (no supply limit) — misleads on below-backing poverty.
5. Item 3 (opt-in omission) — misleads by omission.
6. Item 9 (tax credits/EITC) — could change poverty numbers.
7. Item 6 (Hub targets $82K) — misleads on validation/targets.
8. Item 12 (no central bank/expectations) — misleads on inflation.
9. Item 20 (release data series) — release-specific, charts.
10. Item 7 (Gini mislabel) — misleads on validation.

That's a defensible top ten. Item 22, 10, 13, 17, 18 just miss.

Actually, let me reconsider item 10 (who is simulated). The findings page headline says "0.9% of adult-years" etc. If readers think this is the whole population including children and elderly, that's misleading. The findings page does say "500 adults" and "fixed population (no ageing, births or deaths)" and "Adults outside the labour force... stay far more often below the cost of living." So it partly covers scope. But "who is simulated: working-age adults and their families; the Hub should say so" — the Hub should state this. Medium. I'll leave it just outside top ten.

Let me also reconsider: is item 5 really #3? The BU two-year cycle is a defect in the main row. The release fixes it. So the CURRENT v5.9 figures (which the findings page describes) have this defect. The release regenerates. So the findings page as written describes defective figures. That's a strong reason it's high — the numbers will change. Yes, #3 is right, maybe even higher. But item 1 (full backing) is more fundamental to interpretation. I'll keep 1, 16, 5 order. Actually, should 5 be above 16? Item 16 is wrong figures on the Hub (not the findings page). Item 5 changes the findings page's own numbers. For "change a headline claim," item 5 directly changes the findings-page headlines. Item 16 misleads on the Hub. Both high. I think item 1 > item 5 > item 16 might be better since item 5 changes the actual release headlines. But item 16 has more wrong numbers. Let me think about magnitude.

Item 5: The BU cycle affects basic-living and cost-of-living figures. How much? The supply study says the BU's relief runs a damped two-year cycle. The fix (private price at sale) removes it. The magnitude of change to headline figures isn't stated, but it's a defect fix so presumably material to cost-of-living/basic-living. 

Item 16: Multiple figures off by large amounts (elasticity −0.71 vs −1.6 is more than 2x; 2.86 vs 1.95; £5B; 65% inflation claim; 85/98% poverty). These are grossly wrong. But they're on the Hub, in PDFs, not the findings page.

For "change a headline claim" — the findings-page headlines are the main concern. Item 5 changes those. Item 1 reinterprets those. Item 16 is a separate surface (Hub). 

I'll rank: 1 (full backing), 2 (BU cycle/item 5), 3 (wrong Hub figures/item 16)... no wait, let me keep it clean. The user wants a ranking. Let me go:

1. Item 1 — full backing
2. Item 5 — BU cycle defect (changes the release's own numbers)
3. Item 16 — wrong Hub figures
4. Item 2 — no supply limit below backing
5. Item 3 — opt-in omission
6. Item 9 — tax credits/EITC
7. Item 6 — Hub targets
8. Item 12 — no central bank/expectations
9. Item 20 — release data series
10. Item 7 — Gini mislabel

Hmm, but is item 5 really #2? The release's whole point is to fix it. So by the time of release, it's fixed. The question is about "before that release" — the author wants gaps fixed before release. Item 5's fix IS the release. So the residual gap is "which studies to rerun" (process). The defect itself is being fixed. So maybe item 5's residual risk is lower for the release (it's handled), but the verification (did the fix work, do figures change, are dependent studies rerun) is the gap. I'll frame item 5 as: the fix is the release; the gap is verifying the regenerated figures and rerunning dependent studies. Rank it high because it changes the release's own numbers and dependent studies (readings, financed rows, central bank, history, supply) may now be inconsistent.

OK I think my ranking is defensible. Let me write concise entries.

For each top-ten item: fix in model / fix in text / state as limit, and how to verify.

1. **Item 1 (full backing)**: Fix in text. Put the full-backing condition in the headline card headings and the one-sentence answer, not only the footnote. Verify: each card and the one-sentence answer names full backing and the ~1% (engine) / 6-17% (automation) produced share; a reader who reads only the cards sees the condition.

2. **Item 5 (BU cycle / late private price)**: Fix in model (the release does this). Verify: in regenerated `s90-sale-*` main rows the damped two-year BU cycle is gone; diff v5.9 vs release headline figures and record the delta in DECISIONS.md; confirm the guard test change is recorded.

3. **Item 16 (wrong Hub figures)**: Fix in text (land the corrections package). Verify: each listed figure ($847B, 65%, 15→13pp, 85/98%, $82K+CI, 10,000, −0.71→−1.6, 11.8%, 14→11%, £5B, 2.86→1.95) matches current results; corrections-log entry links each.

4. **Item 2 (no supply limit below backing)**: Fix in text. Keep the Nov 17 note prominent and reconcile "poverty barely depends on backing" with s82 (it depends on wage/BU catch-up; break-even 0.08-0.49). Verify: note present; the "barely depends" sentence carries the s82 qualification.

5. **Item 3 (opt-in does far less)**: Fix in text. Verify: opt-in figure beside every full-coverage headline; the "makes poverty rise in 9 of 12 cells with lost jobs" stays.

6. **Item 9 (tax credits/EITC, no part-time work)**: Fix in model (add part-time work) if feasible before release; else state as limit. Verify: EITC reach vs 15.3% target; poverty with/without the credit.

7. **Item 6 (Hub targets $82K etc.)**: Fix in model/config. Update TARGET_WEALTH/GINI/POVERTY/STABILITY and the "Target $82K" label to current values or remove. Verify: grep the four index.html occurrences; confirm no stale target remains.

8. **Item 12 (no central bank, no expectations, reduced-form rule)**: State as limit, and fix in text. The findings page's inflation figures need the automation study's warning ("measure the size of unbacked money, not a forecast"). Verify: every inflation figure carries that warning; "What no figure covers" names the reduced-form rule and missing essentials-price channel.

9. **Item 20 (release data lacks BLEI/Five Measures series)**: Fix in model/data before release. Verify: BLEI visuals and Five Measures chart render from the regenerated release data.

10. **Item 7 (validation "Gini" mislabeled)**: Fix in text (describe presets in MODEL_SPEC/ODD; relabel the "Gini"). Verify: MODEL_SPEC/ODD describe the presets; the metric is named for what it is (wealth less one year of COL×wage).

**Question 2: Gaps NOT in the inventory that I see in the findings text or limits.**

Let me look for things not in the inventory.

Claims without a stated basis:
- The findings page "one-sentence answer": "the full-coverage design does about 1.4 to 7.1 times as much as the opt-in design." Where does 1.4-7.1 come from? Not obviously derived. Basis unclear.
- "48 of 48 poverty and wealth curves... excludes zero (three environments, two horizons)." 3 env × 2 horizons = 6, but 48 curves? 48 = ... Let me think. Actually "48 of 48 poverty and wealth curves" — with 3 poverty/wealth measures × ... hmm. Actually there are 3 measures (basket poverty, basic living, wealth poverty) plus median wealth = 4? And 2 designs? 3 env × 2 horizons × ... Let me not overanalyze. But note: "48 of 48" vs "46 of 48 financed" — the 48 count. And "three environments, two horizons" = 6 cells. 48/6 = 8 per cell. Could be 4 measures × 2 designs = 8. OK plausible. But the text says "48 of 48 poverty and wealth curves" and separately "the financed rows... 46 of the 48 financed poverty and wealth curves are fragile." So there are 48 financed curves and 48 main curves. Fine.

- "The widest part of the range comes from how much of their spare cash adults spend." This is a claim about the source of variance. Is it backed? It's a marginal propensity to consume parameter. Not in inventory. Could be a design parameter presented as a finding. Actually it's presented as explaining the range, which is a substantive claim needing a sensitivity decomposition. Not obviously backed.

Figures resting on design parameters presented as results:
- The main row's "every dollar matched by new output" — this IS flagged (footnote, item 1). Good.
- The BU adjustment "as the design says" (monthly/quarterly) — design parameter. In supply study.
- "the full-coverage design (the full-coverage design, built to meet NEEC's criterion C2.2)" — the design is built to meet a criterion; the results then show it meets goals. This is somewhat circular: the design is constructed to hit targets, then results show it hits them. This is a "figures resting on design parameters presented as results" issue. The headline cards show the design meeting its own construction criterion. Not in inventory explicitly. Actually item 1 covers full backing. But the broader "design built to meet C2.2" circularity is worth flagging.

- "Median real wealth at year 20: $432,300" — rests on full backing (flagged). But also the erosion share "1.0% of the gain is the erosion of opening balances (in the programme's favour)." This is a small effect. Fine.

Missing unfavourable results:
- The findings page has an "Unfavourable results" section. Let me check what might be missing.
- Participation falls 1-5 points — stated.
- "Less movement out of the lowest wealth fifth: 69.8% still there vs 66.3%" — stated.
- Labour's share falls 11.7-30.5 points — stated.
- Opt-in shrinks in Stress — stated.
- 46/48 financed fragile — stated.
- Programme inflation above no programme in every cell — stated.

What's missing?
- The automation study: "with lost jobs [opt-in] often makes the rise in poverty larger" — this is in the automation text but is it in the main findings unfavourable section? The main findings page unfavourable section doesn't mention the automation opt-in result. But automation is a separate study. The findings page is v5.9 main. Hmm.
- The supply study: "If half of the inflation is never made up in wages, the programme with no backing is worse than no programme on basket poverty." This is a strongly unfavourable result (programme worse than nothing) that's NOT in the main findings page's unfavourable section. The findings page says "poverty effects barely depend on backing" but s82 shows that with wage lag, no-backing programme is WORSE than no programme. This is a missing unfavourable result / a contradiction. Big one.
- "At no backing and 40 years, the opt-in design lowers median real wealth." This IS in the findings page (Prices section note). Good.
- The BU two-year cycle defect (item 5) — being fixed.

Comparisons not like-for-like:
- "the full-coverage design does about 1.4 to 7.1 times as much as the opt-in design" — comparing full coverage (100% take-up) to opt-in (lower take-up). These differ in coverage by design, so the ratio reflects the coverage difference, not efficiency. Not like-for-like. Worth flagging.
- The financed rows "were run without the weighted top tail" — so financed rows aren't comparable to main rows on wealth distribution. The findings page notes this ("These rows were run without the weighted top tail" and "The financed rows leave out the weighted top tail"). So it's disclosed. But comparing financed-row poverty to main-row poverty may not be like-for-like if the top tail affects general equilibrium. Disclosed though.
- "who gains" section: "the full-coverage design raises real wealth by $128,000 at the 10th percentile (from −$2,300) and $218,800 at the 90th." These are full-backing figures. The comparison across percentiles is fine.
- The automation study compares "with lost jobs" vs "shorter hours" — different displacement modes. Fine, disclosed.
- Headline cards compare "against no programme" — the no-programme baseline. Fine.
- The seed interval vs reading spread: "The seed interval covers the model's randomness only, not the choice of reading." Disclosed. Good.
- The 500-adult vs 10,000-adult: "500 adults (a 10,000-adult pair agrees on hours and the top of the wealth distribution)." So they validated 500 against 10,000 on SOME measures. But the headline uses 500. Is the 500-adult sample size adequate for the poverty/wealth figures? They only checked hours and top of wealth distribution agree. Not the poverty rates or median wealth. This is a "figures resting on a design parameter (population size) not fully validated" issue. Worth flagging.

Let me also check:
- "programme inflation is 0.0 to 0.2 points a year above no programme, which is no material change, at every reading." This is at full backing (main row). But the automation study says at the model's own backing (6-17%), inflation is 48-69%. The findings page does present both. But the "0.0 to 0.2 points... no material change" could mislead if read alone. It's qualified by "The main row assumes that every dollar... matched by new output." OK.

- The "backing" threshold: "Inflation stays under 5% a year only above about 86 to 90% backing." And "the model's own mechanism for new output reaches 0.2 to 1.9% of the payout (14 to 20% if its ceiling is removed)." So even removing the ceiling, 14-20% << 86-90%. So the model can never produce enough backing. This is a strong unfavourable result that IS stated. Good.

- Automation produced backing "6-17% at 20 years" vs main "0.2-1.9%". These differ a lot. Why? The automation study has a different mechanism (output per hour). The findings page uses 0.2-1.9% (main row) but automation says 6-17%. Inconsistency in the "produced backing" figure across studies. The findings page one-sentence answer says "the model's own backing mechanism, prices rise 15 to 53 points a year" — but automation says 48-69%. Different numbers for "the model's own backing." This is an inconsistency / not like-for-like. Worth flagging: the "model's own mechanism" produced share differs between the main row (0.2-1.9%) and the automation study (6-17%), and the corresponding inflation differs (15-53 vs 48-69). The findings page should reconcile or explain.

Actually wait — the main row's "0.2 to 1.9%" is the engine's own new-output mechanism in the base model. The automation study's "6-17%" is with automation raising output per hour. Different scenarios. But both are "the model's own mechanism, not assumed full backing." A reader sees "prices rise 15 to 53 points" (main) and "48-69%" (automation) and may be confused. The findings page should clarify these are different runs. This is a coherence gap.

- "Median real wealth... $432,300, against $223,900 (+$208,400)." And "raises median real wealth by $187,600 to $659,600" across readings. The main row $208,400 is near the low end. Fine.

- Erosion: "1.0% of the gain is the erosion of opening balances (in the programme's favour)" and "Less than 3% of any wealth figure is the erosion." And "if all wealth were cash, it would work against it, by at most 5.3%." These are sensitivity checks. Fine.

Let me also check the "How sure we are" section:
- "the full-coverage design lowers basket poverty by 25.9 to 33.3 points; at the main row, 32.4 points (seed interval 32.2 to 32.5)." The seed interval (32.2-32.5) is tiny vs the reading range (25.9-33.3). Disclosed that seed interval ≠ reading spread. Good.
- "48 of 48 poverty and wealth curves... excludes zero." Strong claim. Based on seed intervals excluding zero. But seed intervals only cover randomness, not reading choice. So "robust" here means "sign holds across all readings AND seed interval excludes zero at each." That's a reasonable robustness claim. But "robust" might overstate given the structural limits (no supply limit, full backing). The caption discloses seed interval limits. OK.

Now, "figures resting on design parameters presented as results":
- The headline "full-coverage design, built to meet NEEC's criterion C2.2" — the design is reverse-engineered to meet a criterion. The poverty reductions are partly a consequence of the design being built to achieve them (full coverage, full backing). This circularity is the deepest issue. Item 1 covers full backing; the "built to meet C2.2" and full-coverage-by-design is related. I'll flag the circularity: the design's parameters (full coverage, full backing, BU/basket indexing) are set to achieve the poverty goals, so the headline "it meets the goals" partly restates the construction. Not fully in inventory.

- "the Basic Unit and the cost-of-living basket follow the same prices" — design parameter ensuring real values. This makes the poverty reduction partly mechanical (indexation). Not in inventory. The supply study note (Nov 17) covers "the model has no limit on what the economy can supply. Demand never runs into what can be produced, wages follow prices in full, and the BU and basket follow the same prices." So this is disclosed in the note. But it means the poverty reduction is partly guaranteed by full indexation + no supply limit. Worth flagging as design-parameter-driven.

Missing unfavourable results (continued):
- No mention of the automation opt-in "makes poverty rise" in the main findings unfavourable section (it's in automation text). But automation is separate. The main findings page is about the core programme, not automation. So maybe not required. But if the release page aggregates, it should include.
- The supply study's "no-backing programme worse than no programme on basket poverty (with wage lag)" — this is a core-programme unfavourable result not in the main findings unfavourable section. The findings page says poverty "barely depends on backing" which contradicts s82's wage-lag finding. This is both a missing unfavourable result AND a contradiction. Strong flag.

Comparisons not like-for-like (continued):
- "1.4 to 7.1 times as much as the opt-in design" — full coverage vs opt-in differ in take-up by design; the ratio conflates coverage with per-participant effect. Not like-for-like as an efficiency comparison.
- Main row (full backing, with top tail) vs financed rows (no top tail) — disclosed but the poverty comparison across them may not be like-for-like.
- 500 vs 10,000 adults — only hours and top of wealth validated; poverty/median not validated at 500. The headline uses 500.

Claims without stated basis (continued):
- "1.4 to 7.1 times" — basis?
- "The widest part of the range comes from how much of their spare cash adults spend" — needs a variance decomposition; basis not shown.
- "48 of 48... three environments, two horizons" — the arithmetic (why 48) not shown; minor.
- "a 10,000-adult pair agrees on hours and the top of the wealth distribution" — agrees to what tolerance? Basis not stated.

Let me also check the automation text for gaps not in inventory:
- "the free time displacement brings is mostly secure" / "keeps most of the freed time above the cost of living (4-10% of it below, against 76-81% with no programme)." Basis: free-time valuation. But the main findings page says "no value of care, community work or new ventures" — so free time isn't valued in money. The automation "free time above cost of living" uses some imputed value. Potential inconsistency: main model doesn't value free time, automation study reports free time above cost of living. How is free time valued in automation? Not clear. Could be a basis gap.
- Automation "matches 6-17% of the payout at 20 years" vs main "0.2-1.9%". Already flagged.
- Automation limits: "The produced share depends on m, which the design does not state; every statement here names it." Good disclosure.
- "Lost jobs count adults, not hours" — disclosed.

Supply study gaps not in inventory:
- Limit 5 (BU two-year cycle) is item 5 in inventory. Covered.
- "These two were not run together; the joint run uses the yearly delay" — the wage-lag and BU-delay not run jointly except via yearly. Disclosed.
- The break-even backed share 0.08-0.49 — this is a strong result (programme needs 8-49% backing to beat no programme on poverty when wages lag). Not in main findings. Related to missing unfavourable result above.

OK, I have plenty for Question 2. Let me organize into the categories the user gave: claims without a stated basis, figures resting on design parameters presented as results, missing unfavourable results, comparisons not like-for-like.

**Question 3: What the release step itself is missing.**

The release step (S93):
1. `sp.vAt: 'sale'` default; guard test differs by design, record in DECISIONS.md.
2. Regenerate main rows' findings-page data from `s90-sale-*-b8ccd8d`, replace dated notes with figures.
3. Hub corrections-log entry; root-site indexes.
4. Late-price figures stay as v5.9 record (OSF).
5. Then preregistered amendment deciding which reached studies rerun on release engine.

What's missing:
- **Pre-publish checks**: 
  - No check that regenerated figures are diffed against v5.9 and the deltas explained/recorded. The release changes the default price rule; headline figures WILL change. Need a before/after diff with explanation.
  - No verification that the BU two-year cycle is actually gone in the regenerated main rows (the whole point of the fix).
  - No check that the guard test change is correct (the test "now differs by design" — need to confirm the new expected values are right, not just updated to pass).
  - No independent/outside reading of the regenerated figures (item 22) before publishing.
  - No check that unfavourable results and qualifiers survive the regeneration (the text rule says qualifiers/unfavourable results may not be dropped; need a check that the regenerated figures still support every qualifier, e.g., erosion shares, seed intervals, reading ranges).
  - No reconciliation of the "produced backing" inconsistency (main 0.2-1.9% / 15-53 pts vs automation 6-17% / 48-69 pts).
  - No check that the release data includes the series the BLEI/Five Measures charts need (item 20).
  - No update of the basis-class block (engine hash changes from 104691f to the release version; commands, run dates, OSF freeze reference must update).
  - The findings text says "Engine 104691f (the frozen model, first published as v5.8), batch shown as v5.9." After the release, the engine is the release version with vAt:'sale' default. The basis block must change. Also "first published as v5.8" — versioning clarity.

- **Which studies must be rerun on the release engine**: The release changes the default price rule (private price at sale). Any study whose results depend on the BU price / premium timing must be rerun:
  - The supply study (s82) — explicitly, its limit 5 says the BU cycle predates it and the fix's rerun is preregistered (s90). MUST rerun.
  - The financed rows (contribution) — depend on prices/income. Rerun.
  - The central bank study — depends on prices. Rerun.
  - The history/ageing reading — the ageing reading was rerun after a defect (s82 limit 6); check if it needs rerun on release engine.
  - The readings (the 62 preregistered readings) — the main rows are regenerated, but the full set of 62 readings' data (r2-effects.json) must be regenerated on the release engine, not just the main row. The release step says "Regenerate the main rows' findings-page data" — but the findings page quotes ranges across 62 readings. If only main rows are regenerated, the ranges are stale (v5.9 engine). This is a GAP: the release must regenerate ALL 62 readings, not just main rows, or the ranges won't match the new default.
  - The automation study (s85) — depends on prices (inflation 48-69%). If run on old engine, its inflation figures are inconsistent with the release. Rerun or flag.
  - Erosion trace — depends on prices. Rerun.

  Actually the release step item 5 defers this to "a preregistered amendment deciding which reached studies are rerun." So the release itself acknowledges this is undecided. My job: say which MUST be rerun. The BU price change affects anything touching prices, BU, premiums, inflation, real wealth. That's: the 62 readings (ranges), financed rows, central bank, supply, automation, history/ageing, erosion. The "readings" are the core — the findings page's ranges come from them.

- **What the text must say**:
  - The basis-class block must update: new engine hash/version, new run dates, new commands, new results paths (`s90-sale-*`), OSF freeze reference for the release.
  - Every "corrected Nov 17, 2026" note that is now superseded by regeneration should be replaced with the release figures (the step says "replace the dated notes with the figures") — but must confirm the new figures still carry the required qualifiers (full backing, erosion share, seed interval, reading range).
  - The full-backing condition must be in the headline cards (item 1).
  - The "produced backing" figures must be reconciled across main/automation.
  - The version naming: "v5.9" batch on release engine — clarify what version the release is (v6.0? v5.9 with new default?). The text says "v5.9 release" but the engine changes. Version clarity needed.
  - The late-price figures stay as v5.9 OSF record (step 4) — the text must say these are the OLD (pre-fix) record and why they're kept (as the v5.9 record), so readers don't confuse them with the release figures.
  - A statement of what changed between v5.9 and the release (the price-rule default change and its effect on figures) — a changelog in the text.

**Question 4: Which items are acceptable as stated limits for this release, and why.**

Items that are acceptable as stated limits (can't/shouldn't be fixed before this release, and are properly disclosed or disclosable):
- Item 4 (Creative Collectives' lending): preregistered, build to follow. It's a future engine step. Acceptable as a stated limit ("not yet modelled; preregistered"). Why: it's about producing backing, which is already handled by the full-backing disclosure; adding it now would change the model substantially and isn't a defect.
- Item 8 (MODEL_SPEC gaps/contradictions): documentation; acceptable to state as a known documentation debt, though contradictions should be listed. Why: doesn't change figures; but contradictions should at least be enumerated. Borderline — I'd say the contradictions should be fixed in text (listed), the gaps can be stated.
- Item 10 (who is simulated): acceptable as a stated limit IF the Hub and findings say "working-age adults and their families." Why: scope limitation, honestly disclosed; the labour-force scope option exists for later.
- Item 11 (community business capacity whole-population, one utility share): acceptable as a stated limit. Why: structural simplification, doesn't change headline direction; disclose.
- Item 12 (no private firms/banks/bond market, reduced-form central bank, no expectations): acceptable as a stated limit for the STRUCTURE, but the inflation figures must carry the "not a forecast" warning (text fix). Why: building a full GE model with banks is out of scope; the reduced form is disclosed; the risk is only if inflation is read as a forecast.
- Item 13 (capital income not in price rule; dividend raises no investment): acceptable as a stated limit. Why: structural; disclosed; the automation study already notes "the dividend raises no investment."
- Item 14 (displaced adults' outcomes by fifth not stored): acceptable as a stated limit for this release (data not stored; would need a rerun). Why: it's a missing disaggregation, not a wrong figure; can be added later.
- Item 15 (health/security/output per hour no source): acceptable as a stated limit. Why: no opened source; honestly left out; the automation study discloses it.
- Item 17 (168 cited external figures not opened): borderline. These are external claims; acceptable to state as "cited, not opened" IF flagged, but ideally the ones used in headlines should be opened. For this release, acceptable as a stated sourcing limit for non-headline citations. Why: opening 168 sources is out of scope; but any cited figure used to support a headline must be opened.
- Item 18 (θ calibration not run): acceptable as a stated limit IF the text doesn't claim it was calibrated. If the text implies calibration, must fix. Why: if no claim of calibration is made, it's fine to state "θ set by sweep, not calibrated."
- Item 21 (Hub 32-item audit): the methodological transparency / AI-authorship items are acceptable as stated limits (disclose AI authorship, terminology). Gini comparability should be fixed. Mixed.

Items NOT acceptable as mere stated limits (must fix): 1, 2, 3, 5, 6, 9, 16, 20, and the release-process items. Because they change headlines or are wrong numbers.

Let me be careful: the user asks "Which items are acceptable as stated limits for this release, and why." So I list the items that can be left as disclosed limits, with reasons. I should be concrete.

Acceptable as stated limits: 4, 8 (gaps, not contradictions), 10, 11, 12 (structure, with inflation warning), 13, 14, 15, 17 (non-headline), 18 (if no calibration claim), 21 (transparency/AI-authorship parts).

Let me make sure I'm not contradicting myself. Item 12 I put in top-ten as "state as limit + text fix (inflation warning)." In Q4 I say the structure is acceptable as a limit but the inflation warning is a required text fix. Consistent.

Item 7 I put in top ten (fix in text — relabel/describe). Not acceptable as-is because it's a mislabel. Keep in top ten.

Now let me also reconsider: the user wants "concrete and short." I should avoid over-explaining. Use plain text, numbered. No praise.

Let me also double check the "62 preregistered readings" regeneration gap — this is a strong Q3 point. The release step says "Regenerate the main rows' findings-page data (r2-effects.json and the cards)." But the findings page quotes ranges across 62 readings ("Across the 62 preregistered readings, the full-coverage design lowers basket poverty by 25.9 to 33.3 points"). If only main rows are regenerated on the new default, the 62-reading ranges are from the old engine (vAt not sale). So either (a) regenerate all 62 readings on the release engine, or (b) the ranges are stale/inconsistent with the new main-row figure. This is a real gap. Actually, r2-effects.json might contain all readings' effects. "Regenerate the main rows' findings-page data (data/studies/r2-effects.json and the cards)" — r2-effects.json could be all readings. Ambiguous. But "the main rows'" suggests only main rows. I'll flag: confirm whether r2-effects.json regeneration covers all 62 readings or only main rows; if only main rows, the quoted ranges are on the old default and inconsistent.

Also: the seed intervals and reading ranges quoted (e.g., "32.4 points (seed interval 32.2 to 32.5)") — after regeneration these change. The text must be updated with new intervals, and the "48 of 48 excludes zero" claim re-verified on the release engine.

Also the erosion trace (r2-erosion) — depends on prices; the "1.0% erosion" and "less than 3%" and "5.3% if all cash" figures must be regenerated on the release engine. The release step doesn't mention regenerating the erosion trace. Gap.

Also charts (s64_charts.py) must be regenerated from the new data. The release step says regenerate data and cards but doesn't explicitly say regenerate charts. Gap (minor, implied).

Let me also note: the guard test "now differs by design: record it in DECISIONS.md." Recording is good, but there should be a check that the new guard values are independently correct (not just updated to match output). A test that's updated to match whatever the code produces isn't a test. Verify the new expected values by an independent calculation or the s90 prereg's predicted effect.

Now, the version question: The findings text is titled "The v5.9 model on the findings page: the text for the v5.9 release" and dated Nov 15, 2026. The release (S93) makes vAt:'sale' the default "at that version" (D34, the author's call). So the release might be v5.9 with a new default, or a new version. The basis block says "Engine 104691f (the frozen model, first published as v5.8), batch shown as v5.9." After the release, engine hash changes. The text must state the release engine hash and version clearly, and distinguish "v5.9 (pre-fix, OSF record)" from "the release (vAt:sale default)."

Also the release keeps "late-price figures... as the v5.9 record (OSF)" (step 4). The text must clearly label these as the pre-fix record so readers don't read them as current.

OK. Let me also reconsider Q1 ranking once more for defensibility, and make each entry crisp.

Actually, I realize I should double-check: is item 5 (BU cycle) really changing the HEADLINE figures, or mainly the cost-of-living/basic-living? The BU two-year cycle affects the Basic Unit's relief to cost of living. Basic living (30 days) and cost-of-living basket poverty are headlines. So yes, item 5 changes two of the four headline cards (basic living, cost of living). Median wealth and wealth poverty less directly (through prices). So item 5 is high. Good.

Let me reconsider whether item 16 should be #2 or #3. Item 16 is wrong figures on the Hub (PDFs, old pages). These mislead readers who go to the Hub. But the "findings page" is the main release surface. The user says "change a headline claim or mislead a reader." Hub figures mislead readers. But they're not the release's headlines. I'll rank item 5 (changes release headlines) above item 16 (Hub, separate surface). So: 1, 5, 16. Wait, I earlier had 1, 16, 5. Let me settle: item 5 changes the release's own headline numbers → more central to "change a headline claim." Item 16 misleads on a different surface. I'll go 1, 5, 16? Hmm, but item 16 has MANY grossly wrong numbers (elasticity 2x off, multiplier 2.86 vs 1.95, £5B, 85/98% poverty). That's severe misleading. And item 5 is being fixed by the release itself (so post-release it's handled). 

The question is about "before that release" — what to fix. Item 5's fix IS the release. So the residual action for item 5 is verification + rerunning dependents. Item 16 needs a corrections package landed. Both are pre-release actions. For "could change a headline or mislead," item 1 > item 16 (gross wrong numbers, many) ≈ item 5 (changes release numbers). 

I'll rank: 1 (full backing), 2 (item 16 wrong Hub figures), 3 (item 5 BU cycle). Actually no — item 5 changes the ACTUAL release headlines that the release is publishing. That's the most direct "change a headline claim." I'll put item 5 at 2 and item 16 at 3. Let me go with:

1. Item 1 (full backing)
2. Item 5 (BU cycle — changes release's own headline numbers)
3. Item 16 (wrong Hub figures)
4. Item 2 (no supply limit below backing)
5. Item 3 (opt-in omission)
6. Item 9 (tax credits/EITC)
7. Item 6 (Hub targets)
8. Item 12 (no central bank/expectations)
9. Item 20 (release data series)
10. Item 7 (Gini mislabel)

Good. I'll write concise entries.

Wait, I should reconsider item 9 vs item 6 vs item 12 ordering. Item 9 (EITC reach low, no part-time work) could change poverty/redistribution headlines → fairly high. Item 6 (Hub targets) misleads on validation, visible. Item 12 (no central bank) affects inflation interpretation. I think 9 > 6 > 12 is fine, or 9 > 12 > 6. The EITC/part-time issue directly affects the "who gains" and poverty figures. Keep 9 at 6.

Actually, is item 9's effect on the headline large? "EITC reach is low (11.9% against 15.3%) because the model has no part-time work." This means the model under-delivers EITC to the working poor relative to reality. If the programme's poverty reduction is compared to a baseline where EITC is under-delivered, the programme's relative effect could be overstated (the no-programme baseline is worse than reality). Or the programme substitutes for the missing EITC. Either way, it affects the poverty comparison. Medium-high. Keep at 6.

Let me finalize and write. I need to be concrete and short. Let me write each Q1 entry as: rank, item, fix location, verify.

Let me write it out.

For Q2, organize by the four categories the user named:
- Claims without a stated basis
- Figures resting on design parameters presented as results
- Missing unfavourable results
- Comparisons not like for like

Claims without a stated basis:
- "1.4 to 7.1 times as much as the opt-in design" — no derivation shown.
- "The widest part of the range comes from how much of their spare cash adults spend" — a variance claim with no decomposition shown.
- "a 10,000-adult pair agrees on hours and the top of the wealth distribution" — no tolerance stated; and only hours/top-of-wealth were checked, not the poverty rates or median wealth that are the headlines.
- Automation "keeps most of the freed time above the cost of living" — the main model states it puts "no value of care, community work or new ventures," so the basis for valuing free time against the cost of living is unstated.

Figures resting on design parameters presented as results:
- The headline cards: the design is "built to meet NEEC's criterion C2.2" with full coverage and full backing; the poverty reduction is partly a restatement of the construction (full indexation of BU and basket to the same prices + no supply limit + full backing). The cards present the outcome without flagging that the parameters were chosen to produce it. (Item 1 covers full backing; the full-coverage/indexation circularity is additional.)
- "programme inflation is 0.0 to 0.2 points... no material change" rests on the full-backing design parameter (disclosed in the next sentence) — OK but the "no material change" phrasing can mislead if lifted.

Missing unfavourable results:
- Supply study: with wages not keeping up (half the inflation never made up), the no-backing programme is WORSE than no programme on basket poverty; break-even only at 0.08-0.49 backing. The findings page instead says poverty "barely depends on backing." This unfavourable result (and the contradiction) is absent from the Unfavourable section.
- Automation: opt-in with lost jobs makes the rise in poverty (and low savings in Stress) larger — not in the main Unfavourable section.
- The "produced backing" can never reach the 86-90% needed for <5% inflation even with the ceiling removed (14-20%) — stated in Prices, but the implication (the design cannot self-fund) is not in Unfavourable.

Comparisons not like for like:
- "1.4 to 7.1 times as much as the opt-in design" compares 100% take-up to partial take-up; the ratio reflects coverage, not per-participant effectiveness.
- Main row (with weighted top tail) vs financed rows (without top tail): poverty/wealth levels compared across them aren't like-for-like; disclosed but the comparison is still made.
- Headline uses 500 adults; the 10,000-adult validation covered only hours and top-of-wealth, not the poverty/median-wealth headlines.
- "Model's own mechanism" produced share and inflation differ between the main row (0.2-1.9%, 15-53 pts) and the automation study (6-17%, 48-69 pts); presented in different sections without reconciliation, so "the model's own backing" reads as two different things.

For Q3, I'll structure: pre-publish checks; studies to rerun; what the text must say.

For Q4, list acceptable-as-limit items with reasons.

Let me write it all concisely. I'll aim for tight bullets.

One more check on Q3 — "which studies must be rerun on the release engine." The release changes the default price rule (private price at sale vs the late price). Anything whose results move with the BU price timing:
- The 62 preregistered readings (the ranges on the findings page) — MUST, or the ranges are stale.
- Erosion trace — MUST (the erosion shares are quoted).
- Financed/contribution rows — MUST (prices/income).
- Central bank study — MUST (prices).
- Supply study (s82) — MUST (its limit 5 says the fix's rerun is preregistered s90).
- Automation study (s85) — MUST or flag (inflation 48-69% depends on price rule).
- History/ageing reading — check (ageing was rerun for a defect; confirm on release engine).
- Charts — regenerate from new data.

The release defers this to item 5 (a preregistered amendment). My answer: the amendment must include at minimum the 62 readings, erosion, financed rows, central bank, supply, automation; and the text must not publish ranges/figures from mixed engines.

Also pre-publish checks:
- Diff regenerated vs v5.9 headline figures; record deltas and confirm direction/magnitude expected from the fix.
- Confirm the BU two-year cycle is gone in regenerated main rows.
- Confirm the guard test's new expected values are independently correct (not just re-baselined to output).
- Re-verify every qualifier survives regeneration: full-backing condition, erosion share, seed interval, reading range, "48 of 48 excludes zero," financed fragility count.
- Outside reading of the regenerated figures (item 22) before publish.
- Confirm release data includes series for BLEI/Five Measures (item 20).
- Reconcile produced-backing figures across main/automation.
- Update basis-class block (engine hash, version, dates, commands, results paths, OSF freeze ref).
- Land the Hub corrections (item 16) and update Hub targets (item 6) so the Hub doesn't contradict the release.

What the text must say:
- New engine version/hash and what changed (vAt:'sale' default) and its effect on the headline figures (a changelog).
- Full-backing condition in the card headings (not only footnote).
- The late-price figures are the pre-fix v5.9 OSF record, kept for reference, not the release figures.
- Replace "corrected Nov 17" notes with release figures but keep every required qualifier.
- Reconcile "model's own backing" main vs automation.
- Add the s82 wage-lag unfavourable result (no-backing worse than nothing) or reconcile the "barely depends on backing" sentence.
- Version clarity: is the release v5.9 or a new version number?

Good. Now write final. Keep it concrete and short. Plain text. Numbered per the four questions.

I'll try to keep Q1 to ten crisp entries, Q2 grouped, Q3 grouped, Q4 a list.

Let me make sure not to invent facts. I'm using only what's in the provided text. Good.

Let me write.

Actually, for Q1 verify steps, keep them to one concrete check each.

Let me write the final answer.

I want to be careful about length — "concrete and short." I'll use compact bullets. I'll avoid restating the item descriptions at length; just name and act.

Final structure:
1. Top ten ranking with fix/verify.
2. Gaps not in inventory, grouped by the four types.
3. Release step gaps: checks / reruns / text.
4. Acceptable-as-limit items with reasons.

Write now.