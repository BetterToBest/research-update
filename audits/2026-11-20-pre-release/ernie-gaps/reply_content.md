# 1. Inventory items ranked by power to change a headline or mislead

1. **Item 1 — full backing assumed in the main row.** Every card and the one-sentence answer rest on it; the engine produces ~1% (automation 6–17%). *Fix in text:* put the full-backing condition and the produced share in the card headings and the one-sentence answer, not only the footnote. *Verify:* a reader who reads only the four cards sees the condition; produced-share figures match s85.

2. **Item 5 — late private price / BU two-year cycle.** A defect in every programme row including the main row; it moves the basic-living and cost-of-living cards, and the release changes them. *Fix in model* (the release does this). *Verify:* the damped BU cycle is gone in regenerated `s90-sale-*` rows; diff v5.9 vs release cards and record deltas in DECISIONS.md.

3. **Item 16 — wrong figures live on the Hub** ($847B, 65%, 15→13pp, 85/98%, $82K+CI, 10,000, −0.71→−1.6, 11.8%, 14→11%, £5B, 2.86→1.95). Gross contradictions of the current results. *Fix in text:* land the corrections package. *Verify:* each figure matches current results; corrections-log links each.

4. **Item 2 — no supply limit below full backing.** "Poverty barely depends on backing" misleads; s82 shows it depends on wage/BU catch-up. *Fix in text:* keep the Nov 17 note prominent and reconcile it with s82's break-even (0.08–0.49). *Verify:* the "barely depends" sentence carries the s82 qualification.

5. **Item 3 — opt-in does far less.** A full-coverage card without opt-in beside it misleads. *Fix in text.* *Verify:* opt-in figure beside every full-coverage card; "worse in 9 of 12 cells with lost jobs" retained.

6. **Item 9 — tax credits / EITC reach 11.9% vs 15.3%, no part-time work.** Understates the no-programme baseline, inflating the programme's relative effect. *Fix in model* (part-time work) if feasible; else *state as limit.* *Verify:* EITC reach vs 15.3%; poverty with/without the credit.

7. **Item 6 — Hub targets ($82K, Gini, poverty, stability, "Target $82K" label).** Misleads on what the model targets/validates. *Fix in model/config.* *Verify:* grep the four `index.html` occurrences; no stale target remains.

8. **Item 12 — no central bank, no expectations, reduced-form rule with no essentials-price channel.** The inflation figures (15–53, 48–69) read as forecasts. *State as limit + fix in text:* carry s85's warning ("size of the unbacked money, not a forecast") on every inflation figure. *Verify:* each inflation figure has the warning; "What no figure covers" names the reduced-form rule.

9. **Item 20 — release data lacks series for BLEI visuals / Five Measures chart.** Release-specific; charts break or mislead. *Fix in model/data before release.* *Verify:* both render from the regenerated release data.

10. **Item 7 — validation preset "Gini" is not a wealth Gini.** Misleads on validation. *Fix in text:* describe the presets in MODEL_SPEC/ODD and relabel the metric. *Verify:* the metric is named for what it is (wealth less one year of COL×wage).

# 2. Gaps not in the inventory

**Claims without a stated basis**
- "1.4 to 7.1 times as much as the opt-in design" — no derivation shown.
- "The widest part of the range comes from how much of their spare cash adults spend" — a variance claim with no decomposition.
- "a 10,000-adult pair agrees on hours and the top of the wealth distribution" — no tolerance, and only hours/top-of-wealth were checked, not the poverty or median-wealth headlines that use 500 adults.
- Automation "keeps most of the freed time above the cost of living" — the main model states it puts no value on care/community work/new ventures, so the basis for valuing free time is unstated.

**Design parameters presented as results**
- The cards: the design is "built to meet NEEC's criterion C2.2" with full coverage, full backing, and BU/basket indexed to the same prices with no supply limit. The poverty result is partly a restatement of that construction; the cards do not flag that the parameters were chosen to produce it (item 1 covers only the backing half).
- "programme inflation is 0.0 to 0.2 points… no material change" — true only under the full-backing parameter; the phrase misleads if lifted from its sentence.

**Missing unfavourable results**
- s82: with wages not keeping up (half the inflation never made up), the no-backing programme is *worse than no programme* on basket poverty, breaking even only at 0.08–0.49 backing. The findings page instead says poverty "barely depends on backing" — this is both a missing unfavourable result and a contradiction.
- Automation: opt-in with lost jobs makes the rise in poverty (and low savings in Stress) larger — absent from the main Unfavourable section.
- Even with the ceiling removed the model produces only 14–20% backing, far below the 86–90% needed for <5% inflation; the implication that the design cannot self-fund is not in Unfavourable.

**Comparisons not like for like**
- "1.4 to 7.1 times" compares 100% take-up to partial take-up; the ratio reflects coverage, not per-participant effect.
- Main row (with weighted top tail) vs financed rows (without it): levels are compared across them though disclosed.
- "The model's own mechanism" is 0.2–1.9% / 15–53 pts in the main row but 6–17% / 48–69 pts in s85; presented in different sections without reconciliation, so it reads as two different things.

# 3. What the release step is missing

**Checks before publishing**
- Diff regenerated vs v5.9 headline figures; record deltas and confirm they match the expected direction/magnitude of the price-rule fix.
- Confirm the BU two-year cycle is actually gone in the regenerated main rows.
- Confirm the guard test's new expected values are independently correct, not re-baselined to whatever the code now outputs.
- Re-verify every qualifier survives regeneration: full-backing condition, erosion share, seed interval, reading range, "48 of 48 excludes zero," the 46/48 financed-fragility count.
- Outside reading of the regenerated figures (item 22) before publish.
- Reconcile the produced-backing figures across main and automation.
- Land the Hub corrections (16) and update Hub targets (6) so the Hub does not contradict the release.

**Studies that must be rerun on the release engine** (the price-rule default change moves anything touching BU/premium timing, prices, real wealth)
- The 62 preregistered readings — the release regenerates "the main rows"; if `r2-effects.json` does not cover all 62, the quoted ranges stay on the old default and are inconsistent with the new main-row figure. Confirm and regenerate all 62.
- Erosion trace (the quoted erosion shares depend on prices).
- Financed/contribution rows, central-bank study, supply study (s82, whose limit 5 already preregisters this rerun), automation study (s85 inflation), and the ageing/history reading.
- Regenerate the charts from the new data.
- The text must not publish ranges or figures drawn from mixed engines.

**What the text must say**
- The release engine version/hash, that `vAt:'sale'` is now the default, and its effect on the headline figures (a changelog).
- Full-backing condition in the card headings.
- That the late-price figures kept on OSF are the pre-fix v5.9 record, not the release figures.
- Replace the "corrected Nov 17" notes with release figures while keeping every required qualifier.
- Reconcile "the model's own backing" between main and automation.
- Add or reconcile the s82 wage-lag result (no-backing worse than nothing).
- Version clarity: whether the release is still "v5.9" or a new number, given the engine change.

# 4. Acceptable as stated limits for this release

- **Item 4 (Collectives' lending):** preregistered, build to follow; producing backing is already handled by the full-backing disclosure. Not a defect.
- **Item 8 (MODEL_SPEC gaps):** the ~30 gaps can be stated as documentation debt; the four contradictions should still be listed.
- **Item 10 (who is simulated):** acceptable if the Hub and page say "working-age adults and their families"; the scope option exists for later.
- **Item 11 (whole-population capacity, one utility share):** structural simplification, does not change headline direction.
- **Item 12 (no banks/bond market, reduced-form central bank, no expectations):** the structure is out of scope; acceptable *only* with the "not a forecast" warning on inflation (a text fix, not a limit alone).
- **Item 13 (capital income outside the price rule; no investment from the dividend):** structural, already noted in s85.
- **Item 14 (displaced outcomes by fifth not stored):** a missing disaggregation, not a wrong figure; add later.
- **Item 15 (health/security/output-per-hour, no source):** honestly left out and disclosed in s85.
- **Item 17 (168 cited figures unopened):** acceptable as a sourcing limit for non-headline citations; any citation used to support a headline must be opened.
- **Item 18 (θ calibration never run):** acceptable only if the text makes no calibration claim; otherwise state "θ set by sweep, not calibrated."
- **Item 21 (Hub 32-item audit):** the transparency and AI-authorship items can be stated limits; the Gini-comparability item should be fixed.

Not acceptable as limits (must fix): 1, 2, 3, 5, 6, 7, 9, 16, 20 — each changes a headline, is a wrong number, or breaks a release surface.