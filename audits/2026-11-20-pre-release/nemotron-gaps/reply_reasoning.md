Let me analyze this carefully. I need to review the Compassionism Simulation's findings page and related materials before the next release (S93), which makes the corrected price rule the default and regenerates main figures.

I need to answer four numbered questions:
1. Rank inventory items by how much each could change a headline claim or mislead a reader. For top 10, say whether to fix in model, fix in text, or state as limit, and how to verify.
2. Gaps NOT in inventory that I see in findings text or limits (claims without basis, figures resting on design parameters presented as results, missing unfavorable results, non-like-for-like comparisons).
3. What the release step itself is missing (checks before publishing, which studies must be rerun, what text must say).
4. Which items are acceptable as stated limits for this release, and why.

Let me go through each systematically.

First, the inventory items (A1-A3, B4-B15, C16-C21, D22). I need to rank by potential to change headline claims or mislead readers.

Headline claims from findings page:
- "Below 30 days of basic living: 0.9% vs 19.6% (−18.7 points)"
- "Below cost of living: 3.7% vs 36.1% (−32.4 points)"
- "Too little wealth (under $25,000): 6.0% vs 24.6% (−18.6 points)"
- "Median real wealth at year 20: $432,300 vs $223,900 (+$208,400)"
- "Across all 62 preregistered readings, both designs lower all three poverty measures and raise median real wealth, in every environment and at both horizons; full-coverage does 1.4 to 7.1 times as much as opt-in"
- "At main row, programme inflation is 0.0 to 0.2 points a year above no programme"
- "The model's own mechanism for new output reaches 0.2 to 1.9% of the payout"
- "Inflation stays under 5% a year only above about 86 to 90% backing"
- "At no backing and 40 years, opt-in design lowers median real wealth"
- Financed rows: full-coverage needs 63-77% of all money income, lowers basket poverty by at most 17.5 points; opt-in at 46-71% of wages raises basket poverty by up to 9.6 points
- "46 of 48 financed poverty and wealth curves are fragile"
- Who gains: top 1% share down 4.6 points, bottom half up from 2.9% to 9.2%
- Families in debt fall from 21.9% to 0.7% (full coverage) and 7.4% (opt-in)
- Unfavorable results listed

Now, which inventory items could change these headlines or mislead?

A1: Full backing assumed in main row - THIS IS CRITICAL. The headline wealth figure ($432,300 vs $223,900) rests on full backing. The model's own mechanism only reaches ~1%. The automation study shows 6-17% produced backing with 48-69% inflation. This fundamentally changes the headline if not clearly stated. The footnote says it but the headline cards present the figures prominently.

A2: No limit on total supply below full backing - Related to A1. The dated note says poverty effects barely depend on backing because no supply limit. But supply study exists. Could mislead if reader thinks poverty reduction works without backing in reality.

A3: Opt-in design does far less - Already published and shown, but release text must keep it beside full-coverage headline. Could mislead if full-coverage headline presented alone.

B4: Creative Collectives' lending - Preregistered but not built/run yet. Could affect backing production. Not in current figures.

B5: Late private price (BU's two-year swing) - Fixed behind option, main rows rerun. Release makes it default. Item 5 of release step (deciding which studies rerun) not preregistered. This affects the BU cycle mentioned in supply study limit 5.

B6: Simulation page uses Hub's early figures as targets - Visible to readers, could mislead about what model targets vs. what it produces.

B7: Written description doesn't describe validation presets - Could mislead about what validation actually checks.

B8: MODEL_SPEC gaps and contradictions - Could affect model credibility but may not change headline numbers directly.

B9: Tax credits missing - Could affect poverty figures for families with children.

B10: Who is simulated - Working-age adults only. Headlines say "adults" but exclude 65+. Could mislead about population coverage.

B11: Community business capacity not by zone/sector - Could affect supply-side realism.

B12: No private firms, banks, bond market - Central bank rule reduced form. Could affect inflation/price dynamics.

B13: Capital income not in price rule, automation dividend raises no investment - Could affect wealth distribution and backing.

B14: Displaced adults' outcomes by wealth fifth not stored - Automation study limit.

B15: Health, security, output per hour - No source sizes this. Automation study limit.

C16: Audit-flagged figures still live on Hub - Many incorrect figures in PDFs. Could mislead readers who see Hub vs findings page.

C17: 168 cited external figures not opened - Credibility issue.

C18: θ "Monte Carlo calibration" no record - Model parameter credibility.

C19: BLEI page may state poverty line inverted - Could mislead.

C20: Release data lacks series for BLEI visuals and Five Measures chart - Incomplete release.

C21: Hub's 32-item site audit - Various issues.

D22: Outside readings of results before publish - Done for automation study, not for release's regenerated figures.

Now ranking top 10 by potential to change headline or mislead:

1. A1 - Full backing assumed in main row. Headline wealth figure rests on this. Model's own mechanism only ~1%. Automation study shows 6-17% with high inflation. This is the single biggest issue.

2. A2 - No supply limit below full backing. Dated note says poverty effects barely depend on backing because no supply limit. But in reality, supply limits would bind. Could mislead about feasibility without backing.

3. B5 - Late private price fix not yet default, release makes it default but rerun decision not preregistered. The BU's two-year swing affects cost-of-living figures. Supply study limit 5 says cause is private businesses' lower BU price paid from last year's premium instead of at sale. This affects the BU adjustment figures.

4. B6 - Simulation page uses Hub's early figures as targets. Visible to readers, could confuse what model targets vs. produces.

5. C16 - Audit-flagged figures still live on Hub. Many incorrect figures ($847B net savings, "65% lower inflation", etc.) in PDFs. Readers may see these and be misled.

6. A3 - Opt-in design does far less. Must be kept beside full-coverage headline. If release text leads with full-coverage only, misleading.

7. B10 - Who is simulated: working-age adults only. Headlines say "adults" but exclude 65+. Could mislead about population coverage.

8. B12 - No private firms, banks, bond market. Central bank reduced form. Could affect inflation dynamics, but main row has full backing so inflation immaterial. Still, for financed rows and no-backing scenarios, matters.

9. B9 - Tax credits missing (child care credit, EITC reach low). Could affect poverty figures for families with children.

10. D22 - Outside readings not done for release's regenerated figures. Process gap.

Now for each top 10, say fix in model, fix in text, or state as limit, and how to verify.

1. A1: Full backing assumed. Cannot fix in model (model's mechanism only ~1%). Must fix in text: ensure every headline figure prominently states "assuming full backing (design parameter, not model estimate)" and the footnote is unavoidable. Also state as limit. Verify: check findings page text has qualifier on every headline card and in one-sentence answer.

2. A2: No supply limit. Fix in text: the dated note in "Prices, and how much new output backs the payout" section must remain and be prominent. State as limit. Verify: check note is present and not shortened away.

3. B5: Late private price. Fix in model: the fix is built behind option, release makes it default. Must ensure all main rows rerun with fix. Release step says regenerate main rows from s90-sale-*-b8ccd8d. Verify: check that regenerated data uses sp.vAt: 'sale' default and that BU swing is fixed (no two-year cycle). Also preregister which studies rerun.

4. B6: Simulation page targets. Fix in text/page: remove or clearly label Hub's early figures as "historical targets, not model outputs". Verify: check index.html for "Target $82K" label and CFG.TARGET_* constants.

5. C16: Audit-flagged figures on Hub. Fix in text/page: remove or correct PDFs on Hub. This is Hub content, not findings page. But findings page should not repeat them. Verify: audit Hub PDFs against corrected figures.

6. A3: Opt-in design. Fix in text: ensure release text keeps opt-in beside full-coverage in every headline. Verify: check findings page text has opt-in figures in headline cards and one-sentence answer.

7. B10: Who simulated. Fix in text: clarify "working-age adults (25-64)" in headline cards and methodology. Verify: check text specifies population.

8. B12: No private firms/banks. State as limit in "What no figure here covers". Already mentions "no central bank" but could be more explicit. Verify: check limits section includes this.

9. B9: Tax credits. State as limit. Fix in model if possible before release, but likely not. Verify: check limits section mentions missing child care credit and EITC reach.

10. D22: Outside readings. Process fix: conduct outside readings before publish. Verify: record of outside readings for regenerated figures.

Now question 2: Gaps NOT in inventory that I see in findings text or limits.

From findings text:
- "The model's own mechanism for new output reaches 0.2 to 1.9% of the payout (14 to 20% if its ceiling is removed)." - What ceiling? Not explained. Claim without basis in text.
- "Inflation stays under 5% a year only above about 86 to 90% backing (74 to 77% for the opt-in design in Stress)" - Specific thresholds presented as results but depend on design parameters (price rule, wage indexing). Not stated as design-dependent.
- "At no backing and 40 years, the opt-in design lowers median real wealth." - This is a result but only for opt-in at 40 years no backing. What about full-coverage at 40 years no backing? Not stated. Missing unfavorable result for full-coverage?
- "Every one of these curves is robust: at every reading the effect keeps its sign and its interval excludes zero (48 of 48 poverty and wealth curves, three environments, two horizons)." - But financed rows are separate: "46 of the 48 financed poverty and wealth curves are fragile". The 48 curves here are only the main-row (full backing) curves. Not made clear that financed rows are fragile.
- "The opt-in design's effects shrink by two thirds in Stress." - But full-coverage design's effects grow in Stress. This asymmetry not explained in headline.
- "Families in debt fall from 21.9% to 0.7% (full coverage) and 7.4% (opt-in design)." - What defines "families in debt"? Not defined in text.
- "Adults outside the labour force... stay far more often below the cost of living... under full-coverage design, 8.5 to 16.6% of their adult-years, against 1.8%". The "against 1.8%" is for adults in labour force? Not clear.
- "Programme inflation is above no programme in every cell: immaterial at the main row, 18 to 53 points a year at no backing." - But supply study says 40-49 points at no backing. Inconsistency?
- "Less movement out of the lowest wealth fifth: 69.8% of adults who start there are still there at year 20 under full-coverage design, against 66.3% without the programme." - This is unfavorable but presented. However, is this because programme reduces incentive to accumulate wealth? Not discussed.
- "Labour's share of money income falls by 11.7 to 30.5 points in Reference at 20 years... because the programme's payments are income that is not wages." - This is a mechanical effect, not a behavioral one. Could mislead as if labour share falls due to reduced wages.

From automation study limits:
- "The preregistered savings measure was run only for the headline rows... The sensitivity rows read the batch's nearest stored measure, adult-years below 30 days of basic living, and say so; it is not the preregistered measure and moves differently." - This means most automation study figures use a different measure than preregistered. Not in inventory.
- "The trace splits adults into those who would take part and those who would not, which are fixed groups of latent adults, not the adults enrolled in a given year; it decomposes a difference and does not test a cause by switching something off." - Methodological limit not in inventory.

From supply study limits:
- "The BU's relief to the cost of living runs a damped two-year cycle in every programme row, the main row included." - This is a known defect (late private price) that the release fixes. But the supply study was run with the defect. The release regenerates main rows but what about supply study? Not in inventory.
- "The ageing reading was rerun after a defect was fixed. The batch's ageing figures are superseded, not quoted." - But are the corrected ageing figures used in findings page? Not clear.
- "Building capacity costs nothing in the model's accounts, so the building-speed sweep is a physical sweep, not a fiscal one." - Important limit: supply constraints have no fiscal cost in model.

Other gaps not in inventory:
- Findings page says "Charts: dev/runs/s64-round2/charts/ (made by python3 dev/tools/s64_charts.py; index.html previews them with their captions)." - But are these charts regenerated with the new price rule default? Release step says regenerate main rows' findings-page data from s90-sale-*-b8ccd8d. But charts may not be regenerated.
- "Engine 104691f (the frozen model, first published as v5.8), batch shown as v5.9" - But release step makes sp.vAt: 'sale' default at new version. The engine version for release should be new, not 104691f. Findings page text still references 104691f.
- The "corrected Nov 17, 2026" notes in findings text refer to price rule correction. But release makes this default. The text should be updated to not say "corrected" but state the current rule.
- Financed rows: "These rows were run without the weighted top tail." - What is weighted top tail? Not explained. Could affect results.
- "The seed intervals measure the model's randomness only. They do not cover the choice of main row or full backing (a design statement); the readings the screen held fixed; Stress, which was not screened; or the engine's structure..." - This is good but "readings the screen held fixed" - what screen? Not explained.

Question 3: What the release step itself is missing.

Release step (PLAN.md) S93:
1. sp.vAt: 'sale' becomes default at that version (set_version.py; guard test differs by design: record in dev/DECISIONS.md)
2. Regenerate main rows' findings-page data (data/studies/r2-effects.json and the cards) from s90-sale-*-b8ccd8d, and replace dated notes with figures.
3. Hub corrections-log entry; root-site indexes in step.
4. Late-price figures stay as v5.9 record (OSF).
4. Preregistered amendment deciding which reached studies are rerun on release engine (readings, financed rows, central bank, history, supply).

Missing:
- No mention of regenerating charts (s64_charts.py) - findings page references charts.
- No mention of updating findings page text (dev/reports/s64-findings-page-text.md) to remove "corrected Nov 17, 2026" notes and reflect new default.
- No mention of updating engine version in findings page text (currently says Engine 104691f).
- No mention of running outside readings (D22) for regenerated figures.
- No mention of verifying that supply study, automation study, central bank study, history study are rerun or noted as not rerun. The preregistered amendment (item 5) is to decide which, but not done yet.
- No mention of checking that financed rows are regenerated (they are part of main rows?).
- No mention of updating the simulation page (index.html) to remove Hub's early figure targets (B6).
- No mention of correcting Hub PDFs (C16).
- No mention of verifying that the BU two-year swing is actually fixed in regenerated data (B5).
- No mention of checking that the "weighted top tail" omission in financed rows is documented or fixed.
- No mention of ensuring the "corrected" notes in findings text are replaced with current rule description.
- No check that the 62 preregistered readings still hold with new default (should, since main rows rerun from s90-sale-*-b8ccd8d which should have the fix).
- No mention of updating MODEL_SPEC if needed.
- No mention of the Creative Collectives lending (B4) - preregistered but not built. Should it be in release? Probably not, but should be noted.

Question 4: Which items are acceptable as stated limits for this release, and why.

Acceptable as limits (don't need fix before release, but must be stated):
- A1: Full backing assumed - already stated in footnote and section. Acceptable as limit because it's the design's statement, not a model claim. But must be prominent.
- A2: No supply limit below full backing - dated note covers it. Acceptable as limit for this release since supply study exists but not in main row.
- A3: Opt-in does less - already published and shown. Acceptable if kept beside headline.
- B4: Creative Collectives lending - preregistered but not built. Acceptable as future work, not in current figures.
- B7: Validation presets not described - acceptable as limit if stated in MODEL_SPEC/ODD.
- B8: MODEL_SPEC gaps - acceptable if documented in ledger.
- B9: Tax credits missing - acceptable as limit, stated in ledger.
- B10: Working-age adults only - acceptable if clearly stated in methodology.
- B11: Community business capacity not by zone/sector - acceptable as simplification.
- B12: No private firms/banks - acceptable as model scope limit.
- B13: Capital income not in price rule - acceptable as model limit.
- B14: Displaced adults' outcomes by wealth fifth not stored - acceptable as data limit.
- B15: Health/security/output per hour - acceptable as not sized.
- C17: 168 cited figures not opened - acceptable as ongoing work.
- C18: θ calibration no record - acceptable if θ is swept in sensitivity.
- C19: BLEI page poverty line - acceptable if findings page is correct.
- C20: Release data lacks series for BLEI visuals - acceptable if findings page has its own data.
- C21: Hub's 32-item audit - acceptable as separate Hub work.
- D22: Outside readings for release figures - should be done before release, but if not, state as limit? Better to do it.

Not acceptable as just limits (need fix or prominent disclosure):
- B5: Late private price - fix is built, release makes it default. Must be applied and verified.
- B6: Simulation page targets - visible to readers, should be fixed on page.
- C16: Audit-flagged figures on Hub - should be corrected or removed from Hub.

Also, the findings page text has "corrected Nov 17, 2026" notes that should be cleaned up since the correction is now the default.

Let me structure the answer now.