1. Ranked inventory items (top 10 by potential to change a headline claim or mislead a reader)

| Rank | Item | Fix in model / text / limit | Verification |
|------|------|----------------------------|--------------|
| 1 | A1 – Full backing assumed in main row; model’s own mechanism reaches ~1% | **Text + Limit**. Cannot fix in model (mechanism is structural). Every headline wealth/poverty figure must carry the qualifier “assuming full backing (design parameter, not model estimate)” in the card itself, not only in the footnote. The “Prices” section’s note must stay unshortened. | Open findings page; confirm each headline card and the one-sentence answer include the qualifier; confirm the “Prices” section still contains the full backing disclaimer and the 0.2–1.9% mechanism figure. |
| 2 | A2 – No supply limit below full backing; poverty effects “barely depend on backing” only because demand never hits a supply ceiling | **Text + Limit**. Keep the dated note in “Prices” and the supply-study summary prominent. Do not present below-backing poverty figures as evidence the design works without backing. | Search findings text for “no limit on what the economy can supply” and “not evidence that the design works without backing”; confirm both remain. |
| 3 | B5 – Late private price (BU two-year swing) fixed behind option; release makes it default but rerun decision not preregistered | **Model + Text**. The fix must be the default in the release engine (sp.vAt: 'sale'). All main-row data (r2-effects.json, cards, charts) must be regenerated from the s90-sale-* batch. The preregistered amendment listing which reached studies are rerun (readings, financed rows, central bank, history, supply) must be published before release. | Check `set_version.py` default is `sp.vAt: 'sale'`; run `s64_tables.py` and `s64_charts.py` on the release engine and diff against `s90-sale-*-b8ccd8d` outputs; confirm prereg amendment exists at `prereg/2026-11-s93-rerun-decision.md` (or similar) and lists the studies. |
| 4 | B6 – Simulation page (index.html) still uses Hub’s early figures as targets (CFG.TARGET_WEALTH 82000, “Target $82K” label) | **Text/Page**. Remove or relabel every occurrence as “historical target, not a model output”. | Grep `index.html` and `CFG.TARGET_*`; confirm zero occurrences of “Target $82K” or unqualified target constants on the public page. |
| 5 | C16 – Audit-flagged figures still live on Hub PDFs ($847B net savings, “65% lower inflation”, 85%/98% poverty reduction, etc.) | **Text/Page (Hub)**. Not on findings page, but readers reach Hub from findings page. Must correct or remove the PDFs before release, or add a banner linking to the corrections log. | Open each flagged PDF on Hub; confirm corrected values or a visible correction notice. |
| 6 | A3 – Opt-in design does far less; with lost jobs it makes poverty rise larger in 9 of 12 cells | **Text**. Release text must keep opt-in figures beside every full-coverage headline (cards, one-sentence answer, curve charts). | Verify each headline card shows both designs; one-sentence answer includes “1.4 to 7.1 times as much”; curve charts have opt-in row. |
| 7 | B10 – Only working-age adults (25–64) simulated; headlines say “adults” | **Text**. Change “adults” to “working-age adults (25–64)” in headline cards, one-sentence answer, and “Who gains” section. | Search findings text for “adults” in headline contexts; confirm qualification appears. |
| 8 | B12 – No private firms, banks, bond market; central-bank rule is reduced form with no channel to essentials prices | **Limit**. Add to “What no figure here covers”: “no private financial sector; central-bank rule is a reduced form without an expectations or essentials-price channel”. | Confirm the bullet appears in the limits section. |
| 9 | B9 – Missing child/dependent care credit; EITC reach 11.9% vs 15.3% (no part-time work) | **Limit**. Add to limits: “Tax system omits child/dependent care credit; EITC reach understated because part-time work not modelled”. | Confirm bullet in limits section. |
| 10 | D22 – Outside readings done for automation study, not for release’s regenerated figures | **Process**. Conduct two independent readings of the regenerated main-row tables/charts before publish; record in `audits/2026-11-20-pre-release-triage.md`. | Confirm two dated reviewer sign-offs in the triage file covering the regenerated `r2-effects.json` and charts. |

2. Gaps NOT in the inventory (found in findings text or limits)

1. **“14 to 20% if its ceiling is removed”** (model’s own backing mechanism) – no explanation of what ceiling, where it is set, or why removing it is plausible. Claim without basis in text.
2. **Inflation thresholds** (“under 5% only above 86–90% backing”, “74–77% in Stress”) presented as results but depend on the price rule, wage-indexing parameters, and BU adjustment delay – none of which are disclosed as design-dependent in the sentence.
3. **“At no backing and 40 years, the opt-in design lowers median real wealth”** – full-coverage at 40 years/no backing not stated. Missing unfavourable comparison.
4. **“48 of 48 poverty and wealth curves robust”** – refers only to main-row (full-backing) curves. The very next section says 46 of 48 *financed* curves are fragile. The contrast is not made explicit; a reader could think all 96 curves are robust.
5. **Financed rows “run without the weighted top tail”** – what the weighted top tail is, why it was omitted, and how it biases the contribution/share figures are not explained.
6. **“Families in debt fall from 21.9% to 0.7%”** – “families in debt” never defined (net worth < 0? debt-service > income?).
7. **“Adults outside the labour force… 8.5–16.6%… against 1.8%”** – the 1.8% referent (adults *in* the labour force) is not stated in the sentence.
8. **Programme inflation range discrepancy** – findings page says “18 to 53 points a year at no backing”; supply study says “40–49 points”. Which is current?
9. **Automation study: preregistered savings measure run only for headline rows**; sensitivity rows use a different stored measure (adult-years below 30 days basic living) that “moves differently” (97–102% vs 66–94% offset). Most automation figures therefore do not use the preregistered measure – not disclosed in findings page text.
10. **Automation trace “decomposes a difference and does not test a cause by switching something off”** – methodological limit not carried to findings page.
11. **Supply study: building capacity costs nothing in model accounts** – physical sweep, not fiscal. The Creative Collectives’ lending (next engine step) is what could make backing produced. This limit is not in findings page.
12. **Findings page still references engine `104691f` (v5.8) and batch “shown as v5.9”** – release will use a new version with `sp.vAt: 'sale'` default; the text must be updated.
13. **Charts directory (`dev/runs/s64-round2/charts/`)** – release step regenerates tables but does not mention regenerating charts; captions will be stale.
14. **“Corrected Nov 17, 2026” notes** in findings text refer to the price-rule correction that is now the default; they should be replaced with a clean statement of the current rule.

3. What the release step (S93) is missing

| Missing check / action | Why it matters |
|------------------------|----------------|
| Regenerate **charts** (`s64_charts.py`) from the release engine and verify captions match new data. | Findings page links charts; stale charts mislead. |
| Update **findings-page text** (`dev/reports/s64-findings-page-text.md`): remove “corrected Nov 17” notes, update engine hash/version, reflect new default price rule. | Text frozen at v5.9 will describe the old engine. |
| Publish the **preregistered amendment** listing which reached studies are rerun (readings, financed rows, central bank, history, supply) *before* release. | Step 5 of plan says “then a preregistered amendment deciding…”; without it, rerun scope is opaque. |
| Run **outside readings** (D22) on the regenerated main-row tables/charts and record sign-offs. | Required by team’s own process; currently not done. |
| Verify **BU two-year swing is eliminated** in regenerated data (trace `s64_erosion` or equivalent). | B5 fix is the release’s core correction; must be confirmed in output. |
| Check **financed rows** are regenerated with the new default (they are part of “main rows” in step 2). | If not, financed figures rest on old price rule. |
| Update **simulation page** (`index.html`) to remove/qualify Hub target constants (B6). | Visible to every reader; currently shows stale targets as if current. |
| Add **Hub corrections-log entry** (step 3) *and* banner on flagged PDFs (C16) before release. | Otherwise readers see known-wrong figures on Hub. |
| Confirm **supply study, automation study, central-bank study, history study** are either rerun on release engine or explicitly noted as “run on v5.9 engine, not release engine”. | Cross-study consistency; findings page cites automation/supply limits. |
| Document **“weighted top tail” omission** in financed rows or fix it. | Unexplained omission biases contribution/share figures. |

4. Items acceptable as stated limits for this release (and why)

| Item | Acceptable? | Reason |
|------|-------------|--------|
| A1 (full backing assumed) | **Yes, if qualifier is on every headline card** | It is the design’s statement, not a model estimate; the footnote and “Prices” section already exist. Must not be shortened away. |
| A2 (no supply limit below full backing) | **Yes, with dated note kept** | Supply study exists; the note correctly frames below-backing figures as “not evidence the design works without backing”. |
| A3 (opt-in does less) | **Yes, if kept beside full-coverage headlines** | Already published; release text must not lead with full-coverage alone. |
| B4 (Creative Collectives lending) | **Yes** | Preregistered but not built; future engine step. Not in current figures. |
| B7 (validation presets not described) | **Yes** | Documented in MODEL_SPEC/ODD/ledger; not a findings-page claim. |
| B8 (MODEL_SPEC gaps) | **Yes** | Tracked in ledger; does not change current headline numbers. |
| B9 (tax credits) | **Yes, if stated in limits** | Known simplification; affects family poverty but not aggregate headlines materially. |
| B10 (working-age only) | **Yes, if text says “working-age adults (25–64)”** | Scope limit; acceptable when explicit. |
| B11 (community business capacity not by zone/sector) | **Yes** | Model simplification; noted in ledger. |
| B12 (no private firms/banks) | **Yes, if added to “What no figure here covers”** | Structural scope limit; main row has full backing so inflation channel dormant. |
| B13 (capital income not in price rule) | **Yes** | Model limit; noted in automation study. |
| B14 (displaced adults by wealth fifth not stored) | **Yes** | Data granularity limit; automation study limit. |
| B15 (health/security/output per hour) | **Yes** | No opened source; automation study limit. |
| C17 (168 cited figures not opened) | **Yes** | Ongoing sourcing work; not a findings-page claim. |
| C18 (θ calibration no record) | **Yes** | θ is swept in sensitivity; not a fixed calibration claim. |
| C19 (BLEI page poverty line) | **Yes** | Separate page; findings page uses its own definitions. |
| C20 (release data lacks BLEI series) | **Yes** | Findings page has its own tables; BLEI visuals are separate. |
| C21 (Hub 32-item audit) | **Yes** | Separate Hub work; not findings page. |
| D22 (outside readings for release figures) | **No** | Must be done before release; not acceptable as a limit. |
| B5 (late private price) | **No** | Fix exists; release makes it default. Must be applied and verified. |
| B6 (simulation page targets) | **No** | Visible to readers; must be corrected on page. |
| C16 (audit-flagged Hub figures) | **No** | Known wrong figures on Hub; must be corrected or bannered. |