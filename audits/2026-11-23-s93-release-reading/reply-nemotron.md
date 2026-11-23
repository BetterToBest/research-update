# Independent Review of the Compassionism Simulation Release v5.9.23

## 1. Does every statement in the release report and page's release note follow from the tables? Quote any sentence that overstates, understates or misquotes a figure, and give the correct figure.

### Release Report (`dev/reports/s93-release.md`)

**Misquoted figure — "The price at the sale moved every poverty and wealth effect in the programme's favour."**

The tables show this is **false for the opt-in design**. In the opt-in design, the "Price at the sale" step *increased* (worsened) basket poverty in every cell (e.g., Reference 20y: +0.26 points; Adverse 20y: +0.18; Stress 20y: +0.094; Reference 40y: +0.13; Adverse 40y: +0.079; Stress 40y: +0.037). It also increased (worsened) "below 30 days of basic living" in every opt-in cell (e.g., Reference 20y: +0.19; Adverse 20y: +0.22; Stress 20y: +0.13). The statement only holds for the full-coverage design.

**Correct statement:** "The price at the sale moved every full-coverage design poverty and wealth effect in the programme's favour; for the opt-in design it moved poverty effects against the programme."

---

**Misquoted figure — "Basket poverty: the full-coverage design's cut grew by 0.28 to 0.59 points, the opt-in design's by 0.04 to 0.26."**

The tables show the **total change** (both steps combined) for basket poverty:
- Full-coverage Reference 20y: -0.45 (favour), 40y: -0.49 (favour)
- Full-coverage Adverse 20y: +0.015 (interval includes 0), 40y: +0.32 (against)
- Full-coverage Stress 20y: +0.024 (interval includes 0), 40y: +0.37 (against)
- Opt-in Reference 20y: +0.58 (against), 40y: +0.47 (against)
- Opt-in Adverse 20y: +0.76 (against), 40y: +0.71 (against)
- Opt-in Stress 20y: +0.29 (against), 40y: +0.29 (against)

The quoted ranges (0.28–0.59 and 0.04–0.26) appear to describe only the **first step (price at sale)** for full-coverage, but the sentence says "Basket poverty:" without qualification, implying the total change. The opt-in design's basket poverty *worsened* in every cell, not "grew by 0.04 to 0.26" in the programme's favour.

**Correct statement:** "The price at the sale alone moved full-coverage basket poverty in the programme's favour by 0.28–0.59 points; the total change (both steps) moved full-coverage basket poverty in the programme's favour in Reference but against it in Adverse and Stress, and moved opt-in basket poverty against the programme in every cell (0.29–0.94 points)."

---

**Misquoted figure — "Median real wealth: the gain grew by $481 to $1,525 (full coverage) and $110 to $605 (opt-in)."**

The tables show the **first step (price at sale)** for median real wealth:
- Full-coverage: Reference 20y: +$582; Reference 40y: +$481; Adverse 20y: +$1,141; Adverse 40y: +$1,525; Stress 20y: +$860; Stress 40y: +$1,260
- Opt-in: Reference 20y: +$500; Reference 40y: +$605; Adverse 20y: +$487; Adverse 40y: +$236; Stress 20y: +$229; Stress 40y: +$110

The ranges $481–$1,525 (full coverage) and $110–$605 (opt-in) match the **first step only**, but the sentence says "Median real wealth: the gain grew by..." without specifying this is only the price-at-sale step. The **total change** for median real wealth includes the second step which often offsets (e.g., full-coverage Reference 40y total: -$1,244, interval includes 0; opt-in Reference 40y total: -$1,337, interval includes 0).

**Correct statement:** "The price at the sale alone raised median real wealth by $481–$1,525 (full coverage) and $110–$605 (opt-in); the total change after both steps was smaller and in several cells the interval included zero."

---

**Misquoted figure — "Programme inflation: it changed by less than 0.0001 points a year. It rose by that much at most in four full-coverage cells (Adverse and Stress); elsewhere it fell slightly or did not change measurably."**

The tables show programme inflation **total change** (both steps):
- Full-coverage Reference 20y: +0.007; 40y: +0.003
- Full-coverage Adverse 20y: +0.004; 40y: +0.002
- Full-coverage Stress 20y: +0.004; 40y: +0.002
- Opt-in Reference 20y: +0.003; 40y: +0.002
- Opt-in Adverse 20y: -0.001; 40y: -0.001
- Opt-in Stress 20y: -0.002; 40y: ~0

The first step (price at sale) shows ~0 change (rounded to 0.000). The second step ("The two readings") shows the increases. The sentence says "it changed by less than 0.0001 points a year" which describes the first step only, but then says "It rose by that much at most in four full-coverage cells" — "that much" refers to <0.0001, but the actual rises are 0.002–0.007. This is a confusion between steps.

**Correct statement:** "The price at the sale alone changed programme inflation by less than 0.0001 points a year in all cells. The pay and care credit additions raised full-coverage programme inflation by 0.002–0.007 points a year and changed opt-in programme inflation by -0.002 to +0.003 points a year."

---

**Misquoted figure — "Opt-in design: every poverty cut shrank. Basket poverty by 0.33 to 0.94 points, below 30 days of basic living by 0.13 to 0.39, and too little wealth by 0.19 to 0.42."**

The tables show the **second step ("The two readings")** for opt-in:
- Basket poverty: Reference 20y: +0.84; Reference 40y: +0.60; Adverse 20y: +0.94; Adverse 40y: +0.79; Stress 20y: +0.39; Stress 40y: +0.33 → range 0.33–0.94 ✓
- Below 30 days: Reference 20y: +0.21; Reference 40y: +0.14; Adverse 20y: +0.28; Adverse 40y: +0.39; Stress 20y: +0.13; Stress 40y: +0.17 → range 0.13–0.39 ✓
- Too little wealth: Reference 20y: +0.31; Reference 40y: +0.32; Adverse 20y: +0.35; Adverse 40y: +0.42; Stress 20y: +0.19; Stress 40y: +0.19 → range 0.19–0.42 ✓

This statement correctly describes the **second step only**, but the report presents it as "Pay by household type and the care credit moved the two designs differently... Opt-in design: every poverty cut shrank..." without explicitly stating this is the second step's effect, not the total change. The total change for opt-in basket poverty is +0.29 to +0.94 (since first step also worsens it). The statement is accurate for the second step but could mislead a reader into thinking these are the total changes.

---

**Misquoted figure — "Full-coverage design: its cut below 30 days of basic living grew by 0.42 to 0.75 points, and its other effects moved both ways."**

Second step ("The two readings") for full-coverage "below 30 days":
- Reference 20y: -0.55; Reference 40y: -0.75; Adverse 20y: -0.45; Adverse 40y: -0.43; Stress 20y: -0.44; Stress 40y: -0.42 → range 0.42–0.75 (more negative = larger cut) ✓

But "its other effects moved both ways" — the second step for full-coverage basket poverty: Reference 20y: +0.11 (worsened), Reference 40y: -0.21 (improved), Adverse 20y: +0.59 (worsened), Adverse 40y: +0.61 (worsened), Stress 20y: +0.62 (worsened), Stress 40y: +0.68 (worsened). So basket poverty worsened in 5 of 6 cells, improved in 1. "Both ways" is technically true but understates the predominance of worsening.

---

### Page Release Note (in "v5.9: the answer in ten seconds" section)

**Misquoted figure — "The price at the sale moved every main-row poverty and wealth effect in the programme's favour, and raised the full-coverage design's programme inflation in Adverse and Stress by less than 0.0001 points a year; the two additions made the opt-in design's poverty cuts smaller and the full-coverage design's cut below 30 days of basic living larger."**

Same errors as the release report: "every main-row poverty and wealth effect" is false for opt-in design (price at sale worsened opt-in poverty effects). "Raised the full-coverage design's programme inflation in Adverse and Stress by less than 0.0001 points a year" — the first step did that, but the total change raised it by 0.002–0.004. The sentence conflates steps.

**Correct statement:** "The price at the sale moved every full-coverage main-row poverty and wealth effect in the programme's favour (but moved opt-in poverty effects against the programme), and changed programme inflation by less than 0.0001 points a year in all cells. The two additions (pay by household type and care credit) made the opt-in design's poverty cuts smaller and the full-coverage design's cut below 30 days of basic living larger, while raising full-coverage programme inflation by 0.002–0.004 points a year in Adverse and Stress."

---

**Misquoted figure — "Below full backing, the reading that changed most is wages that follow programme inflation only in part: with no backing the programme is now worse than no programme in 2 of the six cells (Reference at 40 years, Stress at 40 years), better in the other 4 on basket poverty (the supply study, above), and the change comes from the price at the sale."**

The decomposition table (s93-wage-dec-50bc51d) shows:
- Reference 20y: published +10.1 → release -7.9 (sign change)
- Adverse 20y: published +4.8 → release -12.6 (sign change)
- Stress 20y: published +9.2 → release -1.8 (sign change)
- Reference 40y: published +30.7 → release +12.5 (still positive, but smaller)
- Adverse 40y: published +15.9 → release -2.5 (sign change)
- Stress 40y: published +19.0 → release +11.4 (still positive)

The page says "worse than no programme in 2 of the six cells (Reference at 40 years, Stress at 40 years)" — but at 20 years, **all three environments** flipped from worse to better (Reference, Adverse, Stress all changed sign from positive to negative effect on basket poverty). At 40 years, Reference and Stress remain worse (positive effect), Adverse flipped to better. So it's **3 of 6 cells at 20 years** that changed from worse to better, and **1 of 3 at 40 years** (Adverse) that changed from worse to better. The statement "worse than no programme in 2 of the six cells" describes the *release* state (Reference 40y and Stress 40y are worse), but the phrasing "the reading that changed most... the programme is now worse... in 2 of the six cells" is ambiguous. The decomposition confirms the sign change at 20 years in all three environments comes from the price at sale.

**Correction needed:** The page should clarify: "At 20 years, the programme with no backing changed from raising basket poverty in all three environments (published) to lowering it in all three (release). At 40 years, it still raises basket poverty in Reference and Stress but now lowers it in Adverse. The change comes from the price at the sale."

---

## 2. Does the release text do what the preregistration's section G and Amendment 3's G require? What is missing?

### Preregistration Amendment 2, Section G requires:
1. **Release version and engine commit** ✓ (v5.9.23, engine 50bc51d)
2. **Private businesses' lower BU price now set at the sale (Duke's design, Oct 1) and is default** ✓
3. **What that changed, stated from item F1's release figures (not from S92's range)** ✓ (release report states from F1 tables)
4. **Which studies were rerun and which reproduced** ✓ (release report lists all)
5. **Model registered on OSF (v5.8, engine 104691f) and v5.9 figures stay published as record** ✓

### Amendment 3, Section G adds:
- **Main row now includes pay by household type and child and dependent care credit (Duke's decision, Nov 21, after yardstick study's preregistered rule held)** ✓
- **What that changed (F1's split)** ✓
- **That the v5.9 main row without them stays the record** ✓

### What is missing from the release text (page's release note and release report):

**Missing from page release note:** The page's release note says "This release (v5.9.23, engine 50bc51d). The figures in this section come from the preregistered reruns on the release engine. The main row changed in three ways: the private businesses' lower BU price is now set at the sale, as the design states (Duke's design, Oct 1, 2026), instead of a year late out of the previous year's premium; pay differs by household type, as in the survey; and the child and dependent care credit is included (the last two adopted by Duke on Nov 21, 2026, after the yardstick study's preregistered rule held)."

This **does not state** that the v5.9 figures before this release stay published as the record (Amendment 2 G and Amendment 3 G both require this). The release report says it, but the page's release note (which readers see) does not.

**Missing from page release note:** Which studies were rerun and which reproduced (Amendment 2 G requires this). The release report lists them, but the page note does not.

**Missing from page release note:** The OSF registration statement (v5.8, engine 104691f) — required by both Amendment 2 G and Amendment 3 G.

**Missing from release report:** The release report says "The model registered on OSF (v5.8, engine 104691f) and the v5.9 figures stay published as the record." But it does not explicitly state that the **v5.9 main row without pay by household type and care credit** stays as the record (Amendment 3 G: "the v5.9 main row without them stays the record"). It says "the v5.9 figures stay published as the record" which is ambiguous — does it mean all v5.9 figures, or the main row without the two additions?

---

## 3. The supply study's wage reading changed sign at 20 years. Is the decomposition's conclusion (the change comes from the price at the sale) supported by the table given? What else would you check before publishing that sentence?

### Decomposition table (s93-wage-dec-50bc51d) shows:

| Variant | Reference 20y effect | Adverse 20y effect | Stress 20y effect |
|---|---|---|---|
| Published engine (v5.9 row, late price) | +10.1 | +4.8 | +9.2 |
| Release engine, v5.9 row (all three undone) | +10.1 | +4.8 | +9.2 |
| Release row, price a year late (sale undone) | +10.0 | +5.1 | +9.5 |
| Release row, without pay by household type | -7.9 | -13.0 | -2.1 |
| Release row, without care credit | -7.9 | -12.7 | -1.8 |
| Release row (default) | -7.9 | -12.6 | -1.8 |

**Conclusion supported:** Yes. Undoing the price at sale (variant "release row, price a year late") returns the figure to ~+10.0, +5.1, +9.5 — within 0.3 points of the published engine's +10.1, +4.8, +9.2. Undoing pay by household type or care credit alone moves the release figure by at most 0.5 points (actually, it moves it from -7.9 to -7.9/-7.9 in Reference, -12.6 to -13.0/-12.7 in Adverse, -1.8 to -2.1/-1.8 in Stress — so the *release figure* changes by ~0.1–0.4 points when each is undone, but the key is that the *published figure* is only recovered when the price at sale is undone). The v5.9 row on release engine equals published engine, so engine fixes don't move it.

**The decomposition shows which change moves the figure, not the mechanism** — the table's own "limits" row states this.

### What else to check before publishing "the change comes from the price at the sale":

1. **Interaction effects not separated:** The decomposition switches one change at a time from the release row (not a full factorial). The interaction between the price-at-sale change and the two additions is not isolated. The table shows "release row, without pay by household type" = -7.9 (Reference 20y), "release row, without care credit" = -7.9, "release row (default)" = -7.9 — so the two additions together don't change the figure beyond what each does alone in Reference. But in Adverse: without pay = -13.0, without credit = -12.7, default = -12.6 — small interaction. In Stress: without pay = -2.1, without credit = -1.8, default = -1.8. The interaction is small but not zero. The claim "the change comes from the price at the sale" is correct for the *main effect*, but the interaction with the additions should be acknowledged.

2. **Only 20 seeds, not 500:** The decomposition uses seeds 1-20. The main results use 500 seeds. The sign change at 20 years is confirmed on 500 seeds (page check table shows sign change on 500 seeds), but the decomposition's precision (within 0.3 points) is only on 20 seeds. Should verify on 500 seeds or state the limitation clearly.

3. **Only basket poverty measured:** The decomposition only tests basket poverty. The page says "the reading that changed most is wages that follow programme inflation only in part" — but the decomposition only covers one outcome (basket poverty) of that reading. Other outcomes (wealth, inflation) might have different decompositions.

4. **The "never made up" wage reading is a design parameter, not an estimated mechanism:** The page should clarify this is a pessimistic bound, not a forecast.

5. **Check that the "price at sale" variant (sp.vAt 'lag') is correctly implemented:** The decomposition uses "release row, price a year late (sale undone)" which sets sp.vAt 'lag'. Verify this exactly replicates the published engine's price rule.

---

## 4. Below full backing, the preregistered swing measure failed and a measure chosen after the failure is used. Is that handled and labelled fairly in the report?

### Release report states:
"Below full backing, the preregistered swing measure **failed for a known reason**: it counts the steady growth of the BU price level as swing. After that failure, and before it was computed, a measure of the change in growth was chosen. It holds, with ratios of 0.05-0.11, and a sensitivity measure on the detrended series agrees (0.11-0.29). Both are labelled as chosen after the first measure failed, and the figures below full backing are published with both. Duke may instead hold them back."

### Assessment:
- **Fairly labelled:** Yes. The report explicitly states the preregistered measure failed, the reason (counts steady growth as swing), that the replacement was chosen *after* the failure, and that both measures are published with the label "chosen after the first measure failed."
- **Transparency:** The report discloses the failure reason, the post-hoc choice, and the sensitivity measure agreement.
- **Duke's option to hold back:** The report notes "Duke may instead hold them back" — acknowledging the post-hoc nature.

**However, the page text (findings page) does not mention this at all.** The "Below full backing" section on the page presents the supply study results (wage readings, BU adjustment, supply limits) without any qualifier that the swing measure failed and a post-hoc measure was used. The page only says: "The v5.9 engine had no limit on what the economy can supply, and wages, the BU and the cost-of-living basket followed prices in full and at once. A preregistered study adds each of these as a reading..."

**Missing from page:** Any disclosure that the preregistered swing measure failed below full backing and a post-hoc measure was substituted. This is a material qualifier for the "Below full backing" section's credibility.

---

## 5. In the page text: any figure that contradicts another on the page, any section that mixes engines or versions, any qualifier missing (full backing, intervals, the opt-in design beside the full-coverage design)?

### Contradictions on the page:

1. **"No main-row effect changed sign" (page release note) vs. "37 change sign" (page check table)**
   - Page release note: "No main-row effect changed sign."
   - Page check table (s93-page-check.md): "Of 3,262 printed figures, 2,132 change as printed and 37 change sign."
   - The sign changes include: supply study wage reading (3 cells at 20y, 1 at 40y), automation study (9 sign changes), lending study (4), yardstick study (13), central bank (3), financed rows (1).
   - The release note says "No main-row effect changed sign" — "main-row effect" likely means the 60 primary effects (2 designs × 3 env × 2 horizons × 5 outcomes). The main rows table confirms: "effect changes sign 0" for the 60 primary effects. But the page prints many *non-main-row* figures (supply study, automation, etc.) that *did* change sign. The statement "No main-row effect changed sign" is technically correct for the 60 primary effects, but the page prints many other figures that did change sign, and the release note doesn't clarify this distinction. A reader could think *no figure on the page* changed sign.

2. **Median real wealth at 20 years: headline card vs. "How sure we are" table**
   - Headline card: "Median real wealth at year 20: $434,102 against $224,185 with no programme (+$209,918)"
   - "How sure we are" table (20y, full-coverage, Reference): Main row (95% seed interval) = +$209,918 ($208,559 to $211,241)
   - But the main rows table (s93-release-tables.md) shows: Release effect = 209,918 (208,613 to 211,283) — matches.
   - However, the headline card says "Rests on full backing (corrected Nov 17, 2026: it said today's price rule, which full backing barely tests); 1.0% of the gain is the erosion of opening balances, in the programme's favour"
   - The "How sure we are" table footnote: "The wealth figures rest on full backing (corrected Nov 17, 2026: this sentence also said they rest on today's price rule, but at full backing almost no unmatched money reaches prices, so the price rule is barely tested there; below full backing they rest on it), and only a small part of any of them is the erosion of the balances adults held at the start (in the programme's favour; if all wealth were cash, against it)."
   - Consistent.

3. **Programme inflation at full backing: "immaterial" vs. specific values**
   - Page: "At the main row, programme inflation is 0.16 points a year above no programme in Reference at 20 years in the full-coverage design (0.12 in the opt-in design): no material change."
   - Main rows table: Full-coverage Reference 20y programme inflation = 0.16 (0.16 to 0.16); Opt-in Reference 20y = 0.12 (0.12 to 0.12). Matches.

### Sections mixing engines or versions:

- **Central bank section:** Uses seeds 1-100 (not 500), engine 50bc51d. The page states: "Every figure in this section is a mean over 100 paired runs (seeds 1-100), not the 500 of v5.9's main row." Clear.
- **History study:** "The central-bank and history studies start where the main rows do." Uses release engine.
- **Yardstick study:** "The comparison with US data at full take-up, which the rule reads, was not affected, and the rule reads the same on the rerun." Uses release engine (50bc51d) with defect fix.
- **All studies rerun on release engine (50bc51d).** No mixing detected.

### Missing qualifiers:

1. **Full backing qualifier on wealth figures:** Present on headline cards ("Rests on full backing...") and in "How sure we are" footnote. ✓

2. **Interval notes:** "How sure we are" tables show 95% seed intervals. Supply study tables show "95% paired-bootstrap intervals over seeds 1-500 (10,000 replicates); the model's randomness only." Automation study tables show "95% paired-bootstrap intervals over seeds 1-500 (10,000 replicates); the model's randomness only." Central bank: "95% over the same 100 paired seeds." Financed rows: no explicit interval note in the printed table, but the page says "The seed intervals cover the model's randomness only." Could be more prominent.

3. **Opt-in design beside full-coverage design:** Present on all headline cards and "How sure we are" tables. ✓

4. **Missing qualifier on "Below full backing" section:** As noted in Q4, no disclosure that preregistered swing measure failed and post-hoc measure used.

5. **Missing qualifier on supply study wage reading:** The page says "No source says how wages follow an inflation the programme itself makes: the readings never made up are the pessimistic end of the range swept." This is present. ✓

6. **Missing qualifier on automation study backing:** "Full backing is assumed, not produced. Every figure above assumes that each programme dollar is matched by new output (a design parameter)." Present. ✓

7. **Missing qualifier on financed rows:** "These rows were run without the weighted top tail (the 18 adults who carry population weights and stand for the very wealthy), so the top of the wealth distribution is less extreme than on the main rows and the figures that count by population weight (median real wealth, shares of wealth) are the ones that can differ from the main rows'; the size of that difference is not reported." Present. ✓

8. **Missing qualifier on central bank seeds:** "Every figure in this section is a mean over 100 paired runs (seeds 1-100), not the 500 of v5.9's main row; the intervals measure the model's randomness over those runs." Present. ✓

---

## 6. Anything in the report or the page that claims more than the runs measured, or reads as advocacy rather than a report of the figures?

### Release report:

- **"The price at the sale moved every poverty and wealth effect in the programme's favour."** — False for opt-in design (as shown in Q1). This overstates the evidence.

- **"Overall, 21 changes favour the programme, 25 go against it, and in 14 the interval includes zero."** — This is a fair summary of the 60 primary effects.

- **"The change comes from the price at the sale"** (in decomposition section) — Supported by the decomposition table, but with caveats (20 seeds, not full factorial, only basket poverty). The report includes the limits: "That run shows which change moves the figure, not the mechanism inside it." Fair.

- **"Duke may instead hold them back."** (re: below-full-backing figures) — Neutral, not advocacy.

### Page text:

- **"With Compassionism (the full-coverage design), against no programme, Reference, 20 years, main row."** — Factual.

- **"One sentence. Across the 62 preregistered readings, both designs lower all three poverty measures and raise median real wealth, in every environment and at both horizons..."** — Supported by "How sure we are" tables (62 of 62 readings keep sign for all 48 curves).

- **"These results hold when every dollar paid is matched by new output, which is the design's statement and not something the model shows..."** — Correctly qualifies full backing as a design assumption.

- **"With the model's own backing mechanism (with or without its ceiling), prices rise 15.5 to 50.3 points a year across the environments and designs at 20 and 40 years. That is the size of the unbacked money in a model with no central-bank response and no expectations, not a forecast of prices."** — Correctly qualifies.

- **"Do the poverty effects depend on backing? It depends on wages."** — Fair summary of supply study.

- **"Replaced Nov 18, 2026: the dated note of Nov 17 said the poverty effects held because the model had no limit on what the economy can supply; a limit on supply barely moves the curve, but wages that follow programme inflation only in part do."** — Correction noted, fair.

- **"In the opt-in design it takes away much less: −20% to 16% of the rise in basket poverty with lost jobs, and −2% to 66% with shorter hours. With lost jobs it often makes the rise in poverty larger: in 7 of its 12 lost-jobs cells the rise in basket poverty is larger with the programme than without it."** — Fair reporting of unfavourable results.

- **"The fund helps in no cell. Under the preregistered rule (it helps where it lowers basket poverty or yearly wealth poverty and worsens none of the six readings), it helps in 0 of 12 cells..."** — Fair reporting of unfavourable lending study.

- **"The yardstick: with pay by household type and the care credit (the reading Claude recommends for the main row), the opt-in design cuts basket poverty by 0.33 to 0.94 points less in every environment and horizon (study above)."** — "Claude recommends" is a bit advocacy-adjacent but attributed. The figures are correctly reported.

- **"Work: fewer adults work: participation falls (adults who leave work for the programme), with their earnings forgone."** — Supported by Work table.

- **"Mobility: less movement out of the lowest wealth fifth..."** — Supported by "stayed in the lowest wealth fifth" table.

- **"Adults outside the labour force... stay below the cost of living in a large share of their adult-years even with the programme, far more than adults in the labour force, and more so under the opt-in design than under the full-coverage design..."** — Supported by reference to Question 6 report.

- **"Labour's share of money income falls, partly because the programme's payments are income that is not wages..."** — Supported by Work table.

- **"Stress: the opt-in design's effects shrink by about two thirds in the Stress environment."** — Supported by tables (opt-in effects much smaller in Stress).

- **"Financing: 45 of 48 financed poverty and wealth curves are fragile..."** — Supported by page check table (45 of 48 fragile).

### Advocacy language to flag:

1. **"The price at the sale moved every main-row poverty and wealth effect in the programme's favour"** (page release note) — False for opt-in, as shown.

2. **"The change comes from the price at the sale"** (page, supply study section) — True for the decomposition shown, but presented without the caveats (20 seeds, not full factorial, only basket poverty). The release report includes caveats; the page does not.

3. **"Claude recommends this reading for the main row"** (yardstick section) — Attributed, but "recommends" implies endorsement. The preregistered rule held, and Duke adopted it. Better: "The preregistered rule held, and Duke adopted both on Nov 21, 2026."

4. **"The damping claim is not supported. The design says its share of essentials should damp what the central bank and outside shocks do to the cost of basic living. In this engine the rule moves rates, asset prices and job loss, not the price of essentials, so it cannot show that damping, for either design. That is a limit of the model, not evidence about the world."** — Fair, correctly attributes limitation to model.

5. **"The model has not been reviewed by an independent economist."** (What no figure here covers) — Important disclosure, present.

---

## 7. The three most important changes before publication.

### 1. **Correct the release note and report's claim that "the price at the sale moved every poverty and wealth effect in the programme's favour."**
   - **Evidence:** Main rows tables show the price at sale *worsened* opt-in design poverty effects (basket poverty +0.09 to +0.26 points; below 30 days +0.13 to +0.22 points) in every cell.
   - **Required change:** "The price at the sale moved every *full-coverage* poverty and wealth effect in the programme's favour; for the opt-in design it moved poverty effects against the programme."
   - **Locations:** Release report (two occurrences), page release note (one occurrence).

### 2. **Add the missing qualifiers to the page's "Below full backing" section about the failed preregistered swing measure and post-hoc replacement.**
   - **Evidence:** Release report discloses this clearly ("preregistered swing measure failed for a known reason... a measure of the change in growth was chosen [after failure]... Both are labelled as chosen after the first measure failed"). Page text has **zero mention** of this.
   - **Required change:** Add a prominent note in the "Below full backing" section: "The preregistered swing measure failed below full backing (it counted steady BU price growth as swing). A measure of the change in growth was chosen after this failure; it holds with ratios of 0.05–0.11. A sensitivity measure on detrended series agrees (0.11–0.29). Both are post-hoc measures."
   - **Location:** Findings page, "Below full backing: limits on supply, wages and the BU's adjustment" section.

### 3. **Clarify the supply study wage reading sign-change description to match the decomposition (3 of 6 cells flipped at 20 years, not "2 of 6 cells worse at 40 years" as the only change).**
   - **Evidence:** Decomposition shows at 20 years: Reference (+10.1→-7.9), Adverse (+4.8→-12.6), Stress (+9.2→-1.8) — all three flipped from worse to better. At 40 years: Reference (+30.7→+12.5, still worse), Adverse (+15.9→-2.5, flipped to better), Stress (+19.0→+11.4, still worse). Page says: "with no backing the programme is now worse than no programme in 2 of the six cells (Reference at 40 years, Stress at 40 years), better in the other 4 on basket poverty."
   - **Required change:** "At 20 years, the programme with no backing changed from raising basket poverty in all three environments (published) to lowering it in all three (release). At 40 years, it still raises basket poverty in Reference and Stress but now lowers it in Adverse. The change comes from the price at the sale."
   - **Location:** Page release note ("v5.9: the answer in ten seconds") and "Below full backing" section.

---

### Additional important fixes:

4. **Page release note must include:** (a) OSF registration statement (v5.8, engine 104691f), (b) that v5.9 main row *without* pay by household type and care credit stays as record, (c) which studies were rerun/reproduced.

5. **Release report must clarify** that the median real wealth and programme inflation ranges quoted ($481–$1,525, <0.0001) describe only the first step (price at sale), not the total change.

6. **Decomposition caveats** (20 seeds, not full factorial, only basket poverty) should appear in the page text where "the change comes from the price at the sale" is stated.